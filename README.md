# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Jaya Jaya Institut

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout.

Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
Banyak siswa yang tidak menyelesaikan pendidikannya alias dropout, Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan.

### Cakupan Proyek
Adapun Cakupan Proyek dari proyek ini adalah sebagai berikut:

✅ 1. Ringkasan Angka Utama (Scorecard/KPI Cards)

Tujuan: Memberikan gambaran cepat kondisi umum siswa.
Metode: Menggunakan komponen Scorecard.
Judul dan Isi:
-  Total Mahasiswa – Jumlah seluruh siswa dalam data.
-  Jumlah Graduate – Jumlah siswa yang telah lulus.
-  Jumlah Dropout – Jumlah siswa yang mengalami putus studi.
-  Jumlah Enrolled – Jumlah siswa yang masih aktif.

✅ 2. Pie Chart: Jumlah Mahasiswa Berdasarkan Status

Tujuan: Menunjukkan persentase sebaran siswa berdasarkan status pendidikan.
- Judul: "Jumlah Mahasiswa Berdasarkan Status"
- Dimensi: Status
- Metrik: Jumlah siswa (Record Count)

✅ 3. Bar Chart: Jumlah Siswa Berdasarkan Penerima Beasiswa dan Status

Tujuan: Menganalisis apakah penerimaan beasiswa berpengaruh terhadap kelulusan/dropout.
- Judul: "Jumlah Siswa Berdasarkan Status Penerima Beasiswa"
- Dimensi: scholarship_holder
- Metrik: Jumlah siswa (Record Count)
- Breakdown: Status (Graduate, Dropout, Enrolled)

✅ 4. Bar Chart: Jumlah Siswa Berdasarkan Gender dan Status

Tujuan: Mengamati hubungan antara gender dengan kemungkinan dropout.
- Judul: "Jumlah Siswa Berdasarkan Gender dan Status"
- Dimensi: gender
- Metrik: Record Count
- Breakdown: Status

✅ 5. Bar Chart: Jumlah Siswa Berdasarkan Program Studi (Course) dan Status

Tujuan: Mengidentifikasi program studi dengan tingkat dropout tertinggi.
- Judul: "Jumlah Siswa Berdasarkan Program Studi (Course) dan Status"
- Dimensi: Course
- Metrik: Record Count
- Breakdown: Status

✅ 6. Tabel Detail Siswa

Tujuan: Menyediakan informasi lengkap untuk keperluan pemantauan individual.
- Judul: "Detail Data Mahasiswa"
- Kolom yang Ditampilkan:
Gender, Usia Saat Mendaftar, Course, Nilai Rata-rata Semester (1 dan 2), Memiliki Tunggakan Pembayaran, Penerima Beasiswa,Tuition Paid dan Status.

✅ 7. Membangun Model Machine Learning
Model ini digunakan untuk memprediksi status akhir mahasiswa (Graduate, Dropout, Enrolled) berdasarkan fitur-fitur input yang tersedia.

🔧 Model yang Digunakan:
Logistic Regression (Multiclass)
- Model baseline yang simpel dan mudah diinterpretasi.
- Cocok untuk melihat pengaruh linear antar fitur.

Random Forest Classifier
- Model yang lebih kompleks dan menangani non-linearitas.
- Mampu menangani fitur penting secara otomatis dan lebih tahan terhadap overfitting.



### Persiapan

Sumber data: [Jaya-jaya Institute](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv)

Setup environment:
```
conda create --name verzha_new python=3.12
conda activate verzha_new
pip install -r requirements.txt
```

## Business Dashboard
Dashboard **STUDENTS PERFORMANCE** ini adalah sebuah visualisasi interaktif yang digunakan untuk memantau performa dan status akademik mahasiswa dalam suatu institusi pendidikan. Dashboard ini terdiri dari berbagai elemen visual dan tabel data yang memberikan wawasan menyeluruh terhadap jumlah mahasiswa, status akademik mereka, serta kaitannya dengan variabel lain seperti gender, program studi, dan status beasiswa.

Berikut adalah penjelasan detail tiap elemen dalam dashboard tersebut:

🔹 1. Filtering

Status dan Gender: Digunakan untuk memfilter data berdasarkan status mahasiswa (Graduate, Dropout, Enrolled) dan jenis kelamin. Ini memungkinkan pengguna untuk memfokuskan analisis hanya pada subset data tertentu.

🔹 2. Ringkasan Statistik (Score Card)
Terletak di bagian atas kanan:
- Total Mahasiswa: 4,424
- Jumlah Graduate: 2,209
- Jumlah Dropout: 1,421
- Jumlah Enrolled: 794

🔹 3. Pie Chart: 

Jumlah Mahasiswa Berdasarkan Status
Memberikan persentase dari total mahasiswa berdasarkan status:
- Graduate: 49.9%
- Dropout: 32.1%
- Enrolled: 17.9%

🔹 4. Bar Chart: Status berdasarkan Penerima Beasiswa
Judul: Jumlah Siswa Berdasarkan Status Penerima Beasiswa

Dikelompokkan berdasarkan apakah mahasiswa menerima beasiswa (1) atau tidak (0).

Warna:

- Biru = Graduate
- Pink = Dropout
- Merah muda = Enrolled

Note: Menunjukkan bahwa mahasiswa penerima beasiswa cenderung lebih banyak yang lulus dibandingkan dengan yang tidak menerima.

🔹5. Bar Chart: Jumlah Siswa Berdasarkan Program Studi dan Status
- Sumbu X: Kode Program Studi (misalnya 9500, 9147, dll.)
- Sumbu Y: Jumlah Mahasiswa
- Dikelompokkan berdasarkan status (Graduate, Dropout, Enrolled)

🔹 6. Bar Chart: Record Count by Gender and Status
- Sumbu X: Gender (0 = laki-laki, 1 = perempuan — asumsi dari data tabel)
- Warna menunjukkan status mahasiswa

Note: Menunjukkan distribusi status berdasarkan jenis kelamin. Terlihat bahwa mahasiswa laki-laki (gender 0) memiliki jumlah yang lebih tinggi, terutama dalam kategori graduate.


🔹 7. Tabel Data Mahasiswa

Menampilkan data mentah dengan kolom seperti:
- Gender
- Usia Saat Mendaftar
- Course (Program Studi)
- Nilai Rata-rata Semester
- Penerima Beasiswa
- Tuition Fee
- Status
- Record Count

Note: Tabel ini membantu pengguna melakukan drill-down atau investigasi lebih detail terhadap individu mahasiswa.


**Insight Utama dari Dashboard Ini:**
- Sebagian besar mahasiswa telah lulus (49.9%), namun angka dropout juga cukup tinggi (32.1%), yang perlu jadi perhatian institusi.
- Mahasiswa penerima beasiswa memiliki tingkat kelulusan yang lebih tinggi, menunjukkan efektivitas beasiswa dalam mendukung kelulusan.
- Gender tampaknya memengaruhi status mahasiswa, dengan laki-laki memiliki lebih banyak kelulusan namun juga dropout yang tinggi.
- Beberapa program studi memiliki jumlah dropout yang cukup signifikan, bisa menjadi titik fokus evaluasi kualitas pengajaran atau kurikulum.

![alt text](<Screenshot 2025-05-28 154601.png>)

Link Dashboard: [Students Performance](https://lookerstudio.google.com/reporting/33502c4b-3f10-4669-90fa-0be5acf98d0d)


## Menjalankan Sistem Machine Learning
Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```

```

## Conclusion
Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- action item 1
- action item 2
