
import streamlit as st
import plotly.express as px
import pandas as pd

def run():
    st.title("📅 Proje Planlaması ve Zaman Yönetimi")
    st.markdown("""
    Bu modülde proje planı oluşturma, zaman çizelgesi hazırlama, Gantt ve PERT gibi planlama araçlarını öğrenebilirsiniz.

    ### 📌 Konular:
    - Proje hedefleri ve kapsam
    - Görev listesi ve süre tahmini
    - Gantt şeması ve CPM
    - PERT tekniği

    Aşağıda örnek bir Gantt şeması görselleştirilmiştir.
    """)

    gantt_data = {
        "Görev": ["Analiz", "Kodlama", "Test", "Yayınlama"],
        "Başlangıç": ["2024-01-01", "2024-01-15", "2024-02-15", "2024-03-01"],
        "Bitiş": ["2024-01-14", "2024-02-14", "2024-02-28", "2024-03-10"]
    }

    df = pd.DataFrame(gantt_data)
    fig = px.timeline(df, x_start="Başlangıç", x_end="Bitiş", y="Görev", color="Görev")
    fig.update_yaxes(categoryorder="total ascending")

    st.plotly_chart(fig)
