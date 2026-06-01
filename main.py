import argparse

from rich.console import Console
from rich.table import Table

from binance_client import BinanceTrader

from utils.validators import (
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)

from logger_config import logger

console = Console()


def display_summary(args):

    table = Table(title="Order Summary")

    table.add_column("Field")
    table.add_column("Value")

    table.add_row("Symbol", args.symbol)
    table.add_row("Side", args.side)
    table.add_row("Type", args.type)
    table.add_row(
        "Quantity",
        str(args.quantity)
    )

    if args.price:
        table.add_row(
            "Price",
            str(args.price)
        )

    console.print(table)


def display_response(response):

    table = Table(
        title="Order Response"
    )

    table.add_column("Field")
    table.add_column("Value")

    table.add_row(
        "Order ID",
        str(response.get("orderId"))
    )

    table.add_row(
        "Status",
        str(response.get("status"))
    )

    table.add_row(
        "Executed Qty",
        str(response.get("executedQty"))
    )

    table.add_row(
        "Avg Price",
        str(response.get("avgPrice", "N/A"))
    )

    console.print(table)


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--symbol",
        required=True
    )

    parser.add_argument(
        "--side",
        required=True
    )

    parser.add_argument(
        "--type",
        required=True
    )

    parser.add_argument(
        "--quantity",
        required=True
    )

    parser.add_argument(
        "--price"
    )

    args = parser.parse_args()

    try:

        args.side = validate_side(
            args.side
        )

        args.type = validate_order_type(
            args.type
        )

        args.quantity = validate_quantity(
            args.quantity
        )

        args.price = validate_price(
            args.price
        )

        if (
            args.type == "LIMIT"
            and args.price is None
        ):
            raise ValueError(
                "LIMIT order requires price"
            )

        display_summary(args)

        trader = BinanceTrader()

        if args.type == "MARKET":

            response = (
                trader.place_market_order(
                    args.symbol,
                    args.side,
                    args.quantity
                )
            )

        else:

            response = (
                trader.place_limit_order(
                    args.symbol,
                    args.side,
                    args.quantity,
                    args.price
                )
            )

        display_response(response)

        console.print(
            "[green]SUCCESS: Order placed[/green]"
        )

    except Exception as e:

        logger.error(str(e))

        console.print(
            f"[red]ERROR: {e}[/red]"
        )


if __name__ == "__main__":
    main()