import requests

API_KEY = "YOUR_API_KEY"
SYMBOL = "TSM"

def fetch_stock():
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={SYMBOL}&apikey={API_KEY}"
    response = requests.get(url)
    data = response.json()

    price = float(data["Global Quote"]["05. price"])

    return {
        "symbol": SYMBOL,
        "price": price,
        "alert": price < 330
    }

if __name__ == "__main__":
    print(fetch_stock())
