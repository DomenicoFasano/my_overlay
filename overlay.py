from PIL import Image
import numpy as np

# GLOBAL VARIABLES
JPG_PATH = 'sara.jpg'
PNG_PATH = 'slash.png'
PNG_RESIZED_DIMENSION = 32
OUTPUT_JPG_PATH = 'sara_slash.jpg'

# START OF THE SCRIPT 'my_overlay'
img = np.array(Image.open(JPG_PATH))
png = np.array(Image.open(PNG_PATH).resize((PNG_RESIZED_DIMENSION, PNG_RESIZED_DIMENSION)))
n0, n1, n2 = np.shape(img)
# getting the alpha channel of the png
a = png[0:PNG_RESIZED_DIMENSION, 0:PNG_RESIZED_DIMENSION, 3]

for x in range(0, n0 - PNG_RESIZED_DIMENSION, PNG_RESIZED_DIMENSION):
    for y in range(0, n1 - PNG_RESIZED_DIMENSION, PNG_RESIZED_DIMENSION):
        for x2 in range(PNG_RESIZED_DIMENSION):
            for y2 in range(PNG_RESIZED_DIMENSION):
                if a[x2, y2] == 0:
                    img[x + x2, y + y2, 0] = 0
                    img[x + x2, y + y2, 1] = 0
                    img[x + x2, y + y2, 2] = 0

pil_img = Image.fromarray(img.astype('uint8'), 'RGB')
w, h = pil_img.size
# the image is cropped to clean the borders before being saved
pil_img.crop((0, 0, w - PNG_RESIZED_DIMENSION, h - PNG_RESIZED_DIMENSION)).save(OUTPUT_JPG_PATH)
