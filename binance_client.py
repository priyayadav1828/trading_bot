from binance.client import Client
from binance.enums import *

from config import (
    API_KEY,
    API_SECRET,
    TESTNET_URL
)

from logger_config import logger


class BinanceTrader:

    def __init__(self):
        self.client = Client(
            API_KEY,
            API_SECRET
        )

        self.client.FUTURES_URL = TESTNET_URL


    def place_market_order(
        self,
        symbol,
        side,
        quantity
    ):

        logger.info(
            f"MARKET ORDER -> {side} {symbol}"
        )

        response = self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_MARKET,
            quantity=quantity
        )

        logger.info(response)

        return response


    def place_limit_order(
        self,
        symbol,
        side,
        quantity,
        price
    ):

        logger.info(
            f"LIMIT ORDER -> {side} {symbol}"
        )

        response = self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_LIMIT,
            quantity=quantity,
            price=price,
            timeInForce="GTC"
        )

        logger.info(response)

        return response