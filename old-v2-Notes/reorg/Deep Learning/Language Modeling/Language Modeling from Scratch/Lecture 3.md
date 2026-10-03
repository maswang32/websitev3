

VC - dimension - theorectical lens

Summary:
1. Recap of modern transformer
2. most large LMs have in common?
3. common variation?



# Quick Recap of Modern Transformer

### Vanilla
- Position Embedding: sines and cosines
- FFN: ReLU
- Norm type: post-Norm, LayerNorm


### Differences
- Layernorm is in front of the block
- RoPE - implement RoPE
- Implement SwiGLU, not ReLU
- copied much of it over from LLama


# In 2024-2025 - lots of papers

- 19 new dense models
- Qwen3? Olmo3? Gemma4? Marin? Liquid, Ministral 3, GLM, MiniMax.
- Vocab sizes? LayerNorms? Position Embeddings?
# To Cover this Lecture

Variations:
1. Architecture variations (Activations, FFN), 2.
2. Attention Variants
3. Position Embeddings?
4. Number of vocab elements?

Hyperparams:
- ff_dim
- vocab elements

Stability Tricks



# High Level View:
1. Dominance of LLaMA 2 architectures
2. Trends of the years, QK-Norm, Hybrid attention
3. More stuff to improve stabillity (2025)
4. This year (longer context dependence)



# Architectural Decisions
## Pre-Norm vs Post-Norm
1. Everyone agrees on: Norm before FFN and norm before MHA.
2. PostNorm = norm in residual
3. Modern ones: Layernorm outside of the residual stream (OPT350M is the exeception, but OPT was kind of a mess of  language model.)
![[Pasted image 20260728141126.png|328]]

### Why?
1. you need to do a warmup when you train. removing the warmup had very issues of stability and convergence, when using the original transformer. 
2. post-LN increases the expectation of gradient init, and diminishes after warm up, Pre doesn't.
	1. PreNorm: initialization sizes remain the size
	2. Stability is improved under pre-norm, less gradient spoikes.
	3. Salazar and Nguyen
	4. helps go deep.
3. Gradient attenuation issues are the most clear.
4. Want to keep the residual stream clean
5. Why does layer norm at the start of FFN and MHA instead of after?
	1. Grok, Gemma 2, Olmo 2, layernorm is after computation, postnorm but oustide the residual stream
6. Sprinkling in layernorms improves stability
	1. can have layernorm before and after MHA and FFN
7.  RMSNorm:
	1. LLama-Family, PaLM, Chinchilla, T5
	2. In practice, as good as layernorm, but faster.
	3. Want to remove stuff that has lots of memory movement but not a lot of expressive power.
	4. Norm = 0.17% of the FLOPs, but runtime is way more complicated:
		1. Stat. norm can be 25% of the runtime
			1. (Tensor contraction: 99.80% FLOP, 61% runtime).
	5. RMSNorm runtimes have been seen in papers. More steps per second and better performance.
	6. Also people drop bias terms.
8. Layernorm:
	1. GPT3/2/1, OPT, GPT-J, BLOOM.
9. Recap:
	1. Keep good parts of re
10. Eeveryone
	1. prenorm, outside residual stream
	2. nicer gradient spikes.


## Dropping Bias Terms
1. FFN(x) = sigma(xW_1)W_2 - drop the bias. bias are memory intensive, but not arithmetically intensive.
2. Bias can also cause stability issue.
3. Lots of experimentation - dropping bias terms on linear and RMSNorm is OK.

## Activation
1. ReLU, GELU, Swish, ELU, GLU, GeGLU, ReGLU, SeLU, SwiGLU, LiGLU
2.  ReLU:
	1. Chincilla,
	2. T5,
	3.  transformer
	4. Gopher
	5. OPT
3. GeLU
	1. GPT1/2/3, GPTJ, GPT-Neox
	2. Bloom
	3. Tiny divet, changes the gradients right near 0.
4. SwiGLU/GeGLU
	1. Llama, Palm, T5 v1.1., most models post 2023.

### GLU
1. Gating is very helpful.
2. FF(x) = max(0, xW_1)W_2
3. Augment the above with an entrywise linear term:
	1. max(0, xW1) x (xV).
	2. Modulate the output of the ReLU.
4. ReGLU:
	1. (max(0, xW_1) x xV) W2
	2. (ReLU + GLU)
