import os
import streamlit as st
import whisper
import tempfile

# Fix streamlit cache directory
os.environ["STREAMLIT_CACHE_DIR"] = "/tmp/.streamlit"
os.environ["STREAMLIT_CONFIG_DIR"] = "/tmp/.streamlit"

@st.cache_resource
def load_model():
    return whisper.load_model("base")

model = load_model()

st.title("🎙️ Whisper Speech-to-Text")
st.caption("Upload an audio file (.mp3, .wav, .m4a) to transcribe.")

uploaded_file = st.file_uploader("📁 Upload audio", type=["mp3", "wav", "m4a"])

# 🎯 Show feedback immediately after upload
if uploaded_file:
    st.success(f"✅ Uploaded: `{uploaded_file.name}`")
    st.toast("File received successfully! Ready to transcribe.", icon="📤")

    # Optional: show file details
    st.write(f"**File size:** {round(len(uploaded_file.read()) / (1024 * 1024), 2)} MB")
    uploaded_file.seek(0)  # Reset pointer after .read()

    if st.button("🚀 Submit for Transcription"):
        with st.spinner("🔄 Transcribing... please wait..."):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp:
                tmp.write(uploaded_file.read())
                tmp_path = tmp.name

            result = model.transcribe(tmp_path)
            os.remove(tmp_path)

            st.success("🎉 Transcription complete!")
            st.text_area("📝 Transcript", result["text"], height=300)

            # Choose format and download
            file_format = st.selectbox("📤 Choose download format", ["TXT", "DOCX", "PDF"])
            filename = uploaded_file.name.rsplit(".", 1)[0]

            if file_format == "TXT":
                st.download_button("Download TXT", result["text"], f"{filename}.txt", "text/plain")

            elif file_format == "DOCX":
                from docx import Document
                doc = Document()
                doc.add_paragraph(result["text"])
                doc.save(f"{filename}.docx")
                with open(f"{filename}.docx", "rb") as f:
                    st.download_button("Download DOCX", f, f"{filename}.docx", "application/vnd.openxmlformats-officedocument.wordprocessingml.document")

            elif file_format == "PDF":
                from reportlab.pdfgen import canvas
                from io import BytesIO
                buffer = BytesIO()
                pdf = canvas.Canvas(buffer)
                y = 800
                for line in result["text"].split('\n'):
                    pdf.drawString(50, y, line)
                    y -= 15
                    if y < 40:
                        pdf.showPage()
                        y = 800
                pdf.save()
                buffer.seek(0)
                st.download_button("Download PDF", buffer, f"{filename}.pdf", "application/pdf")
