# Ayma Rehman
# 241ADB165
# Lab 1
# Soft Light blending mode

import numpy as np


def soft_light(img1, img2):
    A = img1.astype(np.float32) / 255.0
    B = img2.astype(np.float32) / 255.0
    result = np.where(
        A <= 0.5, (2 * A - 1) * (B - B**2) + B, (2 * A - 1) * (np.sqrt(B) - B) + B
    )
    return (result * 255.0).clip(0, 255).astype(np.uint8)
