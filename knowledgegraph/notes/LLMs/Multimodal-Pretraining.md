# Tokenization
1. BPE for text
2. Audio/Images are either discrete tokens (VQ, neural audio codec) or continuous embeddings.
    1. Discrete = easier for generation
    2. Continuous = better understanding
# Data and objective
1. audio -> transcript
2. image -> caption
3. web pages with media
4. next token loss on text or discrete parts of the output
5. diffusion loss on continuous (audio or image)


# Encoders
## Kimi K3 vision encoder
1. Continuous inputs
2. No contrastive stage - SigLIP initialization caused gradient norm spikes, contrastive training not needed if from scratch
3. No image generation at all, loss is only on text tokens
4. 27-Layer ViT trained jointly with LM
    1. Patch size is 14 x 14
    2. 401M params
    3. positional encodings
5. Passes through another transformer before going to the main backbone.

## CLIP or SigLIP
Encoder is initialized to something trained with CLIP or SigLIP
(see notes)



## Audio encoder - Qwen
1. First, take the base text model
2. Stitch whisper encoder + projection layer onto it
3. train encoder + projector on these tasks:
    1. ASR
    2. speech to text translation
    3. speech emotion recognition
    4. speaker attributes (gender, language, dialect)
    5. sound event classification
    6. acoustic scene classification
    7. audio captioning
    8. music captioning
    9. instrument/genre analysis
    10. speech recognition with timestamps
    11. AQA - audio question answering (free form response about a clip's content)
4. Use this format:
    1. Audio embeddings, task specification, text target
    2. Qwen audio v1: <|transcribe|>, <|caption|>, and <|translate|>
    3. Qwen audio v2: language prompts
5. SFT: encoder frozen, LLM trained


Last Reviewed: 08/25/2026
