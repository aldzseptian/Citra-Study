# rotasi
import cv2

img = cv2.imread("d:\Data Kuliah\Citra Digital - Semester 5\images2.jpeg")
baris, coloms, ghgh = img.shape

MRotasi = cv2.getRotationMatrix2D((coloms/2, baris/2), 90, 1)

print(MRotasi)

dstRotasi = cv2.warpAffine(img, MRotasi, (coloms, baris))

cv2.imshow('title',dstRotasi)

cv2.waitKey(0)
cv2.destroyAllWindows()