5. GeGLU:
	1. (GELU(xW) x xV) W2
	2. T5 v1.1, mT5, LaMBDA, Phi3, Gemma 2, Gemma 3, Gemma 4
6. SwiGLU:
	1. (Swish(xW) x xV) W2
	2. Swish is x times sigmoid x
	3. Llama 1/2/3/, PaLM, Mistral, OlMo
	4. SwiGLU is more dominant.
7. Gated = smaller dims for dff by 2/3.
8. Paper is Shazeer 2020: GLU are consistently better than non-GLU, and Narang et al 2020.
9. GLU not neeeded (GPT3), but does a nice boost.
10. Nemotrons 340B: Squared ReLU

## Serial vs Parallel Layers
1. Parallel isn't as popular.
2. What if MLP and MHA in parallel.
3. x + MLP(LayerNorm(x)) + Attention(Layernnorm(x))
4. GPTJ and PaLM have propogated new ideas, PaLM uses it, it was introduced by GPTJ
	1. Cohere, Falcon2, and Command R+ use it
5. Fallen out of popularity
	1. optimization of the serial form, the gain isn't as good, since there are small hits.
	2. Lost half of the depth

## Summary
1. Pre > post-norm
2. RMSNorm > LayerNorm
3. Gating (GLU is the consensus)
	1. Serial > Parallel Layers



