# Affine
import cv2
import numpy as np

img = cv2.imread("d:\Data Kuliah\Citra Digital - Semester 5\images2.jpeg")
baris, coloms, ghgh = img.shape

ttkAsal = np.float32([[172,109], [282,65], [272,316]])
ttkTujuan = np.float32([[53,128], [471,46], [275, 385]])

MAffine = cv2.getAffineTransform(ttkAsal, ttkTujuan)

print(MAffine)

dstAffine = cv2.warpAffine(img, MAffine, (coloms, baris))

cv2.imshow('title',dstAffine)

cv2.waitKey(0)
cv2.destroyAllWindows()