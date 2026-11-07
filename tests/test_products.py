import pytest
from src.main import(
    find_duplicate_urls,
    validate_unique_urls
)
def test_find_duplicate_urls():
    products=[
        {"url":"https://example.com"},
        {"url":"https://google.com"},
        {"url":"https://example.com"}
    ]
    assert find_duplicate_urls(products)=={
        "https://example.com"
    }
def test_no_duplicate_urls():
    products=[
        {"url":"https://example.com"},
        {"url":"https://google.com"}
    ]
    assert find_duplicate_urls(products)==set()
def test_validate_unique_url_true():
    products=[
        {"url":"https://example.com"},
        {"url":"https://google.com"}
    ]
    assert validate_unique_urls(products) is True
def test_validate_unique_urls_raises_error():
    products=[
        {"url":"https://example.com"},
        {"url":"https://example.com"}
    ]
    with pytest.raises(ValueError):
        validate_unique_urls(products)