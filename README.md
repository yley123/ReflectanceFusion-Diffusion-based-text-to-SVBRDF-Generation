# ReflectanceFusion-Diffusion-based-text-to-SVBRDF-Generation

### [Paper (arXiv)](https://arxiv.org/abs/2406.14565) | [Paper (EG)](https://diglib.eg.org/items/bd1075f3-4f4b-410f-9159-2143b4e97e82) | [Project Page](https://github.com/yley123/ReflectanceFusion-Diffusion-based-text-to-SVBRDF-Generation)

[Bowen Xue](https://github.com/yley123)<sup>1</sup>, 
[Giuseppe Claudio Guarnera](https://sites.google.com/view/giuseppe-claudio-guarnera)<sup>2</sup>, 
[Shuang Zhao](https://www.shuangz.com/)<sup>3</sup>, 
[Zahra Montazeri](https://research.manchester.ac.uk/en/persons/zahra.montazeri)<sup>1</sup>

<sup>1</sup>University of Manchester, 
<sup>2</sup>University of York, 
<sup>3</sup>University of California, Irvine

---

## Abstract

We introduce **ReflectanceFusion**, a novel neural text-to-texture model for generating high-fidelity SVBRDF maps from textual descriptions. Our tandem neural approach leverages Stable Diffusion 2.0 as a backbone combined with our custom **ReflectanceUNet** to accurately model spatially varying reflectance properties. The model generates editable, relightable SVBRDF maps comprising 10 channels (normals, diffuse/specular albedo, and roughness), trained on ~200,000 synthetic materials from INRIA and UBO datasets.

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


```bibtex
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
```
