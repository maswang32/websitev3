# Multimodal
1. Tokenization
    1. BPE for text
    2. Audio/Images are either discrete tokens (VQ, neural audio codec) or continuous embeddings.
        1. Discrete = easier for generation
        2. Continuous = better understanding
2. Data and objective
    1. audio -> transcript
    2. image -> caption
    3. web pages with media
    4. next token loss on text or discrete parts of the output
    5. diffusion loss on continuous (audio or image)
3. Encoders
    1. Kimi K3 vision encoder
        1. Continuous inputs
        2. No contrastive stage - SigLIP initialization caused gradient norm spikes, contrastive training not needed if from scratch
        3. No image generation at all, loss is only on text tokens
        4. 27-Layer ViT trained jointly with LM
            1. Patch size is 14 x 14
            2. 401M params
            3. positional encodings
        5. Passes through another transformer before going to the main backbone.
    2. CLIP or SigLIP (see notes)


Last Reviewed: 08/25/2026
