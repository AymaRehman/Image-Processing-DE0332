# Ayma Rehman
# 241ADB165
# Practical Work 6: Contrast Enhancement - Parallel Combination

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

IMAGES = [
    ("Images/IMG1.jpg", "Underexposed", 0.4, 0.5),
    ("Images/IMG2.jpg", "Low-contrast", 0.2, 1.0),
    ("Images/IMG3.jpg", "Mixed Lighting", 0.5, 0.8),
    ("Images/IMG4.jpg", "High Contrast", 0.8, 1.2),
    ("Images/IMG5.jpg", "Overexposed", 0.7, 2.2),
]

CHANNEL_COLORS = ["red", "green", "blue"]


# Algorithm 1: Gamma Correction (from Lab 2)
def gamma_correction(img: np.ndarray, gamma: float = 1.0) -> np.ndarray:
    img_float = img.astype(np.float32)
    corrected = np.zeros_like(img_float)
    for i in range(3):
        channel = img_float[:, :, i]
        corrected[:, :, i] = 255.0 * (channel / 255.0) ** gamma
    return corrected.astype(np.uint8)


# Algorithm 2: Min-Max Contrast Stretch (from Lab 2)
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


def compute_histogram(channel: np.ndarray) -> np.ndarray:
    return np.bincount(channel.flatten(), minlength=256)


def enhance_parallel(img: np.ndarray, d: float = 0.5, gamma: float = 1.0) -> dict:
    path_a = gamma_correction(img, gamma=gamma)
    path_b = contrast_stretch(img)
    combined = cv2.addWeighted(path_a, d, path_b, 1.0 - d, 0)
    return {"gamma": path_a, "stretch": path_b, "combined": combined}


def process():
    output_dir = "Output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for path, title, d_val, g_val in IMAGES:
        try:
            img = np.array(Image.open(path).convert("RGB"))
        except FileNotFoundError:
            print(f"[WARNING] File '{path}' not found - skipping.")
            continue

        results = enhance_parallel(img, d=d_val, gamma=g_val)

        variants = [
            (img, "Original"),
            (results["gamma"], f"Gamma (γ={g_val})"),
            (results["stretch"], "Min-Max Stretch"),
            (results["combined"], f"Combined (d={d_val})"),
        ]

        fig, axes = plt.subplots(1, 4, figsize=(20, 5))
        fig.suptitle(f"{title}  |  blend d={d_val}, γ={g_val}", fontsize=14)
        for ax, (content, lbl) in zip(axes, variants):
            ax.imshow(content)
            ax.set_title(lbl)
            ax.axis("off")
        plt.tight_layout()

        img_name = f"{title.lower().replace(' ', '_')}_images.png"
        plt.savefig(os.path.join(output_dir, img_name), dpi=150)
        plt.show()

        fig, axes = plt.subplots(1, 4, figsize=(20, 4))
        fig.suptitle(f"{title} - Histograms (per channel)", fontsize=14)
        for ax, (content, lbl) in zip(axes, variants):
            for ch, color in enumerate(CHANNEL_COLORS):
                hist = compute_histogram(content[:, :, ch])
                ax.plot(hist, color=color, alpha=0.8)
            ax.set_title(lbl)
            ax.set_xlim([0, 255])
            ax.set_xlabel("Pixel intensity")
            ax.set_ylabel("Count")
        plt.tight_layout()

        hist_name = f"{title.lower().replace(' ', '_')}_histograms.png"
        plt.savefig(os.path.join(output_dir, hist_name), dpi=150)
        plt.show()

        print(f"[OK] {title} processed and saved to {output_dir}/")


if __name__ == "__main__":
    process()
