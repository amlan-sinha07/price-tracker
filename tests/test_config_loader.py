import json
import pytest

from src.config_loader import load_products
def test_load_products_successfully(tmp_path):
    products = [
        {
            "id": 1,
            "name": "Laptop",
            "url": "https://example.com",
            "target_price": 50000
        }
    ]
    config_file=tmp_path/"products.json"
    config_file.write_text(
        json.dumps({"products":products}),
        encoding="utf-8"
    )
    result=load_products(config_file)
    assert result==products
    assert isinstance(result,list)
def test_missing_config_file(tmp_path):
    missing_file=tmp_path/"missing.json"
    with pytest.raises(FileNotFoundError):
        load_products(missing_file)