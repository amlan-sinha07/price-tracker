import pytest
from src.validator import is_valid_url
@pytest.mark.parametrize(
    "url,expected",
    [
        ("https://example.com",True),
        ("http://example.com",True),
        ("example.com",False),
        ("ftp://example.com",False),
        (" ",False),
        ("https://exa mple.com",False),
        ("[https://example.com](https:example.com)",False)
    ]
)
def test_is_valid_url(url,expected):
    assert is_valid_url(url) is expected
'''
def test_valid_https_url():
    assert is_valid_url("https://example.com") is True
def test_valid_http_url():
    assert is_valid_url("http://example.com") is True
def test_invalid_url_without_scheme():
    assert is_valid_url("example.com") is False
def test_invalid_ftp_url():
    assert is_valid_url("ftp://example.com") is False
'''
'''
print(bool(is_valid_url("https://example.com")))
print(is_valid_url("http://example.com"))
print(is_valid_url("example.com"))
print(is_valid_url("ftp://example.com"))
'''

# use this if you want to use pytest original
# test_ -> method
# python -m pytest tests/test_validators.py -v

# otherwise you can use 
# python -m pytest tests/test_validators.py -v -s
# for if you want print() statement as super neccessary

# the -s flag disables pytest output capturing