# ReflectanceFusion-Diffusion-based-text-to-SVBRDF-Generation
Result of ReflectanceFusion
The ReflectanceFusion result comprises ～700 randomly composed texts, each of which has been generated four times. Within each file, the first image is a rendered picture, the second is the normal map, the third is the albedo, the fourth is the roughness, and the fifth is the specular map.

🌟 Key Features

Text-to-Material Generation: Create detailed SVBRDF maps from natural language descriptions
High-Quality Output: Generates 10-channel maps including normals, diffuse albedo, specular reflectance, and roughness
Physically-Based Rendering: Produces PBR-ready materials compatible with modern rendering engines
Dual-Phase Architecture: Combines Stable Diffusion 2.0 with custom ReflectanceUNet for superior quality
Editable & Relightable: Unlike static images, outputs can be freely edited and relit in any environment
Flexible Control: Optional physical parameters (roughness, specularity) for enhanced customization
Complex Semantics: Generate materials with intricate patterns like "dragon carved wood" or "bike embroidered fabric"


Result Structure
Each generated material includes:

Rendered image - Preview under lighting
Normal map - Surface geometry details
Albedo map - Base color information
Roughness map - Surface smoothness
Specular map - Reflective properties



🎓 Citation
If you find this work useful, please cite our paper:


'''
@inproceedings{10.2312:sr.20241152,
booktitle = {Eurographics Symposium on Rendering},
editor = {Haines, Eric and Garces, Elena},
title = {{ReflectanceFusion: Diffusion-based text to SVBRDF Generation}},
author = {Xue, Bowen and Guarnera, Giuseppe Claudio and Zhao, Shuang and Montazeri, Zahra},
year = {2024},
publisher = {The Eurographics Association},
ISSN = {1727-3463},
ISBN = {978-3-03868-262-2},
DOI = {10.2312/sr.20241152}
}
'''
