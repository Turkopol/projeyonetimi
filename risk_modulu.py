
import streamlit as st

def run():
    st.title("⚠️ Risk Yönetimi")
    st.markdown("""
    Bu modülde proje risklerini tanımlama, analiz etme ve azaltma stratejilerini ele alıyoruz.

    ### 📌 Konular:
    - Teknik, finansal, çevresel ve insan kaynaklı riskler
    - Risk tanımlama yöntemleri: Beyin fırtınası, SWOT, Delphi
    - Risk analizi: Kalitatif ve kantitatif analiz
    - Risk azaltma stratejileri: Kaçınma, azaltma, transfer, kabul
    - Risk yönetim planı oluşturma

    Aşağıda örnek bir risk analizi tablosu yer almaktadır.
    """)

    risk_table = {
        "Risk": ["Hava koşulları", "Bütçe aşımı", "Ekip üyesi ayrılması"],
        "Olasılık": ["Yüksek", "Orta", "Düşük"],
        "Etkisi": ["Yüksek", "Yüksek", "Orta"],
        "Azaltma Stratejisi": [
            "Alternatif kapalı mekan planla",
            "Acil durum fonu ayır",
            "Yedek görev dağılımı yap"
        ]
    }

    import pandas as pd
    df = pd.DataFrame(risk_table)
    st.dataframe(df)
