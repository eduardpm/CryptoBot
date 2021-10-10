import requests


url = "https://api.exchange.coinbase.com/products/LTC-EUR/trades"


headers = {"Accept": "application/json"}


response = requests.request("GET", url, headers=headers)


print(response.text)

API_KEY = "3VYlSIAjG1BEXQmMZfeyOowlhfHAYWpMtmWdOOgNO5uStaNXkjCLcthiinwlKOGrCzYtiivCu70oIn6B0tXsEA=="