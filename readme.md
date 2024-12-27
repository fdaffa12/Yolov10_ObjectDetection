# Helmet Detection System

## 📝 Deskripsi

Sistem deteksi helm menggunakan model YOLO (You Only Look Once) yang dapat memproses video dan mendeteksi penggunaan helm secara real-time. Program ini dapat membedakan orang yang menggunakan helm dan tidak menggunakan helm dengan visualisasi bounding box berwarna.

## 🔧 Persyaratan Sistem

### Dependencies

- Python 3.x
- OpenCV (cv2)
- Ultralytics YOLO
- CVZone
- Tkinter (built-in dengan Python)

### Instalasi Dependencies

bash
pip install opencv-python
pip install ultralytics
pip install cvzone

## 📁 Struktur Project

project/
│
├── helmet_detection_video.py # Script utama
├── RUN DISINI.bat # Batch file untuk menjalankan program
├── Weights/
│ └── best.pt # File model YOLO terlatih
└── output_detection.mp4 # File output hasil deteksi

## ✨ Fitur Utama

### 1. Pemilihan Video

- Dialog GUI untuk memilih file video
- Mendukung format: MP4, AVI, MOV, MKV

### 2. Deteksi Objek

- Mendeteksi 2 kelas:
  - "With Helmet" (Dengan Helm)
  - "Without Helmet" (Tanpa Helm)
- Threshold confidence: 0.5 (50%)
- Visualisasi bounding box:
  - 🟢 Hijau: Menggunakan helm
  - 🔴 Merah: Tidak menggunakan helm

### 3. Output

- Tampilan video hasil deteksi real-time
- Penyimpanan hasil dalam 'output_detection.mp4'
- Resolusi output: 960x540 pixels

## 🚀 Cara Penggunaan

### Metode 1: Menggunakan Batch File

1. Double click file `RUN DISINI.bat`
2. Pilih video yang akan diproses
3. Tunggu proses deteksi

### Metode 2: Menggunakan Command Line

1. Buka terminal/command prompt
2. Navigate ke folder project
3. Jalankan perintah:
   bash
   python helmet_detection_video.py

##Solusi: Install package yang diperlukan
pip install [nama_package]

### 2. Model tidak ditemukan

- Periksa path ke file `best.pt`
- Pastikan file model ada di folder `Weights/`

### 3. Video tidak dapat dibaca

- Periksa format video
- Pastikan path video benar

## 🔍 Komponen Teknis

### Import dan Inisialisasi

python
import cv2
import math
import cvzone
from ultralytics import YOLO
from tkinter import filedialog
import tkinter as tk

### Model dan Kelas

python
model = YOLO("Weights/best.pt")
classNames = ['With Helmet', 'Without Helmet']
colors = [(0, 255, 0), (0, 0, 255)]

## 🔄 Alur Kerja Program

1. Inisialisasi GUI untuk pemilihan file
2. Load model YOLO
3. Baca video input
4. Proses frame-by-frame:
   - Deteksi objek
   - Visualisasi hasil
   - Simpan frame
5. Simpan video output

## 🚧 Pengembangan Lebih Lanjut

- [ ] Penambahan tracking objek
- [ ] Implementasi counting system
- [ ] Recording statistik
- [ ] Optimasi performa real-time

## 📝 Catatan Penting

- Pastikan Python terdaftar dalam PATH sistem
- Semua dependencies harus terinstall
- File model `best.pt` harus tersedia di folder `Weights/`

## 🤝 Kontribusi

Kontribusi selalu diterima. Untuk perubahan besar, harap buka issue terlebih dahulu untuk mendiskusikan perubahan yang diinginkan.

## 📜 Lisensi

[MIT](https://choosealicense.com/licenses/mit/)
