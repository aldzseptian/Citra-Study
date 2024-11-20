import cv2
import numpy as np
import matplotlib.pyplot as plt

# Fungsi untuk menghitung Normalized Correlation (NC) antara dua gambar
def normalized_correlation(imageA, imageB):
    # Mengubah gambar menjadi grayscale
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
    
    # Menghitung rata-rata dan standar deviasi dari kedua gambar
    meanA = np.mean(grayA)
    meanB = np.mean(grayB)
    stdA = np.std(grayA)
    stdB = np.std(grayB)

    # Menghitung Normalized Correlation (NC)
    numerator = np.sum((grayA - meanA) * (grayB - meanB))
    denominator = np.sqrt(np.sum((grayA - meanA) ** 2) * np.sum((grayB - meanB) ** 2))
    
    if denominator == 0:
        return 0  # Hindari pembagian dengan 0 jika standar deviasi 0
    
    nc_score = numerator / denominator
    return nc_score

# Fungsi untuk menampilkan gambar
def display_images(imageA, imageB):
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    
    ax[0].imshow(cv2.cvtColor(imageA, cv2.COLOR_BGR2RGB))
    ax[0].set_title("Gambar 1")
    ax[0].axis("off")

    ax[1].imshow(cv2.cvtColor(imageB, cv2.COLOR_BGR2RGB))
    ax[1].set_title("Gambar 2")
    ax[1].axis("off")
    
    plt.show()

# Membaca dua gambar
imageA = cv2.imread("semangka.jpeg")
imageB = cv2.imread("images.jpeg")  # Gambar yang sedikit dimodifikasi

# Memastikan gambar tidak kosong
if imageA is None or imageB is None:
    print("Gambar tidak ditemukan. Pastikan file gambar sudah benar.")
else:
    # Resize gambar agar ukurannya sama
    heightA, widthA = imageA.shape[:2]
    heightB, widthB = imageB.shape[:2]
    
    if (heightA != heightB) or (widthA != widthB):
        imageB = cv2.resize(imageB, (widthA, heightA))  # Resize imageB agar sama dengan imageA

    # Menampilkan gambar
    display_images(imageA, imageB)
    
    # Menghitung Normalized Correlation (NC)
    nc_score = normalized_correlation(imageA, imageB)
    print(f"Normalized Correlation (NC): {nc_score:.4f}")