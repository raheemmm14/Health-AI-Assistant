import streamlit as st
import google.generativeai as genai
import os
from PIL import Image
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Page
st.set_page_config(
    page_title="Health AI Assistant",
    page_icon="️🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling
st.markdown("""
<style>
    .main {
        background-color: #0f1116;
        color: #e0e0e0;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        height: 3em;
        background-color: #007bff;
        color: white;
        font-weight: bold;
    }
    .stTextInput>div>div>input {
        background-color: #1a1c23;
        color: white;
    }
    .stTextArea>div>div>textarea {
        background-color: #1a1c23;
        color: white;
    }
    .medical-card {
        background-color: #1e2129;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #007bff;
        margin-bottom: 20px;
    }
    .disclaimer {
        font-size: 0.8em;
        color: #ff4b4b;
        background-color: #261b1b;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ff4b4b;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar for Setup
with st.sidebar:
    st.title("️🩺 Health AI Setup")
    api_key = st.text_input("Enter Google Gemini API Key", type="password", value="AIzaSyCw9WrRagzSX0Hbb-1Nt7UcEmOOoshwdXY")
    st.info("Get your API key from [Google AI Studio](https://aistudio.google.com/app/apikey)")
    
    st.divider()
    st.subheader("Capabilities")
    st.write("✅ Report Analysis")
    st.write("✅ Medicine Suggestions")
    st.write("✅ Surgery Risk Assessment")
    st.write("✅ Health Solutions")

# Title and Disclaimer
st.title("⚕️ Health AI Assistant")
st.markdown("""
### Your AI companion for medical report analysis and health guidance.
*Upload your report or describe your symptoms below to get started.*
""")

st.markdown("""
<div class="disclaimer">
    <strong>⚠️ MEDICAL DISCLAIMER:</strong> This AI assistant is for informational purposes only. 
    It is NOT a substitute for professional medical advice, diagnosis, or treatment. 
    Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition. 
    Never disregard professional medical advice or delay in seeking it because of something you have read here.
</div>
""", unsafe_allow_html=True)

st.divider()

# Input Options
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📝 Describe Symptoms")
    user_input = st.text_area("How are you feeling?", placeholder="e.g., I have a persistent cough and high fever for 3 days...", height=200)

with col2:
    st.subheader("📂 Upload Health Reports")
    uploaded_file = st.file_uploader("Upload Image or Text report (PDF/JPG/PNG)", type=["pdf", "jpg", "png", "txt"])
    if uploaded_file:
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")

# Analysis Logic
if st.button("Analyze Health Status"):
    if not api_key:
        st.error("Please provide a Gemini API Key in the sidebar to proceed.")
    elif not user_input and not uploaded_file:
        st.warning("Please provide either symptoms or a health report for analysis.")
    else:
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel('gemini-2.5-flash')
            
            # System Prompt
            system_prompt = """
            You are a highly capable Health AI Assistant. Your goal is to analyze user-provided symptoms and medical reports 
            to provide helpful solutions, suggest general medications/tablets, and assess if surgery might be required.

            CONSTRAINTS:
            1. ALWAYS start with a standard medical disclaimer.
            2. Be professional, empathetic, and clear.
            3. If reports are provided, prioritize finding abnormal values.
            4. Provide medicine suggestions ONLY for common symptoms and always advise consulting a pharmacist/doctor.
            5. For surgery assessments, use phrases like "Based on clinical patterns, this might require surgical consultation..."
            6. Structure your output clearly with headers: [Solution/Diagnosis Overview], [Suggested Medications], [Surgery Assessment], [Lifestyle Changes].
            """

            prompt_parts = [system_prompt]
            
            if user_input:
                prompt_parts.append(f"User Symptoms: {user_input}")
            
            if uploaded_file:
                # Basic handling for text, image or pdf (Gemini 1.5 handles images and PDFs)
                if uploaded_file.type in ["image/jpeg", "image/png"]:
                    img = Image.open(uploaded_file)
                    prompt_parts.append(img)
                    prompt_parts.append("Analyze the attached medical report image.")
                elif uploaded_file.type == "application/pdf":
                    prompt_parts.append(
                        {"mime_type": "application/pdf", "data": uploaded_file.getvalue()}
                    )
                    prompt_parts.append("Analyze the attached medical report PDF.")
                else:
                    text_content = uploaded_file.read().decode("utf-8")
                    prompt_parts.append(f"Medical Report Text: {text_content}")

            with st.spinner("Analyzing your health data..."):
                response = model.generate_content(prompt_parts)
                
                st.markdown("---")
                st.subheader("🔬 AI Health Analysis")
                
                # Render response in a styled card
                st.markdown(f"""
                <div class="medical-card">
                    {response.text}
                </div>
                """, unsafe_allow_html=True)
                
                st.success("Analysis complete. Please consult a doctor for verification.")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

# Footer
st.divider()
st.caption("Powered by Google Gemini | Designed for Sayyed Raheem")
