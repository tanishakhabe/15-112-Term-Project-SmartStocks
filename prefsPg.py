from cmu_graphics import * 
from helpers import *
from stockData import *

def prefsPg_redrawAll(app):
    #Drawing the label at the top.
    drawLabel('Select your stock preferences!', app.cx, 25, align='center', size=20, bold=True, font='monospace')
    #Select your preferred sector(s). 
    drawLabel('Select your preferred sector(s):', app.cx, 75, align='center', size=16, font='monospace')
    drawRect(130, 110, app.sectorW, app.sectorH, align='center', fill='thistle' if app.tech else None, border='black')
    drawLabel('Technology', 130, 110, align='center', size=16, font='monospace')
    drawRect(app.cx, 110, app.sectorW, app.sectorH, align='center', fill='thistle' if app.health else None, border='black')
    drawLabel('Healthcare', app.cx, 110, align='center', size=16, font='monospace')
    drawRect(470, 110, app.sectorW, app.sectorH, align='center', fill='thistle' if app.fin else None, border='black')
    drawLabel('Finance', 470, 110, align='center', size=16, font='monospace')
    drawRect(215, 160, app.sectorW, app.sectorH, align='center', fill='thistle' if app.cs else None, border='black')
    drawLabel('Consumer Staples', 215, 160, align='center', size=14, font='monospace')
    drawRect(385, 160, app.sectorW, app.sectorH, align='center', fill='thistle' if app.comm else None, border='black')
    drawLabel('Communication', 385, 160, align='center', size=16, font='monospace')
    #Select your preferred risk level. 
    drawLabel('Select your preferred risk level (select 1):', app.cx, 225, align='center', size=16, font='monospace')

    #Drawing five boxes to represent the different risk levels.
    boxSize = 60
    space = 8
    numBoxes = 5
    totalWidth = numBoxes * boxSize + (numBoxes - 1) * space
    startX = (app.width - totalWidth) / 2 + boxSize / 2
    for i in range(numBoxes):
        cx = startX + i * (boxSize + space)
        app.riskCoords.append(cx)
        drawRect(cx, 280, boxSize, boxSize, align='center', fill='thistle' if app.risks[i] == True else None, border='black')
        drawLabel(f'{i + 1}', cx, 280, align='center', size=16, font='monospace')
    #Labeling & drawing arrows below the risk scale. 
    drawLabel('Low Risk', startX / 2, 340, size=16, font='monospace')
    drawLabel('High Risk', (app.width - startX / 2), 340, size=16, font='monospace')
    drawLine((startX - boxSize / 2), 340, ((startX + 4 * (boxSize + space))+ boxSize / 2), 340, arrowStart=True, arrowEnd=True)

    #Select your preferred price range. 
    drawLabel('Select your preferred price range (select 1):', app.cx, 390, align='center', size=16, font='monospace')
    priceRanges = ['Below $50', 
    '$50-$150',
    '$150-$200',
    '$200-$300', 
    'Above $300']
    #Drawing five boxes to represent the different price ranges.
    boxSize = 80
    space = 8
    numBoxes = 5
    totalWidth = numBoxes * boxSize + (numBoxes - 1) * space
    startX = (app.width - totalWidth) / 2 + boxSize / 2
    for i in range(numBoxes):
        cx = startX + i * (boxSize + space)
        app.priceCoords.append(cx)
        drawRect(cx, 450, boxSize, boxSize, align='center', fill='thistle' if app.prices[i] == True else None, border='black')
        drawLabel(f'{priceRanges[i]}', cx, 450, align='center', size=12, font='monospace')

    #Get recommendations! button. 
    drawRect(app.cx, 575, 300, 50, align='center', fill=None, border='black')
    drawLabel('Get my recommendations!', app.cx, 575, align='center', size=20, bold=True, font='monospace')
    
    #Log out button
    drawRect(app.cx, 650, 150, 50, align='center', fill=None, border='black')
    drawLabel('LOG OUT', app.cx, 650, align='center', size=20, bold=True, font='monospace')

