import pandas as pd
from scipy import stats

# Load data dari file Excel
file_path = "P-3/Data CM1.xlsx"
df = pd.read_excel(file_path, sheet_name="ID")

# Cek nama kolom dalam dataset
print("Kolom dalam dataset:", df.columns)

# Sesuaikan nama kolom yang ingin dianalisis
kolom_target = "Lama Belajar"  # Pastikan sesuai dengan nama di Excel

# Konversi ke numerik untuk menghindari error
df[kolom_target] = pd.to_numeric(df[kolom_target], errors="coerce")

# Hitung Mean
mean_value = df[kolom_target].mean()

# Hitung Median
median_value = df[kolom_target].median()

# Hitung Modus (bisa lebih dari satu)
mode_result = stats.mode(df[kolom_target].dropna(), keepdims=True)

# Modus dan jumlah frekuensinya
mode_values = mode_result.mode
mode_counts = mode_result.count

# Menampilkan hasil
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")

# Menampilkan semua modus dengan frekuensinya
print("\nModus dan Frekuensinya:")
for mode, count in zip(mode_values, mode_counts):
    print(f"Nilai: {mode}, Frekuensi: {count}")
