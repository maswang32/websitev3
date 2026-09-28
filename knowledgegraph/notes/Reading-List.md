# Dump
- [ ] imagination models: https://x.com/induction_labs/status/2080322704973160760?s=46
- [ ] surya ganguli: https://x.com/suryaganguli/status/2080785091685748808?s=46
- [ ] LLM history: https://x.com/waterloo_intern/status/2081762065392541951?s=46
- [ ] KDA: https://x.com/iamgrigorev/status/2081763587488362888?s=46
- [ ] LLMs can't jump: https://openreview.net/challenge?redirect=%2Fpdf%3Fid%3DklU4737opt
- [ ] andrew ho last post: https://x.com/andrewho03/status/2082615798011744270?s=46
- [ ] matrices as objects: https://x.com/mpoilerfx/status/2082650120328188144/video/1?s=46
- [ ] regularization in RL: https://x.com/shikhargupta02/status/2082549694077817140?s=46
- [ ] explorative modeling: https://x.com/alexiglad/status/2083230922196107288?s=46
- [ ] continual learning predictions: https://x.com/dwarkesh_sp/status/2085781456375218232?s=46
- [ ] dual form of NN: https://x.com/osieberling/status/2091278962001391974?s=46
- [ ] scaling laws: https://x.com/_yusufknl/status/2090429393139097948?s=46
- [ ] deep learning with python: https://x.com/fchollet/status/2091921787978445119?s=46
- [ ] DP, TP, SP:
    - [ ] DP - everyone gets a whole copy of the book, different sequences/sessions, gradients averaged a the end.
    - [ ] TP - each GPU gets a slide of every weight matrix, they work together for computation
    - [ ] SP - sequence parallel - spilt the sentences, each sequence gets split
- [ ] drift models
- [ ] reasoning in continuous space
- [ ] the old world is dying: https://x.com/jasminewsun/status/2064830753264046100?s=46
- [ ] RLHF: https://x.com/neural_avb/status/2064767466900009313?s=46
- [ ] GRPO: https://x.com/neural_avb/status/2065097728393367794?s=46
- [ ] robotics from first principles: https://x.com/sean_pixel/status/2064766757806760405?s=46
    - [ ] https://x.com/retr0jirachi/status/2066383384381984856?s=46
- [ ] how to be good at research: https://x.com/itsreallyvivek/status/2064686372737454155?s=46
- [ ] On policy self distillation: https://x.com/dwarkesh_sp/status/2062353335529935114?s=46
- [ ] biological neurons: https://x.com/jeffdean/status/2065471716734996823?s=46
- [ ] OPSD: https://x.com/ar0cket1/status/2054108160450064571?s=46
- [ ] how to read a paper: https://x.com/paperpaper886/status/2066148829439861016?s=46
- [ ] zen: https://x.com/jxmnop/status/2066668040557867368?s=46
- [ ] GLM 5.2
- [ ] karpathy tutorial: https://x.com/0xmortyx/status/2066878111124250739?s=46
- [ ] fix your life in one day: https://x.com/thedankoe/status/2010751592346030461?s=46
- [ ] sample efficiency: https://x.com/sirbayes/status/2068071851990151377?s=46
- [ ] the most human technology ever made: https://x.com/iidydwns/status/2077188443084644748?s=46





# Interview Reading List
- [ ] Things I should know from xAI
    - [ ] What is the scale of pretraining data in terms of number of hours?
- [ ] Whisper
- [ ] Review an image is 32 tokens
- [ ] PPO
- [ ] GRPO
- [ ] On-Policy Distillation (TML Blog Post)

## Slightly Less Essential
- [ ] DeepSeek Math
- [ ] DeepSeek R1
- [ ] Kimi K3
- [ ] Transfusion
  - [ ] Multimodal Pretraining: https://x.com/tongpetersb/status/2029237530160169286?s=46
- [ ] Flow Matching


## Interview Questions
- [ ] RL Interview Questions 2026:
  - [ ] https://x.com/sheriyuo/status/2063295181131247674?s=46
  - [ ] https://x.com/neural_avb/status/2063957500114960592?s=46
  - [ ] Answers: https://x.com/pradheepraop/status/2063736553357394025?s=46


















































# To write down
- [ ] math trick with fractions, 1 - a / (a + b) = b / (a + b)
- [ ] Interaction models
- [ ] GPT-Live

# Questions
- [ ] What is an hMLP?
- [ ] What audio tokenizer does TML use?
- [ ] LLM Tokenization: what is bits per byte?
- [ ] when you have like dx = dy, what lets you integrate both sides? If you integrate the RHS from 0 to T, what are the limits of the integral on the RHS?
- [ ] Why does PSD imply convex?
- [ ] What is the meaning of log probability in machine learning? Is there something about 'encoding the information in a distribution'?
- [ ] Not sure about 'independent errors' assumption for modeling multidimensional distributions.
- [ ] Information theory - why do we care about encoding sequences of events?
- [x] Why is it bad that the normalizing constant is not tractable?
  - [ ] Answer: because you can increase the probability of your data distribution arbitrarily
