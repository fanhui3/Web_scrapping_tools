from stockrow_scraper_mouse_clicks import get_stockrow_data
from subprocess import call

ticker = "MMM"

# def open_py_file():
#     call(["python", "stockrow_scraper.py"])

get_stockrow_data(ticker)