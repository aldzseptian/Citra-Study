import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load the original image in color
img = cv2.imread('D:/Data Kuliah/Citra Digital - Semester 5/semangka.jpeg')

# Create different types of blurs
blur1 = cv2.blur(img, (3, 3))
blur2 = cv2.GaussianBlur(img, (3, 3), 0)
median = cv2.medianBlur(img, 3)
blur3 = cv2.bilateralFilter(img, 9, 75, 75)

# Titles for the subplots
titles = ['Gambar Asli', 'Averaging', 'Gaussian Blur', 'Bilateral Blur', 'Median Blur']
images = [img, blur1, blur2, blur3, median]

# Display images with appropriate color settings
for i in range(5):  # Adjusted to iterate through all 5 images
    plt.subplot(2, 3, i + 1)
    if i == 0:
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))  # Original image in color
    else:
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY), cmap='gray')  # Blurred images in grayscale
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])

plt.show()
cv2.destroyAllWindows()
