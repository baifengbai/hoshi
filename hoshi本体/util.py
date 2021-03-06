import numpy as np
import cv2


def 屑检测(img, 面积阈值):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return [cnt for cnt in contours if cv2.contourArea(cnt) < 面积阈值]


def 局部二值化(img, d):
    d = max(d, 3)
    # img_bin = img.copy()
    # t = cv2.blur(img_bin, (d, d), 0).astype(np.int)
    # img_bin[np.where(img_bin > t - 5)] = 255
    # img_bin[np.where(img_bin <= t - 5)] = 0
    img_bin = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, d, 6)
    return img_bin


def erode(img, x, y):
    # 为什么0的时候opencv会操作？？？
    if 0 in (x,y):
        return img
    kernel = np.ones((int(x), int(y)), np.uint8)
    return cv2.erode(img, kernel)


def dilate(img, x, y):
    if 0 in (x,y):
        return img
    kernel = np.ones((int(x), int(y)), np.uint8)
    return cv2.dilate(img, kernel)
