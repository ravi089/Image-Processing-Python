# Canny Edge Detection.
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

        # Canny edge detection.
        edges = cv2.Canny(img, 100, 200)

        filename = os.path.basename(file_item).split('.')[0]
        cv2.imwrite(filename + '_l.jpg', edges)
    except IOError:
        print ('Error while reading files!!!')
