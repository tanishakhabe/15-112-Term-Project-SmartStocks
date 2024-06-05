from cmu_graphics import * 
from helpers import * 
from stockData import *
from PIL import Image

def modernaDisplay_redrawAll(app):
    #Display the stock name and symbol. 
    drawLabel(f'Moderna Inc. ({moderna.symbol}): ', app.cx, 50,  size=40, font='monospace')
    drawImage(app.modernaImage, app.cx, 450, width = 200, height = 75, align='center')

    #Display the cut up description so it doesn't run off screen.
    startX = 150
    space = 20
    cutDesc = moderna.description.split(' ')
    for i in range ((len(cutDesc) // 9) + 1):
        drawLabel(f"{' '.join(cutDesc[i * 9: (i + 1) * 9])}", app.cx, startX + space + i*30, size=16)

    #Display an option to display a price graph from the last five years. 
    drawLabel("Press 'g' to view a graph of the stock price.", app.cx, 625, align='center', size=20, font='monospace')
    drawLabel("Press 'b' to go back to the recommendations page.", app.cx, 650, align='center', size=20, font='monospace')
    drawLabel("Press 'f' to view your favorite stocks.", app.cx, 675, align='center', size=20, font='monospace')

    #Option to add or remove from favorites list. 
    drawRect(app.cx, 115, app.loginW, app.loginH, align='center', fill= 'thistle' if app.modernaFaved else None, border='black',)
    drawLabel('Favorite this stock!', app.cx, 115, size=16, bold=True, font='monospace')

def modernaDisplay_onMousePress(app, mouseX, mouseY):
    if (app.cx - app.loginW/ 2) <= mouseX <= (app.cx + app.loginW / 2) and (115 - app.loginH / 2) <= mouseY <= (115 + app.loginH / 2):
        app.modernaFaved = not app.modernaFaved
        if app.modernaFaved: 
            app.currUser.favorites.append(moderna.name)
        else:
            app.currUser.favorites.remove(moderna.name)

def modernaDisplay_onKeyPress(app, key):
    if key == 'g':
        app.modernaGraph = True
        if app.modernaGraph:
            setActiveScreen('modernaGraph')
    if key == 'b':
        setActiveScreen('recsPg')
    if key == 'f':
        setActiveScreen('favsPg')

def modernaGraph_redrawAll(app):
    drawLabel(f'Moderna Inc. ({moderna.symbol}) Stock Price History', app.cx, 50, size=20, font='monospace')
    #Display an option to go back to the company info page. 
    drawLabel("Press 'z' to view the entire graph zoomed in.", app.cx, 670, align='center', size=16, font='monospace')
    drawLabel("Press 'b' to go back.", app.cx, 685, align='center', size=16, font='monospace')

    #Drawing the normal graph within another rectangle.
    if not app.zoomed:
        drawRect (*app.gridPoints, align='center', fill=None, border='black')

    #Drawing the axis labels for normal size graph.
        drawLabel('Price (in USD)', 40, app.cy, align='center', size=16, rotateAngle=270)
        drawLabel('Year', app.cx, 600, align='center', size=16)

    #Drawing the x-axis labels for normal size graph. 
        for i in range(len(app.xAxisLabels)):
            drawLabel(f'{app.xAxisLabels[i]}', app.normXAxis[i], 570, align='center', size=16)
            
    #Drawing y-axis labels for normal size graph
        for i in range(len(app.yAxisLabelsModerna)):
            drawLabel(f'{app.yAxisLabelsModerna[i]}', 80, app.normYAxisModerna[i], align='center', size=16)

    #Drawing the normal points on the graph. 
        newModernaPts = scaling(pricesDict['moderna'], app.normYAxisModerna[1], app.normYAxisModerna[8]) 
        for i in range (1, len(newModernaPts)):
            x1 = app.normXAxis[i-1]
            y1 = newModernaPts[i-1]
            x2 = app.normXAxis[i]
            y2 = newModernaPts[i]
            drawLine(x1, y1, x2, y2)

    #Drawing in the zoomed graph. 
    if app.zoomed: 
        drawRect(*app.zoomedGridPoints, align='center', fill=None, border='black')
        
        #Drawing the axis labels for zoomed in graph. 
        drawLabel('Price (in USD)', (40*app.zoomFactor - 32), app.cy, align='center', size=16, rotateAngle=270)
        drawLabel('Year', app.cx, app.cy + 290, align='center', size=16)

        # Drawing the x-axis labels for zoomed in graph. 
        for i in range(len(app.xAxisLabels)):
            drawLabel(f'{app.xAxisLabels[i]}', app.zoomedXAxis[i], 610, align='center', size=16)        

        #Drawing the y-axis labels for zoomed in graph. 
        for i in range(len(app.yAxisLabelsModerna)):
            drawLabel(f'{app.yAxisLabelsModerna[i]}', 40, app.zoomedYAxisModerna[i], align='center', size=12)

        #Drawing the zoomed points on the graph. 
        newZoomedModernaPts = scaling(pricesDict['moderna'], app.zoomedYAxisModerna[1], app.zoomedYAxisModerna[8])
        for i in range (1, len(newZoomedModernaPts)):
            x1 = app.zoomedXAxis[i-1]
            y1 = newZoomedModernaPts[i-1]
            x2 = app.zoomedXAxis[i]
            y2 = newZoomedModernaPts[i]
            drawLine(x1, y1, x2, y2)

    # Check if a point has been clicked in normal mode for Moderna to draw the pop up box. 
    if app.zoomedBoxModerna == True and app.clickedLineSegModerna != None: 
        # Draw the small pop-up box with the surrounding area zoomed in. 
        (oldX1, oldY1), (oldX2, oldY2) = app.clickedLineSegModerna
        scaledXs = scaling([oldX1, oldX2], (oldX1 + oldX2) / 2 - 75, (oldX1 + oldX2) / 2 + 75)
        scaledYs = scaling([oldY1, oldY2], (oldY1 + oldY2) / 2 - 75, (oldY1 + oldY2) / 2 + 75)
        drawRect((oldX1 + oldX2) / 2, (oldY1 + oldY2) / 2, 150, 150, align='center', fill='white', border='red')  
        
        #Drawing the zoomed in line. 
        for i in range(1, len(scaledXs)):
            newX1 = scaledXs[i - 1]
            newY1 = scaledYs[i - 1]
            newX2 = scaledXs[i]
            newY2 = scaledYs[i]
            drawLine(newX1, newY1, newX2, newY2)
            drawLabel(f"${pricesDict['moderna'][app.selectedIndexModerna]}",(oldX1 + oldX2) / 2 + 80,(oldY1 + oldY2) / 2 - 80, align='center', size=12 )

def modernaGraph_onMousePress(app, mouseX, mouseY):
    for i in range(1, len(app.normXAxis)):
        x1, y1 = app.normXAxis[i - 1], app.newModernaPts[i - 1]
        x2, y2 = app.normXAxis[i], app.newModernaPts[i]
        if x1 <= mouseX <= x2 and min(y1, y2) <= mouseY <= max(y1, y2):
            break
    app.selectedIndexModerna = i 
    app.clickedLineSegModerna = ((x1, y1), (x2, y2))
    app.zoomedBoxModerna = not app.zoomedBoxModerna

def modernaGraph_onKeyPress(app, key):
    if key == 'b':
        setActiveScreen('modernaDisplay')
    if key == 'z': 
        app.zoomed = not app.zoomed
        if app.zoomed: 
            app.zoomFactor = 1.25
        else:
            app.zoomFactor = 1