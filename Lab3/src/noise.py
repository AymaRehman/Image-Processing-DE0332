# Ayma Rehman
# 241ADB165
# Lab 3

import cv2
import numpy as np


def apply_uniform_noise(img, low=-40, high=40):
    noise = np.random.uniform(low, high, img.shape).astype(np.float32)
    return np.clip(img.astype(np.float32) + noise, 0, 255).astype(np.uint8)


def apply_jpeg_artifacts(img, quality=10):
    _, buf = cv2.imencode(".jpg", img, [cv2.IMWRITE_JPEG_QUALITY, quality])
    return cv2.imdecode(buf, cv2.IMREAD_COLOR)
