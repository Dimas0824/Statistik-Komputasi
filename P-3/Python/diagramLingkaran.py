import pandas as pd
import matplotlib.pyplot as plt

# Load data dari file Excel (Pastikan file ada di direktori kerja VS Code)
file_path = "P-3\Data CM1.xlsx"
df = pd.read_excel(file_path, sheet_name="ID")

# Diagram Lingkaran untuk "Lama Belajar"
plt.figure(figsize=(12, 5))

lama_belajar_counts = df["Lama Belajar"].value_counts().sort_index()
plt.subplot(1, 2, 1)
plt.pie(
    lama_belajar_counts, 
    labels=lama_belajar_counts.index, 
    autopct='%1.1f%%', 
    colors=['blue', 'lightblue', 'cyan'], 
    startangle=90,
    pctdistance=0.8,
    labeldistance=1.1
)
plt.title("Proporsi Lama Belajar")

# Diagram Lingkaran untuk "Nilai Ujian"
nilai_ujian_counts = df["Nilai Ujian"].value_counts().sort_index()
plt.subplot(1, 2, 2)
plt.pie(
    nilai_ujian_counts, 
    labels=nilai_ujian_counts.index, 
    autopct='%1.1f%%', 
    colors=['red', 'lightcoral', 'salmon'], 
    startangle=90,
    pctdistance=0.8
)
plt.title("Proporsi Nilai Ujian")

plt.show()
