from operator import index
import streamlit as s
from deep_translator import GoogleTranslator
s.title("Translator")

languages = {

    "Auto-Detect": "auto",

    "العربية": "ar",

    "English": "en",

    "Français": "fr",

    "الإسبانية": "es",

    "الألمانية": "de",

    "الإيطالية": "it",

    "التركية": "tr",

    "اليابانية": "ja",

    "الصينية": "zh-CN",

    "الروسية": "ru",

}

col1, col2 = s.columns(2)
with col1: 
    lang1 = s.selectbox("Source language", list(languages.keys()))
with col2:
    lang2 = s.selectbox("Secondary Language", list(languages.keys()), index=1)
text = s.text_area("Write something", height=300)
if s.button("Translate", use_container_width=True):
    if text.strip() == "":
        s.warning("can you please type something?")
    else:
        try:
            translated = GoogleTranslator(source=languages[lang1], target=languages[lang2]).translate(text)
            s.text_area("result", value=translated, height=150)
        except Exception as e:
            s.error(f"couldnt translate, code: {e}")
        