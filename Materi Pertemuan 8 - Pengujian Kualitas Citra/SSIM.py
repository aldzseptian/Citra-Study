# -- coding: utf-8 --
"""
Created on Tue Nov 19 11:30:40 2024

@author: Asus
"""

import cv2
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt

# Fungsi untuk mengubah ukuran gambar menjadi sama
def resize_images(imageA, imageB):
    height = max(imageA.shape[0], imageB.shape[0])
    width = max(imageA.shape[1], imageB.shape[1])
    dim = (width, height)
    
    resized_imageA = cv2.resize(imageA, dim, interpolation=cv2.INTER_AREA)
    resized_imageB = cv2.resize(imageB, dim, interpolation=cv2.INTER_AREA)
    
    return resized_imageA, resized_imageB

# Fungsi untuk menghitung SSIM antara dua gambar
def calculate_ssim(imageA, imageB):
    # Mengubah gambar menjadi grayscale
    grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
    grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

    # Menghitung SSIM
    score, diff = ssim(grayA, grayB, full=True)
    print(f"SSIM: {score:.4f}")

    # Mengubah perbedaan (diff) menjadi tipe data uint8
    diff = (diff * 255).astype("uint8")

    # Menampilkan gambar asli dan hasil perbedaan
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    ax[0].imshow(cv2.cvtColor(imageA, cv2.COLOR_BGR2RGB))
    ax[0].set_title("Gambar 1")
    ax[0].axis("off")

    ax[1].imshow(cv2.cvtColor(imageB, cv2.COLOR_BGR2RGB))
    ax[1].set_title("Gambar 2")
    ax[1].axis("off")

    ax[2].imshow(diff, cmap='gray')
    ax[2].set_title("Perbedaan")
    ax[2].axis("off")

    plt.tight_layout()
    plt.show()

    return score

# Membaca dua gambar
imageA = cv2.imread("semangka.jpeg")
imageB = cv2.imread("banana.jpg")

# Memastikan gambar tidak kosong
if imageA is None or imageB is None:
    print("Gambar tidak ditemukan. Pastikan file gambar sudah benar.")
else:
    # Mengubah ukuran gambar agar sama
    imageA_resized, imageB_resized = resize_images(imageA, imageB)
    
    # Menghitung SSIM
    score = calculate_ssim(imageA_resized, imageB_resized)