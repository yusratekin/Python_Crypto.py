import requests


def get_crypto_data(token_name):
    response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={token_name}")
    if response.status_code == 200:
        return response.json()

# BTCUSDT
user_input = input("Enter your crypto currency : ")

crypto_response = get_crypto_data(user_input)
print("Sembol :", crypto_response["symbol"])
print("Fiyat :", crypto_response["price"])