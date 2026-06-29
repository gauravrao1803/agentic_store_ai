from langchain_core.tools import tool

from data.orders import orders
from utils.logger import logger


@tool
def get_order(order_id: str):
    """
    Fetch order details using the order ID.
    """

    logger.info(f"Fetching order: {order_id}")

    order = orders.get(order_id)

    if order is None:
        logger.warning(f"Order not found: {order_id}")
        return {"error": "Order not found"}

    return order