- [x] Under the KL divergence interpretation of NLL, what about the input variable?
  - [ ] Answer: It's the KL divergence for a fixed input. As in, in a regression problem, imagine that for one input we observe multiple outputs. Then it's the KL divergence for those outputs vs. the model's predicted distribution for that input. Or, P(y|x) compared to the distribution over y|x.
- [ ] For diffusion ELBO, what does it mean when we say: changing its parameters so that the static encoder does approximate the posterior
- [ ] Why is KL positive?
- [ ] forward vs reverse KL, mode-seeking vs mode-covering
- [ ] KL vs. dimensionality






# General Reading List


## Things to keep up-to-date with
### Podcasts
- Dwarkesh
  - Dario
  - Jensen Huang
  - Rainer Pope
- Latent Space Podcast
- Last Week in AI Podcast

### YouTube Channels
- 3BlueOneBrown
- Veritasium

### Social Media
- X 
- r/machinelearning
- r/learnmachinelearning

## Long Content
### Books
- [ ] Understanding Deep Learning
    - [x] Chapter 8, main text
- [ ] Deep Learning Book
- [ ] Scaling book: https://jax-ml.github.io/scaling-book/

#### Less Important
- [ ] Principles of Deep Learning Theory: https://x.com/k_solidified_/status/2069781542306775063?s=46
- [ ] Information Theory Book

### Classes
- [ ] CS 336
- [ ] Deep Learning, MIT class
- [ ] CS 285L, Berkeley Deep Learning Course.
- [ ] CS 231
- [ ] CS 224N
- [ ] CS 229 review
- [ ] MIT Diffusion Class
- [ ] Signals and Systems
- [ ] I Climb Trees


#### Less Important
- [ ] Robot Learning Course: https://x.com/oier_mees/status/2064734602535612513?s=46
- [ ] https://deepgenerativemodels.github.io/





## One-off-Content

### Videos
- [ ] 3blue one brown information theory and LLMs
- [ ] Yann Lecun: https://x.com/chrisoffner3d/status/2064320485559599247?s=46
- [ ] AMI Labs, Saining Xie interview
- [ ] How We Scaled KIMI 2.5: https://www.youtube.com/watch?v=CwePo4847ho
- [ ] How do LLMs work? Stanford lecture: https://x.com/polydao/status/2063569155677098429?s=46
- [ ] Princeton Lecture on Random Matrices: https://x.com/mpoilerfx/status/2082650120328188144/video/1?s=46
- [ ] Bill Freeman: CVPR Talk
- [ ] Data Efficiency: Dwarkesh: https://x.com/dwarkesh_sp/status/2068019716849815869?s=46
- [ ] RL is reverse KL, Nathan Lambert: https://x.com/shikhargupta02/status/2082549694077817140?s=46
- [ ] Continual Learning Predictions: https://x.com/dwarkesh_sp/status/2085781456375218232?s=46
- [ ] Backprop video - Artem
- [ ] Karpathy - LLM Coding
- [ ] Ilya podcast: If it's so well trained, then it's not that smart.
- [ ] Jeff Dean on latent space podcast
- [ ] Kaiming research philosophy according to Xie
- [ ] Zhilin GTC 2026 keynote on scaling Kimi


### Blog Posts, X Posts, or Papers

#### Advice:
- [ ] Career Advice in the age of AI: https://x.com/himanshustwts/status/2072942463548072006?s=46
- [ ] Biggest Disadvantage is biggest advantage: https://x.com/iampascio/status/2068631757784568094?s=46
- [ ] 100 mental models
- [ ] How to change your life in one day
- [ ] Risk is misunderstood: https://x.com/zarazhangrui/status/2068522129193418759?s=46
- [ ] The cost of staying: https://x.com/amytam01/status/2023593365401636896?s=46
- [ ] Ziming Liu: Blue-ocean opportunities in AI
- [ ] Professor Jiang: https://x.com/kelechisp/status/2093035153983504429?s=46
- [ ] Steve jobs: https://x.com/kelechisp/status/2093035153983504429?s=46
- [ ] Digital Renaissance: https://x.com/thedankoe/status/2093051293078261973?s=46
- [ ] How to win without being the best: https://x.com/Daywrotethis/status/2093191889944232234?s=46
- [ ] Rachmaninoff: https://x.com/Gena_I_Gorlin/status/2093103339718230133?s=46
- [ ] Capital Legibility: https://x.com/nikunj/status/2092748226701210023?s=46
- [ ] Learning Faster: https://x.com/0xHvdes/status/2094075106096009695?s=46
- [ ] Doing better work: https://x.com/MaxTorchbearer/status/2093863687119352251?s=46


