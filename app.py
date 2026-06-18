import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
from langdetect import detect
import tempfile
import os

st.markdown("""
<style>
div[data-testid="stButton"] > button {
    background: linear-gradient(90deg, #2563eb, #3b82f6);
    color: white;
    border: none;
    border-radius: 14px;
    padding: 12px;
    font-weight: 600;
    transition: 0.3s;
}

div[data-testid="stButton"] > button:hover {
    transform: translateY(-2px);
    box-shadow: 0px 6px 20px rgba(59,130,246,0.35);
}
</style>
""", unsafe_allow_html=True)
# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌐",
    layout="centered"
)

# ---------------- CSS STYLING ---------------- #
st.markdown("""
<div style='text-align:center;padding:20px;'>
<h1 style='
font-size:50px;
background: linear-gradient(
90deg,
#60A5FA,
#818CF8,
#C084FC
);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
font-weight:800;'>
Language Translation Tool
</h1>

<p style='color:#9CA3AF;font-size:18px;'>
Translate text between 50+ languages instantly
</p>

</div>
""", unsafe_allow_html=True)



st.markdown("""
<style>
::-webkit-scrollbar {
    width: 10px;
}
::-webkit-scrollbar-track {
    background: #0B0F19;
}
::-webkit-scrollbar-thumb {
    background: #374151;
    border-radius: 10px;
}
::-webkit-scrollbar-thumb:hover {
    background: #60A5FA;
}
[data-testid="metric-container"],
.stTextArea,
.stSelectbox {
    background: rgba(31, 41, 55, 0.55);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 18px;
    padding: 10px;
}
[data-testid="metric-container"] {
    background: rgba(255,255,255,0.04);
    border-radius: 18px;
    padding: 20px;
    box-shadow: 0px 8px 30px rgba(0,0,0,0.35);
}
.stButton > button {
    border-radius: 14px;
    background: #2563EB;
    color: white;
    border: none;
    transition: all 0.3s ease;
    height: 3em;
}
.stButton > button:hover {
    transform: translateY(-3px);
    box-shadow: 0 10px 25px rgba(37,99,235,0.4);
}
.stDownloadButton > button {
    border-radius: 12px;
}
textarea {
    border-radius: 12px !important;
}
.glass {
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 25px;
}
.metric-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.05);
    border-radius: 20px;
    padding: 20px;
}
.stApp {
    background: radial-gradient(circle at 0% 0%, rgba(59,130,246,0.25), transparent 35%),
                radial-gradient(circle at 100% 0%, rgba(168,85,247,0.20), transparent 35%),
                radial-gradient(circle at 50% 100%, rgba(14,165,233,0.15), transparent 40%),
                #050816;
    color: white;
}
</style>
""", unsafe_allow_html=True)




# ---------------- TEXT INPUT ---------------- #

text = st.text_area(
    "Enter Text",
    key="input_text"
)

