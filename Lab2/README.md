# Image Processing (DE0332) - Lab 2
## Contrast Correction Techniques

This lab work implements contrast correction methods for digital images using Python and NumPy. The main objective is to improve the visual quality of underexposed, overexposed, and low-contrast images through pixel-level intensity transformations. OpenCV is used exclusively for image loading, while all correction logic is implemented using NumPy arrays.

## Features

- **Custom NumPy Implementation**: All intensity transformations are applied on `float32` arrays to preserve precision before converting back to `uint8`.
- **Per-Channel Processing**: Each correction method operates independently on the R, G, and B channels to avoid color distortion.
- **Histogram Visualization**: Per-channel histograms are plotted before and after correction to quantify the improvement.
- **Correction Methods Implemented**:
  - **Gamma Correction**: Non-linear brightness adjustment using a tunable gamma exponent.
  - **Min-Max Histogram Stretch**: Linear stretching that maps the full intensity range of each channel to [0, 255].

## Mathematical Formulas

All calculations are performed on normalized pixel values $P \in [0, 1]$.

| Method | Formula |
| :--- | :--- |
| **Gamma Correction** | $C = 255 \cdot \left(\dfrac{P}{255}\right)^{\gamma}$ |
| **Min-Max Stretch** | $C = \dfrac{P - P_{\min}}{P_{\max} - P_{\min}} \cdot 255$ |

**Gamma values used per image type:**

| Image | Gamma (γ) | Effect |
| :--- | :--- | :--- |
| Underexposed | 0.4 | Brightens dark image |
| Overexposed | 2.2 | Darkens blown-out image |
| Grayish | 0.7 | Boosts mid-tone contrast |

## Project Structure

```text
.
├── main.py
├── Images/
│   ├── Underexposed.jpg
│   ├── Overexposed.jpg
│   └── Grayish.jpg
├── src/
│   ├── __init__.py
│   └── contrast_correction.py
├── Output/
└── README.md
```

## Requirements

- Python 3.x
- NumPy
- OpenCV (opencv-python)
- Matplotlib

## Install dependencies

```
pip install numpy opencv-python matplotlib
```

## Usage

Run the script directly from the terminal. It will process all three images automatically and save results to the `Output/` folder.

```
python3 main.py
```

## Outputs

For each image (`Underexposed`, `Overexposed`, `Grayish`), two files are saved in the `Output/` directory:

```
Output/
├── underexposed_images.png      # Side-by-side: Original | Gamma | Min-Max
├── underexposed_histograms.png  # Per-channel histograms for each variant
├── overexposed_images.png
├── overexposed_histograms.png
├── grayish_images.png
└── grayish_histograms.png
```

Each image output shows three variants side by side:
- **Original** — unmodified input
- **Gamma (γ=x)** — gamma-corrected version
- **Min-Max Stretch** — histogram-stretched version

Each histogram output plots the R, G, and B channel intensity distributions across [0, 255] for all three variants.

---
Ayma Rehman  
241ADB165  
11 March 2026
