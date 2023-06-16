import requests
import csv


def get_klines_data(interval, symbol):
    # Binance API endpoint for klines (candlestick data)
    api_endpoint = "https://api.binance.com/api/v3/klines"

    # Parameters for the API request
    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": 1000,  # Number of data points to retrieve (max: 1000)
    }

    # Send GET request to Binance API
    response = requests.get(api_endpoint, params=params)
    data = response.json()

    # Save data to a CSV file
    filename = f"{symbol}_{interval}_data.csv"
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Open time", "Open", "High", "Low", "Close", "Volume", "Close time"])
        for item in data:
            writer.writerow(item[:6])  # Exclude the last element (ignore close time)

    print(f"Data saved to {filename}")


def get_market_caps():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 10,
        "page": 1,
        "sparkline": False
    }

    response = requests.get(url, params=params)
    data = response.json()

    symbols = []
    market_caps = []

    for entry in data:
        symbols.append(entry["symbol"].upper())
        market_caps.append(entry["market_cap"])

    return symbols, market_caps


if __name__ == "__main__":
    # Interval and symbol for data collection
    test_interval = "1d"  # Replace with your desired interval (e.g., 1d, 4h, 1h)
    test_symbol = "BTCUSDT"  # Replace with your desired symbol (e.g., BTCUSDT, ETHUSDT)

    get_klines_data(test_interval, test_symbol)