#### AI
- [ ] Visualization of Gradient Descent Methods: https://towardsdatascience.com/a-visual-explanation-of-gradient-descent-methods-momentum-adagrad-rmsprop-adam-f898b102325c
- [ ] Flow matching
- [ ] DINO
- [ ] SigLIP
- [ ] Whisper
- [ ] Adam
- [ ] ODISE
- [ ] SAM
- [ ] Presto
- [ ] DDIM/SDE interpretation
- [ ] EDM
- [ ] 26 essential papers
- [ ] All elementary functions from a single operator
- [ ] Self-Distillation Zero
- [ ] Language model harnesses are compositional generalizers: https://x.com/a1zhang/status/2079203524395573442?s=46
- [ ] Recursive Language Models
- [ ] Tool Shaped Objects: https://x.com/willmanidis/status/2021655191901155534?s=46
- [ ] Oliver Sieberling: "A very interesting observation on backpropogation is..."
- [ ] Hanchen li: self improving AI reflections
- [ ] Ilya's reading list: https://github.com/dzyim/ilya-sutskever-recommended-reading
- [ ] paperswithcode most cited
- [ ] Andrew Ho's Startup Post: https://x.com/andrewho03/status/2082615798011744270?s=46
- [ ] Can LLMs be computers? https://www.percepta.ai/blog/can-llms-be-computers
  - [ ] Also see X post from Christos Tzamos
- [ ] Wave Field Lab
- [ ] Scaling Laws: https://x.com/lilianweng/status/2070237256070389897?s=46
- [ ] Unconventional AI image generation: https://x.com/naveengrao/status/2070184079199494583?s=46
- [ ] Test-Time thinking: https://lilianweng.github.io/posts/2025-05-01-thinking/
- [ ] Sutton letter
- [ ] LLMs can't jump: https://openreview.net/pdf?id=klU4737opt
- [ ] Explorative Modeling: https://x.com/alexiglad/status/2083230922196107288?s=46
- [ ] mHC
- [ ] Video model tokenization: https://x.com/majumdar_ani/status/2067619531124506742?s=46
- [ ] Hierarchical Reasoning Models
- [ ] Tiny Reasoning Models
- [ ] Frechet Distance
- [ ] Patchwise Diffusion
- [ ] Score-Based generative models: https://yang-song.net/blog/2021/score/
- [ ] Stable Diffusion
- [ ] VQVAE - Autoregressive coding
- [ ] Auto-Encoding Variational Bayes
- [ ] Scientific Theory of deep learning: https://x.com/learning_mech/status/2047723849874330047?s=46
- [ ] Group testing, Amin Karbasi
- [ ] why we think


#### Generative Models
- [ ] instruct prompt2prompt
- [ ] instruct pix2pix
- [ ] dreamfusion
- [ ] classifier-free guidance
- [ ] ELBO: https://yunfanj.com/blog/2021/01/11/ELBO.html
- [ ] Diffusion: https://calvinyluo.com/2022/08/26/diffusion-tutorial.html
- [ ] RF inversion
- [ ] Cross-attention-based condition editing


#### LLM Setup/Architecture
- [ ] KV-Cache
- [ ] LoRA
- [ ] mamba
- [ ] A Weird Thought About Transformers
- [ ] Linear Attention
- [ ] DeltaNet
- [ ] Qwen
- [ ] KDA :https://x.com/iamgrigorev/status/2081763587488362888?s=46
- [ ] Attention Residuals
  - [ ] Attention Residuals revisted
- [ ] Looped Transformers: https://x.com/ridgerzhu/status/2046736781035618602?s=46
- [ ] Energy Transformers
- [ ] NoPE
- [ ] Nested Learning
- [ ] Continual Learning
- [ ] Latent Reasoning
- [ ] andrej karpathy video on tokenization
- [ ] Mesa Layer
- [ ] Native sparse attention
- [ ] Deepseek series
- [ ] screening
- [ ] mechanistic interpretability
- [ ] ziming liu - blue ocean opportunities in AI
- [ ] how LLMs really work: https://x.com/anuragdotdev/status/2093697517481517323?s=46
- [ ] agent civilizations: https://x.com/dwarkesh_sp/status/2093833419377815719?s=46
- [ ] Scaling laws: https://x.com/_yusufknl/status/2094528020610719767?s=46
- [ ] Kimi R1


#### World Models
- [ ] World action model
- [ ] LeWorld Model
- [ ] JEPA reading list: https://x.com/abdelstark/status/2064298937939378420?s=46


#### Anthropic Posts
- [ ] Project glasswing: https://www.anthropic.com/institute/recursive-self-improvement
- [ ] Circuit Tracing
- [ ] Mechanistic Interpretability



