# Introduction to the TAs
1. Percy Liang
	1. Used to do small Language Models
2. Tatsu
3. Marcel
	1. 2024 TA
	2. Architecture stuff, higher order gradients training
4. Herman
5. Stephen - first time CA, LLMs, data efficiency.

# Why this course?
Modern LM ingredients - MoE, long context, agents.


Timeline
1. 2016 - researchers get their own model
2. 2018 - researchers fine tune models
3. Today - researchers prompt models

Abstractions are Leaky though.

Fundamental research - need to tear up the whole stack.

Industrialization - GPT-4 - cost 100M to train, nowadays 1 Billion
2025: 230k GPUs training Grok.


Small language models: <1B - maybe not representative
1. At small scales: MLP = 44%
2. large scales: 80%

### Emergence
Emergence happens at larger scale (10^22 training FLOPs)
A - Modular arithmetic
B - Word unscramble
C - Persian QA
D - word in context
Critical scale required for improvement


### Things that do transfer:
1. mechanics (how things work, model parallelism)
2. mindset (squeezing hardware, scaling)
3. intuitions (data and modeling decisions)
	1. can only partially teach, doesn't necessary transfer across scales.
	2. comes from experimentations - some design decisions are just not justifiable (e.g. SwiGLU - divine benevolence)

### Bitter Lesson:
1. Wrong interpretations: scale is all that matters, algorithms don't matter
2. Correct interpretation: algorithms that scale are what matter

### Efficiency is Important
- accuracy = efficiency x resources. Efficiency is way more important at larger scales.c
- Hernandez 2020 - 44x algorithmic efficiency improvement on imagenet between 2012 and 2019. maximize efficiency!


**Pretraining:** Compute Budget Matters
- Way more data than compute

**Data Bound** - Might be different.


# Current LM landscape

### Before 2010s:
1950 - LMs to measure the entropy of English
N-grams models are used in speech recognition and machine translation

### 2010s:
- LSTM: 1997
- Neural Language Model: Bengio (feedforward network on context)
- Seq2Seq: compress a sentence into  vector
- Adam
- Attention (2014)
- Transformer (2017)
- mixture of experts (shazeer 2017)
- model parallelism (huang 2018)
### Late 2010s
- ELMO (LSTM, pretrained, finetuning improves downstream tasks) (Peters 2018)
- BERT + fine tuning (Devlin 2018), on QA
- T5: 11B: cast everything as text to text (Raffel 2019)

### Embracing Scaling
- OpenAI GPT-2, 1.5B, fluent text, zero-shot (Radford 2019)
- Scaling Laws (Kaplan 2020)
- GPT-3: 175B (in context learning, Brown 2020)
- PALM (540B): massive scale, undertrained (2022)
- DeepMind: 70B: compute-optimal scaling laws (Hoffman 2022)


### Open (Weight) Models 
- Replicating GPT-3
	- Eleuther  (The Pile, GPT-J) (2020/2021)
	- Meta OPT: (175B) lots of hardware issues (2022)
	- HuggingFace (176B) data sourcing BLOOM (2022)
- Better models:
	- Meta Llama (2023)
	- Mistral (2023/2024)
	- Deepseek
	- Alibaba Qwen (missing a lot details, data mixture)
	- Kimi
	- GLM
	- Minimax
	- Xiami
	- ByteDance
	- Tencent
	- Approaching closed source

### Open Source Models (Code, etc.)
- AI2, Olmo (2024)
- NVIDIA Nemotron (2024/2025)
- Marin (open development) (8B/32B)

Openness is important for trust and innovation (Kapoor 2024)

# What is a language model?
- 2018: something you fine tune (BERT)
- 2020: something you prompt (GPT-3)
- 2022: something you talk to (ChatGPT)
- 2026: agents (very strong)
The fundamentals are still the same: attention, kernels, optimization, transformer.

Specs are different: longer context, inference efficiency matters




