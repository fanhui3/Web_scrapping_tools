import pyautogui as pg
import webbrowser
import time

ticker = "crwd"

def go_to_site(browser_location, stock):
    """This function open up the stockrow financial page in annual format 

    Args:
        stock (_str_): ticker symbol listed on thy nyse or nasdaq
        browser_location (_str_): location where you keep your brower exe
    """

    url = 'https://stockrow.com/{}/financials/income/annual'.format(stock)
    print(url)
    webbrowser.register('chrome',
        None,
        webbrowser.BackgroundBrowser(browser_location))
    webbrowser.get('chrome').open(url)

def export_table(table):
    """this scripts will find the table on the site and proceed to click export

    Args:
        table (_str_): the button name in your screenshot folder without hte png extension
    """
    time.sleep(2)
    coord = pg.locateCenterOnScreen("./Screenshots/{}.png".format(table), confidence=0.8)
    pg.moveTo(coord, duration=1)
    pg.leftClick()
    time.sleep(1)
    coord = pg.locateCenterOnScreen("./Screenshots/export_button.png", confidence=0.8)
    pg.moveTo(coord, duration=1)
    pg.leftClick()

brower_path = open("browser_location.txt",'r').readline()
go_to_site(stock=ticker, browser_location=brower_path)

buttons = ["income_button", "balance_sheet_button", "cashflow_button", "metric_button", "growth_button"]
for button in buttons:
    export_table(button)

