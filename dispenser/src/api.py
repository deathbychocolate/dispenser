"""This file will contain the endpoints needed for the backend"""

import json
from uuid import uuid4
from flask import Flask, jsonify, request

from src.constants import (
    PATH_PROJECT_AVAILABLE_CASH_DATA_FILE,
    PATH_PROJECT_STOCK_DATA_FILE,
)


app = Flask(__name__)


@app.route("/")
def home():
    """The root of the API"""
    return "Welcome to the drink dispenser."


@app.get("/stock")
def stock_get():
    """Gets the stock available for the user"""

    stock_count = None
    with open(PATH_PROJECT_STOCK_DATA_FILE, encoding="utf8") as filepointer:
        stock_count = json.load(filepointer)["available_units"]

    return stock_count


@app.get("/price")
def price_get():
    """Gets the price of the available stock for the user

    Extended description of function.

    Returns:
        bool: Description of return value

    """

    stock_count = None
    with open(PATH_PROJECT_STOCK_DATA_FILE, encoding="utf8") as filepointer:
        stock_count = json.load(filepointer)["prices"]

    return stock_count


def is_product_expired(product_is_expired: dict, product_name: str) -> bool:
    """Tells you if a product is expired or not.

    Args:
        product_is_expired (dict): JSON where the key is the product name and the value is True or False
        product_name (str): A simple product name that acts as the dictionary key

    Returns:
        bool: Value that says if the product is expired or not

    """
    is_expired = product_is_expired[product_name]
    return is_expired


def is_product_available(product_count: dict, product_name: str) -> bool:
    """Checks if the product is available.

    Args:
        product_count (dict): JSON where the key is the product name and the value is an integer
        product_name (str): A simple product name that acts as the dictionary key

    Returns:
        bool: Value that says if the product is available or not

    """
    count = product_count[product_name]
    return count > 0


def is_sufficient_change_available_for_transaction(
    amount_inserted: dict, product_cost: dict, product_name: str
) -> bool:
    """Check if we have available change for this customer and their product choice

    Calculation based on coins inserted and the price of the product.

    Args:
        amount_inserted (float): The amount inserted by the user into the dispenser
        product_cost (dict): JSON where the key is the product name and the value is the cost of the product
        product_name (str): A simple product name that acts as the dictionary key

    Returns:
        bool: all conditions met for dispersing change

    NOTE by Damian Vonapartis:
    I am not considering the amount or kind of coins needed for change.
    Doing so would require all the time available to me. However, I will point out
    that we need to consider the classical coin problem: https://www.youtube.com/watch?v=x-QkFoh-i5Y
    """
    amount = get_cash_available_at_dispenser()
    change_to_dispense = amount_inserted["cash"] - product_cost[product_name]
    is_change_needed = change_to_dispense > 0
    is_change_available = amount > 0
    is_change_sufficient = change_to_dispense < amount

    return is_change_needed and is_change_available and is_change_sufficient


def get_cash_available_at_dispenser() -> float:
    """Get the amount of cash available at the Dispenser

    Returns:
        bool: Description of return value

    """
    amount = 0
    with open(PATH_PROJECT_AVAILABLE_CASH_DATA_FILE, encoding="utf8") as filepointer:
        amount = json.load(filepointer)["available"]
    return amount


@app.route("/purchase", methods=["POST"])
def purchase() -> dict:
    """Checks if the product is available.

    Returns:
        bool: A JSON object to send to the frontend

    NOTE: to test this endpoint, use commands similar to the following:
    curl -X POST http://127.0.0.1:5000/purchase -H 'Content-Type: application/json' -d '{"product_name":"Water"}'

    """

    purchase_quantity = 1

    stock = None
    with open(PATH_PROJECT_STOCK_DATA_FILE, encoding="utf8") as filepointer:
        stock = json.load(filepointer)

    data = request.get_json()
    product_name = data["product_name"]

    if (
        is_product_available(stock["available_units"], product_name=product_name)
        and not is_product_expired(stock["is_expired"], product_name=product_name)
        and is_sufficient_change_available_for_transaction(
            amount_inserted={"cash": 2},
            product_cost=stock["prices"],
            product_name=product_name,
        )
    ):
        purchase_id = str(uuid4())
        stock["available_units"][product_name] -= purchase_quantity

        with open(PATH_PROJECT_STOCK_DATA_FILE, "w", encoding="utf8") as filepointer:
            json.dump(stock, filepointer,indent=4)

        return jsonify(
            {
                "message": "Purchase successful!",
                "purchase_id": purchase_id,
                "product_name": product_name,
                "quantity_purchased": purchase_quantity,
                "remaining_in_stock": stock["available_units"][product_name],
            }
        )
    else:
        return jsonify({"message": "Out of stock!"}), 400


def get_product_attributes() -> dict:
    """Summary line.

    Returns:
        bool: Description of return value

    """
    return {}


@app.patch("/products")
def products_patch():
    """Update or Modify the number of a product"""
    # TODO


def run():
    """Start the api"""
    app.run()
