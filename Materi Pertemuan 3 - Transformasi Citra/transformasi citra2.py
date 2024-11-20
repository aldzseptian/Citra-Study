# Skala Gambar
import cv2
#from google.colab.patches import cv2_imshow

img = cv2.imread('d:\\Data Kuliah\\Citra Digital - Semester 5\\images2.jpeg')

dstSkala = cv2.resize(img, None, fx=2.5, fy=2, interpolation=cv2.INTER_CUBIC)
cv2.imshow('original ',img)
cv2.imshow('resize',dstSkala)

cv2.waitKey(0)
cv2.destroyAllWindows()

#Translasi Citra
# translasi

import numpy as np

print(img.shape)

baris, coloms, ghgh = img.shape

MTranslasi = np.float32([
     [2, 0, 100],
     [0, 2, 50]           
    ])

print(MTranslasi, '\n')


dst = cv2.warpAffine(img, MTranslasi, (coloms, ghgh))
cv2.imshow(dst)
