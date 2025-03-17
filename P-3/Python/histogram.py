import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load data dari file Excel (Pastikan file ada di direktori kerja VS Code)
file_path = "P-3\Data CM1.xlsx"
df = pd.read_excel(file_path, sheet_name="ID")

plt.figure(figsize=(12, 5))

# Histogram Lama Belajar
plt.subplot(1, 2, 1)
sns.histplot(df["Lama Belajar"], bins=10, kde=True, color="blue")
plt.title("Histogram Lama Belajar")
plt.xlabel("Lama Belajar (jam)")
plt.ylabel("Frekuensi")

# Histogram Nilai Ujian
plt.subplot(1, 2, 2)
sns.histplot(df["Nilai Ujian"], bins=10, kde=True, color="red")
plt.title("Histogram Nilai Ujian")
plt.xlabel("Nilai Ujian")
plt.ylabel("Frekuensi")

plt.show()
