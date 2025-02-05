# Analisis Dataset Produk

Proyek ini memberikan analisis terhadap data produk dalam berbagai kategori, dengan fokus pada dimensi produk, berat, dan fitur relevan lainnya.

## Ringkasan Proyek

Dataset ini berisi informasi tentang produk, termasuk kategori, panjang nama produk, panjang deskripsi produk, jumlah foto, berat, dan dimensi fisik (panjang, tinggi, lebar). Tujuan dari analisis ini adalah untuk mendapatkan wawasan terkait kategori produk dan bagaimana karakteristiknya bervariasi di berbagai dimensi.

## Fitur dalam Dataset
- **product_id**: Identifikasi unik untuk setiap produk.
- **product_category_name**: Kategori produk.
- **product_name_lenght**: Panjang nama produk (dalam karakter).
- **product_description_lenght**: Panjang deskripsi produk (dalam karakter).
- **product_photos_qty**: Jumlah foto yang terkait dengan produk.
- **product_weight_g**: Berat produk dalam gram.
- **product_length_cm**: Panjang produk dalam sentimeter.
- **product_height_cm**: Tinggi produk dalam sentimeter.
- **product_width_cm**: Lebar produk dalam sentimeter.

## Proses Pembersihan Data

Proses pembersihan data yang dilakukan meliputi:
1. **Menghapus duplikasi**: Baris duplikat dalam dataset dihapus.
2. **Menangani nilai yang hilang**: 
    - Nilai yang hilang diisi dengan median untuk kolom numerik.
    - Baris yang memiliki data kosong dihapus jika diperlukan.
3. **Rekayasa Fitur**: 
    - **total_dimension**: Fitur baru yang dibuat dengan menjumlahkan panjang, tinggi, dan lebar produk.
    - **name_to_desc_ratio**: Fitur baru yang dibuat dengan membagi panjang nama produk dengan panjang deskripsi produk untuk mendapatkan rasio nama terhadap deskripsi.

## Pertanyaan Bisnis yang Dieksplorasi

### 1. Kategori produk mana yang terkait dengan dimensi dan berat rata-rata tertinggi?
Kami mengeksplorasi nilai rata-rata untuk panjang nama produk, panjang deskripsi produk, berat, dan dimensi total per kategori produk. Wawasan diperoleh untuk mengidentifikasi kategori mana yang biasanya memiliki produk yang lebih besar dan lebih berat.

### 2. Apakah berat dan dimensi produk mempengaruhi kategori atau harga?
Kami menganalisis distribusi berat produk dan dimensi berdasarkan kategori. Visualisasi seperti boxplot digunakan untuk memahami apakah produk yang lebih berat dan lebih besar cenderung berada pada kategori tertentu. Ini dapat memberikan wawasan tentang bagaimana dimensi produk memengaruhi harga.

## Visualisasi

Proyek ini menyertakan visualisasi kunci sebagai berikut:
- Diagram batang yang menunjukkan rata-rata fitur (seperti panjang nama, berat, dan dimensi total) per kategori produk.
- Boxplot yang menggambarkan distribusi berat dan dimensi (panjang, tinggi, dan lebar) berdasarkan kategori produk.

## Kesimpulan

1. **Prediksi Produk dengan Dimensi dan Berat Lebih Besar**: Kategori produk dengan dimensi yang lebih besar (panjang, tinggi, lebar) cenderung memiliki produk yang lebih berat. Produk yang lebih besar umumnya lebih mahal karena biaya produksi dan pengiriman yang lebih tinggi.
2. **Pengaruh Dimensi dan Berat Produk terhadap Kategori**: Terdapat hubungan yang kuat antara ukuran produk (berat dan dimensi) dengan kategori produk, dengan beberapa kategori yang cenderung memiliki produk lebih besar.

## Memulai Proyek

Untuk menjalankan analisis ini:

2. Instal pustaka yang diperlukan:
    ```
    pip install -r requirements.txt
    ```
3. Jalankan skrip analisis menggunakan Streamlit:
    ```
    streamlit run analysis.py
    ```

Ini akan meluncurkan aplikasi Streamlit di mana Anda dapat melihat data yang telah dibersihkan, berinteraksi dengan visualisasi, dan mengeksplorasi hasil analisis.

## Ketergantungan
- pandas
- matplotlib
- seaborn
- streamlit