## Positional Embeddings
1. sine embeddings (original)
2. absolute embeddings (GPT 1/2/3, OPT)
3. relative embeddings: add a vector to attention computation (T5, Gopher, Chinchilla)
4. Rope embeddings (dominant, most 2024+ embeddings, GPTJ, PaLM, LLaMa. GPTJ innovation from a random blog post and paper computation

### Relative Positional Embedding:
1. Idea - don't care about absolute position.
	1. f(x, i), such that dot <f(x, i), (f(y,j)> = g(x,y, i-j)
2. Attention function only epends on the relative position.
3. Sine:
	1. various cross terms that are not relative
4. Absolute, not relative
5. Relative embeddings: not an inner product, just adding to attentoin matix
6. Solution Idea:
	1. Inner products are invariant to arbitrary position.
	2. Takes the semantic word vectors, and rotate each word based on its position.
	3. Rotating the words doesn't affect the inner product.
7. High dimensional:
	1. cut up the d dimensions into rows of 2, and rotate each of them.
	2. the amount they rotate depends on which group of 2.
	3. rotate the query and keys 
8. Gemma only rotates the first two coordinates. (P-rope).

===reading a single paper in isolation is hard===

===papers vary in terms of their findings: PaLM is very confident about parallel layers, no performance drop, 15% speedup===
# Hyperparameters
1. How much bigger should FF be compared to hidden size?
2. how many heads?
3. what should vocab size be?
4. do people regularize?
5. deep model vs wide models?
  
space of things that people try is pretty small.


### Consensus Hyperparam 1: FF Ratio
1. FF size is 4 times d model. this is almost always true.
2. works well - this is a fine number to choose.
3. exception 1:
	1. GLU variants: scale this down by 2/3 (2.5 (T5)- 3.5 (LLama-2, which emphasizes MLP a bit more.))
	2. PaLM = 4.
4. Exception #2 - T5:
	1. T5 have insane isettings:
		1. dff = 65536, 1024 (64 ratio)
		2. this is because TPUs are efficient.
	2. Gemma 2: 8x
	3. Gemma3/4: 4x at GLU.
5. Empirically, the best ratio (kaplan 2020, neural scaling laws, 50M parameters), the basin is between 1-10 (fixed number of parameters at 50M. 10-100 is bad).
6. Default choice is dff = 4d_model, dff = 2.66d_model
7. T5 v1.1 - that is improved and uses 2.5 multiplier on GeGLU.
### Consensus Hyperparameter 2: 
1. head dim to model dim ratio:
2. num heads times head dim = model time.
3. GPT3 = 128 head eim, 96 heads, model time 12288, ratio = 1.
4. T5 has 1024 as model time, PaLM has 18432 as model dim
5. LLaMA2 has 8192 as model time.
6. T5 = 16, T5 v1.1. goes back to 1.
7. LlaMA2 is 1.
8. forgiving hyperparameter.


### Aspect Ratios
1. d model / n_layer.
2. the sweet spot is aroud 100 ? (GPT3/OPT/Mistral/Qwen), 128 d_model/n_layer

### Depth
1. Varies much more than other hyperparamters.
2. Models don't go too deep.
3. model's don't go too wide.
4. 100 d_model / n_layers.
5. Deep models are harder to parallelizer, high latency.
6. If you pipeline parallel (cut up layers into GPUs)
7. width is a lot easier (tensor parallel).
8. Deep = epxressive.
9. Kaplan 2020:
	1. Aspect ratio: 10 / 100, around 100 is good.


### Vocab sizes
1. Original: 37000
2. GPT2/3: 50257:
3. T5: 32128
4. LLaMA: 32000
5. Deepseek: 100,000
6. Qwen: 152064.
7. Google models usually have more vocab.
8. Bigger the model, larger vocab it can handle.


# Regularization
### Arguments against:
1. lots of data, more than parameters.
2. SGD only does a single pass on a corpus, hard to memorize
3. some even only look at training loss

## In practice
1. Older models used dropout during pretraining
2. New models rely only on weight decay (popular)
3. people don't really use dropout

### weight decay
1. papers argued and shown that weight decay is not a regularizer sometimes, but really interacts with the optimizer to make it better.
2. weight decay doesn't solve overfitting, validation loss looks fine.
3. But, weight decay plus learning decay do better: they start out slow, but converge to a better minimum later
4. changes throughout training with learning rate.




# Stability
1. very big emphasis recently
2. don't want it to get to a point where it cannot be trained further.


## Softmaxes
1. ill behaved due to division by zero or exponentiation.
2. found at the output side, and another where we normalize the attention.


### Z loss
1. z loss - output softmax.
	1. encourage F
	2. Baichuan, DCLM, OLMo 2, OLMo 3.
	3. $logP(x) = log(e^U_r(x) / Z(x))$ 
	4. $U_r(x) - \log(Z(x))$ 
	5. log(Z(x)) might be ill-behaved.
	6. want Z near 1, or log(Z) near 0
	7. softmax is overparametrized, you can add a constant to U
	8. regularizer : 10^(-4)*log^2(Z) penalize this loss
	9. prevents really small too (if Z is realy small, log is very negative)

### QK Norm
1. Add in a layer norm before multiplying the Qs and Ks
2. Q and K are RMS normed before going into softmax - keeps softmax stable.
3. very standard
4. doesn't affect performance
5. prevent attention degeneracies
6. add layernorm after nonlinearities, throwing them in Qs and Ks

### Logit Soft Cap (not as a popular)
1. cap off the logits: logits = soft_cap * tanh(logits/softcap)
2. Gemma, 2, 3, 4.
3. some performance issues though?
4. QKNorm does a little better
5. soft capping alone loses performance.
6. cannot express very confident signals.

# Attention Heads
1. most model don't touch attention heads
2. GQA / MQA - group query and multi-query (most models)
3. Sparse/sliding window attention.
4. Exotic SSM stuff  - next lecture


### Compute

1. need to pay for FLOPs (compute) and also memory.
2. projection: total arithmetic operation is roughly batch size  * sequence length * hidden dim squared:  
3. Arithmetic intensity = compute/memory
4. Need a KV-cache: maintain a matrix of QK^T. 

### KV-Cache
1. only used during generation
2. Store K and V for previous inputs
3. then a new token comes you just compute the Q, and then dot it with all the Ks, and weighted average with all the Vs.
4. bad for computational intensity - n*d*2 for the memory accesses.

### MQA:
1. share the K and V across all the heads, and only thing that are the same are the queries
2. KV cache is significantly smaller.
3. ask different questions, the knowledge is still the same.
4. increases arithmetic intensity, makes KV-cache smaller.
5. loses significant expressive power
6. MLA - deepseek v2 - sweet spot.

### GQA:
1. reduce number of values and keys, many query heads gets grouped to the same key and value.
2. GQA trade off is kind of favorable, small performance hit.
3. almost as fast as MQA, almost as good as MHA

### Sliding window attention
1. GPT3, GPT-OSS, Gemma4
2. alternate big attention and a local attention
3. cohere comand A: every 4th layer is a full attention, 3 layers in between have sliding window attention.
4. embedding format - get rid of things like rope for long range information.
5. LLaMA 4, Gemma 3, Gemma 5, OLMo 3 does SWA+Full RoPE
6. Qwen 3.5 - alternate a state space gated delta net model, and a full attention.