import streamlit as st

st.set_page_config(page_title="Proje Yönetimi Eğitim Uygulaması", layout="wide")

st.title("📘 Proje Yönetimi Eğitim Portalı")
st.markdown("Bu platform, proje yönetiminin temel alanlarını öğrenmek isteyen öğrenciler ve profesyoneller için geliştirilmiştir.")

modules = [
    "📅 1. Proje Planlaması ve Zaman Yönetimi",
    "💰 2. Kaynak ve Bütçe Planlaması",
    "⚠️ 3. Risk Yönetimi",
    "✅ 4. Kalite Yönetimi",
    "🗣️ 5. İletişim ve Takım Yönetimi",
    "🛒 6. Tedarik ve Satın Alma Süreçleri",
    "🔍 7. Uygulama ve İzleme",
    "📦 8. Kapanış ve Değerlendirme"
]

modul = st.sidebar.selectbox("📚 Modül Seçin", modules)

if "Zaman" in modul:
    import zaman_modulu
    zaman_modulu.run()
elif "Bütçe" in modul:
    import butce_modulu
    butce_modulu.run()
# Diğer modüller bu şekilde eklenir
