# Image Processing (DE0332) - Practical Work 7
## Evaluation of Image Quality and Image Processing Algorithms

This work extends Practical Work 6 (contrast enhancement via parallel
combination of gamma correction and min-max stretch) by adding quantitative
quality evaluation using objective metrics. The goal is to measure how well
the enhancement algorithm restores a degraded image, and to study how
different metrics reflect visual perception.

## Pipeline

1. Start from a high-quality **reference** image.
2. **Degrade** it by reducing contrast (linear compression toward mid-gray).
3. **Process** the degraded image with the Lab 6 parallel enhancement
   (gamma correction + min-max stretch, blended by weight d).
4. **Evaluate** both the degraded and processed images against the reference
   using MSE, PSNR, and SSIM.

## Metrics

| Metric | Meaning | Better when |
| :--- | :--- | :--- |
| **MSE**  | Mean squared per-pixel error | Lower |
| **PSNR** | Peak signal-to-noise ratio (dB) | Higher |
| **SSIM** | Structural similarity (luminance, contrast, structure) | Higher (max 1.0) |

MSE, PSNR, and SSIM are computed using scikit-image's `skimage.metrics`
module. SSIM is the windowed structural similarity index (sliding Gaussian
window), computed per RGB channel and averaged via `channel_axis=2`. PSNR
uses `data_range=255`; the identical-image case (MSE = 0) is reported as
infinite PSNR.

## Project Structure

```text
.
├── main.py
├── Images/
│   ├── Image1.jpg
│   ├── Image2.jpg
│   └── Image3.jpg
├── src/
│   ├── __init__.py
│   ├── degrade.py
│   └── metrics.py
├── Output/
└── README.md
```

## Requirements

- Python 3.x
- NumPy
- Matplotlib
- Pillow

## Install dependencies
```bash
pip install numpy matplotlib pillow scikit-image
```

## Usage

Place three high-quality images in `Images/` named `Image1.jpg`, `Image2.jpg`,
`Image3.jpg`, then run:
```bash
python3 main.py
```

## Outputs

For each image, a side-by-side figure (reference | degraded | processed) is
saved to `Output/`, annotated with the metric values. Metric values are also
printed to the terminal.

---
Ayma Rehman
241ADB165
27 May 2026