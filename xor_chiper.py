import streamlit as st

# Fungsi XOR Cipher
def xor_cipher(text, key):
    """Fungsi untuk enkripsi dan dekripsi menggunakan XOR."""
    output = ""
    for i in range(len(text)):
        output += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return output

# CSS untuk tombol
st.markdown("""
    <style>
    .encrypt-button {
        background-color: #007bff; /* Biru */
        color: white;
        border: none;
        padding: 8px 20px;
        font-size: 16px;
        border-radius: 5px;
        cursor: pointer;
    }
    .decrypt-button {
        background-color: #4c4c4c; /* Abu-abu gelap */
        color: white;
        border: none;
        padding: 8px 20px;
        font-size: 16px;
        border-radius: 5px;
        cursor: pointer;
    }
    </style>
    """, unsafe_allow_html=True)

# Judul aplikasi
st.title("XOR Cipher Encryption & Decryption")

# Input dari pengguna
input_text = st.text_input("Text:")
key = st.text_input("Key:")

# Tombol Enkripsi dan Dekripsi
encrypt = st.button("Encrypt", key="encrypt", help="Klik untuk enkripsi teks", on_click=None, kwargs=None, args=None)
decrypt = st.button("Decrypt", key="decrypt", help="Klik untuk dekripsi teks", on_click=None, kwargs=None, args=None)

# Proses enkripsi atau dekripsi
if encrypt and input_text and key:
    # Proses enkripsi dengan XOR cipher
    result = xor_cipher(input_text, key)
    st.subheader("Hasil Enkripsi:")
    st.write(result)

elif decrypt and input_text and key:
    # Proses dekripsi dengan XOR cipher
    result = xor_cipher(input_text, key)
    st.subheader("Hasil Dekripsi:")
    st.write(result)
elif not input_text or not key:
    st.warning("Mohon masukkan teks dan kunci.")
