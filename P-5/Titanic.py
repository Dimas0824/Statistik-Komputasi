import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore, norm, mode

# Path dataset di lokal
path_berkas = r"D:\MAIN TUGAS\Semester 4\Statistik Komputasi\P-5\Titanic-Dataset.csv"

# Memuat dataset
data = pd.read_csv(path_berkas)

# Menampilkan 5 data pertama
print("Data awal Titanic:")
print(data.head())

# 1. Mengecek jumlah data yang hilang pada "Usia" dan "Tarif"
nilai_hilang = data[['Age', 'Fare']].isnull().sum()
print("\nJumlah data yang hilang:")
print(nilai_hilang)

# Menampilkan grafik distribusi sebelum imputasi pada kedua variabel ("Age" dan "Fare")
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Distribusi Usia sebelum imputasi
sns.histplot(data['Age'], bins=30, kde=True, ax=axes[0], color='blue')
axes[0].set_title('Distribusi Usia Sebelum Imputasi')
axes[0].set_xlabel('Usia')
axes[0].set_ylabel('Frekuensi')

# Distribusi Tarif sebelum imputasi
sns.histplot(data['Fare'], bins=30, kde=True, ax=axes[1], color='green')
axes[1].set_title('Distribusi Tarif Sebelum Imputasi')
axes[1].set_xlabel('Tarif')
axes[1].set_ylabel('Frekuensi')

plt.tight_layout()
plt.show()

# Imputasi data yang hilang pada "Age" dengan Mean, Median, dan Modus
# Imputasi dengan Mean
rata_usia = data['Age'].mean()
rata_tarif = data['Fare'].mean()
data_mean = data.copy()
data_mean[['Age', 'Fare']] = data_mean[['Age', 'Fare']].fillna({'Age': rata_usia, 'Fare': rata_tarif})

# Imputasi dengan Median
median_usia = data['Age'].median()
median_tarif = data['Fare'].median()
data_median = data.copy()
data_median[['Age', 'Fare']] = data_median[['Age', 'Fare']].fillna({'Age': median_usia, 'Fare': median_tarif})

# Imputasi dengan Modus
mode_usia = data['Age'].mode()[0]
mode_tarif = data['Fare'].mode()[0]
data_mode = data.copy()
data_mode[['Age', 'Fare']] = data_mode[['Age', 'Fare']].fillna({'Age': mode_usia, 'Fare': mode_tarif})


# Menampilkan jumlah data yang hilang setelah imputasi
print("\nJumlah Data Hilang Setelah Imputasi (Mean):")
print(data_mean[['Age', 'Fare']].isnull().sum())

print("\nRingkasan Statistik Setelah Imputasi (Mean):")
print(data_mean[['Age', 'Fare']].describe())

print("\nJumlah Data Hilang Setelah Imputasi (Median):")
print(data_median[['Age', 'Fare']].isnull().sum())

print("\nRingkasan Statistik Setelah Imputasi (Median):")
print(data_median[['Age', 'Fare']].describe())

print("\nJumlah Data Hilang Setelah Imputasi (Modus):")
print(data_mode[['Age', 'Fare']].isnull().sum())

print("\nRingkasan Statistik Setelah Imputasi (Modus):")
print(data_mode[['Age', 'Fare']].describe())

# Distribusi Usia setelah imputasi dengan Mean
plt.figure(figsize=(7, 5))
sns.histplot(data_mean['Age'], bins=30, kde=True, color='blue')
plt.title('Distribusi Usia Setelah Imputasi dengan Mean')
plt.xlabel('Usia')
plt.ylabel('Frekuensi')
plt.show()

# Distribusi Fare setelah imputasi dengan Mean
plt.figure(figsize=(7, 5))
sns.histplot(data_mean['Fare'], bins=30, kde=True, color='blue')
plt.title('Distribusi Fare Setelah Imputasi dengan Mean')
plt.xlabel('Tarif')
plt.ylabel('Frekuensi')
plt.show()

# Distribusi Usia setelah imputasi dengan Median
plt.figure(figsize=(7, 5))
sns.histplot(data_median['Age'], bins=30, kde=True, color='orange')
plt.title('Distribusi Usia Setelah Imputasi dengan Median')
plt.xlabel('Usia')
plt.ylabel('Frekuensi')
plt.show()

# Distribusi Fare setelah imputasi dengan Median
plt.figure(figsize=(7, 5))
sns.histplot(data_median['Fare'], bins=30, kde=True, color='orange')
plt.title('Distribusi Fare Setelah Imputasi dengan Median')
plt.xlabel('Tarif')
plt.ylabel('Frekuensi')
plt.show()

# Distribusi Usia setelah imputasi dengan Modus
plt.figure(figsize=(7, 5))
sns.histplot(data_mode['Age'], bins=30, kde=True, color='green')
plt.title('Distribusi Usia Setelah Imputasi dengan Modus')
plt.xlabel('Usia')
plt.ylabel('Frekuensi')
plt.show()

# Distribusi Fare setelah imputasi dengan Modus
plt.figure(figsize=(7, 5))
sns.histplot(data_mode['Fare'], bins=30, kde=True, color='green')
plt.title('Distribusi Fare Setelah Imputasi dengan Modus')
plt.xlabel('Tarif')
plt.ylabel('Frekuensi')
plt.show()

# Menampilkan box plot untuk melihat distribusi dan outlier pada "Age"
plt.figure(figsize=(6, 5))
sns.boxplot(x=data_mean['Age'], color='lightblue')
plt.title('Box Plot untuk Usia (Age)')
plt.xlabel('Usia')
plt.show()

# Menghitung z-score dari "Age" untuk semua data
data_mean['z_score'] = zscore(data_mean['Age'])

# Menentukan jumlah outlier (z > 3)
outlier_count = (data_mean['z_score'].abs() > 3).sum()

# Menampilkan beberapa outlier
outliers = data_mean.loc[data_mean['z_score'].abs() > 3, ['Age', 'Fare']]

# Diasumsikan "Age" terdistribusi normal, menghitung peluang "Age" < 20
peluang_age_20 = norm.cdf(20, loc=rata_usia, scale=data_mean['Age'].std())

print(f"Jumlah outlier (z > 3) pada Age: {outlier_count}")
print("Outlier yang terdeteksi:")
print(outliers.head())
print(f"Peluang untuk Age < 20: {peluang_age_20:.4f}")