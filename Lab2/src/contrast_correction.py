# Ayma Rehman
# 241ADB165
# Lab 2

import numpy as np


def gamma_correction(img, gamma=1.8):
    img_float = img.astype(np.float32)
    corrected = np.zeros_like(img_float)

    for i in range(3):
        channel = img_float[:, :, i]
        corrected[:, :, i] = 255.0 * (channel / 255.0) ** gamma

    return corrected.astype(np.uint8)


def histogram_linear_correction(img):
    img_float = img.astype(np.float32)
    corrected = np.zeros_like(img_float)

    for i in range(3):
        channel = img_float[:, :, i]
        c_min = channel.min()
        c_max = channel.max()

        if c_max - c_min == 0:
            corrected[:, :, i] = channel
        else:
            corrected[:, :, i] = (channel - c_min) / (c_max - c_min) * 255.0

    return corrected.astype(np.uint8)


def compute_histogram_fast(channel):
    return np.bincount(channel.flatten(), minlength=256)
