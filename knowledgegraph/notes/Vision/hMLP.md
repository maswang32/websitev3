- You patchify an image (say 64 x 64 x 3) into tiny patches (say 32 x 32 x 12 patches)
    - Means you split it up into 32 x 32 squares, then each the pixels in square is represented by a flattened vector.
- Then you pass the 32 x 32 x 12 image into an MLP, getting a 32 x 32 x C1
- Then you patchify again, getting like 8 x 8 x C1*16, and pass it through another MLP, getting a (8 x 8 x C2)
- Then you patchify again, getting like a 2 x 2 x C2*16
- Basically a CNN, but without overlap (leakage) between patches (stride equals kernel size)
- Produces continuous outputs


Last Reviewed: 8/31/2026
