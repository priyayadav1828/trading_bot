# Binance Futures Testnet Trading Bot

## Overview

A Python-based Trading Bot for Binance Futures Testnet (USDT-M) that allows users to place Market and Limit orders through a Command Line Interface (CLI).

The project is designed with a modular architecture, input validation, logging, and exception handling to ensure maintainability and reliability.

---

## Features

* Place Market Orders
* Place Limit Orders
* Supports BUY and SELL orders
* Command Line Interface (CLI)
* Input Validation
* Structured Code Architecture
* Logging of Requests, Responses, and Errors
* Exception Handling
* Binance Futures Testnet Integration

---

## Project Structure

```text
trading_bot/
│
├── main.py
├── config.py
├── binance_client.py
├── logger_config.py
├── requirements.txt
├── README.md
│
├── logs/
│   └── app.log
│
└── utils/
    └── validators.py
```

---

## Prerequisites

* Python 3.9+
* Binance Futures Testnet Account
* Binance Futures Testnet API Credentials

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd trading_bot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file in the project root directory:

```env
API_KEY=YOUR_BINANCE_TESTNET_API_KEY
API_SECRET=YOUR_BINANCE_TESTNET_SECRET_KEY
```

### Important

The `.env` file is intentionally not included in the repository for security reasons.

Users must create their own `.env` file and provide their own Binance Futures Testnet API credentials.

---

## Running the Application

### Market Buy Order

```bash
python main.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Market Sell Order

```bash
python main.py --symbol BTCUSDT --side SELL --type MARKET --quantity 0.001
```

### Limit Buy Order

```bash
python main.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.001 --price 50000
```

### Limit Sell Order

```bash
python main.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 120000
```

---

## Sample Output

### Order Summary

```text
Order Summary
-------------
Symbol   : BTCUSDT
Side     : BUY
Type     : MARKET
Quantity : 0.001
```

### Order Response

```text
Order Response
--------------
Order ID     : 123456789
Status       : FILLED
Executed Qty : 0.001
Avg Price    : 105000
```

### Success Message

```text
SUCCESS: Order placed successfully
```

---

## Logging

Application logs are stored in:

```text
logs/app.log
```

The log file contains:

* API Requests
* API Responses
* Order Details
* Errors and Exceptions

Example:

```text
2026-06-01 22:30:15 - INFO - MARKET ORDER -> BUY BTCUSDT
2026-06-01 22:30:16 - INFO - Order placed successfully
```

---

## Error Handling

The application handles:

* Invalid order side
* Invalid order type
* Invalid quantity
* Missing price for LIMIT orders
* Binance API errors
* Network connectivity issues
* Unexpected runtime exceptions

---

## Assumptions

* User has a valid Binance Futures Testnet account.
* User has generated valid API credentials.
* Trading is performed only on Binance Futures Testnet.
* User has sufficient Testnet balance.
* Internet connectivity is available.

---

## Technologies Used

* Python 3
* python-binance
* python-dotenv
* rich
* argparse
* logging

---

## Author

PRIYA YADAV

B.Tech CSE (AI & ML)

Noida Institute of Engineering and Technology (NIET)
