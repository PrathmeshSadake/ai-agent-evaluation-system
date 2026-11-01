from langchain.tools import tool
from dotenv import load_dotenv
from datetime import date
import logging

from data import users_data
from objects import PurchaseItem

load_dotenv()


logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


@tool
def get_user_purchase_history(user: str) -> dict:
    """
    This tool is used to get the purchase history of a user.
    It takes the username as an argument and returns the purchase history of the user if user exists.
    """
    logging.info(f"Getting purchase history for user: {user}")
    if (users_data.get(user)):
        return users_data[user]
    else:
        return {"status": "error", "message": "User not found"}


@tool
def calculate_right_refund(user: str, items: list[PurchaseItem]) -> str:
    """
    This tool is used to calculate the right refund for a user.
    It takes the username and the item as an argument and returns the right refund for the item.
    """
    logging.info(
        f"Calculating right refund for user: {user} and item: {items}")
    if (users_data.get(user)):
        total_price = 0
        for item in items:
            if (users_data[user].get(item.name)):
                total_price += users_data[user][item.name]["price"]
            else:
                return {"status": "error", "message": "Item not found"}
        return total_price
    else:
        return {"status": "error", "message": "User not found"}


@tool
def issue_refund_ticket(user: str, refund_amount: float) -> str:
    """
    This tool is used to issue a refund ticket for a user.
    It takes the username and the refund amount as an argument and returns the refund ticket for the user.
    """
    logging.info(
        f"Issuing refund ticket for user: {user} and refund amount: {refund_amount}")
    if (users_data.get(user)):
        return {"status": "success", "message": "Refund ticket issued"}
    else:
        return {"status": "error", "message": "User not found"}


@tool
def get_today_date(user: str) -> str:
    """
    This tool is used to get the today's date.
    It returns the today's date in the format of YYYY-MM-DD.
    """
    logging.info("Getting today's date")
    return date.today()


# print(get_user_purchase_history.invoke("user123"))

# book = PurchaseItem(name="book")
# pen = PurchaseItem(name="pen")
# items = [book, pen]
# print(calculate_right_refund.invoke({"user": "user123", "items": items}))


# print(issue_refund_ticket.invoke({"user": "user123", "refund_amount": 10000}))

# print(get_today_date.invoke({"user": "user123"}))
