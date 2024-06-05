from cmu_graphics import *
from helpers import *
from stockData import *

#This function will display a new screen with the user's stock recommendations. 
def recsPg_redrawAll(app): 
#Drawing the label at the top.
    drawLabel('Here are your recommendations!', app.cx, 25, align='center', size=20, bold=True, font='monospace')
    drawLabel('Click on the company names to read more.', app.cx, 50, align='center', size=16, font='monospace')

#Displaying each stock recommendation and its information summarized in a box. 
    stockBoxW = 450
    stockBoxH = 100
    space = 10
    numBoxes = len(app.recs)
    totalHeight = numBoxes * stockBoxH + (numBoxes - 1) * space
    startY = (app.height - totalHeight) / 2 + stockBoxH / 2
    for i in range(numBoxes):
    # Draw a box for each stock. 
        cy = startY + i * (stockBoxH + space)
        drawRect(app.cx, cy, stockBoxW, stockBoxH, align='center', fill=None, border='black')
    #Display the stock name, symbol, logo, and shortened description in each box. 
        drawLabel(f'{app.recs[i].name} ({app.recs[i].symbol})', app.cx, cy-20, align='center', size=20, font='monospace')
        drawLabel(f'{app.recs[i].description[:75]} ... ', app.cx, cy+20, align='center')

    #Display a button to navigate back to the preferences page.
    drawLabel("Press 'p' to navigate back to the preferences page!", app.cx, 580, align='center', size=14, font='monospace')
    drawLabel("Press 'f' to view your favorite stocks.", app.cx, 605, align='center', size=16, font='monospace')

    #Log out button
    drawRect(app.cx, 650, 150, 50, align='center', fill=None, border='black')
    drawLabel('LOG OUT', app.cx, 650, align='center', size=20, bold=True, font='monospace')


def recsPg_onMousePress(app, mouseX, mouseY):
    
    stockBoxW = 450
    stockBoxH = 100
    space = 10

    # Using lists to store boundaries of each box. 
    boxLefts = []
    boxRights = []
    boxTops = []
    boxBottoms = []

    for i in range(len(app.recs)):
        # Calculating the boundaries of the current box and storing those values in a list. 
        boxLeft = app.cx - stockBoxW / 2
        boxRight = app.cx + stockBoxW / 2
        boxTop = (app.height - len(app.recs) * stockBoxH + (len(app.recs) - 1) * space) / 2 + i * (stockBoxH + space) - stockBoxH / 2
        boxBottom = boxTop + stockBoxH

        boxLefts.append(boxLeft)
        boxRights.append(boxRight)
        boxTops.append(boxTop)
        boxBottoms.append(boxBottom)

    # Check if at any point the mouse click is within the boundaries of any box displayed. 
    for i in range(len(app.recs)):
        if boxLefts[i] <= mouseX <= boxRights[i] and boxTops[i] <= mouseY <= boxBottoms[i]:
            if app.recs[i].name in app.availableGraphs:
                if app.recs[i].name == 'Apple Inc.':
                    setActiveScreen('appleDisplay')
                if app.recs[i].name == 'Moderna Inc.':
                    setActiveScreen('modernaDisplay')
                if app.recs[i].name == 'Johnson & Johnson':
                    setActiveScreen('jnjDisplay')
                if app.recs[i].name == 'Block Inc.':
                    setActiveScreen('blockDisplay')
                if app.recs[i].name == 'PayPal Holdings Inc.':
                    setActiveScreen('paypalDisplay')
                if app.recs[i].name == 'Bank of America Corporation':
                    setActiveScreen('boaDisplay')
                if app.recs[i].name == 'e.l.f. Beauty Inc.':
                    setActiveScreen('elfDisplay')
                if app.recs[i].name == 'PepsiCo Inc.':
                    setActiveScreen('pepsiDisplay')
                if app.recs[i].name == 'Spotify Technology S.A.': 
                    setActiveScreen('spotifyDisplay')
                if app.recs[i].name == 'AT&T Inc.':
                    setActiveScreen('atatDisplay')
    
    #Making the log out button functional. 
    if (app.cx - 150 / 2) <= mouseX <= (app.cx + 150 /2) and (650 - 50 / 2) <= mouseY <= (650 + 50 /2):
        setActiveScreen('loginPg')
        resetLoginPg(app)

def recsPg_onKeyPress(app, key):
    if key == 'p':
        setActiveScreen('prefsPg')
        resetPrefsPg(app)
    if key == 'f':
        setActiveScreen('favsPg')

    