# I accidentally rendered my blender simulation as 250 separate PNGs for each frame,
# so I created this simple script to help me turn it into a video rather than
# re-rendering it for another 24 hours.

import cv2
import numpy as np
import glob

imageArray = []
for file in glob.glob("C:/Users/User/Desktop/Blender-3D-Models/*.png"): # Change file directory to your directory
    img = cv2.imread(file)
    height, width, layers = img.shape
    size = (width, height)
    imageArray.append(img)

output = cv2.VideoWriter('output.avi', cv2.VideoWriter.fourcc(*'DIVX'), 15, size)

for x in range(len(imageArray)):
    output.write(imageArray[x])

output.release()