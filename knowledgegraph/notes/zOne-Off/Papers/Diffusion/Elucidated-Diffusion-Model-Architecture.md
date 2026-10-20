
# 10. Implementation Details
## Datasets
They implement their modifications on 4 different datasets:
- 32 x 32 CIFAR 10
- 64 x 64 FFHQ
- 64 x 64 AFHQv2
- 64 x 64 ImageNet



### Config A
| Hyperparameter    | 32 x 32     | 64 x 64 |
| -------------------| -------------| ---------|
| Training Examples | 200 Million | Same    |
| Batch Size        | 128         | Same    |
| NFE               | 35          | 79      |
| LR                | 2e-4        | 2e-4    |

This is 1.6M training iterations at batch size 128, and would be 400k training iterations at batch size 512.

### Config B
| Hyperparameter    | 32 x 32     | 64 x 64          |
| -------------------| -------------| ------------------|
| Training Examples | 200 Million | Same             |
| Batch Size        | 512         | 256              |
| NFE               | 35          | 79               |
| LR (Max)          | 1e-3        | 2e-4             |
| EMA half-life     | 500k images         | Same             |
| Dropout           | 13%         | 5/25%, FFHQ/AFHQ |

Other Notes:
- This config increases from 4 -> 8 GPUs
- No gradient clipping
- Learning rate ramp up to 1e-3 for 10 million images (instead of 0.64 million images)

### Config C
Adjust Config A:
- Remove bottleneck 4x4 layers (these overfit), double 16x16 layer capacity


| Resolution | # Chan. - Conf. B | # Chan. Conf. C |
| ------------| -------------------| -----------------|
| 64 x 64    | 128/None          | 128/None        |
| 32 x 32    | 128               | 256             |
| 16 x 16    | 256               | 256             |
| 8 x 8      | 256               | 256             |
| 4 x 4      | 256               | None            |

Reduces trainable parameters:
 - 32 x 32 - 56 million
 - 64 x 64 - 62 million

### Configs D, E, F
- D uses new preconditioning
- E uses new noise distribution/loss weighting
- F uses non-leaking augmentation (helps with overfitting)

### ImageNet
- 32 GPUs, batch size 4096 (128 per GPU)
- Mixed Precision
    - Weights stored at fp32, cast to fp16 during training
    - Embedding/Self attention layers have no casting
- 2 weeks, 2500 million images, 600k iterations
- 296 million parameters
- No augmentation
- EMA of 50 million images
- lr 1e-4
- In the diffusion beats GANs paper, it is 296 million parameters for the 64x64 model, and 554M for 256 x 256.
- For a 1D UNet for audio, you probably increase the capacity of the model to account for the channel and frequency axis being the same.
- The kernels would also be 3x smaller for 1D conv.
- 188 M for a 256 x 80 model seems reasonable.

## Architectures
In Config A, we start with:
- VP uses DDPM++
- VE uses NSCN++
And use two different formulations. However, after all EDM's changes, both formulations are the same except for the architecture.
- DDPM++ seems to perform better according to the table.
- Differences:
    - DDPM++ uses Box filter [1, 1], while NSCN++ uses bilinear [1 3 3 1]
    - NSCN++ has skip/residual blocks
    - DDPM++ has positional encoding scheme, NSCN++ uses random Fourier features
    - NSCN++ has extra residual skip connnections

- For ImageNet, Use ADM architecture, no changes.
- Compared to DDPM++: 
    - Shallower model: 3 residual blocks per resolution
    - More self attention layers (22 instead of 6) interspersed throughout model
    - More attention heads (12 in lowest res.)
    - More channels (768 in the lowest res. instead of 256)

Conclusion: For smaller datasets, use DDPM++.

## Single-Level

## Architectural Notes
- To do: write these down in website


### Block Level
- There is 1 more decoder block than encoder block per level.
- There are skip connections for EVERY Encoder UNet block (20 of them). 
- There are skip connections connecting the beginning of the block to the end.


