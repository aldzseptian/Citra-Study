import cv2
import numpy as np
from scipy import ndimage

# Read the original image
img = cv2.imread('686027dc0db04ae6272ac72b6a7ed195.jpg') 
# Display original image
cv2.imshow('Original', img)

# Convert to grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Blur the image for better edge detection
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0)

# Sobel Edge Detection
sobelx = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=0, ksize=5) # Sobel Edge Detection on the X axis
sobely = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=0, dy=1, ksize=5) # Sobel Edge Detection on the Y axis
sobelxy = cv2.Sobel(src=img_blur, ddepth=cv2.CV_64F, dx=1, dy=1, ksize=5) # Combined X and Y Sobel Edge Detection
# Display Sobel Edge Detection Images
cv2.imshow('Sobel X', sobelx)
cv2.imshow('Sobel Y', sobely)
cv2.imshow('Sobel X Y using Sobel() function', sobelxy)

# Canny Edge Detection
edges = cv2.Canny(image=img_blur, threshold1=100, threshold2=200) # Canny Edge Detection
cv2.imshow('Canny Edge Detection', edges)

# Prewitt Edge Detection
prewittx = cv2.filter2D(img_blur, -1, np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])) # Prewitt X
prewitty = cv2.filter2D(img_blur, -1, np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])) # Prewitt Y
prewittxy = prewittx + prewitty
cv2.imshow('Prewitt X', prewittx)
cv2.imshow('Prewitt Y', prewitty)
cv2.imshow('Prewitt XY', prewittxy)

# Roberts Edge Detection
robertsx = cv2.filter2D(img_blur, -1, np.array([[1, 0], [0, -1]])) # Roberts X
robertsy = cv2.filter2D(img_blur, -1, np.array([[0, 1], [-1, 0]])) # Roberts Y
robertsxy = robertsx + robertsy
cv2.imshow('Roberts X', robertsx)
cv2.imshow('Roberts Y', robertsy)
cv2.imshow('Roberts XY', robertsxy)

# Laplacian of Gaussian (LoG) Edge Detection
log = cv2.Laplacian(img_blur, cv2.CV_64F, ksize=3)
cv2.imshow('Laplacian of Gaussian (LoG)', log)

# Zero-Crossing Edge Detection (menggunakan Laplacian)
laplacian = cv2.Laplacian(img, cv2.CV_64F)
zero_crossing = np.zeros_like(laplacian)
zero_crossing[laplacian > 0] = 255
zero_crossing[laplacian < 0] = 0
cv2.imshow('Zerro Crossing', zero_crossing)

cv2.waitKey(0)
cv2.destroyAllWindows()