# Deskripsi FaceLocalization

Berikut Merupakan Penjelasan Kodingan ini dan tampilan Output yang ditampilkan.

## Penjelasan Kodingan Berikut.

Kode ini merupakan implementasi sistem pelacakan lokasi wajah secara probabilistik dengan kalibrasi berbasis z-axis. 
Sistem dimulai dengan deteksi wajah menggunakan OpenCV dan model Haar Cascade. 
Tahap pertama adalah kalibrasi di mana pengguna menentukan tiga titik referensi lokasi (terdekat, netral, terjauh) berdasarkan ukuran wajah yang terdeteksi. 
Selama kalibrasi, interpolasi dilakukan untuk menghasilkan distribusi lokasi di sepanjang sumbu-z. 
Setelah kalibrasi, sistem memperbarui estimasi lokasi secara real-time menggunakan prinsip Bayesian berdasarkan ukuran wajah yang terdeteksi. 
Hasil akhirnya adalah lokasi dengan probabilitas tertinggi ditampilkan di layar secara dinamis, memberikan indikasi posisi wajah relatif terhadap kamera.

## Hasil Output dari kodingan.
Tombol W
![Contoh Gambar](https://github.com/aldzseptian/Citra-Study/blob/main/Materi%20Pertemuan%209%20-%20UAS/Gambar/tombol%20c.png)

Tombol C
![Contoh Gambar](https://github.com/aldzseptian/Citra-Study/blob/main/Materi%20Pertemuan%209%20-%20UAS/Gambar/tombol%20s.png)

Tombol S
![Contoh Gambar](https://github.com/aldzseptian/Citra-Study/blob/main/Materi%20Pertemuan%209%20-%20UAS/Gambar/tombol%20w.png)

## Penjelasan Hasil Output dari kodingan.
Tombol W - Terdekat
Saat tombol W ditekan, ukuran deteksi wajah (face_box[2] dan face_box[3]) disimpan ke dalam calibration_rects pada indeks 0, yang merepresentasikan titik terdekat dalam sumbu-z. 
Ukuran ini menjadi referensi untuk lokasi terdekat, biasanya ketika wajah berada sangat dekat dengan kamera.

Tombol C - Netral
Tombol ini menetapkan ukuran wajah untuk lokasi netral (tengah sumbu-z) dan menyimpannya dalam indeks no_points_either_side, yaitu tengah dari panjang z_axis_length (contoh: indeks ke-5 jika z_axis_length = 11). 
Ini menjadi titik tengah skala untuk menghitung perubahan ukuran ke arah terdekat atau terjauh.

Tombol S - Terjauh
Ketika tombol ini ditekan, ukuran wajah untuk lokasi terjauh disimpan pada indeks z_axis_length - 1 (contoh: indeks ke-10 jika z_axis_length = 11). 
Ini merepresentasikan lokasi di mana wajah terdeteksi dalam ukuran terkecil, biasanya jauh dari kamera.

Tombol Q - Selesai Kalibrasi
Setelah semua titik referensi (W, C, S) ditentukan, menekan Q akan memproses skala antar-titik. 
Perbedaan ukuran wajah di antara titik-titik dihitung, dan interpolasi dilakukan untuk mengisi nilai di setiap indeks di antara lokasi terdekat, netral, dan terjauh. 
Hasilnya adalah daftar lengkap ukuran wajah di setiap posisi pada sumbu-z, merepresentasikan hubungan ukuran dengan jarak.

Kode menghasilkan skala ukuran wajah yang terdistribusi di sepanjang sumbu-z berdasarkan ukuran terdekat, netral, dan terjauh. 
Skala ini digunakan untuk memetakan posisi wajah dalam ruang 3D relatif terhadap kamera.
