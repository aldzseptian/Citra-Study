import cv2
import numpy as np

# Membaca gambar pertama dan kedua
images = [
    cv2.imread("lahan1.png"),  # Membaca gambar pertama
    cv2.imread("lahan2.png")   # Membaca gambar kedua
]

# Fungsi untuk menghitung titik tengah antara dua titik (centroid)
def getCenterofLine(object1, object2, x=0, y=0):
    offset = (int(object1[0] / 2) + int(object2[0] / 2) + x,
              int(object1[1] / 2) + int(object2[1] / 2) + y)
    return offset

# Menentukan iterasi untuk operasi morfologi
closeIterations = [7, 2]
openIterations = [1, 4]
kernelOpen = np.ones((5, 5), np.uint8)  # Kernel untuk operasi opening (5x5 matriks)
kernelClose = np.ones((5, 5), np.uint8) # Kernel untuk operasi closing (5x5 matriks)

centers = []  # List untuk menyimpan posisi centroid

# Proses untuk setiap gambar
for i in range(len(images)):
    # Mengubah ukuran gambar menjadi 640x480
    images[i] = cv2.resize(images[i], (640, 480))

    # Mengubah gambar menjadi grayscale
    gray = cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY)

    # Melakukan thresholding untuk mendapatkan citra biner
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Melakukan operasi closing dan opening pada citra
    closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernelClose, iterations=closeIterations[i])
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernelOpen, iterations=openIterations[i])

    # Segmentasi citra dengan Canny edge detection
    segment = cv2.Canny(opening, 200, 200)

    # Menemukan kontur dari hasil segmentasi
    contours, hierarchy = cv2.findContours(segment, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Mengonversi citra segmentasi menjadi RGB untuk menggambar kontur
    segment = cv2.cvtColor(segment, cv2.COLOR_GRAY2RGB)

    # Menggambar setiap kontur pada gambar
    for j in range(len(contours)):
        moments = cv2.moments(contours[j])
        if moments['m00'] != 0:  # Menghindari pembagian dengan nol
            center_x = int(moments['m10'] / moments['m00'])  # Menghitung koordinat x centroid
            center_y = int(moments['m01'] / moments['m00'])  # Menghitung koordinat y centroid
            centers.append((center_x, center_y))  # Menambahkan centroid ke list

            # Menggambar titik pada posisi centroid
            cv2.circle(images[i], centers[-1], 1, (0, 0, 255), -1)  # Titik merah di centroid

            # Memberikan nomor pada setiap centroid
            cv2.putText(images[i], str(j + 1), centers[-1], cv2.FONT_HERSHEY_DUPLEX, 0.75, (255, 0, 0), 1)

    # Menghitung jarak antara centroid pada gambar pertama (dalam piksel dan kilometer)
    if len(centers) > 1:
        pixelDistance = cv2.norm(centers[0], centers[1], cv2.NORM_L2)  # Menghitung jarak Euclidean antara centroid
        kmDistance = pixelDistance / 40.1836969001148  # Mengkonversi jarak piksel ke kilometer (1 km = 40 piksel)
        # Menggambar garis antara kedua centroid dan menampilkan jarak dalam piksel
        cv2.line(images[i], centers[0], centers[1], (0, 255, 255), 2)
        cv2.putText(images[i], f'd = {pixelDistance:.2f} px', getCenterofLine(centers[0], centers[1]), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 255), 1)
        cv2.putText(images[i], f'd = {kmDistance:.4f} km', getCenterofLine(centers[0], centers[1], y=-20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 255), 1)

    # Menghitung jarak antara centroid pada gambar kedua (dalam piksel dan meter)
    if len(centers) > 3:
        pixelDistance = cv2.norm(centers[2], centers[4], cv2.NORM_L2)  # Menghitung jarak Euclidean antara centroid
        kmDistance = pixelDistance / 0.24705882352941178  # Mengkonversi jarak piksel ke meter (1 meter = 0.24 piksel)
        # Menggambar garis antara kedua centroid dan menampilkan jarak dalam piksel
        cv2.line(images[i], centers[2], centers[4], (0, 255, 255), 2)
        cv2.putText(images[i], f'd = {pixelDistance:.2f} px', getCenterofLine(centers[2], centers[4]), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 255), 1)
        cv2.putText(images[i], f'd = {kmDistance:.4f} m', getCenterofLine(centers[2], centers[4], y=-20), cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 255), 1)

# Menampilkan gambar yang telah diproses
for i in range(len(images)):
    cv2.imshow(f'Gambar {i+1}', images[i])  # Menampilkan gambar

# Menunggu hingga tombol ditekan dan menutup jendela
cv2.waitKey(0)
cv2.destroyAllWindows()
