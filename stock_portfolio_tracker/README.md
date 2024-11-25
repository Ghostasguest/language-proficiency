# Stock Dashboard App

This Stock Dashboard App is a Streamlit-based application that allows users to:
1. Track stock price movements over time.
2. Manage a stock portfolio.
3. View top 10 news articles and their sentiment analysis for a selected stock.

---

## Features

### 1. Pricing Data
- Users can select a stock ticker and a date range.
- Displays a line chart of the adjusted closing price.
- Provides annual return and annual standard deviation.

### 2. Stock Portfolio Tracker
- Add stocks to your portfolio with the number of shares.
- Fetches current stock prices and calculates:
  - Total portfolio value.
  - Individual stock value, profit/loss, and percentage changes.
- Option to remove stocks from the portfolio.

### 3. Top 10 News
- Fetches the top 10 news articles for a selected stock.
- Displays:
  - News title.
  - Summary.
  - Title sentiment.
  - Summary sentiment.

---

## Installation

### Prerequisites
- Python 3.9 or later
- Install `pip` if not already installed.

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository-url.git
   cd stock-dashboard

## Install the required dependencies:

pip install -r requirements.txt

## Download the dataset for stock tickers and place it in the datasets folder:

    File: datasets/stock_info.csv
    Column: Ticker (List of valid stock tickers)

## Run the app:

    streamlit run app.py

## Usage

    Open the app in your browser using the local Streamlit server link provided in the terminal.
    Use the sidebar to:
        Select a stock ticker.
        Set a date range for stock pricing data.
    Navigate through the tabs for:
        Viewing pricing data and returns.
        Managing your stock portfolio.
        Reading the latest stock news.

## Folder Structure

.
├── app.py               # Main application script
├── datasets/
│   └── stock_info.csv   # List of stock tickers
├── requirements.txt     # Python dependencies
└── README.md            # Documentation

## Dependencies

See requirements.txt.
