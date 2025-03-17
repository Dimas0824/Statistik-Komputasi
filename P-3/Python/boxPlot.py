import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load dataset dari file
file_path = "P-3/Data CM1.xlsx"  # Pastikan path sesuai
df = pd.read_excel(file_path, sheet_name="ID")

# Membuat figure dan axis
plt.figure(figsize=(12, 6))

# Plot pertama: Lama Belajar
plt.subplot(1, 2, 1)
sns.boxplot(y=df["Lama Belajar"], color="skyblue")
plt.title("Box Plot Lama Belajar")
plt.yticks(fontsize=7)

# Menyesuaikan interval pada sumbu Y
min_val = df["Lama Belajar"].min()
max_val = df["Lama Belajar"].max()
plt.yticks(np.arange(min_val, max_val + 1, step=2))

# Menambahkan grid untuk memperjelas angka
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Plot kedua: Nilai Ujian
plt.subplot(1, 2, 2)
sns.boxplot(y=df["Nilai Ujian"], color="salmon")
plt.title("Box Plot Nilai Ujian")
plt.yticks(fontsize=7)

# Menyesuaikan interval pada sumbu Y
min_val = df["Nilai Ujian"].min()
max_val = df["Nilai Ujian"].max()
plt.yticks(np.arange(min_val, max_val + 1, step=2))

# Menampilkan grid untuk plot kedua juga
plt.grid(axis="y", linestyle="--", alpha=0.7)

# Tampilkan plot
plt.tight_layout()
plt.show()
