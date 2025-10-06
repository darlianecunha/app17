import io
import time
import streamlit as st
from gtts import gTTS

st.set_page_config(page_title="TTS Multilíngue", page_icon="🎙️", layout="centered")

st.title("🎙️ Gerador de Áudio (gTTS)")
st.caption("Português 🇧🇷 • Inglês 🇬🇧 • Holandês 🇳🇱  |  Baixe o MP3 gerado na hora")

lang_map = {
    "Português (Brasil) 🇧🇷": ("pt", "com.br"),
    "Inglês (britânico) 🇬🇧": ("en", "co.uk"),
    "Holandês 🇳🇱": ("nl", "nl"),
}

col1, col2 = st.columns([3,1])
with col1:
    text = st.text_area(
        "Digite ou cole o texto",
        height=220,
        placeholder="Olá! Este é um teste de geração de áudio..."
    )
with col2:
    idioma = st.selectbox("Idioma", list(lang_map.keys()), index=0)

nome_arquivo = st.text_input("Nome do arquivo (sem .mp3)", value="audio_teste")
gerar = st.button("Gerar MP3")

if gerar:
    if not text.strip():
        st.warning("Digite algum texto para gerar o áudio.")
    else:
        lang, tld = lang_map[idioma]
        st.info(f"Gerando áudio em {idioma}…")
        # gTTS precisa de internet (ok no Streamlit Cloud)
        t0 = time.time()
        tts = gTTS(text=text.strip(), lang=lang, tld=tld)
        buf = io.BytesIO()
        tts.write_to_fp(buf)
        buf.seek(0)
        dur = time.time() - t0
        st.success(f"Pronto! (≈{dur:.1f}s)")

        st.audio(buf, format="audio/mp3")
        st.download_button(
            "⬇️ Baixar MP3",
            data=buf,
            file_name=(nome_arquivo.strip() or "audio") + ".mp3",
            mime="audio/mpeg",
        )

st.markdown("---")
st.caption("Criado por Darliane Cunha.")
