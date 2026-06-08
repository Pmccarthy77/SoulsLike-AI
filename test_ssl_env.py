import requests
import ssl
import certifi

print("Python SSL version:", ssl.OPENSSL_VERSION)
print("Certifi CA file:", certifi.where())

try:
    response = requests.get("https://example.com")
    print("HTTPS test status code:", response.status_code)
except requests.exceptions.SSLError as e:
    print("SSL error:", e)