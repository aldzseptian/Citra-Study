import cv2
import numpy as np
import matplotlib.pyplot as plt

def bit_error_rate(image1, image2):
    """
    Menghitung Bit Error Rate (BER) antara dua citra biner.
    
    Args:
        image1: Citra pertama (numpy array, grayscale).
        image2: Citra kedua (numpy array, grayscale).
    
    Returns:
        ber: Nilai Bit Error Rate (float).
    """
    # Pastikan kedua citra memiliki ukuran yang sama
    if image1.shape != image2.shape:
        print("Ukuran citra berbeda, melakukan resize...")
        image2_resized = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
    else:
        image2_resized = image2

    # Binerkan citra (thresholding untuk mendapatkan citra biner)
    _, image1_bin = cv2.threshold(image1, 127, 255, cv2.THRESH_BINARY)
    _, image2_bin = cv2.threshold(image2_resized, 127, 255, cv2.THRESH_BINARY)

    # Hitung jumlah kesalahan bit (pixel yang berbeda)
    error_pixels = np.sum(image1_bin != image2_bin)
    
    # Hitung Bit Error Rate (BER)
    total_pixels = image1.size
    ber = error_pixels / total_pixels

    return ber, image2_resized

def display_images(image1, image2_resized):
    """
    Fungsi untuk menampilkan dua citra dalam satu jendela menggunakan matplotlib.
    
    Args:
        image1: Citra pertama (numpy array).
        image2_resized: Citra template yang telah diresize (numpy array).
    """
    plt.figure(figsize=(12, 6))

    # Menampilkan citra utama (image1)
    plt.subplot(1, 2, 1)
    plt.imshow(image1, cmap='gray')
    plt.title("Gambar 1")
    plt.axis('off')

    # Menampilkan citra template setelah resize (image2_resized)
    plt.subplot(1, 2, 2)
    plt.imshow(image2_resized, cmap='gray')
    plt.title("Gambar 2")
    plt.axis('off')

    plt.show()

def main():
    # Membaca citra utama dan citra template
    image1 = cv2.imread('images.jpeg', cv2.IMREAD_GRAYSCALE)  # Citra utama
    image2 = cv2.imread('images2.jpeg', cv2.IMREAD_GRAYSCALE)  # Citra template
    
    # Pastikan citra dibaca dengan benar
    if image1 is None or image2 is None:
        print("Gagal membaca salah satu citra!")
        return
    
    # Hitung Bit Error Rate (BER)
    ber_value, image2_resized = bit_error_rate(image1, image2)
    print(f"Bit Error Rate (BER): {ber_value:.6f}")
    
    # Menampilkan citra utama dan template setelah resize menggunakan display_images
    display_images(image1, image2_resized)

if __name__ == "__main__":
    main()
