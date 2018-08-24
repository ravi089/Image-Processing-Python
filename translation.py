# Image Translation (Shifting the object).
import cv2
import numpy as np
import glob
import os
from PIL import Image

DIR_PATH = '../Images/*'

# Read all images.
all_files_dir = glob.glob(DIR_PATH)

# Create translation matrix.
# If the shift is (x, y) then matrix would be
# M = [1 0 x]
#     [0 1 y]

# Let's shift by (100, 50).
M = np.float32([[1, 0, 100], [0, 1, 50]])

for file_item in all_files_dir:
    try:
        # Read image from disk.
        img = cv2.imread(file_item)
        (rows, cols) = img.shape[:2]
        
        filename = os.path.basename(file_item).split('.')[0]

        res = cv2.warpAffine(img, M, (cols, rows))
        # Write image back to disk.
        cv2.imwrite(filename + '_t.jpg', res)
    except IOError:
        print ('Error while reading files!!!')
        