#### RL
- [ ] GDPO
- [ ] Ouyang
- [ ] RLHF
- [ ] DPO
- [ ] PPO
- [ ] SFT
- [ ] RLHAIF


#### Physics/Stats/Math
- [ ] Surya Ganguli Physics: https://x.com/suryaganguli/status/2079521732915065007?s=46
- [ ] History of LLMs: https://x.com/waterloo_intern/status/2081762065392541951?s=46
- [ ] Interpreting the determinant in terms of volume, determinant of jacobian
- [ ] two sided vs one sided tests
- [ ] 6.5 interpretations of KL divergence


#### DSP
- [ ] Window method
- [ ] PM method
- [ ] aliasing
- [ ] Downsampling and upsampling
- [ ] Pole zero graphs
- [ ] MFCCs
- [ ] Formants
- [ ] PQDM
- [ ] Cosine as a differential equation - the second derivative is related to the value. exponential is where first derivative is equal to the value.


#### AI Coding
- [ ] Claude Skills: https://x.com/polydao/status/2060715587387400424?s=46
- [ ] Andrej Karpathy AI Coding: https://x.com/0xchromium/status/2063321324605280569?s=46
- [ ] Claude + Obsidian: https://x.com/chewadot/status/2071564521735684253?s=46



#### Speech-to-Speech Models
- [ ] QwenOmni
- [ ] KAME
- [ ] MoshiRAG
- [ ] PersonaPlex


#### Audio Papers
- [ ] Next scale prediction for audio
- [ ] Conformer paper: https://arxiv.org/pdf/2005.08100
- [ ] Physical Modeling: https://www.youtube.com/watch?v=hw9bWnDei-k
- [ ] what is a vocoder?
- [ ] Jukebox
- [ ] Wavenet
- [ ] tacotron
- [ ] how many CNN layers does it take to compute a spectrogram?
- [ ] Hubert
- [ ] Wav2vec
- [ ] w2v-bert
- [ ] ICMC best paper


#### Software
- [ ] Model size vs peak usage
- [ ] PyTorch lightning: https://pytorch-lightning.readthedocs.io/en/0.9.0/lightning-module.html
- [ ] omegaconf (an interpolation is a placeholder value in omegaconf, resolve=True fills in any interpolations)



#### Less Important
- [ ] LLM Arch:
  - [ ] The Neuroscience of Transformers
  - [ ] Transformers are Bayesian Networks
  - [ ] Functional Attention: https://x.com/phoenixyin13/status/2069953027931255247?s=46
  - [ ] Canon Layers
  - [ ] Native Sparse Attention
- [ ] Scientific Theory of Deep Learning: https://x.com/learning_mech/status/2047723849874330047?s=46
- [ ] Mesa Layer: https://x.com/googleresearch/status/2047630714145776053?s=46
- [ ] OpenClaw RL
- [ ] Amin Karbasi: Group testing is an elegant...
- [ ] The physics of LLMs
- [ ] StyleGAN Series
- [ ] Variational inference: https://towardsdatascience.com/variational-inference-the-basics-f70ac511bcea
- [ ] Diffusion Tutorial: https://calvinyluo.com/2022/08/26/diffusion-tutorial.html --- do all the derivations by hand
- [ ] ViLA U

##### Less Important (Audio):
- [ ] Transformers with Convolutional Context https://arxiv.org/pdf/1904.11660
- [ ] Deep Audio Priors Emerge from Harmonic Convolution
- [ ] wave2midi2wave
- [ ] Video to Audio Generation - DIFF Foley
- [ ] Music Transformer
- [ ] MIDI DDSP
- [ ] Multi Source Diffusion Models
- [ ] Shih-Lun Paper
- [ ] Source Separation Stuff
- [ ] Ge's work
- [ ] FLAM
- [ ] midi-DDSP
- [ ] NSynth
- [ ] GANSynth
- [ ] john thickstun
- [ ] MusicLM


# Deleted
## Done
- [x] Notes on the interview job search - Alisa Liu
- [x] How to get into a frontier lab, Vlad Feinberg
- [x] Notes on the job search: https://x.com/yong_zhengxin/status/2069985772288016836?s=46
- [x] Nathan Lambert: https://www.interconnects.ai/p/thoughts-on-the-hiring-market-in
- [x] Ultimate Interview Guide: https://silviasapora.github.io/blog/ml-interviews.html
- [x] Review Notes on Information Theory/Statistics/Probability
- [x] Open AI RealTime
- [x] Thinking Machines Interaction Model

## Newletters (no need)
- huggingface papers page
- papers with code trending
- marktechpost
- Huggingface Papers
- Alpha Signal
- arxivdigest
- AI newsletter
- AI Today - Essential Brief
- NLP Newsletter
- Elvis - Founders Corner, the AI Break
- Exponential View
- Google scholar alerts
- Essential AI