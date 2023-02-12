import pyautogui as pg
import webbrowser
import time

BUTTONS = ["income_button", "balance_sheet_button", "cashflow_button", "metric_button", "growth_button"]

def go_to_site(browser_location: str, stock: str) -> None:
    """This function open up the stockrow financial page in annual format 

    Args:
        stock (_str_): ticker symbol listed on thy nyse or nasdaq
        browser_location (_str_): location where you keep your brower exe
    """
    url = f'https://stockrow.com/{stock}/financials/income/annual'
    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser(browser_location))
    webbrowser.get('chrome').open(url)


def export_table(table:str):
    """this scripts will find the table on the site and proceed to click export

    Args:
        table (_str_): the button name in your screenshot folder without hte png extension
    """
    time.sleep(2)
    coordinates = pg.locateCenterOnScreen(f"./Screenshots/{table}.png", confidence=0.8)
    pg.moveTo(coordinates, duration=1)
    pg.leftClick()
    time.sleep(1)
    coordinates = pg.locateCenterOnScreen("./Screenshots/export_button.png", confidence=0.8)
    pg.moveTo(coordinates, duration=1)
    pg.leftClick()


def get_stockrow_data(stock):
    brower_path = open("browser_location.txt",'r').readline()
    go_to_site(brower_path, stock)

    for button in BUTTONS:
        export_table(button)

if __name__ =="__main__":
    ticker = "tsla"
    get_stockrow_data(ticker)
