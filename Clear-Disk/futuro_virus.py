import pyautogui as pa
import time

pa.hotkey("win","r")
pa.write("cleanmgr")
pa.press("enter")

pa.press("Tab")
pa.press("enter")

time.sleep(2)
pa.click(x=421, y=229)
pa.press("Tab")
pa.press("enter")