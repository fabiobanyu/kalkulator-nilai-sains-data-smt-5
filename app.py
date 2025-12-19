import streamlit as st

# --- KONFIGURASI HALAMAN ---
st.set_page_config(page_title="Kalkulator Nilai Sains Data ITERA", layout="centered")

def tentukan_grade(na):
    if na >= 75: return "A", 4.0, "Lulus"
    elif na >= 70: return "AB", 3.5, "Lulus"
    elif na >= 65: return "B", 3.0, "Lulus"
    elif na >= 60: return "BC", 2.5, "Lulus"
    elif na >= 50: return "C", 2.0, "Lulus"
    elif na >= 40: return "D", 1.0, "Tidak Lulus"
    else: return "E", 0.0, "Tidak Lulus"

st.title("🎓 Kalkulator Nilai Akademik Semester 5 2023 Sains Data")
st.write("Gunakan aplikasi ini untuk menghitung estimasi nilai akhir berdasarkan kontrak kuliah.")

# --- SIDEBAR UNTUK PILIH MATKUL ---
matkul = st.selectbox(
    "Pilih Mata Kuliah:",
    [
        "Analisis Multivariat", 
        "Komputasi Statistik", 
        "Data Mining", 
        "Teknologi Basis Data", 
        "Teori Optimasi", 
        "Keamanan dan Data Privasi", 
        "Kecerdasan Buatan", 
        "Analitik Bisnis", 
        "Pergudangan Data"
    ]
)

st.divider()
st.subheader(f"Input Nilai: {matkul}")

# --- LOGIKA INPUT BERDASARKAN MATKUL ---
na = 0
info_praktikum = False

if matkul == "Analisis Multivariat":
    k = st.number_input("Kuis (22%)", 0, 100)
    t = st.number_input("Tugas (12%)", 0, 100)
    p = st.number_input("Presentasi (5%)", 0, 100)
    uts = st.number_input("UTS (20%)", 0, 100)
    uas = st.number_input("UAS (25%)", 0, 100)
    l = st.number_input("Tugas Kelompok (16%)", 0, 100)
    na = (k*0.22) + (t*0.12) + (p*0.05) + (uts*0.20) + (uas*0.25) + (l*0.16)

elif matkul == "Komputasi Statistik":
    part = st.number_input("Partisipasi/Kuis (20%)", 0, 100)
    t = st.number_input("Tugas (10%)", 0, 100)
    pr = st.number_input("Praktikum (22%)", 0, 100)
    uts = st.number_input("UTS (14%)", 0, 100)
    uas = st.number_input("UAS (19%)", 0, 100)
    l = st.number_input("Tugas Kelompok (15%)", 0, 100)
    na = (part*0.20) + (t*0.10) + (pr*0.22) + (uts*0.14) + (uas*0.19) + (l*0.15)
    info_praktikum = True

elif matkul == "Data Mining":
    uts = st.number_input("UTS (25%)", 0, 100)
    uas = st.number_input("UAS (25%)", 0, 100)
    k = st.number_input("Kuis (10%)", 0, 100)
    t = st.number_input("Tugas (20%)", 0, 100)
    pr = st.number_input("Praktikum (20%)", 0, 100)
    na = (uts*0.25) + (uas*0.25) + (k*0.10) + (t*0.20) + (pr*0.20)
    info_praktikum = True

elif matkul == "Teknologi Basis Data":
    uts = st.number_input("UTS (25%)", 0, 100)
    uas = st.number_input("UAS (25%)", 0, 100)
    k = st.number_input("Kuis (20%)", 0, 100)
    t = st.number_input("Tugas (10%)", 0, 100)
    pr = st.number_input("Praktikum (20%)", 0, 100)
    na = (uts*0.25) + (uas*0.25) + (k*0.20) + (t*0.10) + (pr*0.20)
    info_praktikum = True

elif matkul == "Teori Optimasi":
    t = st.number_input("Tugas (30%)", 0, 100)
    uts = st.number_input("UTS (25%)", 0, 100)
    uas = st.number_input("UAS (25%)", 0, 100)
    p = st.number_input("Presentasi (10%)", 0, 100)
    k = st.number_input("Partisipasi/Kuis (10%)", 0, 100)
    na = (t*0.30) + (uts*0.25) + (uas*0.25) + (p*0.10) + (k*0.10)

elif matkul == "Keamanan dan Data Privasi":
    k = st.number_input("Kehadiran/Kuis (10%)", 0, 100)
    ti = st.number_input("Tugas Individu (25%)", 0, 100)
    tk = st.number_input("Tugas Kelompok (15%)", 0, 100)
    uts = st.number_input("UTS (20%)", 0, 100)
    uas = st.number_input("UAS (20%)", 0, 100)
    na = (k*0.10) + (ti*0.25) + (tk*0.15) + (uts*0.20) + (uas*0.20)

elif matkul == "Kecerdasan Buatan":
    t = st.number_input("Tugas (33%)", 0, 100)
    p = st.number_input("Unjuk Kerja/Presentasi (19%)", 0, 100)
    uts = st.number_input("UTS (17%)", 0, 100)
    uas = st.number_input("UAS (16%)", 0, 100)
    k = st.number_input("Partisipasi/Quiz (15%)", 0, 100)
    na = (t*0.33) + (p*0.19) + (uts*0.17) + (uas*0.16) + (k*0.15)

elif matkul == "Analitik Bisnis":
    t = st.number_input("Tugas (25%)", 0, 100)
    uas = st.number_input("UAS (25%)", 0, 100)
    uts = st.number_input("UTS (20%)", 0, 100)
    kp = st.number_input("Kuis/Presentasi (20%)", 0, 100)
    h = st.number_input("Kehadiran (10%)", 0, 100)
    na = (t*0.25) + (uas*0.25) + (uts*0.20) + (kp*0.20) + (h*0.10)

elif matkul == "Pergudangan Data":
    pr = st.number_input("Observasi Praktik (30%)", 0, 100)
    uas = st.number_input("UAS (22%)", 0, 100)
    uts = st.number_input("UTS (20%)", 0, 100)
    k = st.number_input("Kuis (13%)", 0, 100)
    t = st.number_input("Observasi Tugas (10%)", 0, 100)
    l = st.number_input("Tugas Kelompok (5%)", 0, 100)
    na = (pr*0.30) + (uas*0.22) + (uts*0.20) + (k*0.13) + (t*0.10) + (l*0.05)
    info_praktikum = True

# --- TOMBOL HITUNG ---
if st.button("Hitung Nilai Akhir"):
    nh, nm, status = tentukan_grade(na)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Skor Akhir", f"{na:.2f}")
    col2.metric("Grade", nh)
    col3.metric("Status", status)
    
    if info_praktikum:
        st.warning("⚠️ Ingat: Matakuliah ini mensyaratkan kehadiran Praktikum 100% untuk lulus.")
    
    if status == "Tidak Lulus":
        st.error("Status: TIDAK LULUS. Nilai minimal untuk lulus adalah C (50).")
    else:
        st.success("Selamat! Anda lulus matakuliah ini.")
