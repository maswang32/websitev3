# Demo - what can it do?
- "Friend" - as soon as someone comes into the frame, say friend
- realtime translation
- Search while talking and listening
- Can generate bar charts, and respond while doing things






# What is it?

- **Interaction is handled by the model, not through scaffolding**
- Goal: make AI interactive in real time across any modality
- Allows humans in the loop, instead of AI doing everything itself.
    - AI doing everything itself is not possible, can't specify all requirements up front
    - more like collaborating, less like prompting
    - Move beyond turn based interface - that's like resolving a conflict over email instead of in person
- Need to make things a part of the model itself - bitter lesson
    - instead of handcrafted rules (turns and orchestration)
- The interaction model can be the interface for interacting with a deeper AI




# Abilities
- model waits for you to finish talking
- model can talk over user, follow instructions, interrupt
- model can tell you to sit up straight
- model can speak at same time as you (realtime translation into HR speech)
- model is aware of elapsed time, can set timer.
- model is kind of slow
- model can produce UIs at the same time while you speak to it
- model can be an earpiece, coaching in your ear or correcting.





# Approach
- multistream design
- microturns of 200ms
    - microturns, interleaved - input 0, output 0, input 1, output 1....
- inputs and outputs are flattened

## Two components
1. Time aware component has real time presence
2. Asynchronous background model handles sustained reasoning, tool use, and long horizon work

Both share the same context


## Interaction Model
- The interaction model (1) is one that is constant exchange with the user
- Interaction model on its own is competitive in benchmarks

Normally things consist of
- VAD, which is less intelligent than model itself
- hard to interject, hard to react to visual cues, can't speak while listening


### Architecture:
- dMel encoder (discrete Mel)
- transform via lightweight embedding layer
- images = 40x40 patches encoded by hMLP
- audio decoder is a flow head
- 276B MoE


## Inference
- lots of prefill and decode calls
- streaming sessions - client sends 200 ms chunk as separate request, inference server appends these chunks into a persistent sequence.
- sglang PR

### Stuff I don't understand yet:
- Trainer-sampler alignment
- parallelism
- split-KV


## Background Model
interaction model delegation sends full context


# Safety
- modality refusals: text to speech data for refusals
- red teaming harness to generate refusal data.



# Future work
- context management
- delayed frames

Last Reviewed: 8/31/2026