def collect_ticker_symbols():
    print("Enter stock ticker symbols one at a time. Type 'done' when finished.")
    ticker_symbols = []

    while True:
        symbol = input("Enter ticker symbol: ").strip().upper()
        if symbol == 'DONE':
            break
        elif symbol.isalpha():
            ticker_symbols.append(symbol)
        else:
            print("Invalid input. Please enter a valid ticker symbol (letters only).")

    print("\nYou entered the following ticker symbols:")
    for ticker in ticker_symbols:
        print(f"- {ticker}")

    return ticker_symbols

if __name__ == "__main__":
    collect_ticker_symbols()
