from langchain_core.tools import tool

from data.products import products
from utils.logger import logger


@tool
def search_products(query: str):
    """
    Search products by keyword.
    """

    logger.info(f"Searching products for: {query}")

    query = query.lower()

    results = []

    for pid, product in products.items():

        text = (
            product["name"]
            + " "
            + product["category"]
            + " "
            + product["brand"]
            + " "
            + product["description"]
        ).lower()

        if query in text:

            results.append(
                {
                    "product_id": pid,
                    **product
                }
            )

    logger.info(f"Found {len(results)} products")

    return results