# Executable Lectures
- Execute a program that you step through to execute the lecture
- Step through code
- See hierarchical structure

# Course Logistics
- All info online
- 5 unit class
- 5 intense assignments
- First assignment was the first 5 assignments from CS 224N
- Why you should take it
	- obsessive need to understand how things work.
	- build up research engineering muscles
	- Statistical Learning Theory - first course from Percy , but field has shifted to systems/empirical side, but this course will give you enough depth to make things easier
- Don't take it
	- research needs to get done
	- interested in learning hottest new techniques (take a seminar for RAG, agents, multimodality)
	- Want to get good results on your own application domain

# Following online at home
 - Lecture materials and assignments are online
 - Recorded via CGOE -> YouTube


# Assignments
1. (basics, systems, scaling laws, data, alignment)
2. no scaffolding code, but yes unit tests
3. implement locally to test for benchmarks, then run on cluster for benchmarking
4. leaderboard for some assignments (minimize perplexity given training budgets)


# AI Policy
1. Coding agents will solve all the assignment, but won't learng anything
2. useful for tutoring
3. AGENTS.md asks the AI to be pedagogically minded
4. AI policy guide

# Compute
1. modal provides compute
2. there's a guide


# Syllabus
1. Basics (first two weeks)
	1. Tokenization
		1. What are the atoms that the model operates on?
		2. Bytes -> sequences of integers
		3. BPE tokenizer (1000 bytes -> 250 tokens)
		4. Adaptive computation, model capacity used on interesting parts of the input
		5. The dream: tokenizer-free model architectures, operating directly on bytes (Xue 2021 - Hwang 2025)
	2. Model architecture
		1. Original transformer: Vaswani 2017
		2. Refinements:
			1. ReLu, SwiGLU
			2. Positional Encoding: sinusoidal, RoPE
			3. Normalization: LayerNorm, RMSNorm, QKNorm, pre-norm vs post-norm
			4. Attention: Full, sparse/local, group-query, multi-head latent attention, n2
			5. Linear attention: Mamba, GatedDeltaNet
			6. MLP: Dense, MoE
			7. Shape (hidden dimensions, depth, number of heads, number of experts)
	3. Training
		1. Loss function (e.g. multitoken prediction)
		2. Optimizer (AdamW, SOAP, Muon)
		3. Initialization Scale (Xavier init, muP)
		4. Learning rate schedule (cosine, WSD)
		5. Regularization (dropout, weight decay)
		6. Batch size (critical batch size)
		7. MoE specific: load balancing
	4. Assignment 1:
		1. Implement BPE tokenizer
		2. implement transformer, CE loss, AdamW, training loop
		3. resource accounting
		4. TinyStories and OpenWebText
		5. Leaderboard: Drive down perplexity on OpenWebText
	5. Principles:
		1. Balance expressivity, stability (grad norms in goldilocks), and efficiency (run fast for training and inference)
