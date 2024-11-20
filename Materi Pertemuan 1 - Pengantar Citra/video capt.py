import cv2

# Inisialisasi kamera bawaan laptop
cap = cv2.VideoCapture(0)

camera = cv2.VideoCapture(0, cv2.CAP_DSHOW) #Membuka koneksi ke kamera dengan ID 0 (kamera default) menggunakan DirectShow (cv2.CAP_DSHOW) sebagai backend untuk menangkap video dari kamera.
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 680)  #Mengatur lebar frame video sebesar 680 piksel 
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 340) #Mengatur ketinggian frame video 340 piksel

while True:
    # Baca frame dari kamera
    ret, frame = cap.read()

    # Membalik frame secara horizontal
    frame = cv2.flip(frame, 1)

    # Konversi frame ke mode HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    print(hsv_frame)
    # Konversi frame ke grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.threshold(gray_frame, 128, 255, cv2.THRESH_BINARY)
    print(gray_frame)
    # Konversi frame ke citra hitam-putih (binary)
    _, bw_frame = cv2.threshold(gray_frame, 128, 255, cv2.THRESH_BINARY)
    print(bw_frame)
    
    # Tampilkan empat jendela
    
    #cv2.imshow('Original', frame) #jendela warna asli
    #cv2.imshow('HSV', hsv_frame) #jendela warna pekat 
    cv2.imshow('Grayscale', gray_frame) #jendela warna abu abu
    #cv2.imshow('Black and White', bw_frame) #jendela warna hitam putih

    # Tekan tombol 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Tutup kamera dan jendela
cap.release()
cv2.destroyAllWindows()
