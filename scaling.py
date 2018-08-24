# Image Processing.
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
        filename = os.path.basename(file_item).split('.')[0]
        (height, width) = img.shape[:2]
        res = cv2.resize(img, (2*width, 2*height), interpolation=cv2.INTER_CUBIC)
        # Write image back to disk.
        cv2.imwrite(filename + '_.jpg' ,res)
    except IOError:
        print ('Error while reading files!!!')
        

