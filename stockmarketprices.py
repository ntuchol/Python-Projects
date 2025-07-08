from flask import Flask, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route('/stock_price/<symbol>')
def get_stock_price(symbol):
    try:
        ticker = yf.Ticker(symbol)
        data = ticker.history(period="1d") # Get the last day's data
        latest_price = data['Close'].iloc[-1]
        return jsonify({'symbol': symbol, 'price': latest_price})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)