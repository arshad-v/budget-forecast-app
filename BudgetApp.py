import pandas as pd
import streamlit as st
import datetime
from gemini_config import GeminiAPI




class BudgetAnalyzerApp:
    def __init__(self):
        self.gemini = GeminiAPI()

    
    def handle_csv_input(self):
        uploaded_file = st.file_uploader("📁 Upload your CSV file", type=["csv"])
        
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)

            st.subheader("🔍 Preview of CSV")
            st.dataframe(df)

            if st.button("Analyze Expenses"):
                st.subheader("AI Budget Analysis")
                with st.spinner("Analyzing..."):
                    prompt = f"Analyze the following expense data (make sure in Indian rupees). Provide a detailed budget forecast, identify spending trends, and offer actionable suggestions for improvement. Present the analysis in a clear, structured format:\n{df.to_string()}"
                    response = self.gemini.generate_response(prompt)
                    st.write(response)

    def handle_manual_input(self):
        st.subheader("📝 Enter Expenses (Add/Delete Rows Below)")

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
            try:
                st.subheader("AI Budget Analysis")
                with st.spinner("Analyzing..."):
                    prompt = f"Analyze the following expense data (in Indian rupees). Provide a detailed budget forecast, identify spending trends, and offer actionable suggestions for improvement. Present the analysis in a clear, structured format:\n{edited_df.to_string()}"
                    response = self.gemini.generate_response(prompt)
                    st.write(response)
            except Exception as e:
                st.error(f"❌ Error processing data: {e}")

                