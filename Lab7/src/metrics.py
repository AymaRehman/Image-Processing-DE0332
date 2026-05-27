# Ayma Rehman
# 241ADB165
# Practical Work 7: Image Quality Evaluation - Objective Metrics

from skimage.metrics import (
    mean_squared_error,
    peak_signal_noise_ratio,
    structural_similarity,
)


def mse(reference, test) -> float:
    return float(mean_squared_error(reference, test))


def psnr(reference, test, max_val: float = 255.0) -> float:
    if mean_squared_error(reference, test) == 0:
        return float("inf")  
    return float(peak_signal_noise_ratio(reference, test, data_range=max_val))


def ssim(reference, test, max_val: float = 255.0) -> float:
    return float(
        structural_similarity(reference, test, channel_axis=2, data_range=max_val)
    )


def evaluate(reference, test) -> dict:
    return {
        "MSE": mse(reference, test),
        "PSNR": psnr(reference, test),
        "SSIM": ssim(reference, test),
    }