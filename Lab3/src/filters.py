# Ayma Rehman
# 241ADB165
# Lab 3

import cv2


def mean_filter(img, k=5):
    return cv2.blur(img, (k, k))


def median_filter(img, k=5):
    return cv2.medianBlur(img, k)


def gaussian_filter(img, k=5, sigma=1.5):
    return cv2.GaussianBlur(img, (k, k), sigma)
