import cv2
import numpy as np

img = cv2.imread("d:\\Data Kuliah\Citra Digital - Semester 5\\banana.jpg", 0)
imgO = cv2.imread("d:\\Data Kuliah\Citra Digital - Semester 5\\apel.jpg", 0)
imgC = cv2.imread("d:\\Data Kuliah\Citra Digital - Semester 5\\semangka.jpeg", 0)

kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
dilation = cv2.dilate(img,kernel,iterations = 1)
opening = cv2.morphologyEx(imgO, cv2.MORPH_OPEN, kernel)
opening = cv2.resize(opening, (300,300))
closing = cv2.morphologyEx(imgC, cv2.MORPH_CLOSE, kernel)
closing = cv2.resize(closing, (300,300))

titles = ['Normal Image', 'Erosion',
          'Dilation', 'Before Opening', 
          'Opening', 'Before Closing', 'Closing']

images = [img, erosion, dilation, imgO, opening, imgC, closing]

cv2.imshow("img", img)
cv2.imshow("erosion", erosion)
cv2.imshow("dilation", dilation)
cv2.imshow("imgO", imgO)
cv2.imshow("opening", opening)
cv2.imshow("imgC", imgC)
cv2.imshow("closing", closing)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("banana", erosion)
cv2.waitKey(0)

"""
for i in range(7):
    plt.subplot(2,5,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
"""