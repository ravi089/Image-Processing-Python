# Image Processing.
import cv2
import numpy as np
import glob
import os
from matplotlib import pyplot as plt
from PIL import Image

DIR_PATH = '../Images/*'

# Read all images.
all_files_dir = glob.glob(DIR_PATH)

for file_item in all_files_dir:
    try:
        # Read image from disk.
        img = cv2.imread(file_item)

        # Laplacian filter.
        laplacian = cv2.Laplacian(img, cv2.CV_64F)
        # Sobel : Derivative along 'x' direction.
        sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
        # Sobel : Derivative along 'y' direction.
        sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

        filename = os.path.basename(file_item).split('.')[0]
        cv2.imwrite(filename + '_l.jpg', laplacian)
        cv2.imwrite(filename + '_sx.jpg', sobelx)
        cv2.imwrite(filename + '_sy.jpg', sobely)
    except IOError:
        print ('Error while reading files!!!')