2. Systems (Kernels, parallelism, inference)
	1. Resource Accounting
		1. memory
		2. compute
		3. how many FLOPS is trainig a 70B parameter model on 1T tokens?
			1. roughly 6 * 70e9 * 1e12 (6 times number of params * num tokens)
				1. (is it multiply + add for forward, multiply/add backward, and two optimizer moment updates?)

		4. Memory to compute bottlenecks:
		5. B200: 2.25 PFlops per second at bf16, 8TB/sec memory
		6. Roofline analysis: compute or memory bound (usually memory bound)
		7. Benchmarking/Profiling
		8. DGX: b200:
			1. NVLInk connects 8 GPUs
			2. infiniband or ethernet connects multiple nodes
	2. Kernels:
		1. PyTorch primitives launch particular kernels
		2. you can write custom kernels to make GPUs go brrr
		3. organize compute to minimize data movement
		4. Naive: read HBM:. compute A;, write HBM; read HBM;, compute B, write HBM.
		5. Fused: read HBM;, compute A + B, then write it back.
		6. Tiling (FlashAttention)
		7. operator fusion: (Matmul + activation)
		8. Warp divergence, memory coalescing, bank conflicts, occupancy, bulk-async memory tranfers
		9. Write kernel in CUDA/Triton/CUTLASS/ThunderKitten
	3. Parallelism:
		1. 1024 GPUs?
		2. Minimize data movement, but moving data between diff GPUs is more expensive
		3. classic collective operations (gather, reduce, all reduce) - distributed training
		4. Shard memory across GPUs (params, activatoins, gradients, optimizer states)
		5. How to split computation (data, tensor, pipeline, sequence, expert) parallelism.
	4. Inference:
		1. Generate tokens given prompt
		2. Need for RL, test-time compute, evaluation, synthetic data
		3. Two phases: prefill and decode
			1. prefill: tokens are given, process all at tonce
			2. decode: one token at a time, memory bound
		4. Cheaper model: (distilllation, pruning, quaniztionat)
		5. spec dec:
			1. cheaper draft model generate multiple tokens, then evaluate likelihood or top-1
		6. systems optimization: fused kernels, continuous batching.
		7. inference: queries are coming at different times, how do we batch them up?
	5. Assignment 2:
		1. RMSNorm kernel in Triton
		2. Distributed data parellel
		3. optimizer state sharding
		4. benchmark/profile implementations
	6. Recommended book: How to scale your Model:
		1. how to approach systems for LLMs conceptually
		2. Foregrounds TPUs, but high-level concepts are similar.
3. Scaling Laws
	1. 1e25 FLOPs (10s of millions of dollars), what model would you train? what hyperparams?
	2. Instead of a single scale, think scaling recipe: FLOPs -> hyperparams
	3. Run experiments to compute the loss at smaller scales, and fit a scaling law to figure out the hyperparams at the target scale.
	4. Now
		1. optimize the scaling recipe targeting larger scale using smaller scale expeimrents
		2. predict the loss at the target scale before running experiment (this lets us raise money)
		3. Scaling laws don't happen automatically, they require a careful construction of scaling recipe, parameterize your hyperparmas a s  a function of scale
			1. the thing that mattered were model size, data amount, learning, and batch size
			2. need hyperparameter transfer from small to large scales.
		4. predicability is as important as optimality:
			1. want to get the most info gain from scaling law experiments
	5. Question: given a FLOPs budge (C = 6 N D), use a bigger model or train more tokens?
		1. compute optimal curves (Kaplan, Chinchilla 2022)
		2. Fix a FLOP budget, sweep across different model sizes, choose the best one that intersects the min:
			1. The red lines are the fit scaling laws, the black ones are the minimums for each U shape
			2. 
	6. ![[Pasted image 20260727161132.png]]
	7. D = 20N: 70B model should be trained on 1.4T tokens.
	8. You want to the model to be small to minimize inference costs anyway, so the optimal model is smaller than the training FLOP budget
	9. Assignment 3:
		1. hyperparameters -> loss based on previous runs.
		2. submit training jobs under a FLOPs budget, gather data points
		3. Fit scaling laws to the data points
		4. Submit real extrapolated hyperparams and loss predictions
		5. Leaderboard: minimize loss given FLOPs budget
