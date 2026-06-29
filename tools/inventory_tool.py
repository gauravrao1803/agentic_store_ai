from langchain_core.tools import tool

from data.products import products
from utils.logger import logger


@tool
def check_stock(product_id: str):
    """
    Check product stock availability.
    """

    logger.info(f"Checking stock for {product_id}")

    product = products.get(product_id)

    if not product:
        return {"error": "Product not found"}

    return {
        "product": product["name"],
        "stock": product["stock"]
    }