import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Data 
data = np.array([
    21, 20, 31, 24, 15, 21, 24, 18, 33, 8,
    26, 17, 27, 29, 24, 14, 29, 41, 15, 11,
    13, 28, 22, 16, 12, 15, 11, 16, 18, 17,
    29, 16, 24, 21, 19, 7, 16, 12, 45, 24,
    21, 12, 10, 13, 20, 35, 32, 22, 12, 10
])

# Menentukan jumlah kelas dengan aturan Sturges
k = 1 + 3.322 * np.log10(len(data))
k = int(np.ceil(k))

# Membuat tabel frekuensi
freq_table = pd.cut(data, bins=k, right=False).value_counts().sort_index()

# Membuat tabel frekuensi sebagai DataFrame
freq_table_df = pd.DataFrame({'Interval': freq_table.index.astype(str), 'Frekuensi': freq_table.values})

# Menampilkan tabel frekuensi
freq_table_df

# Membuat histogram
plt.bar(freq_table_df['Interval'], freq_table_df['Frekuensi'])
plt.xlabel('Interval')
plt.ylabel('Frekuensi')
plt.show()