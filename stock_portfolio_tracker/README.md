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

