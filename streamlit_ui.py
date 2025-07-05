import pandas as pd
import streamlit as st
from BudgetApp import BudgetAnalyzerApp


def run():
        budget = BudgetAnalyzerApp()
        st.title("AI Budget Planner with Expense Forecasting")
        input_mode = st.radio("Choose input method:", ["Upload CSV", "Enter Data Manually"])

        if input_mode == "Upload CSV":
            budget.handle_csv_input()
        else:
            budget.handle_manual_input()
