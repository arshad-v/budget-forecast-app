import pandas as pd
import streamlit as st
import datetime

st.title("AI Budget Planner with Expense Forecasting ")


# Choose input method
input_mode = st.radio("Choose input method:", ["Upload CSV", "Enter Data Manually"])

if input_mode == "Upload CSV":
    uploaded_file = st.file_uploader("📁 Upload your CSV file", type=["csv"])
    
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        st.subheader("🔍 Preview of CSV")
        st.dataframe(df)



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

    # Submit button
    if st.button("Submit Expenses"):
        # Clean and validate
        try:
            edited_df["Date"] = pd.to_datetime(edited_df["Date"])
            edited_df["Amount"] = edited_df["Amount"].astype(float)
            

            st.success("✅ Entries Submitted Successfully!")
            st.dataframe(edited_df)
            

        except Exception as e:
            st.error(f"❌ Error processing data: {e}")