
import streamlit as st
import pandas as pd

def run():
    st.title("📦 Proje Kapanışı ve Değerlendirme")
    st.markdown("""
    Bu modülde projenin resmi olarak kapatılması, sonuçların değerlendirilmesi ve öğrenilen derslerin paylaşılması ele alınır.

    ### 📌 Konular:
    - Proje teslimatlarının tamamlanması ve onaylanması
    - Bütçe, zaman ve kalite açısından performans değerlendirmesi
    - Geri bildirim toplama yöntemleri (anket, mülakat, toplantı)
    - Ders çıkarma ve geleceğe yönelik öneriler

    Aşağıda örnek bir değerlendirme tablosu yer almaktadır.
    """)

    data = {
        "Kriter": ["Zaman Yönetimi", "Bütçe Kontrolü", "Kalite", "Katılımcı Memnuniyeti"],
        "Durum": ["Tam zamanında", "Bütçe %10 aşıldı", "Standartlara uygun", "Yüksek memnuniyet"],
        "Yorum": [
            "Hazırlıkta küçük gecikmeler oldu",
            "Ek mikrofon ihtiyacı doğdu",
            "Tüm ürünler başarıyla teslim edildi",
            "Yemek kalitesi geliştirilebilir"
        ]
    }

    df = pd.DataFrame(data)
    st.dataframe(df)

    st.success("📝 Ders Çıkarma: Gelecek projelerde malzeme planlaması ve alternatif bütçe opsiyonları dikkate alınmalıdır.")