## Test Encoder
We use channel_mult = [2, 3, 4, 5] for clarity on how the UNet is structured. In reality, it is [1, 2, 2, 2]
| Name           | In Channels | Out Channels | In Resolutions | Out Resolutions |
|----------------|-------------|--------------|----------------|-----------------|
| 64x64_conv     | 3           | 128          | 64             | 64              |
| 64x64_block0   | 128         | 256          | 64             | 64              |
| 64x64_block1   | 256         | 256          | 64             | 64              |
| 64x64_block2   | 256         | 256          | 64             | 64              |
| 64x64_block3   | 256         | 256          | 64             | 64              |
| 32x32_down     | 256         | 256          | 64             | 32              |
| 32x32_block0   | 256         | 384          | 32             | 32              |
| 32x32_block1   | 384         | 384          | 32             | 32              |
| 32x32_block2   | 384         | 384          | 32             | 32              |
| 32x32_block3   | 384         | 384          | 32             | 32              |
| 16x16_down     | 384         | 384          | 32             | 16              |
| 16x16_block0   | 384         | 512          | 16             | 16              |
| 16x16_block1   | 512         | 512          | 16             | 16              |
| 16x16_block2   | 512         | 512          | 16             | 16              |
| 16x16_block3   | 512         | 512          | 16             | 16              |
| 8x8_down       | 512         | 512          | 16             | 8               |
| 8x8_block0     | 512         | 640          | 8              | 8               |
| 8x8_block1     | 640         | 640          | 8              | 8               |
| 8x8_block2     | 640         | 640          | 8              | 8               |
| 8x8_block3     | 640         | 640          | 8              | 8               |

## Decoder
| Name           | In Channels | Out Channels | In Resolutions | Out Resolutions | Skip From  |
|----------------|-------------|--------------|----------------|-----------------|------------|
| 8x8_in0        | 640         | 640          | 8              | 8               |            |
| 8x8_in1        | 640         | 640          | 8              | 8               |            |
| 8x8_block0     | 1280        | 640          | 8              | 8               | 8x8_block3 |
| 8x8_block1     | 1280        | 640          | 8              | 8               | 8x8_block2 |
| 8x8_block2     | 1280        | 640          | 8              | 8               | 8x8_block1 |
| 8x8_block3     | 1280        | 640          | 8              | 8               | 8x8_block0 |
| 8x8_block4     | 1152        | 640          | 8              | 8               | 8x8_down   |
| 16x16_up       | 640         | 640          | 8              | 16              |            |
| 16x16_block0   | 1152        | 512          | 16             | 16              | 16x16_block3 |
| 16x16_block1   | 1024        | 512          | 16             | 16              | 16x16_block2 |
| 16x16_block2   | 1024        | 512          | 16             | 16              | 16x16_block1 |
| 16x16_block3   | 1024        | 512          | 16             | 16              | 16x16_block0 |
| 16x16_block4   | 896         | 512          | 16             | 16              | 16x16_down |
| 32x32_up       | 512         | 512          | 16             | 32              |            |
| 32x32_block0   | 896         | 384          | 32             | 32              | 32x32_block3 |
| 32x32_block1   | 768         | 384          | 32             | 32              | 32x32_block2 |
| 32x32_block2   | 768         | 384          | 32             | 32              | 32x32_block1 |
| 32x32_block3   | 768         | 384          | 32             | 32              | 32x32_block0 |
| 32x32_block4   | 640         | 384          | 32             | 32              | 32x32_down |
| 64x64_up       | 384         | 384          | 32             | 64              |            |
| 64x64_block0   | 640         | 256          | 64             | 64              | 64x64_block3 |
| 64x64_block1   | 512         | 256          | 64             | 64              | 64x64_block2 |
| 64x64_block2   | 512         | 256          | 64             | 64              | 64x64_block1 |
| 64x64_block3   | 512         | 256          | 64             | 64              | 64x64_block0 |
| 64x64_block4   | 384         | 256          | 64             | 64              | 64x64_conv |
| 64x64_aux_norm |             |              |                |                 |            |
| 64x64_aux_conv | 256         | 3            | 64             | 64              |            |


## More details
- All linear and conv have bias 0
- All conv1s (second conv in block) have weight 1e-6
- the output projection from attention also have weight 1e-6
- also aux conv
- First thing is a 64x64 Conv






Block kwargs
- 512 embedding channels
- 1 head
- 0.1 dropout
- eps 1e-06
- xavier uniform initialization
- for attention blocks
    - sqrt(0.2) as init_weight
    - xavier uniform initialization

- for zero-initialized
    - 1e-5 init weight
- [1,1] resample filter
- resample projection is true
- skip scale is 1/sqrt(2)


UNet Block
- x = conv0(silu(norm0(x)))
- first norm is group norm with in_channels, 1e-6
- first conv has kernel size 3, potential upsampling/downsampling, xavier uniform initialization
- linear from emb_channels to out_channels
- x + linear(embedding)
- silu(norm2(x))
- dropout x
- conv1 x, conv2 has out, out, kernel size 3, 1e-5 initial weight  



### Positional Encoding

Notes:
- log(sigma) lyings 6 stds outside the mean has prob. 1.973e-9,
- This is 1 in 506 Million.
With P_mean=-1.2, range is [-8.4, 6]
c_noise ranges from -2.1 to 1.5

Last Reviewed: 10/19/2026
