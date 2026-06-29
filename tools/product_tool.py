from langchain_core.tools import tool

from data.products import products
from utils.logger import logger


@tool
def get_product(product_id: str):
    """
    Fetch product details using the product ID.
    """

    logger.info(f"Fetching product: {product_id}")

    product = products.get(product_id)

    if product is None:
        logger.warning(f"Product not found: {product_id}")
        return {"error": "Product not found"}

    return product