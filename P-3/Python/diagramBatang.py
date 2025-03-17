import matplotlib.pyplot as plt
import pandas as pd

# Load data dari file Excel (Pastikan file ada di direktori kerja VS Code)
file_path = "P-3\Data CM1.xlsx"
df = pd.read_excel(file_path, sheet_name="ID")

# Menghitung frekuensi untuk variabel "Lama Belajar" dan "Nilai Ujian"
lama_belajar_counts = df["Lama Belajar"].value_counts().sort_index()
nilai_ujian_counts = df["Nilai Ujian"].value_counts().sort_index()

# Membuat Diagram Batang
fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Diagram Batang untuk Lama Belajar
ax[0].bar(lama_belajar_counts.index, lama_belajar_counts.values, color='skyblue', width=2)
ax[0].set_title("Distribusi Lama Belajar")
ax[0].set_xlabel("Lama Belajar (jam)")
ax[0].set_xticks(lama_belajar_counts.index[::2])  # Menampilkan label dengan interval 2
ax[0].tick_params(axis='x', rotation=90)  # Putar hingga vertikal
ax[0].tick_params(axis='x', labelsize=8)  # Mengurangi ukuran teks sumbu x
ax[0].set_ylabel("Jumlah Mahasiswa")

# Diagram Batang untuk Nilai Ujian
ax[1].bar(nilai_ujian_counts.index, nilai_ujian_counts.values, color='lightcoral', width=2)
ax[1].set_title("Distribusi Nilai Ujian")
ax[1].set_xlabel("Nilai Ujian")
ax[1].set_xticks(nilai_ujian_counts.index[::2])  # Menampilkan label dengan interval 2
ax[1].tick_params(axis='x', rotation=90)  # Putar hingga vertikal
ax[0].tick_params(axis='x', labelsize=8)  # Mengurangi ukuran teks sumbu x
ax[1].set_ylabel("Jumlah Mahasiswa")

plt.tight_layout()
plt.show()
