from langchain_core.tools import tool

from data.products import products
from utils.logger import logger


@tool
def find_cheaper_products(category: str, max_price: float):
    """
    Find cheaper products within the same category.
    """

    logger.info(
        f"Finding cheaper products in {category} below {max_price}"
    )

    cheaper = []

    for pid, product in products.items():

        if (
            product["category"].lower() == category.lower()
            and product["price"] < max_price
        ):

            cheaper.append(
                {
                    "product_id": pid,
                    **product
                }
            )

    cheaper.sort(key=lambda x: x["price"])

    return cheaper


@tool
def best_rated_products(category: str):
    """
    Return the highest-rated products in a category.
    """

    logger.info(f"Finding best-rated products in {category}")

    result = []

    for pid, product in products.items():

        if product["category"].lower() == category.lower():

            result.append(
                {
                    "product_id": pid,
                    **product
                }
            )

    result.sort(
        key=lambda x: x["rating"],
        reverse=True
    )

    return result