# Ayma Rehman
# 241ADB165
# Lab 1
# Difference blending mode

import numpy as np


def difference(img1, img2):
    A = img1.astype(np.float32) / 255.0
    B = img2.astype(np.float32) / 255.0
    result = np.abs(A - B)
    return (result * 255.0).clip(0, 255).astype(np.uint8)
