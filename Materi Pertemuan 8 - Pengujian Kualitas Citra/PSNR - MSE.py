import cv2
import numpy as np
import sys

def mse(image1, image2):
    # Menghitung Mean Squared Error (MSE)
    error = np.mean((image1 - image2) ** 2)
    return error

def psnr(image1, image2):
    mse_value = mse(image1, image2)
    if mse_value == 0:
        return float('inf')  # Jika MSE 0, maka PSNR tak terhingga
    max_pixel = 255.0
    psnr_value = 20 * np.log10(max_pixel / np.sqrt(mse_value))
    return psnr_value

# Membaca dua citra
image1 = cv2.imread('semangka.jpeg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('semangka.jpeg', cv2.IMREAD_GRAYSCALE)

# Memeriksa apakah citra berhasil dibaca
if image1 is None or image2 is None:
    print("Gagal membaca citra.")
    sys.exit()

# Memastikan ukuran citra sama, jika tidak sama maka ubah ukurannya
if image1.shape != image2.shape:
    print("Ukuran citra tidak sama, melakukan resize.")
    image2 = cv2.resize(image2, (image1.shape[1], image1.shape[0]))

# Menambahkan sedikit noise pada citra kedua agar bisa dihitung MSE dan PSNR
noise = np.random.normal(0, 10, image2.shape).astype(np.uint8)
image2 = cv2.add(image2, noise)

# Menghitung MSE dan PSNR
mse_value = mse(image1, image2)
psnr_value = psnr(image1, image2)

print(f"MSE: {mse_value:.2f}")
print(f"PSNR: {psnr_value:.2f} dB")

# Menampilkan gambar
cv2.imshow("Gambar 1 (Asli)", image1)
cv2.imshow("Gambar 2 (Dengan Noise)", image2)

# Menunggu tombol tekan untuk menutup jendela
cv2.waitKey(0)
cv2.destroyAllWindows()