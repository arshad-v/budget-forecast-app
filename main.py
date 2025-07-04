import pandas as pd
import streamlit as st
import datetime
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Configure the Gemini API
# Load API key
API_KEY = os.getenv("GEMINI_API_KEY")

# Define Gemini endpoint
GEMINI_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

# Function to call Gemini API
def get_gemini_response(input_text):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": input_text
                    }
                ]
            }
        ]
    }
    response = requests.post(GEMINI_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        return result['candidates'][0]['content']['parts'][0]['text']
    else:
        return f"API Error: {response.status_code} - {response.text}"




st.title("AI Budget Planner with Expense Forecasting ")
input_mode = st.radio("Choose input method:", ["Upload CSV", "Enter Data Manually"])

if input_mode == "Upload CSV":
    uploaded_file = st.file_uploader("📁 Upload your CSV file", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.subheader("🔍 Preview of CSV")
        st.dataframe(df)

        if st.button("Analyze Expenses"):
            st.subheader("AI Budget Analysis")
            with st.spinner("Analyzing..."):
                prompt = f"Analyze the following expense data (make sure in Indian rupees). Provide a detailed budget forecast, identify spending trends, and offer actionable suggestions for improvement. Present the analysis in a clear, structured format:\n{df.to_string()}"
                response = get_gemini_response(prompt)
                st.write(response)

else:
    st.subheader("📝 Enter Expenses (Add/Delete Rows Below)")

    # Preload empty rows
    default_data = pd.DataFrame({
        "Date": [datetime.date.today()],
        "Category": ["Groceries"],
        "Amount": [0.0]
    })

    edited_df = st.data_editor(
        default_data,
        num_rows="dynamic",
        use_container_width=True,
        key="expense_editor"
    )

    
    if st.button("Submit Expenses"):
        # Clean and validate
        try:
            st.subheader("AI Budget Analysis")
            with st.spinner("Analyzing..."):
                prompt = f"Analyze the following expense data (in Indian rupees). Provide a detailed budget forecast, identify spending trends, and offer actionable suggestions for improvement. Present the analysis in a clear, structured format:\n{edited_df.to_string()}"
                response = get_gemini_response(prompt)
                st.write(response)

        except Exception as e:
            st.error(f"❌ Error processing data: {e}")
