import json
from pathlib import Path

PROJECT_ROOT=Path(__file__).resolve().parent.parent
PRODUCTS_FILE=PROJECT_ROOT / "config" / "products.json"

def save_products(products,product_file=None):
    file_path=Path(product_file) if product_file else PRODUCTS_FILE
    if not isinstance(products,list):
        raise TypeError(
            f"Products must be in list"
        )
    file_path.parent.mkdir(parents=True,exist_ok=True)
    temp_file=file_path.with_suffix(".json.tmp")
    with temp_file.open("w",encoding="utf-8") as file:
        json.dump(
            {"products":products},
            file,
            indent=4
        )
    temp_file.replace(file_path)
def load_products(products_file=None):
    file_path=(
        Path(products_file)
        if products_file
        else PRODUCTS_FILE
    )
    if not file_path.exists:
        return []
    try:
        with file_path.open("r",encoding="utf-8") as file:
            data=json.load(file)
    except FileNotFoundError as error:
        raise FileNotFoundError(
            f"Configuration file not found: {file_path}"
        ) from error
    except json.JSONDecodeError as error:
        raise ValueError(
            f"Invalid JSON configuration: {error}"
        ) from error
    if not isinstance(data,dict):   
        raise ValueError("Configuration must be jso object")
    products=data.get("products")
    if not isinstance(products,list):
        raise ValueError("'products' must be a list")
    return products