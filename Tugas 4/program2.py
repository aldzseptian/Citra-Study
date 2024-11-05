import cv2
import numpy as np

# Membaca gambar
images = [
    cv2.imread("lahan1.png"),
    cv2.imread("lahan2.png")
]

# Menentukan parameter untuk operasi morfologi
closeIterations = [4, 7]
openIterations = [20, 1]
kernelOpen = np.ones((5, 5), np.uint8)
kernelClose = np.ones((5, 5), np.uint8)

# Proses untuk setiap gambar
for i in range(len(images)):
    # Mengubah ukuran gambar
    images[i] = cv2.resize(images[i], (640, 480))

    # Mengubah gambar menjadi grayscale
    gray = cv2.cvtColor(images[i], cv2.COLOR_BGR2GRAY)

    # Melakukan thresholding untuk mendapatkan citra biner
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Melakukan operasi closing dan opening pada citra biner
    closing = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, kernelClose, iterations=closeIterations[i])
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernelOpen, iterations=openIterations[i])

    # Segmentasi citra dengan Canny edge detection
    segment = cv2.Canny(opening, 200, 200)

    # Menemukan kontur dari hasil segmentasi
    contours, hierarchy = cv2.findContours(segment, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    # Mengonversi citra segmentasi menjadi RGB untuk menggambar kontur
    segment = cv2.cvtColor(segment, cv2.COLOR_GRAY2RGB)

    # Menggambar kontur pada gambar
    cv2.drawContours(images[i], contours, -1, (0, 0, 255), 1)

    # Segmentasi, clustering, pemberian label, dan menghitung parameter pada citra
    centers = []
    for j in range(len(contours)):
        # Menghitung centroid dari setiap kontur
        moments = cv2.moments(contours[j])
        if moments['m00'] != 0:  # Menghindari pembagian dengan nol
            center_x = int(moments['m10'] / moments['m00'])
            center_y = int(moments['m01'] / moments['m00'])
            centers.append((center_x, center_y))

            # Menggambar bulat pada centroid
            cv2.circle(images[i], centers[-1], 1, (0, 0, 255), -1)

            # Memberi nomor pada centroid
            cv2.putText(images[i], str(j + 1), centers[-1], cv2.FONT_HERSHEY_DUPLEX, 0.75, (0, 255, 255), 1)

            # Menghitung parameter kontur: area dan perimeter
            area = round(cv2.contourArea(contours[j]), 2)
            perimeter = round(cv2.arcLength(contours[j], True), 2)

            # Menampilkan nilai area dan perimeter pada gambar
            offset = (centers[-1][0], centers[-1][1] + 20)
            cv2.putText(images[i], f"Area = {area}", offset, cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 0, 0), 1)
            offset = (centers[-1][0], centers[-1][1] + 40)
            cv2.putText(images[i], f"Perimeter = {perimeter}", offset, cv2.FONT_HERSHEY_DUPLEX, 0.5, (0, 255, 0), 1)

# Menampilkan gambar yang telah diproses
for i in range(len(images)):
    cv2.imshow(f'Gambar {i+1}', images[i])

# Menunggu hingga tombol ditekan dan menutup jendela
cv2.waitKey(0)
cv2.destroyAllWindows()
