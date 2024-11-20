import cv2

# Membaca gambar
img = cv2.imread('d:\\Data Kuliah\\Citra Digital - Semester 5\\images2.jpeg')

# Mengubah ukuran gambar
dstSkala = cv2.resize(img, None, fx=2.5, fy=2, interpolation=cv2.INTER_CUBIC)

# Menampilkan gambar asli
cv2.imshow('Original Image', img)

# Menampilkan gambar yang telah diubah ukurannya
cv2.imshow('Resized Image', dstSkala)

# Menunggu tombol ditekan dan menutup semua jendela
cv2.waitKey(0)
cv2.destroyAllWindows()
