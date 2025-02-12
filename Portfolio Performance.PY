import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Function to fetch stock data
def get_stock_data(tickers, start_date, end_date):
    data = yf.download(tickers, start=start_date, end=end_date)['Adj Close']
    return data

# Function to calculate portfolio returns
def calculate_portfolio_returns(data, weights):
    log_returns = np.log(data / data.shift(1))
    portfolio_returns = log_returns.dot(weights)
    return portfolio_returns

# Function to calculate key metrics
def calculate_metrics(portfolio_returns, risk_free_rate=0.02):
    cumulative_return = np.exp(portfolio_returns.cumsum())[-1] - 1
    annualized_volatility = portfolio_returns.std() * np.sqrt(252)
    sharpe_ratio = (portfolio_returns.mean() * 252 - risk_free_rate) / annualized_volatility
    max_drawdown = (portfolio_returns.cumsum() - portfolio_returns.cumsum().cummax()).min()
    
    return {
        "Cumulative Return": round(cumulative_return * 100, 2),
        "Annualized Volatility": round(annualized_volatility * 100, 2),
        "Sharpe Ratio": round(sharpe_ratio, 2),
        "Max Drawdown": round(max_drawdown * 100, 2),
    }

# Get user inputs
tickers = ["AAPL", "MSFT", "GOOGL"]  # Change as needed
start_date = "2023-01-01"
end_date = "2024-01-01"

# Assigning equal weights for simplicity
weights = np.ones(len(tickers)) / len(tickers)

# Fetch stock data
stock_data = get_stock_data(tickers, start_date, end_date)

# Calculate portfolio returns
portfolio_returns = calculate_portfolio_returns(stock_data, weights)

# Calculate performance metrics
metrics = calculate_metrics(portfolio_returns)

# Display performance metrics
print("\nPortfolio Performance Metrics:")
for key, value in metrics.items():
    print(f"{key}: {value}%")

# Plot cumulative returns
cumulative_returns = np.exp(portfolio_returns.cumsum())
plt.figure(figsize=(12, 5))
plt.plot(cumulative_returns.index, cumulative_returns.values, label="Portfolio Cumulative Returns")
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.title("Portfolio Cumulative Returns Over Time")
plt.legend()
plt.grid()
plt.show()

# Plot drawdowns
drawdowns = portfolio_returns.cumsum() - portfolio_returns.cumsum().cummax()
plt.figure(figsize=(12, 5))
plt.fill_between(drawdowns.index, drawdowns.values, color="red", alpha=0.3)
plt.xlabel("Date")
plt.ylabel("Drawdown (%)")
plt.title("Portfolio Drawdowns Over Time")
plt.grid()
plt.show()

# Export report to Excel
report_data = pd.DataFrame(metrics, index=[0])
report_data.to_excel("portfolio_performance.xlsx", index=False)
print("\n✔ Report saved as 'portfolio_performance.xlsx'")
