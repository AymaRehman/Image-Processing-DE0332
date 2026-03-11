# Ayma Rehman
# 241ADB165
# Lab 2

import numpy as np
import cv2
import matplotlib.pyplot as plt
import os
from src.contrast_correction import (
    gamma_correction,
    histogram_linear_correction,
    compute_histogram_fast,
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "Images")
OUTPUT_DIR = os.path.join(BASE_DIR, "Output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

underexposed = cv2.imread(os.path.join(IMAGE_DIR, "Underexposed.jpg"))
overexposed = cv2.imread(os.path.join(IMAGE_DIR, "Overexposed.jpg"))
grayish = cv2.imread(os.path.join(IMAGE_DIR, "Grayish.jpg"))

images = {
    "Underexposed": underexposed,
    "Overexposed": overexposed,
    "Grayish": grayish,
}

gamma_values = {
    "Underexposed": 0.4,
    "Overexposed": 2.2,
    "Grayish": 0.7,
}

COLORS = ["b", "g", "r"]

for name, img in images.items():
    if img is None:
        print(f"[WARNING] Could not load '{name}' — skipping.")
        continue

    g = gamma_values[name]
    gamma_corrected = gamma_correction(img, gamma=g)
    minmax_corrected = histogram_linear_correction(img)

    variants = [
        ("Original", img),
        (f"Gamma (γ={g})", gamma_corrected),
        ("Min-Max Stretch", minmax_corrected),
    ]

    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    fig.suptitle(f"{name} — Images", fontsize=14)

    for ax, (title, image) in zip(axes, variants):
        ax.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
        ax.set_title(title)
        ax.axis("off")

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f"{name.lower()}_images.png"), dpi=150)
    plt.show()

    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    fig.suptitle(f"{name} — Histograms (per channel)", fontsize=14)

    for ax, (title, image) in zip(axes, variants):
        for i, color in enumerate(COLORS):
            hist = compute_histogram_fast(image[:, :, i])
            ax.plot(hist, color=color, alpha=0.8)
        ax.set_title(title)
        ax.set_xlim([0, 255])
        ax.set_xlabel("Pixel intensity")
        ax.set_ylabel("Count")

    plt.tight_layout()
    plt.savefig(os.path.join(OUTPUT_DIR, f"{name.lower()}_histograms.png"), dpi=150)
    plt.show()

print(f"Done. Results saved to {OUTPUT_DIR}")
