import pandas as pd
from tabulate import tabulate  # Import tabulate untuk format tabel

# Load data dari file Excel
file_path = "P-3\Data CM1.xlsx"
df = pd.read_excel(file_path, sheet_name="ID")

# Membuat tabel frekuensi untuk "Lama Belajar"
frekuensi_lama_belajar = df["Lama Belajar"].value_counts().sort_index().reset_index()
frekuensi_lama_belajar.columns = ["Lama Belajar (jam)", "Frekuensi"]
frekuensi_lama_belajar.to_csv("P-3/lama_belajar_frek.csv", index=False)


# Membuat tabel frekuensi untuk "Nilai Ujian"
frekuensi_nilai_ujian = df["Nilai Ujian"].value_counts().sort_index().reset_index()
frekuensi_nilai_ujian.columns = ["Nilai Ujian", "Frekuensi"]
frekuensi_nilai_ujian.to_csv("P-3/nilai_ujian_frek.csv", index=False)


# Menampilkan tabel dengan format tabulate
from prettytable import PrettyTable

def print_pretty_table(df, title):
    table = PrettyTable(df.columns.tolist())
    for row in df.itertuples(index=False):
        table.add_row(row)
    
    print(f"{title}\n{table}\n")

print_pretty_table(frekuensi_lama_belajar, "Tabel Frekuensi Lama Belajar:")
print_pretty_table(frekuensi_nilai_ujian, "Tabel Frekuensi Nilai Ujian:")

