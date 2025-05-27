
import streamlit as st

def run():
    st.title("✅ Kalite Yönetimi")
    st.markdown("""
    Bu modülde kalite standartları, kalite kontrol araçları ve sürekli iyileştirme süreçlerini öğrenebilirsiniz.

    ### 📌 Konular:
    - Kalite tanımı ve önemi
    - ISO 9001, Six Sigma ve TQM standartları
    - Pareto analizi, kontrol grafikleri, Kaizen
    - Sürekli iyileştirme adımları

    Aşağıda örnek Pareto analizi sonuçları yer almaktadır.
    """)

    pareto_data = {
        "Sorun": ["Geç Teslimat", "Eksik Ürün", "Yanlış Etiket", "Ambalaj Hatası"],
        "Frekans": [40, 25, 20, 15]
    }

    import pandas as pd
    import plotly.express as px

    df = pd.DataFrame(pareto_data)
    fig = px.bar(df, x="Sorun", y="Frekans", title="Pareto Analizi (80/20 Kuralı)", text="Frekans")
    st.plotly_chart(fig)
