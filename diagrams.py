from os import path

from flask import Flask, render_template
import pandas as pd
import plotly.graph_objects as go

from data_collecting import get_market_caps, get_klines_data

app = Flask(__name__)


@app.route("/")
def home():
    interval = "1d"  # Replace with your desired interval (e.g., 1d, 4h, 1h)
    symbol = "BTCUSDT"  # Replace with your desired symbol (e.g., BTCUSDT, ETHUSDT)

    # Read the CSV file containing the candlestick data
    candlestick_filename = f"{symbol}_{interval}_data.csv"  # Replace with the actual filename

    # Check if the file exists
    if path.exists(candlestick_filename):
        # Read the existing CSV file
        candlestick_df = pd.read_csv(candlestick_filename)
    else:
        # Generate CSV file and read it
        get_klines_data(interval, symbol)
        candlestick_df = pd.read_csv(candlestick_filename)

    # Convert the timestamps to datetime objects for better readability
    candlestick_df["Open time"] = pd.to_datetime(candlestick_df["Open time"], unit="ms")

    # Create a candlestick chart using Plotly
    candlestick_chart = go.Candlestick(
        x=candlestick_df["Open time"],
        open=candlestick_df["Open"],
        high=candlestick_df["High"],
        low=candlestick_df["Low"],
        close=candlestick_df["Close"]
    )

    # Create the layout for the candlestick chart
    candlestick_layout = go.Layout(
        title="Candlestick Chart",
        xaxis_title="Time",
        yaxis_title="Price"
    )

    # Receive data from Binance API for the pie chart
    symbols, market_caps = get_market_caps()

    # Create the pie chart using Plotly
    pie_chart = go.Pie(labels=symbols, values=market_caps)

    # Create the layout for the pie chart
    pie_layout = go.Layout(
        title="Market Caps"
    )

    # Create the figures for both charts
    candlestick_figure = go.Figure(data=[candlestick_chart], layout=candlestick_layout)
    pie_figure = go.Figure(data=[pie_chart], layout=pie_layout)

    # Convert the figures to JSON for JavaScript rendering
    candlestick_data = candlestick_figure.to_json()
    pie_data = pie_figure.to_json()

    # Render the Flask template with the chart data
    return render_template("index.html", candlestick_data=candlestick_data, pie_data=pie_data)


if __name__ == "__main__":
    app.run()
