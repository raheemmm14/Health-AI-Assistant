# AI Health Assistant 🩺

An intelligent, interactive web application built with Python and Streamlit that leverages the power of Google's advanced Gemini AI. Designed to act as a preliminary health companion, this application allows users to analyze their symptoms and medical reports to gain structured health insights.

---

## 🌟 Features

- **Symptom Analysis:** Describe your symptoms in natural language, and the AI will evaluate your current health status and suggest potential underlying causes.
- **Medical Report Uploads:** Securely upload medical documents, laboratory reports, and prescription images (supporting PDF, JPG, and PNG formats).
- **Medication Suggestions:** Receive general, over-the-counter medication recommendations for common, non-critical ailments.
- **Surgery Risk Assessment:** Identifies clinical patterns or abnormal metrics in uploaded reports that might indicate the need for a professional surgical consultation.
- **Lifestyle Advice:** Offers actionable lifestyle modification advice customized to your scenario.
- **Modern UI:** Designed with a sleek, dark-mode styling for an optimal user experience.

---

## ⚠️ Medical Disclaimer

**IMPORTANT:** This AI Health Assistant is designed exclusively as an informational tool and is **NOT** a formal diagnostic medical device. 

The AI's insights should never replace professional medical diagnosis, targeted treatment, or the expert opinion of a certified healthcare provider. Always consult with a doctor or qualified health provider regarding any medical condition.

---

## 🚀 Tech Stack

- **Python 3.x**
- **Streamlit:** For the interactive web interface.
- **Google Generative AI (Gemini 2.5 Flash):** For natural language processing and image/document analysis.
- **Pillow (PIL):** For image processing.
- **python-dotenv:** For environment variable management.

---

## 🛠️ Installation & Setup

Follow these steps to run the application locally on your machine.

### 1. Prerequisites
Ensure you have Python installed on your system. You will also need a **Google Gemini API Key**. You can get one for free from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 2. Required Libraries
Install the necessary Python dependencies using `pip`:

```bash
pip install streamlit google-generativeai python-dotenv pillow
```

### 3. Running the Application
Navigate to the directory containing your project files in your terminal, and start the Streamlit server:

```bash
streamlit run streamlit_app.py
```

### 4. Using the App
1. The app will open in your default web browser (usually at `http://localhost:8501`).
2. Your API key is pre-configured in the code (or you can enter it in the sidebar).
3. Type your symptoms into the text area or upload a medical report.
4. Click **"Analyze Health Status"** and read the generated report!

---

## 👨‍💻 Author

Designed & Built by **Sayyed Raheem**.
