
import streamlit as st

def run():
    st.title("🗣️ İletişim ve Takım Yönetimi")
    st.markdown("""
    Bu modülde etkili iletişim teknikleri, takım dinamikleri, liderlik ve çatışma yönetimi konularını inceleyebilirsiniz.

    ### 📌 Konular:
    - Netlik, dinleme becerisi ve geribildirim
    - Takım rolleri ve sorumlulukların dağıtılması
    - Liderlik tarzları ve özellikleri
    - Çatışma türleri ve çözüm yöntemleri

    Aşağıda örnek bir iletişim araçları tablosu yer almaktadır.
    """)

    import pandas as pd
    data = {
        "İletişim Aracı": ["E-posta", "Toplantı", "Anlık Mesajlaşma", "Raporlar"],
        "Avantaj": [
            "Resmi ve kayıtlı iletişim",
            "Yüz yüze/ekran üzerinden detaylı tartışma",
            "Hızlı yanıt alma",
            "Düzenli bilgi akışı sağlama"
        ],
        "Dezavantaj": [
            "Anında geri dönüş zordur",
            "Zaman alabilir",
            "Mesajlar kaybolabilir",
            "Hazırlama süresi gerektirir"
        ]
    }

    df = pd.DataFrame(data)
    st.dataframe(df)
