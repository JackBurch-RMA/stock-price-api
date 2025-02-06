from flask import Flask, request, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route('/stock_price', methods=['GET'])
def stock_price():
    ticker = request.args.get('ticker', '').upper()
    if not ticker:
        return jsonify({"error": "Please provide a valid stock ticker"}), 400

    try:
        stock = yf.Ticker(ticker)
        current_price = stock.history(period="1d")["Close"].iloc[-1]
        return jsonify({"ticker": ticker, "price": round(float(current_price), 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)