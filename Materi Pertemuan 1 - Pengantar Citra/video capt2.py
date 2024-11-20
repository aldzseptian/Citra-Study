import numpy as np
import cv2

# Fungsi konvolusi manual
def konvolusi(image, kernel):
    row, col = image.shape
    mrow, mcol = kernel.shape
    h = mrow // 2

    canvas = np.zeros((row, col), np.uint8)
    for i in range(h, row - h):
        for j in range(h, col - h):
            imgsum = 0
            for k in range(-h, h + 1):
                for l in range(-h, h + 1):
                    imgsum += image[i + k, j + l] * kernel[h + k, h + l]
            canvas[i, j] = np.clip(imgsum, 0, 255)
    return canvas

# Kernel HPF dan LPF
def kernel1(image):
    kernel = np.array([[-1/9, -1/9, -1/9], [-1/9, 8/9, -1/9], [-1/9, -1/9, -1/9]], np.float32)
    return konvolusi(image, kernel)

def kernel2(image):
    kernel = np.array([[0, 1/8, 0], [1/8, 1/2, 1/8], [0, 1/8, 0]], np.float32)
    return konvolusi(image, kernel)

# Menangkap video dari kamera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Tidak dapat membuka kamera.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Tidak dapat membaca frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Terapkan filter HPF dan LPF
    hpf_result = kernel1(gray)
    lpf_result = kernel2(gray)

    # Tampilkan hasil
    cv2.imshow("Original", frame)
    cv2.imshow("High Pass Filter", hpf_result)
    cv2.imshow("Low Pass Filter", lpf_result)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
