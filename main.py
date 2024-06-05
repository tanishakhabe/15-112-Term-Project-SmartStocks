#This page will allow users to select their stock preferences. 
from cmu_graphics import *
from stockData import *
from helpers import *
from loginPg import *
from prefsPg import *
from recsPg import *
from favsPg import *
from applePg import *
from modernaPg import *
from jnjPg import *
from blockPg import *
from paypalPg import *
from boaPg import *
from elfPg import *
from pepsiPg import *
from spotifyPg import *
from atatPg import *
from PIL import Image

#CITATION: I retrieved the stock history for the graphs for each company from https://www.statmuse.com/money/questions. 
#CITATION I retrieved more details about each company for the stock descriptions and images from these links.
# https://en.wikipedia.org/wiki/Tesla,_Inc.
# https://en.wikipedia.org/wiki/Adobe
# https://en.wikipedia.org/wiki/Apple_Inc.
# https://en.wikipedia.org/wiki/Microsoft
# https://en.wikipedia.org/wiki/Moderna 
# https://en.wikipedia.org/wiki/Pfizer
# https://en.wikipedia.org/wiki/Johnson_%26_Johnson
# https://en.wikipedia.org/wiki/Block,_Inc.
# https://en.wikipedia.org/wiki/PayPal
# https://en.wikipedia.org/wiki/Bank_of_America
# https://en.wikipedia.org/wiki/E.l.f._(cosmetics)
# https://en.wikipedia.org/wiki/Costco
# https://en.wikipedia.org/wiki/PepsiCo
# https://en.wikipedia.org/wiki/Meta_Platforms
# https://en.wikipedia.org/wiki/Spotify
# https://en.wikipedia.org/wiki/AT%26T

#-------------------------------------------------------------------------------
def onAppStart(app):
    app.allUsers = []
    app.width = 600
    app.height = 700
    app.cx = app.width / 2
    app.cy = app.height / 2
    app.tech = False
    app.health = False
    app.fin = False
    app.cs = False
    app.comm = False
    app.risks = [False, False, False, False, False]
    app.prices = [False, False, False, False, False]
    app.get = False
    app.recs = None
    app.availableGraphs = ['Apple Inc.', 'Moderna Inc.', 'Johnson & Johnson', 'Block Inc.', 'PayPal Holdings Inc.', 'Bank of America Corporation', 'e.l.f. Beauty Inc.', 'PepsiCo Inc.', 'Spotify Technology S.A.', 'AT&T Inc.' ]

    #Login pg button widths and coordinates. 
    app.loginW = 300
    app.loginH = 50
    app.oldNameTyping = False
    app.oldPasswordTyping = False
    app.newNameTyping = False
    app.newPasswordTyping = False
    app.loginUsername = ''
    app.loginPassword = ''
    app.newUsername = ''
    app.newPassword = ''
    app.currUser = None

    #Prefs pg button widths and coordinates. 
    app.sectorW = 150
    app.sectorH = 35
    app.riskCoords = []
    app.priceCoords = []

