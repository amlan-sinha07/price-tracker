import os
import json

from pathlib import Path 
from dotenv import load_dotenv
from src.validator import is_valid_url
from src.config_loader import load_products,save_products

from src.product_manager import (
    add_product,
    get_product,
    update_product,
    remove_product
)
PROJECT_ROOT=Path(__file__).resolve().parent.parent

def load_products(filename="products.json"):
    file_path= PROJECT_ROOT / filename
    with open(file_path,"r",encoding="utf-8") as file:
        
        data=json.load(file)
    return data["products"]
def find_duplicate_urls(products):

    seen =set()
    duplicates=set()
    for product in products:
    
        url=product["url"]
        if url in seen:
            duplicates.add(url)
    
        else:
            seen.add(url)
    return duplicates

def validate_unique_urls(products):
    duplicates=find_duplicate_urls(products)
    if duplicates:

        raise ValueError(
            f"Duplicate product urls: {sorted(duplicates)}"
        )
    return True
def main():
    load_dotenv(PROJECT_ROOT / ".env")
    request_timeout=int(os.getenv("REQUEST_TIMEOUT","10"))
    products=load_products()
    
    try:
        validate_unique_urls(products)
    except ValueError as error:
        print(error)
        return
    for product in products:
        url=product["url"]
        if not is_valid_url(url):
            print(f"Invalid url: {url}")
            continue
        print(f"Url accepted: {url}")
    try:
        products=load_products()
    except (FileNotFoundError,ValueError) as error:
        print(f"Configuration error: {error}")
        return
    print(f"loaded {len(products)} products.")
    new_product=add_product(products,{
        "name":"laptop",
        "url":"https://example.com/laptop",
        "target_price":50000
    })
    save_products(products)
    product=get_product(products,new_product['id'])
    print(product)
    updated_products=update_product(
        products,
        new_product['id'],
        {"target_price":45000}
        )
    if updated_products is not None:
        save_products(updated_products)
    deleted=remove_product(products,new_product['id'])
    if deleted:
        save_products(products)
if __name__ == "__main__":
    main()