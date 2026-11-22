import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("trading_bot.log"), # Saves to file
            logging.StreamHandler()                # Shows in terminal
        ]
    )
    return logging.getLogger(__name__)