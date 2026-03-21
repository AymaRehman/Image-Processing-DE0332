# Ayma Rehman
# 241ADB165
# Lab 3

import os
import cv2
from src.noise import apply_uniform_noise, apply_jpeg_artifacts
from src.filters import mean_filter, median_filter, gaussian_filter

os.makedirs("Outputs", exist_ok=True)

images = []
for fname in sorted(os.listdir("Images")):
    if fname.lower().endswith((".png", ".jpg", ".jpeg")):
        img = cv2.imread(f"Images/{fname}")
        if img is not None:
            images.append((os.path.splitext(fname)[0], img))

assert len(images) >= 2, "Add at least 2 images to the Images/ folder"

for stem, img in images[:2]:
    noisy = {
        f"{stem}_uniform": apply_uniform_noise(img),
        f"{stem}_jpeg": apply_jpeg_artifacts(img),
    }
    for name, noisy_img in noisy.items():
        cv2.imwrite(f"Outputs/{name}.png", noisy_img)
        for filter_name, fn in [
            ("mean", mean_filter),
            ("median", median_filter),
            ("gaussian", gaussian_filter),
        ]:
            cv2.imwrite(f"Outputs/{name}_{filter_name}.png", fn(noisy_img))

print("Done. Check the Outputs/ folder.")
