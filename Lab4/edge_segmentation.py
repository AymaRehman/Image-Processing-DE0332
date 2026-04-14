# Ayma Rehman
# 241ADB165
# Lab 4

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

IMAGE_1_PATH = os.path.join(BASE_DIR, "images", "clean.jpg")
IMAGE_3_PATH = os.path.join(BASE_DIR, "images", "random.jpg")

def add_gaussian_noise(gray: np.ndarray, mean: float = 0, std: float = 25) -> np.ndarray:
    noise = np.random.normal(mean, std, gray.shape)
    noisy = gray.astype(np.float64) + noise
    return np.clip(noisy, 0, 255).astype(np.uint8)


def canny_detect(gray: np.ndarray,
                 low_threshold: int = 50,
                 high_threshold: int = 150) -> np.ndarray:

   
    blurred = cv2.GaussianBlur(gray, (5, 5), sigmaX=1.4)

    return cv2.Canny(blurred, low_threshold, high_threshold, apertureSize=3)


def sobel_manual(gray: np.ndarray) -> dict:
    gray = gray.astype(np.float64)
    h, w = gray.shape

    Gx = np.zeros((h, w), dtype=np.float64)
    Gy = np.zeros((h, w), dtype=np.float64)

  
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            tl = gray[y - 1, x - 1]; tc = gray[y - 1, x]; tr = gray[y - 1, x + 1]
            ml = gray[y,     x - 1];                        mr = gray[y,     x + 1]
            bl = gray[y + 1, x - 1]; bc = gray[y + 1, x]; br = gray[y + 1, x + 1]

            Gx[y, x] = (-tl + tr) + 2 * (-ml + mr) + (-bl + br)
            Gy[y, x] = (-tl - 2 * tc - tr) + (bl + 2 * bc + br)

    G = np.sqrt(Gx ** 2 + Gy ** 2)
    g_max = G.max()
    gradient_map = (G / g_max * 255).astype(np.uint8) if g_max > 0 else G.astype(np.uint8)

    return {"gradient_map": gradient_map}


def process(gray: np.ndarray, rgb: np.ndarray, title: str):
    canny = canny_detect(gray)
    sobel = sobel_manual(gray)

    fig, axes = plt.subplots(1, 3, figsize=(14, 5))
    fig.suptitle(title, fontsize=13, fontweight="bold")

    for ax, (img, label, cmap) in zip(axes, [
        (rgb,                     "Original",               None),
        (canny,                   "Canny",                  "gray"),
        (sobel["gradient_map"],   "Sobel - gradient map",   "gray"),
    ]):
        ax.imshow(img, cmap=cmap)
        ax.set_title(label, fontsize=10)
        ax.axis("off")

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    rgb_1  = np.array(Image.open(IMAGE_1_PATH).convert("RGB"))
    gray_1 = np.array(Image.open(IMAGE_1_PATH).convert("L"))
    process(gray_1, rgb_1, "Image 1 - Clean")

    gray_2 = add_gaussian_noise(gray_1)
    rgb_2  = np.stack([gray_2] * 3, axis=-1)  
    process(gray_2, rgb_2, "Image 2 - Noisy (Gaussian noise added)")

    rgb_3  = np.array(Image.open(IMAGE_3_PATH).convert("RGB"))
    gray_3 = np.array(Image.open(IMAGE_3_PATH).convert("L"))
    process(gray_3, rgb_3, "Image 3 - Free choice")