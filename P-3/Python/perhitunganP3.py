import numpy as np
import pandas as pd
from scipy import stats

# Load data dari file Excel (Pastikan file ada di direktori kerja VS Code)
file_path = "P-3\Data CM1.xlsx"
df = pd.read_excel(file_path, sheet_name="ID")

# Menghitung Mean
mean_lama_belajar = np.mean(df["Lama Belajar"])
mean_nilai_ujian = np.mean(df["Nilai Ujian"])

# Menghitung Median
median_lama_belajar = np.median(df["Lama Belajar"])
median_nilai_ujian = np.median(df["Nilai Ujian"])

# Menghitung Modus
modus_lama_belajar = stats.mode(df["Lama Belajar"], keepdims=True)[0][0]
modus_nilai_ujian = stats.mode(df["Nilai Ujian"], keepdims=True)[0][0]

# Menampilkan hasil
print("### Ukuran Kecenderungan Memusat ###")
print(f"Mean Lama Belajar: {mean_lama_belajar}")
print(f"Median Lama Belajar: {median_lama_belajar}")
print(f"Modus Lama Belajar: {modus_lama_belajar}\n")

print(f"Mean Nilai Ujian: {mean_nilai_ujian}")
print(f"Median Nilai Ujian: {median_nilai_ujian}")
print(f"Modus Nilai Ujian: {modus_nilai_ujian}")
