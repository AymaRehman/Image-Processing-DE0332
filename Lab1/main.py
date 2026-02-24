# Ayma Rehman
# 241ADB165
# Lab 1
# Main script to apply blending modes

import os
import argparse
import cv2
import numpy as np

from src.soft_light import soft_light
from src.lighten import lighten
from src.difference import difference
from src.hard_light import hard_light

BLENDS = {
    "soft_light": soft_light,
    "lighten": lighten,
    "difference": difference,
    "hard_light": hard_light,
}


def load_images(path1: str, path2: str):
    img1 = cv2.imread(path1, cv2.IMREAD_COLOR)
    img2 = cv2.imread(path2, cv2.IMREAD_COLOR)

    if img1 is None:
        raise FileNotFoundError(f"Could not read image: {path1}")
    if img2 is None:
        raise FileNotFoundError(f"Could not read image: {path2}")

    if img1.shape != img2.shape:
        img2 = cv2.resize(
            img2, (img1.shape[1], img1.shape[0]), interpolation=cv2.INTER_AREA
        )

    return img1, img2


def ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)


def main():
    parser = argparse.ArgumentParser(description="Assignment 1: Image Blending Modes")
    parser.add_argument("--img1", required=True, help="Path to base image (A)")
    parser.add_argument("--img2", required=True, help="Path to blend image (B)")
    parser.add_argument(
        "--mode", choices=BLENDS.keys(), required=True, help="Blending mode"
    )
    parser.add_argument(
        "--d", type=float, default=0.5, help="Alpha for transparency mode (0..1)"
    )
    parser.add_argument("--out", default="Results", help="Output directory")

    args = parser.parse_args()

    img1, img2 = load_images(args.img1, args.img2)
    ensure_dir(args.out)

    result = BLENDS[args.mode](img1, img2)
    out_name = f"{args.mode}.png"

    out_path = os.path.join(args.out, out_name)
    cv2.imwrite(out_path, result)

    print(f"Success! Saved blended image to: {out_path}")


if __name__ == "__main__":
    main()
