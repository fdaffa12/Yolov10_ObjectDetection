Dokumentasi Deteksi Helm Menggunakan YOLO
Library yang Dibutuhkan
Instal library berikut menggunakan pip:

pip install opencv-python
pip install cvzone
pip install ultralytics

Penjelasan Kode

1. Import Library yang Diperlukan

   import cv2 # Untuk pemrosesan gambar dan video
   import math # Untuk operasi matematika
   import cvzone # Untuk menggambar kotak deteksi
   from ultralytics import YOLO # Model YOLO untuk deteksi objek

2. Inisialisasi Video

   Program menggunakan video dari file Sample.mp4
   Bisa diganti dengan webcam dengan mengubah video_path menjadi 0
   Program mengambil properti video (lebar, tinggi, fps)
   Menyiapkan file output dengan nama output_detection.mp4

3. Model YOLO

   Menggunakan model YOLO yang sudah dilatih dengan file weights best.pt
   Dapat mendeteksi 2 kelas:
   With Helmet (Dengan Helm) - ditandai warna hijau
   Without Helmet (Tanpa Helm) - ditandai warna merah

4. Proses Deteksi

   Program membaca frame video satu per satu
   Setiap frame diproses menggunakan model YOLO
   Untuk setiap objek yang terdeteksi:
   Mengambil koordinat kotak pembatas (bounding box)
   Menghitung tingkat kepercayaan (confidence)
   Menampilkan kotak dengan warna sesuai kelas jika confidence > 0.5
   Catatan Penting
   Pastikan file model best.pt tersedia di folder Weights
   Pastikan video input tersedia di folder Media
   Program akan membuat file output bernama output_detection.mp4
   Format video output disesuaikan dengan ukuran 960x540 piksel
