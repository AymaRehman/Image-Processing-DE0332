# Ayma Rehman
# 241ADB165
# Practical Work 7: Degradation - Contrast Reduction

import numpy as np


def reduce_contrast(img: np.ndarray, factor: float = 0.35,
                    midpoint: float = 127.5) -> np.ndarray:
    # Linearly compress intensities toward mid-gray.
    # factor=1.0 keeps the original; smaller factor = lower contrast.
    img_float = img.astype(np.float32)
    degraded = (img_float - midpoint) * factor + midpoint
    return np.clip(degraded, 0, 255).astype(np.uint8)