4. Data
	1. What capabilities do you want the model to have?
	2. Evaluation:
		1. Purpose
			1. Internal: Guide model development (smoothness across scales, relative performance matters, e.g. training loss)
			2. External: real use case
		2. Examples:
			1. Perplexity (run on things not on the internet)
			2. Advanced used cases (GPQA, HLE, SWE-bench, Terminal-bench)
		3. LMs are general purpose, requires diverse evaluations!
	3. LMs require a diverse set of evaluations: don't average too many things into one thing.
	4. Curation:
		1. outside of classes, data is not just given to you
		2. webpages crawled from the internet, books, arXiv papers, github code, etc.
		3. 2021: "The Pile".
		4. Fair use to train on copyrighted data?
		5. License data (google with reddit data) 
		6. raw data is HTML, PDF, or directories (requires processing)
		7. transformation:
			1. nontext into text
		8. filtering keep high quality data
		9. dedup (bloom/minhash)
		10. Data mixing (how much to upweight/downweight each source)
		11. rewriting/synthetic data (use LM to augment real data, more similar to downstream tasks)
	5. Pretraining: large and diverse
	6. midtraining: high quality at end of pretraining (long context data, code repos, boooks)
	7. post-training (SFT, conversations, agentic transfers with tool calling)
	8. Assignment A4:
		1. Convert common crawl HTML to text
		2. train classifiers to filter for quality and harmful context
		3. dedup musing minhash
		4. Leaderboard: minimize perplexity given token budget.
5. Alignment
	1. weak supervision (not full token sequences)
		1. why? easier to critique than generate
		2. don't have GT answers
	2. generate responses, score responses (human, verifier, LM)
	3. update the model to prefer better responses
	4. Algorithms:
		1. PPO
		2. DPO
		3. GRPO
	5. Challenges:
		1. RL algorithms are unstable and hard to tune
		2. new infrastructure (async rollouts)
		3. constantly trading off systems efficiency and on-policy-ness
	6.  Assignment 5: alignment:
		1. Implement DPO
		2. Implement GRPO


# Efficiency:
1. data + hardware (compute, memory, communication bandwidth)
2. how to build the best model given a fixed set of resources
3. all about efficiency
	1. tokenizer
	2. architecture
	3. data filtering - bad data might not hurt you, but means less time on good data
	4. scaling laws - hyperparam tuning on smaller models.


# Tokenization
1. Text is represented as unicode strings (assigns number to every character)
2. Observations:
	1. a word and preceding space are part of the same token
	2. word at the beginning and middle are represented differently (e.g. "hello, hello").
	3. numbers are tokenized into every few digits (some tokenizers make every digit a token)
	4. GPT-tokenizer (tiktoken)
	5. human vision based, no need for tokenizer.
	6. tokenizers should round trip
3. Compression ratio: number of bytes per token
4. Larger compression ratio = shorter the sequence.
5. increasing compression ratio by increasing vocab size, but this increases sparsity.
6. tokenizers have 100k or 200k unique, distinct tokens.


### Character Tokenization
1. unicode string -> unicode character each character is an integer (ord)
2. character level tokenizer - there are 150k unicode characters, vocab size is 150k, that is a lot.
3. many characters are quite rare, inefficient use of the vocab
4. compression ratio is not great: using a lot of tokens (1.5)

### Byte tokenizer
1. a string is 1 byte or multiple bytes.
2. vocab size is 256
3. compression ratio is 1


### Word tokenizer
1. split strings into words (by spaces, or other regex)
2. good: each token is meaningful.
3. vocab size = number of unique chunks in the training data
4. compression ratio is good, but vocab size is too big
5. many words are rare, model won't learn
6. vocab is unbounded - not complete (unk token)
	1. can use word + character.


### BPE
1. Gage, Phillip: 1994
2. adapted to NLP 2015.
3. BPE was used by GPT-2
4. Idea: train the tokenizer on raw text
5. Intuition: common sequences are represented by a single token, rare are represented by many
6. Sketch: start with each byte as a token, and succcesively merge the most common pairs of adjacent tokens.
7. Compression

##### Training
1. find the pair that happens the most often
2. merge the pair, new token (called token 256), representing the new pair, add to vocab, and merge the corpus.

##### Inference:
1. go through all merges that you made, then apply the merges to your string.
2. don't loop over all the merges
3. detect and preserve special tokens
4. use pre-tokenization (break text into chunks)
5. try to make implementation fast
6. Rust or C is way faster

### Getting rid of tokenization?
1. model, transformer needs to operate on abstractions of the sequence
2. lengths should be variable.








Stuff to add to coding questions:
- Muon
- KV-Cache
