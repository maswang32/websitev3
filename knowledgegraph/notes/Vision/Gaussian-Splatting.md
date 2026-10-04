# Overview 
1. Gaussian Splats are a novel 3D representation, where 3D scenes are represented by millions of 3D Gaussians of various shapes and opacities.
2. We can couple this with a real-time differentiable renderer, which allows us to do realtime novel view synthesis as well as speedy optimization to fit a scene
3. Gaussian Splats combine the best of both worlds: the continuous nature of NeRFs, as well as the speedy rendering/rasterization of meshes.


# Benefits of Gaussian Splatting
1. Super Fast Rendering - realtime display rates at 1080p, 30 fps
    1. Fast radiance field methods can do 10-15 frames per second
2. Optimization times are competitive with the fastest previous methods (Plenoxels)
3. At comparable training times to InstantNGP, Gaussian splatting has similar quality
4. At training time of 51 minutes, Gaussian splats achieve state-of-the-art quality
    1. even better than Mip-NeRF360, which requires up to 48 hours of training time.



Nerf and voxel-based 3D representations require stochastic sampling for rendering - computationally expensive, result in noise

# Method

## Training
1. Calibrate cameras with Structure-from-Motion.
2. These give you sparse point clouds too. Initialize the 3D Gaussians with these sparse point clouds.
3. Rendering - project the Gaussians to 2D, use alpha-blending and volumetric rendering
4. Optimize Gaussian properties:
    1. Opacity $\alpha$
    2. Anisotropic Covariance
    3. Spherical Harmonic coefficients
5. Adaptive density control - add and remove 3D Gaussians during optimization.

The result is 1-5 million gaussians per scene.


## Rendering
Rendering avoids computation in empty space, unlike volumetric rendering using NeRFs.

# To do:
I have read the introduction, keep reading past the intro

Last Reviewed: 10/3/2026