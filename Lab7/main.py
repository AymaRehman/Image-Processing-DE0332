# Ayma Rehman
# 241ADB165
# Practical Work 7: Evaluation of Image Quality - Contrast Enhancement

import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

from src.degrade import reduce_contrast
from src.metrics import evaluate

def gamma_correction(img: np.ndarray, gamma: float = 1.0) -> np.ndarray:
    img_float = img.astype(np.float32)
    corrected = np.zeros_like(img_float)
    for i in range(3):
        channel = img_float[:, :, i]
        corrected[:, :, i] = 255.0 * (channel / 255.0) ** gamma
    return corrected.astype(np.uint8)


def contrast_stretch(img: np.ndarray) -> np.ndarray:
    img_float = img.astype(np.float32)
    corrected = np.zeros_like(img_float)
    for i in range(3):
        channel = img_float[:, :, i]
        c_min, c_max = channel.min(), channel.max()
        if c_max - c_min == 0:
            corrected[:, :, i] = channel
        else:
            corrected[:, :, i] = (channel - c_min) / (c_max - c_min) * 255.0
    return corrected.astype(np.uint8)


def enhance_parallel(img: np.ndarray, d: float = 0.5,
                     gamma: float = 1.0) -> np.ndarray:
    path_a = gamma_correction(img, gamma=gamma).astype(np.float32)
    path_b = contrast_stretch(img).astype(np.float32)
    combined = path_a * d + path_b * (1.0 - d)
    return np.clip(combined, 0, 255).astype(np.uint8)

IMAGES = [
    ("Images/Image1.jpg", "Image 1", 0.5, 0.7),
    ("Images/Image2.jpg", "Image 2", 0.5, 0.7),
    ("Images/Image3.jpg", "Image 3", 0.5, 0.7),
]

CONTRAST_FACTOR = 0.35 


def fmt(metrics: dict) -> str:
    return (f"MSE={metrics['MSE']:.2f}  "
            f"PSNR={metrics['PSNR']:.2f} dB  "
            f"SSIM={metrics['SSIM']:.4f}")


def process():
    output_dir = "Output"
    os.makedirs(output_dir, exist_ok=True)

    for path, title, d_val, g_val in IMAGES:
        try:
            reference = np.array(Image.open(path).convert("RGB"))
        except FileNotFoundError:
            print(f"[WARNING] File '{path}' not found - skipping.")
            continue

        degraded = reduce_contrast(reference, factor=CONTRAST_FACTOR)
        processed = enhance_parallel(degraded, d=d_val, gamma=g_val)

        m_degraded = evaluate(reference, degraded)
        m_processed = evaluate(reference, processed)

        print(f"\n=== {title} ===")
        print(f"  Degraded  vs reference : {fmt(m_degraded)}")
        print(f"  Processed vs reference : {fmt(m_processed)}")

        variants = [
            (reference, "Reference (original)"),
            (degraded, f"Degraded\n{fmt(m_degraded)}"),
            (processed, f"Processed\n{fmt(m_processed)}"),
        ]

        fig, axes = plt.subplots(1, 3, figsize=(16, 5))
        fig.suptitle(f"{title}  |  contrast factor={CONTRAST_FACTOR}, "
                     f"d={d_val}, γ={g_val}", fontsize=13, fontweight="bold")
        for ax, (content, lbl) in zip(axes, variants):
            ax.imshow(content)
            ax.set_title(lbl, fontsize=9)
            ax.axis("off")
        plt.tight_layout()

        out_name = f"{title.lower().replace(' ', '_')}_metrics.png"
        plt.savefig(os.path.join(output_dir, out_name), dpi=150)
        plt.show()

        print(f"[OK] {title} processed and saved to {output_dir}/")


if __name__ == "__main__":
    process()