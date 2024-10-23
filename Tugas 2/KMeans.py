import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('686027dc0db04ae6272ac72b6a7ed195.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Reshape the image to a 2D array of pixels
pixels = image.reshape(-1, 3)

# Number of clusters (K)
k = 5

# Apply K-means clustering
kmeans = KMeans(n_clusters=k)
kmeans.fit(pixels)

# Get the cluster centers (dominant colors)
colors = kmeans.cluster_centers_.astype(int)

# Assign each pixel to the nearest cluster center
labels = kmeans.labels_
segmented_image = colors[labels].reshape(image.shape)

# Display the original and segmented images
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.title('Original Image')
plt.imshow(image)
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Segmented Image with K-means')
plt.imshow(segmented_image)
plt.axis('off')

plt.show()
