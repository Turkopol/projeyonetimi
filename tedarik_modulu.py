
import streamlit as st
import pandas as pd

def run():
    st.title("🛒 Tedarik ve Satın Alma Süreçleri")
    st.markdown("""
    Bu modülde proje kapsamında dış kaynak ihtiyaçlarının belirlenmesi, tedarikçi seçimi ve sözleşme yönetimi ele alınmaktadır.

    ### 📌 Konular:
    - Dış kaynak ihtiyaç analizi
    - Tedarikçi seçim kriterleri ve teklif değerlendirme
    - Satın alma sürecinin zamanlamaya etkisi
    - Sözleşme türleri ve yönetim ilkeleri

    Aşağıda örnek bir teklif değerlendirme tablosu bulunmaktadır.
    """)

    data = {
        "Tedarikçi": ["A", "B", "C"],
        "Fiyat (TL)": [10000, 8000, 9000],
        "Kalite": ["Yüksek", "Orta", "Yüksek"],
        "Teslim Süresi (gün)": [3, 5, 2],
        "Referanslar": ["İyi", "Orta", "İyi"]
    }

    df = pd.DataFrame(data)
    st.dataframe(df)

    st.markdown("👉 En uygun seçenek: **Tedarikçi C** (yüksek kalite, kısa teslim süresi)")
