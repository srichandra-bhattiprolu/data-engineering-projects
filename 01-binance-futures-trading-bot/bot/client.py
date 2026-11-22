import os
from binance.client import Client
from dotenv import load_dotenv

load_dotenv() # This loads your API keys from the .env file

def get_binance_client():
    api_key = os.getenv('BINANCE_API_KEY')
    api_secret = os.getenv('BINANCE_API_SECRET')
    # testnet=True is the most important part!
    return Client(api_key, api_secret, testnet=True)