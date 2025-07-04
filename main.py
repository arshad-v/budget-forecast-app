import pandas as pd
import streamlit as st
import datetime
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure the Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


def get_gemini_response(input_text):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(input_text)
    return response.text

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
