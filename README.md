# 🥗 AI Nutritionist Pro

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.31.0-red)
![Gemini Vision](https://img.shields.io/badge/AI-Gemini%20Vision-green)

Aplikasi kesehatan cerdas yang mengubah caramu melacak kalori. Cukup foto makananmu, dan AI akan menganalisa kandungan nutrisinya secara instan.

**Project Portofolio: Computer Vision & Health Tech.**

## 🌟 Fitur Utama

* **📸 Snap & Analyze:** Mendukung input dari Kamera langsung (Real-time) atau Upload foto galeri.
* **📊 Nutrition Breakdown:** Menampilkan estimasi Kalori, Protein, Lemak, dan Karbohidrat dalam format tabel yang rapi.
* **🩺 AI Doctor Opinion:**
    * Memberikan **Skor Kesehatan** (A-E).
    * Memberikan komentar medis tentang dampak makanan tersebut.
    * Saran penyeimbang gizi.
* **🎨 Modern UI:** Tampilan dashboard yang responsif dengan visual feedback interaktif.

## 🛠️ Teknologi

* **Frontend:** Streamlit (Python)
* **AI Model:** Google Gemini Pro Vision (Multimodal AI)
* **Image Processing:** Pillow (PIL)

## 🚀 Cara Menjalankan (Local)

1.  **Clone Repo:**
    ```bash
    git clone [https://github.com/farhanputrabungamayang/ai-nutritionist-pro.git](https://github.com/farhanputrabungamayang/ai-nutritionist-pro.git)
    ```
2.  **Install Library:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Setup API Key:**
    Buat file `.streamlit/secrets.toml` isi dengan `GOOGLE_API_KEY`.
4.  **Run:**
    ```bash
    streamlit run app.py
    ```

---
Dibuat dengan ❤️ oleh Farhan