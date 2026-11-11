import pytest
import uuid

from src.product_manager import(
    add_product,
    get_product,
    update_product,
    remove_product
)
@pytest.fixture
def sample_products():
    return [
        {
            "id": "product-001",
            "name": "laptop",
            "url": "https://example.com/laptop",
            "target_price": 50000
        },
        {
            "id": "product-002",
            "name": "Keyboard",
            "url": "https://example.com/keyboard",
            "target_price": 2000
        }
    ]
'''Test 1'''
def test_add_product():
    products=[]
    new_product = {
        "name": "mouse",
        "url": "https://example.com/mouse",
        "target_price": 1000
    }
    created_product=add_product(products,new_product)
    assert len(products)==1
    assert created_product in products
    assert created_product["name"]=="mouse"
    assert created_product["target_price"]==1000

    assert uuid.uuid4(created_product["id"]).version==4

    assert "id" not in new_product

'''test 2'''
def test_get_product_found(sample_products):
    result=get_product(sample_products,"product-001")
    assert result is not None
    assert result["name"]=="laptop"
    assert result["target_price"]==50000
'''test 3'''
def test_get_product_not_found(sample_products):
    result=get_product(sample_products,"unknown-id")
    assert result is None
'''test 4'''
def test_update_product(sample_products):
    result=update_product(
        sample_products,
        "product-001",
        {"target_price":45000}
    ) 
    assert result is sample_products
    assert result[0]["target_price"]==45000
    assert result[0]["name"]=="laptop"
'''test 5'''
def test_update_preserves_id(sample_products):
    original_id=sample_products[0]["id"]
    with pytest.raises(ValueError):
        update_product(
            sample_products,
            original_id,
            {"id":"new-id"}
        )
    assert sample_products[0]["id"]==original_id
'''test-6'''
def test_remove_product(sample_products):
    result=remove_product(sample_products,"product-001")
    assert result is True
    assert len(sample_products)==1
    assert sample_products[0]["id"]=="product-002"