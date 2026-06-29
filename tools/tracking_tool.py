from langchain_core.tools import tool
from data.orders import orders
from utils.logger import logger


@tool
def track_order(order_id: str):
    """
    Return tracking information for an order.
    """

    print("=" * 60)
    print("ORDER ID RECEIVED:", order_id)
    print("TYPE:", type(order_id))
    print("=" * 60)

    order = orders.get(order_id)

    print("ORDER FOUND:", order)

    if order is None:
        return {"error": f"Order '{order_id}' not found"}

    return {
        "tracking_id": order.get("tracking_id"),
        "shipping_partner": order.get("shipping_partner"),
        "status": order.get("status"),
        "expected_delivery": order.get("expected_delivery"),
    }