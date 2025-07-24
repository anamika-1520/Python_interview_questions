import re

def valid_url(url):
    return re.match(r'^(https?://)[^\s]+$', url) is not None

# Test cases
test_cases = [
    "https://www.example.com",
    "http://example.com",
    "www.example.com",
    "example.com",
    "https://example.com/path/to/resource",
    "http://example.com/path/to/resource",
    "https://chatgpt.com/c/68203386-9688-8010-b1ed-6c3398626e4c"]

for url in test_cases:
    if valid_url(url):
        print(f"'{url}' is a valid URL")
    else:
        print(f"'{url}' is not a valid URL")