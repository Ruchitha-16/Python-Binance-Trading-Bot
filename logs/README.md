# Binance Futures Trading Bot

This project is a simple Python CLI application that places orders on the Binance Futures Testnet.

Features
- Market order support
- Limit order support
- BUY and SELL operations
- Input validation
- Logging system
- Error handling

Setup

1. Clone repository

2. Install dependencies

pip install -r requirements.txt

3. Add Binance API keys inside cli.py

Example Commands

Market Order

python bot/cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.002

Limit Order

python bot/cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000