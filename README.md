# AI Budget Planner with Expense Forecasting

This project is a Streamlit web application designed to help users track their expenses and plan their budget. It offers two ways to input expense data: by uploading a CSV file or by entering data manually. The application also includes a feature for expense forecasting, leveraging AI to provide insights into future spending.

## Features

-   **Data Input:** Users can either upload a CSV file with their expense data or enter it manually through an interactive table.
-   **Data Preview:** For CSV uploads, a preview of the data is displayed.
-   **Data Validation:** The application validates the manually entered data to ensure correctness.
-   **Expense Forecasting:** (Coming Soon) AI-powered forecasting to predict future expenses.

## Requirements

The project requires the following Python libraries:

-   `streamlit`
-   `pandas`
-   `google-generativeai`
-   `python-dotenv`
-   `datetime`

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/ai-budget-planner.git
    cd ai-budget-planner
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```


    ```

## How to Run

To run the application, execute the following command in your terminal:

```bash
streamlit run main.py
```

The application will open in your default web browser.

