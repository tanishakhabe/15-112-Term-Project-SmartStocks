from cmu_graphics import * 

#Creating a class called user to store the user information. 
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.sector = set()
        self.risk = 0
        self.minPrice = 0
        self.maxPrice = 0
        self.favorites = []

    def __repr__(self):
        return f'{self.username}'

    def createNewUser(username, password):
        newUser = User(username=username, password=password)
        app.allUsers.append(newUser)
        print(app.allUsers)

#-------------------------------------------------------------------------------
#Stock recommendation algorithm. 
def filterStocks(user, stocksList): 
    recsList = []
    for stock in stocksList:
        if (stock.sector in user.sector and stock.risk == user.risk) or (stock.sector in user.sector and user.minPrice <= stock.price <= user.maxPrice):
            recsList.append(stock)
    return recsList
#-------------------------------------------------------------------------------
# CITATION: I got some background information for the feature graph scaling algorithm from https://www.atoti.io/articles/when-to-perform-a-feature-scaling/
def scaling(xCoords, start, end):
    newCoords = []
    minVal = min(xCoords)
    maxVal = max(xCoords)

    if maxVal == minVal: 
        return [start] * len(xCoords)

    for coord in xCoords:
        numerator = (coord - minVal) * (end - start)
        denominator = maxVal - minVal
        final = start + numerator / denominator
        newCoords.append(final)
    return newCoords
#-------------------------------------------------------------------------------
#Function to reset the stock preferences page. 
def resetPrefsPg(app):
    app.tech = False
    app.health = False
    app.fin = False
    app.cs = False
    app.comm = False
    app.risks = [False, False, False, False, False]
    app.prices = [False, False, False, False, False]
    app.get = False
    app.recs = None
#-------------------------------------------------------------------------------

#Function to log out which resets the login page. 
def resetLoginPg(app):
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

#-------------------------------------------------------------------------------
#Function to check login credentials. 
def checkLogin(app):
    for user in app.allUsers:
        if app.loginUsername == user.username and app.loginPassword == user.password:
            print(f'Login successful for user {app.loginUsername}')
            app.currUser = user
            print(f'The current user is {app.currUser}')
            return True
    print('Invalid username or password')
    return False

#-------------------------------------------------------------------------------
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5