def prefsPg_onMousePress(app, mouseX, mouseY):
    #Store the user's preferred sector(s).
    if (130 - app.sectorW/2)<= mouseX <= (130 + app.sectorW/2) and (110 - app.sectorH/2) <= mouseY <= (110 + app.sectorH/2): 
        app.tech = not app.tech
        if app.tech: 
            app.currUser.sector.add('Technology')
    if (app.cx - app.sectorW/2) <= mouseX <= (app.cx + app.sectorW/2) and (110 - app.sectorH/2) <= mouseY <= (110 + app.sectorH/2): 
        app.health = not app.health
        if app.health:
            app.currUser.sector.add('Healthcare')
    if (470 - app.sectorW/2) <= mouseX <= (470 + app.sectorW/2) and (110 - app.sectorH/2) <= mouseY <= (110 + app.sectorH/2):
        app.fin = not app.fin
        if app.fin:
            app.currUser.sector.add('Finance')
    if (215 - app.sectorW/2) <= mouseX <= (215 + app.sectorW/2) and (160 - app.sectorH/2) <= mouseY <= (160 + app.sectorH/2):
        app.cs = not app.cs
        if app.cs: 
            app.currUser.sector.add('Consumer Staples')
    if (385 - app.sectorW/2) <= mouseX <= (385 + app.sectorW/2) and (160 - app.sectorH/2) <= mouseY <= (160 + app.sectorH/2):
        app.comm = not app.comm
        if app.comm:
            app.currUser.sector.add('Communication')

    #Store the user's preferred risk level. 
    if (app.riskCoords[0] - 30) <= mouseX <= (app.riskCoords[0] + 30) and (280 - 30) <= mouseY <= (280 + 30): 
        app.risks[0] = not app.risks[0]
        if app.risks[0]: 
            app.currUser.risk = 1
    if (app.riskCoords[1] - 30) <= mouseX <= (app.riskCoords[1] + 30) and (280 - 30) <= mouseY <= (280 + 30): 
        app.risks[1] = not app.risks[1]
        if app.risks[1]:
            app.currUser.risk = 2
    if (app.riskCoords[2] - 30) <= mouseX <= (app.riskCoords[2] + 30) and (280 - 30) <= mouseY <= (280 + 30):  
        app.risks[2] = not app.risks[2]
        if app.risks[2]:
            app.currUser.risk = 3
    if (app.riskCoords[3] - 30) <= mouseX <= (app.riskCoords[3] + 30) and (280 - 30) <= mouseY <= (280 + 30): 
        app.risks[3] = not app.risks[3]
        if app.risks[3]:
            app.currUser.risk = 4
    if (app.riskCoords[4] - 30) <= mouseX <= (app.riskCoords[4] + 30) and (280 - 30) <= mouseY <= (280 + 30): 
        app.risks[4] = not app.risks[4]
        if app.risks[4]:
            app.currUser.risk = 5

    #User's preferred price range. 
    if (app.priceCoords[0] - 40) <= mouseX <= (app.priceCoords[0] + 40) and (450 - 40) <= mouseY <= (450 + 40): 
        app.prices[0] = not app.prices[0]
        if app.prices[0]:
            app.currUser.minPrice = 0
            app.currUser.maxPrice = 50
    if (app.priceCoords[1] - 40) <= mouseX <= (app.priceCoords[1] + 40) and (450 - 40) <= mouseY <= (450 + 40): 
        app.prices[1] = not app.prices[1]
        if app.prices[1]:
            app.currUser.minPrice = 50
            app.currUser.maxPrice = 150
    if (app.priceCoords[2] - 40) <= mouseX <= (app.priceCoords[2] + 40) and (450 - 40) <= mouseY <= (450 + 40): 
        app.prices[2] = not app.prices[2]
        if app.prices[2]:
            app.currUser.minPrice = 150
            app.currUser.maxPrice = 200
    if (app.priceCoords[3] - 40) <= mouseX <= (app.priceCoords[3] + 40) and (450 - 40) <= mouseY <= (450 + 40):  
        app.prices[3] = not app.prices[3]
        if app.prices[3]: 
            app.currUser.minPrice = 200
            app.currUser.maxPrice = 300
    if (app.priceCoords[4] - 40) <= mouseX <= (app.priceCoords[4] + 40) and (450 - 40) <= mouseY <= (450 + 40): 
        app.prices[4] = not app.prices[4]
        if app.prices[4]:
            app.currUser.minPrice = 300
            app.currUser.maxPrice = 1000

    #Making the Get recommendations! button functional. 
    if (app.cx - 300/2) <= mouseX <= (app.cx + 300/2) and (600 - 50/2) <= mouseY <= (600 + 50/2): 
        app.get = True
    
    #Making the log out button functional. 
    if (app.cx - 150 / 2) <= mouseX <= (app.cx + 150 /2) and (650 - 50 / 2) <= mouseY <= (650 + 50 /2):
        setActiveScreen('loginPg')
        resetLoginPg(app)
        
    #Call the recommendations algorithm.
    #Display the recommendations page. 
    if app.get == True: 
        app.recs = filterStocks(app.currUser, stocksList)
        setActiveScreen('recsPg')