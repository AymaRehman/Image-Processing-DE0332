# Image Processing (DE0332) - Lab 1
## Image Blending Modes & Transition Effects

This lab work implements various image blending modes using Python and NumPy. The main objective is to perform pixel-level arithmetic based on mathematical formulas to combine two images. OpenCV is used exclusively for image loading and saving, while all blending logic is implemented using NumPy arrays.

## Features
- **Custom NumPy Implementation**: All blending math is performed on normalized `float32` arrays [0, 1].
- **Clamping Logic**: Final results are clamped to the [0, 255] range and converted back to `uint8` to prevent overflow/underflow artifacts.

- **Blending Modes Implemented**:
  - **Lighten**: Selects the lighter pixel between the two images.
  - **Difference**: Highlights the absolute difference between images.
  - **Hard Light**: A high-contrast mode that multiplies or screens depending on the blend layer.
  - **Soft Light**: A subtle mode that darkens or lightens the base image based on its own intensity.

## Mathematical Formulas
All calculations are performed on normalized pixel values $P \in [0, 1]$.

| Mode | Formula |
| :--- | :--- |
| **Lighten** | $if B ≤ A then C = A ; if B > A then C = B $|
| **Difference** | $C = \|A - B\|$ |
| **Hard Light** | $if A ≤ 0.5 then C = 2 ∙ A ∙ B ; if A > 0.5 then C = 1 -2 ∙ (1-A)∙(1-B)$  |
| **Soft Light** | $if A ≤ 0.5 then C = (2 ∙ A - 1) ∙ (B-B^2)+B; if A > 0.5 then C = (2 ∙ A - 1)∙(\sqrt{B}-B)+B$ |

## Project Structure
```text
.
├── main.py              
├── Sample_Images/       
├── src/                 
│   ├── __init__.py      
│   ├── lighten.py
│   ├── difference.py
│   ├── hard_light.py
│   └── soft_light.py
├── Results/             
└── README.md
```

## Requirements
- Python 3.x
- NumPy
- OpenCV (opencv-python)

## Install dependencies
```
pip install numpy opencv-python
```

## Usage

Run the script from the terminal by specifying the two input images and the desired blending mode.

```
python3 main.py --img1 <path_to_img1> --img2 <path_to_img2> --mode <mode_name>
```

## Examples for Every Mode
```
# Lighten
python3 main.py --img1 Sample_Images/imageA.jpg --img2 Sample_Images/imageB.jpg --mode lighten

# Difference
python3 main.py --img1 Sample_Images/imageA.jpg --img2 Sample_Images/imageB.jpg --mode difference

# Hard Light
python3 main.py --img1 Sample_Images/imageA.jpg --img2 Sample_Images/imageB.jpg --mode hard_light

# Soft Light
python3 main.py --img1 Sample_Images/imageA.jpg --img2 Sample_Images/imageB.jpg --mode soft_light
```

## Outputs

By default, the processed images are saved in the Results/ folder with the name of the mode (e.g., lighten.png). You can change the output folder using the --out flag:

```
python3 main.py --img1 a.jpg --img2 b.jpg --mode lighten --out MyCustomFolder
```

---

Ayma Rehman  
  
241ADB165  
  
21 February 2026  
