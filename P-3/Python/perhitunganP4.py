import pandas as pd
import numpy as np
from tabulate import tabulate

# Load dataset dari file yang diunggah
file_path = "P-3/Data CM1.xlsx"  
df = pd.read_excel(file_path, sheet_name="ID")

# Ambil kolom yang relevan
lama_belajar = df["Lama Belajar"].values
nilai_ujian = df["Nilai Ujian"].values

# 1. Menghitung Rentang (Range)
range_lama_belajar = np.max(lama_belajar) - np.min(lama_belajar)
range_nilai_ujian = np.max(nilai_ujian) - np.min(nilai_ujian)

# 2. Menghitung Varians (Population & Sample)
variasi_populasi_lama_belajar = np.var(lama_belajar, ddof=0)  # Populasi
variasi_sampel_lama_belajar = np.var(lama_belajar, ddof=1)  # Sampel

variasi_populasi_nilai = np.var(nilai_ujian, ddof=0)  # Populasi
variasi_sampel_nilai = np.var(nilai_ujian, ddof=1)  # Sampel

# 3. Menghitung Simpangan Baku (Standard Deviation)
std_population_lama = np.sqrt(variasi_populasi_lama_belajar)
std_sample_lama = np.sqrt(variasi_sampel_lama_belajar)

std_population_nilai = np.sqrt(variasi_populasi_nilai)
std_sample_nilai = np.sqrt(variasi_sampel_nilai)

# Membuat dataframe untuk hasil
data = {
    "Statistik": [
        "Rentang",
        "Varians Populasi",
        "Varians Sampel",
        "Simpangan Baku Populasi",
        "Simpangan Baku Sampel"
    ],
    "Lama Belajar": [
        range_lama_belajar,
        variasi_populasi_lama_belajar,
        variasi_sampel_lama_belajar,
        std_population_lama,
        std_sample_lama
    ],
    "Nilai Ujian": [
        range_nilai_ujian,
        variasi_populasi_nilai,
        variasi_sampel_nilai,
        std_population_nilai,
        std_sample_nilai
    ]
}

# Konversi ke DataFrame
df_hasil = pd.DataFrame(data)

# Tampilkan tabel
print(tabulate(df_hasil, headers="keys", tablefmt="grid"))
