import streamlit as st 
import base64

# Konversi karakter ke integer berdasarkan urutan ASCII
def text_to_int(text):
    return [ord(char) for char in text]

# Konversi integer kembali ke karakter teks
def int_to_text(integers):
    return ''.join(chr(i) for i in integers)

# Fungsi enkripsi menggunakan (n, e)
def encrypt_rsa(plaintext, n, e):
    plaintext_int = text_to_int(plaintext)
    encrypted_int = [(char ** e) % n for char in plaintext_int]
    # Gabungkan hasil enkripsi sebagai string dan ubah ke bytes untuk Base64
    encrypted_str = ','.join(map(str, encrypted_int))
    encrypted_base64 = base64.b64encode(encrypted_str.encode()).decode('utf-8')
    return encrypted_base64

# Fungsi dekripsi menggunakan (n, d)
def decrypt_rsa(encrypted_base64, n, d):
    # Decode dari Base64 ke string, lalu pisahkan menjadi list angka
    encrypted_str = base64.b64decode(encrypted_base64).decode('utf-8')
    encrypted_int = list(map(int, encrypted_str.split(',')))
    decrypted_int = [(char ** d) % n for char in encrypted_int]
    return int_to_text(decrypted_int)

# Nilai-nilai RSA yang diberikan
a = 109
b = 127
n = a * b  # 13843
phi_n = (a - 1) * (b - 1)  # 13608
e = 65537
d = 4259

# Tampilan aplikasi
st.title("Enkripsi dan Dekripsi RSA dengan Streamlit")

st.write("""
Aplikasi ini menggunakan algoritma RSA untuk mengenkripsi dan mendekripsi teks.
Anda bisa memasukkan teks untuk dienkripsi atau teks terenkripsi untuk didekripsi secara langsung.
""")

# Input untuk Enkripsi
st.header("Enkripsi")
plaintext = st.text_input("Masukkan teks untuk dienkripsi:")
if plaintext:
    # Enkripsi plaintext
    encrypted_message = encrypt_rsa(plaintext, n, e)
    st.write("Hasil Enkripsi (Base64):", encrypted_message)

# Input untuk Dekripsi
st.header("Dekripsi")
encrypted_base64 = st.text_input("Masukkan teks terenkripsi dalam Base64:")
if encrypted_base64:
    try:
        # Dekripsi ciphertext
        decrypted_message = decrypt_rsa(encrypted_base64, n, d)
        st.write("Hasil Dekripsi:", decrypted_message)
    except Exception as e:
        st.error("Gagal mendekripsi teks. Pastikan teks terenkripsi benar dan dalam format Base64.")
