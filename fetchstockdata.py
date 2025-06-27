import yfinance as yf
from rx import Observable # Assuming the ReactiveX library is installed as 'rx' based on a potential source.
from rx.subject import Subject

# 1. Fetch Stock Data using yfinance
def fetch_stock_data(ticker, start_date, end_date):
    """Fetches historical stock data using yfinance."""
    try:
        data = yf.download(ticker, start=start_date, end=end_date)
        return data
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

# 2. Create an Observable from the Stock Data
def create_stock_observable(stock_data):
    """Creates an Observable from the stock data."""
    source = Observable.from_(stock_data.iterrows())  # Use from_ to iterate over DataFrame rows
    return source

# 3. Example Usage:
if __name__ == "__main__":
    ticker = "AAPL"
    start_date = "2023-01-01"
    end_date = "2024-01-01"

    stock_data = fetch_stock_data(ticker, start_date, end_date)

    if stock_data is not None:
        stock_observable = create_stock_observable(stock_data)

        # Subscribe to the Observable and process the data
        stock_observable.subscribe(
            on_next=lambda item: print(f"Date: {item[0].date()}, Close Price: {item[1]['Close']}"),
            on_error=lambda e: print(f"Error occurred: {e}"),
            on_completed=lambda: print("Stock data processing completed.")
        )