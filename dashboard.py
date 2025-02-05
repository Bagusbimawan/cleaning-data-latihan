import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Fungsi untuk memuat data (ganti dengan metode pemuatan data yang sesuai)
df = pd.read_csv('/Users/macbookpro2019/Developer/Machine-Learning/machine-learning/data/products_dataset.csv')

# 1. Menghapus duplikasi
df.drop_duplicates(inplace=True)

# 2. Menangani Missing Values
df.fillna(df.median(numeric_only=True), inplace=True)  # Isi nilai kosong dengan median

df.dropna(inplace=True)

# Menampilkan informasi dataset setelah cleaning
st.title("Cleaning Data - Analisis Kategori Produk")

st.subheader("Jumlah Data Setelah Pembersihan")
st.write(f"Total data setelah cleaning: {df.shape[0]} baris, {df.shape[1]} kolom")

# Menampilkan jumlah missing values setelah pembersihan
st.subheader("Jumlah Missing Values Setelah Cleaning")
st.write(df.isnull().sum())

st.subheader("Data Setelah Cleaning")
st.write(df.head())

st.subheader("Setelah Data kosong dihapus")
st.write(df.isnull().sum())

# Feature Engineering
df['total_dimension'] = df['product_length_cm'] + df['product_height_cm'] + df['product_width_cm']
df['name_to_desc_ratio'] = df['product_name_lenght'] / (df['product_description_lenght'] + 1)

# Pilih hanya kolom numerik untuk agregasi
numeric_columns = df.select_dtypes(include=['float64']).columns

# Kelompokkan berdasarkan kategori dan hitung nilai rata-rata untuk setiap fitur numerik
category_stats = df.groupby('product_category_name')[numeric_columns].mean()

# Menampilkan statistik rata-rata per kategori setelah cleaning
st.subheader("Pertayaan Pertama ")
st.write("1. **Kategori produk mana yang memiliki produk lebih besar dan lebih berat?**")

# Menambahkan fitur total dimensi
df['total_dimension'] = df['product_length_cm'] + df['product_height_cm'] + df['product_width_cm']

# Menghitung rata-rata per kategori
numeric_columns = df.select_dtypes(include=['float64']).columns  # Memilih kolom numerik
category_stats = df.groupby('product_category_name')[numeric_columns].mean()


category_stats_sorted_by_weight = category_stats.sort_values(by='product_weight_g', ascending=False)
category_stats_sorted_by_dimension = category_stats.sort_values(by='total_dimension', ascending=False)

# Menampilkan kategori dengan produk berat dan dimensi terbesar
st.write("Kategori dengan Produk Berat Terbesar:")
st.write(category_stats_sorted_by_weight[['product_weight_g']].head())

st.write("Kategori dengan Produk Dimensi Terbesar:")
st.write(category_stats_sorted_by_dimension[['total_dimension']].head())

# Plot untuk visualisasi
fig, ax = plt.subplots(figsize=(10, 6))
category_stats[['product_weight_g', 'total_dimension']].plot(kind='bar', ax=ax)
plt.title('Rata-rata Berat dan Dimensi Total per Kategori')
plt.ylabel('Nilai Rata-rata')
st.pyplot(fig)


st.subheader("Pertayaan Kedua")
st.write("2. **Apakah berat dan dimensi produk memengaruhi kategori atau harga?**")
# Plot hubungan antara kategori dan berat produk
st.subheader("Distribusi Berat Produk Berdasarkan Kategori")
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='product_category_name', y='product_weight_g')
plt.xticks(rotation=90)
plt.title('Distribusi Berat Produk Berdasarkan Kategori')
st.pyplot(plt)

# Plot hubungan antara kategori dan dimensi produk (Panjang, Tinggi, Lebar)
st.subheader("Distribusi Dimensi Produk Berdasarkan Kategori")

fig, ax = plt.subplots(1, 3, figsize=(18, 6))

# Plot Panjang Produk
sns.boxplot(data=df, x='product_category_name', y='product_length_cm', ax=ax[0])
ax[0].set_title('Panjang Produk Berdasarkan Kategori')
ax[0].tick_params(axis='x', rotation=90)

# Plot Tinggi Produk
sns.boxplot(data=df, x='product_category_name', y='product_height_cm', ax=ax[1])
ax[1].set_title('Tinggi Produk Berdasarkan Kategori')
ax[1].tick_params(axis='x', rotation=90)

# Plot Lebar Produk
sns.boxplot(data=df, x='product_category_name', y='product_width_cm', ax=ax[2])
ax[2].set_title('Lebar Produk Berdasarkan Kategori')
ax[2].tick_params(axis='x', rotation=90)

plt.tight_layout()
st.pyplot(fig)

st.subheader("Kesimpulan")

st.write("1. **Kategori produk mana yang memiliki produk lebih besar dan lebih berat?**")
st.write("Berdasarkan analisis, kategori produk yang memiliki dimensi total lebih besar dan berat lebih tinggi adalah kategori dengan produk yang lebih besar dan lebih berat. Kategori produk ini berpotensi memiliki biaya produksi dan pengiriman yang lebih besar.")
st.write("2. Apakah Berat dan Dimensi Produk Mempengaruhi Kategori atau Harga?")
st.write("Dapat diasumsikan bahwa produk dengan dimensi dan berat yang lebih besar mungkin cenderung lebih mahal, meskipun ini perlu verifikasi lebih lanjut melalui analisis harga. Kategori dengan produk besar kemungkinan memiliki harga yang lebih tinggi karena biaya produksi dan pengiriman yang lebih besar.")

