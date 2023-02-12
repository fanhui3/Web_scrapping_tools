import pyautogui as pg
import time

time.sleep(3)
while True:
    pg.move(800,0, duration=3)
    pg.leftClick()
    pg.move(-800,0, duration=3)
    pg.leftClick()
    time.sleep(5)