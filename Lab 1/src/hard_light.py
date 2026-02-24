# Ayma Rehman
# 241ADB165
# Lab 1
# Hard Light blending mode

import numpy as np


def hard_light(img1, img2):
    A = img1.astype(np.float32) / 255.0
    B = img2.astype(np.float32) / 255.0
    result = np.where(B <= 0.5, 2 * A * B, 1 - 2 * (1 - A) * (1 - B))
    return (result * 255.0).clip(0, 255).astype(np.uint8)
