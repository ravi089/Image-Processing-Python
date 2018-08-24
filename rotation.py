# Image Rotation.
import cv2
import numpy as np
import glob
import os
from PIL import Image

DIR_PATH = '../Images/*'

# Read all images.
all_files_dir = glob.glob(DIR_PATH)

for file_item in all_files_dir:
    try:
        # Read image from disk.
        img = cv2.imread(file_item)
        (rows, cols) = img.shape[:2]

        # Rotation w.r.t center to 45 without scaling.
        M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
        res = cv2.warpAffine(img, M, (cols, rows))

        # Write image back to disk.
        filename = os.path.basename(file_item).split('.')[0]
        cv2.imwrite(filename + '_r.jpg', res)
    except IOError:
        print ('Error while reading files!!!')
        

