# How do you have an LLM output continuous outputs with a diffusion head?
Short answer - train the transformer to do next token prediction and diffusion.


# Transfusion
## Representations
- Text is discrete tokens
- Images are continuous latents from a frozen VAE, patchified
- Images occupy positions inside BOI/EOI tokens

## Architecture
- Input and output projection layers
    - linear
        - Patchify latent map from the VAE into patches, then linear project into model dim.
        - output has a linear projection too, into the VAE-dim space
        - not tied to the input
    - UNet
        - UNet-Down on the input, UNet-Up on the output
        - Encoder side:
            - Runs latent feature map through the UNet Encoder/Downsampler
            - Flattens it into the transformer sequence.
        - Decoder side
            - Reshape, then pass to UNet Decoder (Upsampler)
        - Beats linear even on parameter-matched variants
        - Also reduces number of sequence slots an image costs



## Attention
- Attention is bidirectional within each image block, each patch can see each other patch (and everything before it)
- Text only sees the past

## Training
- Remember that training has inputs.
- Usually in a text LLM, you input the whole sequence, and the output is the sequence shifted one over.
- Here you still pass in a full sequence of text, but you pass in noisy images.
- When images are in the sequence:
    - Sample a diffusion timestep
    - Noise all patches together at the input layer
    - have model predict the noise you added
    - image patches attend to everything before it, and every patch within that image
    - weight LM loss + lambda times diffusion loss
- Naively (without a loss mask), EOI has a loss on it too - it's predicted from all the noisy image tokens before it.

## Inference
- Decode text autoregressively
- When emit BOI
    - Append a block of pure noise patches
        - all images are the same size by construction
    - run the entire denoising schedule
    - append EOI
    - resume decoding text autoregressively
- Note that in training, we predict text assuming noisy images in the context (since the input sequence has noisy images), while at test time, the images in the input are always clean. This is a slight train/inference gap.
    - Timestep = 0 covers the case where the images in the context are clean.


# Audio

## Audio - VibeVoice
- Diffusion head on top of transformer
- The final hidden state $h_t$ would usually be sent into the linear output projection + SoftMax, but instead is instead used to condition the diffusion model
- Discrete control tokens decide when the head runs
    - Diffusion is started by a start token
    - While in diffusion mode, discrete tokens are still being output in the background, when an end token is output, the we return to discrete outputs
    - the diffusion head's final output is fed back into the LLM again at the next position, using an input projection layer
- Loss = next token prediction loss plus diffusion loss

Last Reviewed 8/31/2026
