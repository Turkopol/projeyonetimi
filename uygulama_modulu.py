
import streamlit as st
import pandas as pd

def run():
    st.title("🔍 Proje Uygulama ve İzleme")
    st.markdown("""
    Bu modülde proje uygulama süreci, performans izleme araçları ve değişiklik yönetimi konularını öğrenebilirsiniz.

    ### 📌 Konular:
    - Uygulama sürecinde kaynak kullanımı ve zaman yönetimi
    - Performans izleme: Gantt, CPM, EVM, raporlama sistemleri
    - Değişiklik türleri ve değişiklik yönetim süreci

    Aşağıda örnek bir performans izleme tablosu yer almaktadır.
    """)

    data = {
        "Görev": ["Analiz", "Kodlama", "Test", "Yayınlama"],
        "Planlanan Süre (gün)": [7, 20, 10, 5],
        "Gerçekleşen Süre (gün)": [6, 22, 9, 5],
        "Durum": ["Zamanında", "Gecikti", "Zamanında", "Zamanında"]
    }

    df = pd.DataFrame(data)
    st.dataframe(df)

    st.info("⚙️ Gecikme yaşanan 'Kodlama' aşaması için aksiyon planı hazırlanmalıdır.")
