import streamlit as st
import pandas as pd
import joblib

# Load models and encoder
rf_model = joblib.load("random_forest_model.pkl")
lr_model = joblib.load("logistic_regression_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

st.title("Prediksi Status Mahasiswa")
st.write("Masukkan beberapa data penting untuk memprediksi status mahasiswa.")

# Sidebar model choice
model_choice = st.sidebar.selectbox("Pilih Model", ["Random Forest", "Logistic Regression"])

# Fitur penting (disederhanakan)
selected_features = {
    "Previous_qualification_grade": st.number_input("Nilai Kualifikasi Sebelumnya (Previous_qualification_grade)", 0.0, 200.0, step=0.1),
    "Admission_grade": st.number_input("Nilai Penerimaan (Admission_grade)", 0.0, 200.0, step=0.1),
    "Curricular_units_1st_sem_grade": st.number_input("IP Semester 1 (Curricular_units_1st_sem_grade)", 0.0, 200.0, step=0.1),
    "Curricular_units_2nd_sem_grade": st.number_input("IP Semester 2 (Curricular_units_2nd_sem_grade)", 0.0, 200.0, step=0.1),
    "Debtor": st.selectbox("Punya Tunggakan? (Debtor)", [0, 1]),
    "Scholarship_holder": st.selectbox("Penerima Beasiswa? (Scholarship_holder)", [0, 1]),
    "Tuition_fees_up_to_date": st.selectbox("SPP Sudah Dibayar? (Tuition_fees_up_to_date)", [0, 1]),
}

# Prediksi
if st.button("Prediksi Status"):
    # Siapkan input untuk model (lengkapi fitur yang tidak diinput manual dengan 0 atau nilai default)
    full_feature_list = [
        'Marital_status', 'Application_mode', 'Application_order', 'Course',
        'Daytime_evening_attendance', 'Previous_qualification', 'Previous_qualification_grade',
        'Nacionality', 'Mothers_qualification', 'Fathers_qualification',
        'Mothers_occupation', 'Fathers_occupation', 'Admission_grade', 'Displaced',
        'Educational_special_needs', 'Debtor', 'Tuition_fees_up_to_date', 'Gender',
        'Scholarship_holder', 'Age_at_enrollment', 'International',
        'Curricular_units_1st_sem_credited', 'Curricular_units_1st_sem_enrolled',
        'Curricular_units_1st_sem_evaluations', 'Curricular_units_1st_sem_approved',
        'Curricular_units_1st_sem_grade', 'Curricular_units_1st_sem_without_evaluations',
        'Curricular_units_2nd_sem_credited', 'Curricular_units_2nd_sem_enrolled',
        'Curricular_units_2nd_sem_evaluations', 'Curricular_units_2nd_sem_approved',
        'Curricular_units_2nd_sem_grade', 'Curricular_units_2nd_sem_without_evaluations',
        'Unemployment_rate', 'Inflation_rate', 'GDP'
    ]

    # Inisialisasi semua nilai dengan 0
    input_data = {feature: 0 for feature in full_feature_list}

    # Masukkan nilai input yang tersedia
    for key, value in selected_features.items():
        input_data[key] = value

    # Prediksi
    input_df = pd.DataFrame([input_data])
    model = rf_model if model_choice == "Random Forest" else lr_model
    prediction = model.predict(input_df)[0]
    label = label_encoder.inverse_transform([prediction])[0]

    st.success(f"Prediksi Status Mahasiswa: **{label}**")