if text:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown(f"""
            <div class='metric-card'>
            <h4>Characters</h4>
            <h2>{len(text)}</h2>
            </div>
            """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
            <div class='metric-card'>
            <h4>Words</h4>
            <h2>{len(text.split())}</h2>
            </div>
            """, unsafe_allow_html=True)




# ---------------- LANGUAGES ---------------- #

language_codes = {
    "Arabic": "ar",
    "Bengali": "bn",
    "Bulgarian": "bg",
    "Catalan": "ca",
    "Chinese (Simplified)": "zh-CN",
    "Chinese (Traditional)": "zh-TW",
    "Croatian": "hr",
    "Czech": "cs",
    "Danish": "da",
    "Dutch": "nl",
    "English": "en",
    "Estonian": "et",
    "Filipino": "tl",
    "Finnish": "fi",
    "French": "fr",
    "German": "de",
    "Greek": "el",
    "Gujarati": "gu",
    "Hebrew": "iw",
    "Hindi": "hi",
    "Hungarian": "hu",
    "Icelandic": "is",
    "Indonesian": "id",
    "Italian": "it",
    "Japanese": "ja",
    "Kannada": "kn",
    "Korean": "ko",
    "Latvian": "lv",
    "Lithuanian": "lt",
    "Malay": "ms",
    "Malayalam": "ml",
    "Marathi": "mr",
    "Nepali": "ne",
    "Norwegian": "no",
    "Persian": "fa",
    "Polish": "pl",
    "Portuguese": "pt",
    "Punjabi": "pa",
    "Romanian": "ro",
    "Russian": "ru",
    "Serbian": "sr",
    "Slovak": "sk",
    "Slovenian": "sl",
    "Spanish": "es",
    "Swahili": "sw",
    "Swedish": "sv",
    "Tamil": "ta",
    "Telugu": "te",
    "Thai": "th",
    "Turkish": "tr",
    "Ukrainian": "uk",
    "Urdu": "ur",
    "Vietnamese": "vi"
}
languages = sorted(language_codes.keys())

# ---------------- SESSION STATE ---------------- #

if "source_lang" not in st.session_state:
    st.session_state.source_lang = "Auto Detect"

if "target_lang" not in st.session_state:
    st.session_state.target_lang = "English"

if "history" not in st.session_state:
    st.session_state.history = []

# ---------------- LANGUAGE SELECTORS ---------------- #

col1, col2, col3 = st.columns([4, 1, 4])

with col1:
    source_lang = st.selectbox(
        "Source Language",
        ["Auto Detect"] + list(language_codes.keys()),
        key="source_lang"
    )

with col2:
    st.write("")
    st.write("")

    if st.button("⇄", use_container_width=True):

        if st.session_state.source_lang != "Auto Detect":

            (
                st.session_state.source_lang,
                st.session_state.target_lang
            ) = (
                st.session_state.target_lang,
                st.session_state.source_lang
            )

            st.rerun()

with col3:
    target_lang = st.selectbox(
        "Target Language",
        list(language_codes.keys()),
        key="target_lang"
    )


# ---------------- TRANSLATE BUTTON ---------------- #
btn1, btn2 = st.columns(2)

with btn1:
    translate_btn = st.button(
        "Translate",
        use_container_width=True
    )

def clear_text():
    st.session_state.input_text = ""

with btn2:
    clear_btn = st.button(
        "Clear",
        on_click=clear_text,
        use_container_width=True
    )

if translate_btn:
    if text == "":
        st.error("Please enter some text.")

    elif source_lang == target_lang:
        st.warning("Please select different languages.")

    else:

        if source_lang == "Auto Detect":
            source_code = "auto"
        else:
            source_code = language_codes[source_lang]

        
        target_code = language_codes[target_lang]

        
        translator = GoogleTranslator(
            source=source_code,
            target=target_code
        )

        result = translator.translate(text)

        st.markdown("""
                <hr style="
                border:none;
                height:2px;
                background:linear-gradient(90deg, transparent, #60A5FA, #A855F7, transparent);
                ">
                """, unsafe_allow_html=True)

        st.markdown(f"""
        <div style="
        background: linear-gradient(135deg, rgba(37,99,235,0.20), rgba(29,78,216,0.12));
        border-radius: 20px;
        padding: 22px;
        backdrop-filter: blur(20px);
        font-size: 22px;
        color: white;">
        <strong>Translation: </strong>
        {result}
        </div>
        """, unsafe_allow_html=True)

        st.download_button(
            label="⬇ Download Translation",
            data=result,
            file_name="translation.txt",
            mime="text/plain"
        )
        st.session_state.history.insert(
            0,
            {
                "source": source_lang,
                "target": target_lang,
                "original": text,
                "translation": result
            }
        )
        st.session_state.history = st.session_state.history[:5]

        
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            temp_audio_path = temp_audio.name
        
        tts = gTTS(result)
        tts.save(temp_audio_path)
        
        with open(temp_audio_path, "rb") as audio_file:
            st.download_button(
                label="⬇ Download Audio",
                data=audio_file,
                file_name="translation.mp3",
                mime="audio/mp3"
            )
        
        st.audio(temp_audio_path)
        
      
        try:
            os.unlink(temp_audio_path)
        except:
            pass

        reverse_language_codes = {
            value: key
            for key, value in language_codes.items()
        }
        
        if source_lang == "Auto Detect" and len(text.split()) >= 3:
            detected_code = detect(text)
            detected_name = reverse_language_codes.get(detected_code, "Unknown")
            if detected_name != "Unknown":
                st.info(f"Detected Language: {detected_name}")
            st.caption("Language detection may be inaccurate for short text.")
        

if st.session_state.history:

    for item in st.session_state.history:

        with st.expander(
            f"{item['source']} → {item['target']}"
        ):

            st.write(
                f"Original: {item['original']}"
            )

            st.write(
                f"Translation: {item['translation']}"
            )

else:
    st.info("No translations yet.")

if st.button("🗑 Clear History"):
    st.session_state.history = []
    st.rerun()


# ---------------- FOOTER ---------------- #

st.markdown("""
<hr>
<div style='text-align:center;
            color:gray;
            padding:20px;
            font-size:16px;'>
Built by Aditya Batri using
Python • Streamlit • Deep Translator
</div>
""", unsafe_allow_html=True)





