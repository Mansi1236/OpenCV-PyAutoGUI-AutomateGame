import time
import pyautogui as pag


time.sleep(6)
#print(pag.position()) -> this command is used to print the position of the coordinate the cursor is pointing currently at
# Since it immediately points the coordinate of the cursor we need to add some time delay to point our cursor at desired location 

#x=125, y=749
# the cursor moves to the windows search bar and opens Google Chrome by typibg it in there
pag.moveTo(125, 749, 3)
time.sleep(2)
pag.leftClick()
time.sleep(3)
pag.typewrite('Google Chrome')

time.sleep(2)
pag.press('enter')
time.sleep(10)

# moves to url bar to open the dino game
pag.moveTo(151, 52, 4)
time.sleep(2)
pag.leftClick()
time.sleep(5)
pag.typewrite('https://chromedino.com/')
time.sleep(3)
pag.press('enter')

# It presses space keyword to start the game 
time.sleep(6)
pag.moveTo(366, 285, 3)
time.sleep(2)
pag.press('space')



