import streamlit as st
import google.generativeai as genai
from PIL import Image

# ==========================================
# 1. KONFIGURASI HALAMAN & CSS
# ==========================================
st.set_page_config(page_title="AI Nutritionist Pro", page_icon="🥗", layout="wide")

# CSS Kustom untuk tampilan mewah
st.markdown("""
<style>
    /* Mengubah font utama */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }
    
    /* Styling Tombol */
    .stButton>button {
        width: 100%;
        background: linear-gradient(to right, #11998e, #38ef7d);
        color: white;
        border: none;
        border-radius: 25px;
        font-weight: bold;
        padding: 15px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    
    /* Kotak Laporan */
    .nutrition-card {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border-left: 6px solid #11998e;
        margin-bottom: 20px;
    }
    
    /* Judul Bagian */
    .section-title {
        color: #11998e;
        font-weight: 600;
        font-size: 1.2rem;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. SETUP API KEY
# ==========================================
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
    model = genai.GenerativeModel('gemini-flash-latest')
else:
    st.error("⚠️ API Key hilang! Cek secrets.toml.")
    st.stop()

# ==========================================
# 3. FUNGSI OTAK (VISION)
# ==========================================
def analisa_makanan(image):
    # Prompt kita desain agar outputnya rapih pakai Markdown
    prompt = """
    Kamu adalah Ahli Gizi Profesional. Analisa gambar makanan ini.
    
    Format Output (Gunakan Markdown):
    
    ### 🍽️ Menu Terdeteksi
    (Sebutkan nama makanannya dengan singkat)
    
    ---
    ### 📊 Kandungan Nutrisi (Estimasi)
    | Komponen | Jumlah |
    | :--- | :--- |
    | **Kalori** | ... kkal |
    | **Protein** | ... g |
    | **Lemak** | ... g |
    | **Karbohidrat** | ... g |
    
    ---
    ### 🩺 Penilaian Dokter
    **Skor Kesehatan:** (A/B/C/D/E) - (Berikan Emoji yang sesuai, misal A 🟢, C 🟡, E 🔴)
    
    **Komentar Medis:**
    (Jelaskan singkat 2-3 kalimat tentang dampak makanan ini bagi tubuh)
    
    **💡 Saran Sehat:**
    (Satu kalimat saran konkret untuk menyeimbangkan menu ini)
    """
    
    try:
        response = model.generate_content([prompt, image])
        return response.text
    except Exception as e:
        return "Maaf, server AI sedang sibuk. Coba lagi ya!"

# ==========================================
# 4. HEADER UTAMA
# ==========================================
col_logo, col_judul = st.columns([1, 8])
with col_logo:
    st.image("https://cdn-icons-png.flaticon.com/512/2921/2921822.png", width=80) # Icon Salad
with col_judul:
    st.title("AI Nutritionist Pro")
    st.caption("Personal Diet Assistant powered by Google Gemini Vision")

st.divider()

# ==========================================
# 5. UI INPUT & PROSES
# ==========================================
col_kiri, col_kanan = st.columns([1, 1.5]) # Layout 2 Kolom

with col_kiri:
    st.markdown("### 📸 Ambil Foto Makanan")
    
    # Pilihan Input Pakai Tabs biar rapi
    tab1, tab2 = st.tabs(["📷 Kamera", "📂 Upload"])
    
    image_input = None
    
    with tab1:
        cam_img = st.camera_input("Jepret langsung")
        if cam_img: image_input = Image.open(cam_img)
            
    with tab2:
        file_img = st.file_uploader("Pilih dari Galeri", type=["jpg", "png", "jpeg"])
        if file_img: image_input = Image.open(file_img)

    # Preview Gambar
    if image_input:
        st.success("✅ Gambar berhasil dimuat!")
        st.image(image_input, use_container_width=True, caption="Foto Makananmu")
        
        # Tombol Eksekusi
        if st.button("🍴 CEK GIZINYA SEKARANG"):
            st.session_state['analisa_aktif'] = True
    else:
        st.info("👈 Silakan upload foto dulu di atas.")

with col_kanan:
    # Bagian Hasil Analisa
    if st.session_state.get('analisa_aktif') and image_input:
        
        with st.spinner("🔍 AI sedang menghitung kalori & membedah nutrisi..."):
            hasil_analisa = analisa_makanan(image_input)
            
            # Tampilkan Hasil dalam Card yang Cantik
            st.markdown("### 📝 Laporan Gizi")
            
            # Container CSS Custom
            st.markdown(f"""
            <div class="nutrition-card">
                {hasil_analisa}
            </div>
            """, unsafe_allow_html=True)
            
            # Feedback Interaktif
            if "skor kesehatan: a" in hasil_analisa.lower() or "🟢" in hasil_analisa:
                st.balloons()
                st.success("Wih, makanan sehat nih! Pertahankan Masbro! 💪")
            elif "🔴" in hasil_analisa or "skor kesehatan: e" in hasil_analisa.lower():
                st.error("Waduh! Awas kolesterol & gula. Jangan sering-sering ya! 🚨")
            else:
                st.warning("Not bad, tapi imbangi dengan air putih & olahraga ya. 🏃")
                
            # Tombol Reset
            if st.button("🔄 Cek Makanan Lain"):
                st.session_state['analisa_aktif'] = False
                st.rerun()

    elif not image_input:
        # Placeholder kalau belum ada gambar (biar kanan gak kosong)
        st.markdown("""
        <div style="text-align: center; padding: 50px; color: #888;">
            <h3>👋 Halo Masbro!</h3>
            <p>Saya siap menghitung kalori makananmu.</p>
            <p>Upload foto di sebelah kiri untuk memulai.</p>
            <br>
            <img src="https://cdn-icons-png.flaticon.com/512/706/706164.png" width="150" style="opacity: 0.5;">
        </div>
        """, unsafe_allow_html=True)