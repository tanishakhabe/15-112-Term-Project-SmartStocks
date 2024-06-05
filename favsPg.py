from cmu_graphics import *
from helpers import *
from stockData import *

def favsPg_redrawAll(app): 
#Drawing the label at the top.
    drawLabel(f' Hi {app.currUser}, here are your favorite stocks!', app.cx, 25, align='center', size=20, bold=True, font='monospace')
    drawLabel('Click on the company names to read more.', app.cx, 50, align='center', size=16, font='monospace')
    drawLabel("Press 'r' to navigate back to the recommendations page!", app.cx, 575, align='center', size=14, font='monospace')
    drawRect(app.cx, 650, 150, 50, align='center', fill=None, border='black')
    drawLabel('LOG OUT', app.cx, 650, align='center', size=20, bold=True, font='monospace')

#Displaying each favorite stock and its information summarized in a box. 
    stockBoxW = 450
    stockBoxH = 100
    space = 10
    numBoxes = len(app.currUser.favorites)
    totalHeight = numBoxes * stockBoxH + (numBoxes - 1) * space
    startY = (app.height - totalHeight) / 2 + stockBoxH / 2
    for i in range(numBoxes):
    # Draw a box for each stock. 
        cy = startY + i * (stockBoxH + space)
        drawRect(app.cx, cy, stockBoxW, stockBoxH, align='center', fill=None, border='black')
    #Display the stock name in each box.
        drawLabel(f'{app.currUser.favorites[i]}', app.cx, cy, align='center', size=20, font='monospace')

def favsPg_onKeyPress(app, key):
    if key == 'r':
        setActiveScreen('recsPg')

def favsPg_onMousePress(app, mouseX, mouseY):
    stockBoxW = 450
    stockBoxH = 100
    space = 10

    # Using lists to store boundaries of each box. 
    boxLefts = []
    boxRights = []
    boxTops = []
    boxBottoms = []

    for i in range(len(app.currUser.favorites)):
        # Calculating the boundaries of the current box and storing those values in a list. 
        boxLeft = app.cx - stockBoxW / 2
        boxRight = app.cx + stockBoxW / 2
        boxTop = (app.height - len(app.currUser.favorites) * stockBoxH + (len(app.currUser.favorites) - 1) * space) / 2 + i * (stockBoxH + space) - stockBoxH / 2
        boxBottom = boxTop + stockBoxH

        boxLefts.append(boxLeft)
        boxRights.append(boxRight)
        boxTops.append(boxTop)
        boxBottoms.append(boxBottom)

    # Check if at any point the mouse click is within the boundaries of any box displayed. 
    for i in range(len(app.currUser.favorites)):
        if boxLefts[i] <= mouseX <= boxRights[i] and boxTops[i] <= mouseY <= boxBottoms[i]:
            if app.currUser.favorites[i] in app.availableGraphs:
                if app.currUser.favorites[i] == 'Apple Inc.':
                    setActiveScreen('appleDisplay')
                if app.currUser.favorites[i] == 'Moderna Inc.':
                    setActiveScreen('modernaDisplay')
                if app.currUser.favorites[i] == 'Johnson & Johnson':
                    setActiveScreen('jnjDisplay')
                if app.currUser.favorites[i] == 'Block Inc.':
                    setActiveScreen('blockDisplay')
                if app.currUser.favorites[i] == 'PayPal Holdings Inc.':
                    setActiveScreen('paypalDisplay')
                if app.currUser.favorites[i] == 'Bank of America Corporation':
                    setActiveScreen('boaDisplay')
                if app.currUser.favorites[i] == 'e.l.f. Beauty Inc.':
                    setActiveScreen('elfDisplay')
                if app.currUser.favorites[i] == 'PepsiCo Inc.':
                    setActiveScreen('pepsiDisplay')
                if app.currUser.favorites[i] == 'Spotify Technology S.A.': 
                    setActiveScreen('spotifyDisplay')
                if app.currUser.favorites[i] == 'AT&T Inc.':
                    setActiveScreen('atatDisplay')
        
    if (app.cx - 150 / 2) <= mouseX <= (app.cx + 150 /2) and (650 - 50 / 2) <= mouseY <= (650 + 50 /2):
        setActiveScreen('loginPg')
        resetLoginPg(app)
