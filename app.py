from flask import Flask, render_template
import pandas as pd
import yfinance as yf
app = Flask(__name__)
@app.route('/')
def home():
    # Download the historical stock data for a specific ticker
    ticker = "TATAMOTORS.NS"
    data = yf.download(ticker, period="max")

    # Calculate the moving averages
    ma50 = data['Close'].rolling(window=1).mean()
    ma200 = data['Close'].rolling(window=2).mean()

    # Determine the trend based on the moving averages
    if ma50[-1] > ma200[-1]:
        trend = "Bullish You can Buy for short Range"
    elif ma50[-1] < ma200[-1]:
        trend = "Bearish You can sell or hold "
    else:
        trend = "Neutral You can Wait for breakout !"

    # Render the HTML template and pass in the moving averages and trend
    return render_template('index.html', ma50=ma50[-1], ma200=ma200[-1], trend=trend)

if __name__ == '__main__':
    app.run(debug=True,port=5000)
