import cv2
import numpy as np
import matplotlib.pyplot as plt

# Membaca gambar
image = cv2.imread('semangka.jpeg', cv2.IMREAD_GRAYSCALE)

# Tampilkan gambar asli
plt.imshow(image, cmap='gray')
plt.title('Gambar Asli')
plt.axis('off')
plt.show()

# Menghitung mean dan standar deviasi menggunakan OpenCV
mean, std_dev = cv2.meanStdDev(image)
mean = mean[0][0]
std_dev = std_dev[0][0]

print(f"Mean (Rata-rata): {mean:.2f}")
print(f"Standar Deviasi: {std_dev:.2f}")

# Menghitung kovarian
cov_matrix = np.cov(image.astype(float), rowvar=False)
print("Matriks Kovarian:")
print(cov_matrix)

# Visualisasi histogram untuk melihat distribusi piksel
#plt.hist(image.ravel(), bins=256, color='blue', alpha=0.7)
#plt.title('Histogram Gambar')
#plt.xlabel('Intensitas Piksel')
#plt.ylabel('Frekuensi')
plt.show()