# Ayma Rehman
# 241ADB165
# Lab 5

import cv2
import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

IMAGE_1_PATH = "Images/image1.jpg"    
IMAGE_2_PATH = "Images/image2.jpg"       
IMAGE_3_PATH = "Images/image3.jpg"       

K = 3  

def mean_adaptive_threshold(gray: np.ndarray, block_size: int = 35, C: int = 5) -> np.ndarray:

    if block_size % 2 == 0:
        block_size += 1  

    return cv2.adaptiveThreshold(
        gray,                                               
        maxValue=255,                                       
        adaptiveMethod=cv2.ADAPTIVE_THRESH_MEAN_C,          
        thresholdType=cv2.THRESH_BINARY_INV,               
        blockSize=block_size,                              
        C=C                                               
    )

def kmeans_segment(rgb: np.ndarray, k: int = K) -> tuple[np.ndarray, np.ndarray]:

    pixels = rgb.reshape(-1, 3).astype(np.float32)

    criteria = (
        cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,
        100,   
        0.2    
    )

    _, labels, centers = cv2.kmeans(
        pixels,                         
        k,                             
        None,                          
        criteria,                      
        attempts=10,                  
        flags=cv2.KMEANS_PP_CENTERS    
    )

    centers = np.uint8(centers)                         
    segmented_pixels = centers[labels.flatten()]        
    segmented = segmented_pixels.reshape(rgb.shape)   

    labels_2d = labels.reshape(rgb.shape[:2])        
    return segmented, labels_2d                      


def process(path: str, title: str, k: int = K) -> None:

    rgb  = np.array(Image.open(path).convert("RGB"))
    gray = np.array(Image.open(path).convert("L"))

    mean_thresh       = mean_adaptive_threshold(gray)
    kmeans_seg, _     = kmeans_segment(rgb, k=k)

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle(title, fontsize=13, fontweight="bold")

    panels = [
        (rgb,          "Original",                          None),
        (mean_thresh,  "Mean Adaptive\n(block=35, C=5)",   "gray"),
        (kmeans_seg,   f"K-Means Segmented\n(k={k})",       None),
    ]

    for ax, (img, label, cmap) in zip(axes, panels):
        ax.imshow(img, cmap=cmap)
        ax.set_title(label, fontsize=10)
        ax.axis("off")

    plt.tight_layout()


if __name__ == "__main__":
    process(IMAGE_1_PATH, "Image 1 - Grayscale / Multiple Objects")
    process(IMAGE_2_PATH, "Image 2 - Person / Animal / Car")
    process(IMAGE_3_PATH, "Image 3 - Free Choice")
    plt.show()