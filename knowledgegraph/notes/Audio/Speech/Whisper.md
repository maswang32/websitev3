# Sept 2022 Version
## Tasks
- Multilingual transcription
- Speech trasnlation to english
- language ID
- voice activity detection
- alignment

## Data
- 680k hours
    - 438k hours english audio + transcripts
    - 126k hours non-English audio and english transcripts
- Weakly-supervised web audio
    - human transcripts or subtitles, never verified, aligned, or curated
    - filtering
        - reject machine generated transcripts
            - all caps
            - punctuation free
        - language mismatches
            - if text language doesn't match audio language
            - audio language classifier is proto-whisper fine-tuned on VoxLingua107
- Undisclosed sources, but likely
    - Captioned video (youtube)
    - podcasts with published transcripts
    - audiobooks
    - lectures
    - news captions

## Format
### English Transcription:

`<|start of transcript|> <|en|> <|transcribe|> <|notimestamps|> hello guys! <|endoftext|>`

### With timestamps
`<|start of transcript|> <|en|> <|transcribe|> <|0.00|> hello, my name is mason <|3.14|> <|3.14|> and I like <|7.37|> <|endoftext|>`

### Translation
`<|start of transcript|> <|fr|> <|translate|> <|notimestamps|> hello guys! <|endoftext|>`


### No Speech
`<|start of transcript|> <|nospeech|> <|endoftext|>`

### What is prefixed?
- `<|startoftranscript|>`
- language token
- task token
- Exceptions:
    - language token can be predicted too
    - no-speech can be predicted right after `<|startoftranscript|>`
     

### Timestamp tokens
- Text emits some timestamp tokens, e.g.
    - e.g., these come from subtitle files, which have timing
- inference is constrained, timestamps appear in monotonic order.
- last completed timestamp tells you where to start the next window, when doing sliding-window inference.
- Vocab goes up to 30s, increments by 20 ms

## Architecture
- Encoder/Decoder Transformer
- log-mel spectrogram
- two 1D convs
- encoder and decoder are same width and depth
- decoder has GPT-2 vocab
- Sizes:
    - Tiny: 39M
    - Base: 74M
    - Small: 244M
    - Medium: 769M
    - Large: 1.55B





# December 2022 Version (large-v2)
- More training/regularization



# November 2023 (large-v3)
- 80 -> 128 mel bins
- 1M hours weakly labeled
- 4M hours psuedo-labeled by large-v2.



# October 2024 (large-v3-turbo)
- Decoder pruned from 32 to 4 layers
- 809M params
- 8x faster, minor quality loss


Last Reviewed: 08/26/2026
