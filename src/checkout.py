"""
For Testing purposes
    Take image from user, crop the background and transform perspective
    from the perspective detect the word and return the array of word's
    bounding boxes
"""

from src import words, page
from PIL import Image
import numpy as np
import cv2
import os, shutil

import model
#array of images
def check(path):
    z="pre.jpg"
    I_data = []
    # User input page image
    image = cv2.cvtColor(cv2.imread(z), cv2.COLOR_BGR2RGB)

    # Crop image and get bounding boxes
    crop = page.detection(image)
    boxes = words.detection(crop)
    lines = words.sort_words(boxes)
    # for delete the previous segmented images data.
    folder = '../segmented'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


    # Saving the bounded words from the page image in sorted way
    i = 0
    for line in lines:
        text = crop.copy()
        for (x1, y1, x2, y2) in line:
            # roi = text[y1:y2, x1:x2]
            save = Image.fromarray(text[y1:y2, x1:x2])
            save.save("temp.png")
            img = cv2.imread("temp.png", cv2.IMREAD_GRAYSCALE)

            # increase contrast
            pxmin = np.min(img)
            pxmax = np.max(img)
            imgContrast = (img - pxmin) / (pxmax - pxmin) * 255

            # increase line width
            kernel = np.ones((1,1), np.uint8)
            imgMorph = cv2.erode(imgContrast, kernel, iterations=1)
            I_data.append(imgMorph)

            i += 1
    length=len(I_data)
    for x in range(0,length):
        image=I_data[x]
        cv2.imwrite('../segmented/segment'+str(x)+'.png', image)
    from src import Main
    Main.grammer()



















    # DIR = '../segmented'
    # wordss = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    # for i in range(wordss):
    #     Main.infer( "../segmented/segment" + str(i) + ".png")
    #     abc = infer.text
    #     print(abc)