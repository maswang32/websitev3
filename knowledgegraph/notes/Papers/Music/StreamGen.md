Analyze real time accompaniment with two things:
- offset between output playback and input time used for conditioning
- output chunk duration
- naive MLE is insufficient, need some sort of anticipation
- raw audio
- Output audio must musically align with input audio at the same time

# Contributions
- $t_f$ and $k$ formalization
- study on Slakh about quality/latency/responsiveness trade-offs
- supervised training is not enough (exposure bias).


# Formalization
- Output of the model at step t: $y(t:t+k)$
- Input of the model then: $x(1:t+t_f)$, and previous output $y(1:t)$.
- negative $t_f$ means that the model has to produce audio without seeing what it will accompany at that time.


# Related Work
- Score following
- accompaniment from hand-crafted heuristics, recombination from a corpus
- target symbolic tasks or chord sequence prediction
- Magenta RealTime - acoustic music accompanies the user, with text prompts

# Tradeoffs and Design Space
## Tradeoffs
- $k$ allows parallel generation/buffering.
    - larger $k$ bad:
        - more delay
        - So think about it. if you are in the negative $t_f$ regime, you have to generate $t_f$ ahead AND $k$ ahead.
    - large $k$ good:
        - Improve throughput and stability
        - a window exists for the computation of the next chunk, that's more flexible if $k$ is larger
        - accomodates non-autoregressive models, e.g. diffusion
        - better for throughput
- Some combos are not possible
    - small $t_f$ with small $k$, is very reactive, but very little tolerance to variable delays
    - $-t_f$ must be bigger than $t_{sys}$ and $t_{jitter}$
    - Rate of generation must be $1/k$.

## Design space
- Ignoring input means decoder-only unconditional generative model
- $k=1$ means autoregressive decoding, $k=T$ means parallel generation, where all tokens are predicted in one big chunk
- Anticipatory music transform is $t_f > 0$
- RealChords is $t_f=0$, $k=1$.


# Experiment
- Condition the model on a random mixture of other tracks, generate one missing track.
- Sweep $t_f$ and $k$.

- input tracks are added in waveform space
- encoded using DAC
- output stream is delay patterned, and prepended instrument token (4 tokens)
- output and input stream are aligned

## Training Data
- Slakh 2100, 145 hours, virtual instruments
- sample one target stem, then sample uniformly the number of other stems, then create input mixture.

## Tokenizer
- DAC tokenizer, 4 layers, trained on MTG-Jamendo
    - 32 kHZ
    - 50 Hz audio codes
    - causal DAC (Towards Codec LM codesign...)

## Transformer Arch
- LLaMA style, 16 layers, 16 heads, hidden size 1024
- MusicGen delay pattern (0.08s delay)

## Conditions
- Input stream - sum the frozen DAC codebook embeddings across frames
    - projet to model dim
    - gated function: Layernorm(Project(FROZEN DAC)) + g * Layernorm(LEARNED EMBEDDING SUM), g initialized to zeros
- Output stream - learned codebook embeddings for different RVQ levels
- instrument embedding is leanred lookup

## Chunking 
- k = 1 - normal autoregressive decoder
    - generate in standard way
- k > 1 - prefix decoder, fused input = prefix, model predicts next k output frames
    - generate k frames, update the prefix, generate next chunk

## Baselines
- masked langauge model baseline, Stemgen
- prefix decoder where input is fully seen


## Metrics
- Metrics
    - Rhythm alignment score - beat F1 using madmom
    - COCOLA score
    - audio quality (FAD) using VGGish, references from test split.
    - pairwise listening study


# Results
- as soon as t_f goes zero or negative,
    - COCOLA score goes down
    - audio quality goes down
    - rhythm alignment goes down
- subjective preference for $k=1$:
    - ground truth is the best
    - offline stemgen (non autoregressive) is second best
    - offline prefix decoder is third best
    - $t_f = 1$ is fourth
    - $t_f = 0$ is fifth
    - random pairing is 6th
    - $t_f = -1$ is seventh
- chunk size
    - smaller is better when $t_f$ is negative
    - large is better when $t_f$ is positive

