stocks = [
    ("AAPL", 155.25),
    ("GOOG", 145.75),
    ("MSFT", 25.50),
    ("AMZN", 14.80),
    ("TSLA", 16.10),
]

selected_stocks = [stock for stock in stocks if stock[1] > 15.00]

print(selected_stocks)