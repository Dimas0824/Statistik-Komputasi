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
data_mean = data.copy()
data_mean['Age'] = data_mean['Age'].fillna(rata_usia)

# Imputasi dengan Median
median_usia = data['Age'].median()
data_median = data.copy()
data_median['Age'] = data_median['Age'].fillna(median_usia)

# Imputasi dengan Modus
mode_usia = data['Age'].mode()[0]
data_mode = data.copy()
data_mode['Age'] = data_mode['Age'].fillna(mode_usia)

# Menampilkan jumlah data yang hilang setelah imputasi
print("\nJumlah Data Hilang Setelah Imputasi (Mean):")
print(data_mean['Age'].isnull().sum())

print("\nRingkasan Statistik Setelah Imputasi (Mean):")
print(data_mean['Age'].describe())

print("\nJumlah Data Hilang Setelah Imputasi (Median):")
print(data_median['Age'].isnull().sum())

print("\nRingkasan Statistik Setelah Imputasi (Median):")
print(data_median['Age'].describe())

print("\nJumlah Data Hilang Setelah Imputasi (Modus):")
print(data_mode['Age'].isnull().sum())

print("\nRingkasan Statistik Setelah Imputasi (Modus):")
print(data_mode['Age'].describe())

# Distribusi Usia setelah imputasi dengan Mean
plt.figure(figsize=(7, 5))
sns.histplot(data_mean['Age'], bins=30, kde=True, color='blue')
plt.title('Distribusi Usia Setelah Imputasi dengan Mean')
plt.xlabel('Usia')
plt.ylabel('Frekuensi')
plt.show()

# Distribusi Usia setelah imputasi dengan Median
plt.figure(figsize=(7, 5))
sns.histplot(data_median['Age'], bins=30, kde=True, color='orange')
plt.title('Distribusi Usia Setelah Imputasi dengan Median')
plt.xlabel('Usia')
plt.ylabel('Frekuensi')
plt.show()

# Distribusi Usia setelah imputasi dengan Modus
plt.figure(figsize=(7, 5))
sns.histplot(data_mode['Age'], bins=30, kde=True, color='green')
plt.title('Distribusi Usia Setelah Imputasi dengan Modus')
plt.xlabel('Usia')
plt.ylabel('Frekuensi')
plt.show()

# Menampilkan box plot untuk melihat distribusi dan outlier pada "Age"
plt.figure(figsize=(6, 5))
sns.boxplot(x=data_mean['Age'], color='lightblue')
plt.title('Box Plot untuk Usia (Age)')
plt.xlabel('Usia')
plt.show()

# Menampilkan box plot untuk melihat distribusi dan outlier pada "Age"
plt.figure(figsize=(6, 5))
sns.boxplot(x=data_mean['Age'], color='lightblue')
plt.title('Box Plot untuk Usia (Age)')
plt.xlabel('Usia')
plt.show()

# Menghitung z-score dari "Age" untuk semua data
data_mean['z_score'] = zscore(data_mean['Age'])

# Memilih beberapa kolom yang sesuai dengan tampilan di gambar
selected_columns = ['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 
                    'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked', 'z_score']

# Menentukan data yang merupakan outlier (z_score > 3 atau z_score < -3)
outliers = data_mean[abs(data_mean['z_score']) > 3]

# Menampilkan hanya outlier (maksimal 10 baris pertama jika banyak)
print(outliers[selected_columns].round(6).head(10))

# Menentukan jumlah outlier
outlier_count = outliers.shape[0]

# Menampilkan beberapa outlier
outliers = data_mean.loc[data_mean['z_score'].abs() > 3, ['Age']]

# Diasumsikan "Age" terdistribusi normal, menghitung peluang "Age" < 20
peluang_age_20 = norm.cdf(20, loc=rata_usia, scale=data_mean['Age'].std())

print(f"Jumlah outlier (z > 3) pada Age: {outlier_count}")
print("Outlier yang terdeteksi:")
print(outliers.head())
print(f"Peluang untuk Age < 20: {peluang_age_20:.4f}")