#COMMON VARIABLES FOR ALL GRAPHS
    app.gridSize = 400
    app.zoomed = False
    app.zoomFactor = 1.25
    app.gridPoints = [app.cx, app.cy, app.gridSize, app.gridSize]
    app.zoomedGridPoints = [app.cx, app.cy] + [app.zoomFactor * point for point in app.gridPoints[2:]]
    app.xAxisLabels = [2019, 2020, 2021, 2022, 2023]
    app.normXAxis = scaling(app.xAxisLabels, app.cx-app.gridSize/2, app.cx + app.gridSize/2)
    app.zoomedXAxis = scaling(app.xAxisLabels, app.cx - app.gridSize*app.zoomFactor/2, app.cx + app.gridSize*app.zoomFactor/2)
    
    #APPLE
    app.yAxisLabelsApple = [0, 50, pricesDict['apple'][0], 100, 150, pricesDict['apple'][4], 200, 250, 300]
    app.normYAxisApple = scaling(app.yAxisLabelsApple, app.cy + app.gridSize/2, app.cy - app.gridSize/2)
    app.zoomedYAxisApple = scaling(app.yAxisLabelsApple, app.cy + app.gridSize*app.zoomFactor/2, app.cy - app.gridSize*app.zoomFactor/2)
    app.newApplePts = scaling(pricesDict['apple'], app.normYAxisApple[2], app.normYAxisApple[5]) 
    app.appleGraph = False
    app.clickedLineSegApple = None
    app.zoomedBoxApple = False
    app.appleFaved = False
    app.selectedIndexApple = None
    app.appleImage = Image.open('Logo Images/appleLogo.png')
    app.appleImage = CMUImage(app.appleImage)
    
    #MODERNA
    app.yAxisLabelsModerna = [0, pricesDict['moderna'][0], 50, 100, 150, 200, 250, 300, pricesDict['moderna'][2]]
    app.normYAxisModerna = scaling(app.yAxisLabelsModerna, app.cy + app.gridSize/2, app.cy - app.gridSize/2)
    app.zoomedYAxisModerna = scaling(app.yAxisLabelsModerna, app.cy + app.gridSize*app.zoomFactor/2, app.cy - app.gridSize*app.zoomFactor/2)
    app.newModernaPts = scaling(pricesDict['moderna'], app.normYAxisModerna[1], app.normYAxisModerna[8]) 
    app.modernaGraph = False
    app.clickedLineSegModerna = None
    app.zoomedBoxModerna = False
    app.modernaFaved = False
    app.selectedIndexModerna = None
    app.modernaImage = Image.open('Logo Images/modernaLogo.png')
    app.modernaImage = CMUImage(app.modernaImage)

    #JNJ
    app.yAxisLabelsJNJ = [0, 50, 100, pricesDict['jnj'][0], 150, pricesDict['jnj'][3], 200, 250, 300]
    app.normYAxisJNJ = scaling(app.yAxisLabelsJNJ, app.cy + app.gridSize/2, app.cy - app.gridSize/2)
    app.zoomedYAxisJNJ = scaling(app.yAxisLabelsJNJ, app.cy + app.gridSize*app.zoomFactor/2, app.cy - app.gridSize*app.zoomFactor/2)
    app.newJNJPts = scaling(pricesDict['jnj'], app.normYAxisJNJ[3], app.normYAxisJNJ[5]) 
    app.jnjGraph = False
    app.clickedLineSegJNJ = None
    app.zoomedBoxJNJ = False
    app.jnjFaved = False
    app.selectedIndexJNJ = None
    app.jnjImage = Image.open('Logo Images/jnjLogo.png')
    app.jnjImage = CMUImage(app.jnjImage)

    #BLOCK
    app.yAxisLabelsBlock = [0, 50, pricesDict['block'][4], 100, 150, 200, pricesDict['block'][1], 250, 300]
    app.normYAxisBlock = scaling(app.yAxisLabelsBlock, app.cy + app.gridSize/2, app.cy - app.gridSize/2)
    app.zoomedYAxisBlock = scaling(app.yAxisLabelsBlock, app.cy + app.gridSize*app.zoomFactor/2, app.cy - app.gridSize*app.zoomFactor/2)
    app.newBlockPts = scaling(pricesDict['block'], app.normYAxisBlock[2], app.normYAxisBlock[6]) 
    app.blockGraph = False
    app.clickedLineSegBlock = None
    app.zoomedBoxBlock = False
    app.blockFaved = False
    app.selectedIndexBlock = None
    app.blockImage = Image.open('Logo Images/blockLogo.png')
    app.blockImage = CMUImage(app.blockImage)

    #PAYPAL
    app.yAxisLabelsPaypal = [0, 50, pricesDict['paypal'][4], 100, 150, 200, pricesDict['paypal'][1], 250, 300]
    app.normYAxisPaypal = scaling(app.yAxisLabelsPaypal, app.cy + app.gridSize/2, app.cy - app.gridSize/2)
    app.zoomedYAxisPaypal = scaling(app.yAxisLabelsPaypal, app.cy + app.gridSize*app.zoomFactor/2, app.cy - app.gridSize*app.zoomFactor/2)
    app.newPaypalPts = scaling(pricesDict['paypal'], app.normYAxisPaypal[2], app.normYAxisPaypal[6])
    app.paypalGraph = False
    app.clickedLineSegPaypal = None
    app.zoomedBoxPaypal = False
    app.paypalFaved = False
    app.selectedIndexPaypal = None
    app.paypalImage = Image.open('Logo Images/paypalLogo.png')
    app.paypalImage = CMUImage(app.paypalImage)

    #BOA
    app.yAxisLabelsBOA = [0, pricesDict['boa'][1], pricesDict['boa'][2], 50, 100, 150, 200, 250, 300]
    app.normYAxisBOA = scaling(app.yAxisLabelsBOA, app.cy + app.gridSize/2, app.cy - app.gridSize/2)
    app.zoomedYAxisBOA = scaling(app.yAxisLabelsBOA, app.cy + app.gridSize*app.zoomFactor/2, app.cy - app.gridSize*app.zoomFactor/2)
    app.newBOAPts = scaling(pricesDict['boa'], app.normYAxisBOA[1], app.normYAxisBOA[2])
    app.boaGraph = False
    app.clickedLineSegBOA = None
    app.zoomedBoxBOA = False
    app.boaFaved = False
    app.selectedIndexBOA = None
    app.boaImage = Image.open('Logo Images/boaLogo.png')
    app.boaImage = CMUImage(app.boaImage)

    #ELF
    app.yAxisLabelsELF = [0, pricesDict['elf'][0], 50, 100, pricesDict['elf'][4], 150, 200, 250, 300,]
    app.normYAxisELF = scaling(app.yAxisLabelsELF, app.cy + app.gridSize/2, app.cy - app.gridSize/2)
    app.zoomedYAxisELF = scaling(app.yAxisLabelsELF, app.cy + app.gridSize*app.zoomFactor/2, app.cy - app.gridSize*app.zoomFactor/2)
    app.newELFPts = scaling(pricesDict['elf'], app.normYAxisELF[1], app.normYAxisELF[4])
    app.elfGraph = False
    app.clickedLineSegELF = None
    app.zoomedBoxELF = False
    app.elfFaved = False
    app.selectedIndexELF = None
    app.elfImage = Image.open('Logo Images/elfLogo.png')
    app.elfImage = CMUImage(app.elfImage)

    #PEPSI
    app.yAxisLabelsPepsi = [0, 50, 100, pricesDict['pepsi'][0], 150, pricesDict['pepsi'][3], 200, 250, 300]
    app.normYAxisPepsi = scaling(app.yAxisLabelsPepsi, app.cy + app.gridSize/2, app.cy - app.gridSize/2)
    app.zoomedYAxisPepsi = scaling(app.yAxisLabelsPepsi, app.cy + app.gridSize*app.zoomFactor/2, app.cy - app.gridSize*app.zoomFactor/2)
    app.newPepsiPts = scaling(pricesDict['pepsi'], app.normYAxisPepsi[3], app.normYAxisPepsi[5])
    app.pepsiGraph = False
    app.clickedLineSegPepsi = None
    app.zoomedBoxPepsi = False
    app.pepsiFaved = False
    app.selectedIndexPepsi = None
    app.pepsiImage = Image.open('Logo Images/pepsiLogo.png')
    app.pepsiImage = CMUImage(app.pepsiImage)

    #SPOTIFY
    app.yAxisLabelsSpotify = [0, 50, pricesDict['spotify'][3], 100, 150, 200, 250, pricesDict['spotify'][1], 300]
    app.normYAxisSpotify = scaling(app.yAxisLabelsSpotify, app.cy + app.gridSize/2, app.cy - app.gridSize/2)
    app.zoomedYAxisSpotify = scaling(app.yAxisLabelsSpotify, app.cy + app.gridSize*app.zoomFactor/2, app.cy - app.gridSize*app.zoomFactor/2)
    app.newSpotifyPts = scaling(pricesDict['spotify'], app.normYAxisSpotify[2], app.normYAxisSpotify[7])
    app.spotifyGraph = False
    app.clickedLineSegSpotify = None
    app.zoomedBoxSpotify = False
    app.spotifyFaved = False
    app.selectedIndexSpotify = None
    app.spotifyImage = Image.open('Logo Images/spotifyLogo.png')
    app.spotifyImage = CMUImage(app.spotifyImage)

    #ATAT
    app.yAxisLabelsATAT = [0, pricesDict['atat'][2], pricesDict['atat'][0], 50, 100, 150, 200, 250, 300,]
    app.normYAxisATAT = scaling(app.yAxisLabelsATAT, app.cy + app.gridSize/2, app.cy - app.gridSize/2)
    app.zoomedYAxisATAT = scaling(app.yAxisLabelsATAT, app.cy + app.gridSize*app.zoomFactor/2, app.cy - app.gridSize*app.zoomFactor/2)
    app.newATATPts = scaling(pricesDict['atat'], app.normYAxisATAT[1], app.normYAxisATAT[2])
    app.atatGraph = False
    app.clickedLineSegATAT = None
    app.zoomedBoxATAT = False
    app.atatFaved = False
    app.selectedIndexATAT= None
    app.atatImage = Image.open('Logo Images/atatLogo.png')
    app.atatImage = CMUImage(app.atatImage)

def main():
    runAppWithScreens(initialScreen='loginPg')

main()