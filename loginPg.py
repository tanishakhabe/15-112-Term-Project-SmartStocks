from cmu_graphics import *
from helpers import *

def loginPg_redrawAll(app):
    drawRect(app.cx, 30, 550, 45, align='center', fill='thistle')
    drawLabel('Welcome to Smart Stocks!', app.cx, 30, align='center', size=30, bold=True, font='monospace')
    
#RETURNING USERS: 
    drawLabel('Login with your username or password.', app.cx, app.cy - 250, align='center', size=20, bold=True, font='monospace')
    drawLabel('Enter your username: ', app.cx - 150, app.cy - 200, align = 'center', size =16, font='monospace')
    drawLabel('Enter your password: ', app.cx - 150, app.cy - 125, align = 'center', size = 16, font='monospace')
    #Drawing the textbox for returning users to enter their username. 
    drawRect(app.cx + 100, app.cy - 200, app.loginW, app.loginH, align='center', fill='thistle' if app.oldNameTyping else None, border='black' )
    drawLabel(f'{app.loginUsername}', app.cx + 100, app.cy - 200, align = 'center', size=16, font='monospace')
    #Drawing the textbox for returning users to enter their password. 
    drawRect(app.cx + 100, app.cy - 125, app.loginW, app.loginH, align = 'center', fill='thistle' if app.oldPasswordTyping else None, border='black')
    drawLabel(f'{app.loginPassword}', app.cx + 100, app.cy - 125, align = 'center', size=16, font='monospace')
    #Login button. 
    drawLabel('LOG IN', app.cx, app.cy - 50, align='center', size=20, bold=True, font='monospace')
    drawRect(app.cx, app.cy - 50, app.loginW, app.loginH, align='center', fill=None, border='black')

#NEW USERS:
    drawLabel('Or create a new account to get started.', app.cx, app.cy + 25, align = 'center', size = 20, bold =True, font='monospace')
    drawLabel('Create a new username: ', app.cx - 160, app.cy + 75, align='center', size=16, font='monospace')
    drawLabel('Create a new password: ', app.cx - 160, app.cy + 150, align='center', size=16, font='monospace')
    #Drawing the textbox for new users to enter their username. 
    drawRect(app.cx + 100, app.cy + 75, app.loginW, app.loginH, align='center', fill='thistle' if app.newNameTyping else None, border='black')
    drawLabel(f'{app.newUsername}', app.cx + 100, app.cy + 75, align='center', size=16, font='monospace')
    #Drawing the textbox for new users to enter their password.
    drawRect(app.cx + 100, app.cy + 150, app.loginW, app.loginH, align='center', fill='thistle' if app.newPasswordTyping else None, border='black')
    drawLabel(f'{app.newPassword}', app.cx + 100, app.cy + 150, align ='center', size = 16, font='monospace')
    #Create new account button.
    drawLabel('CREATE NEW ACCOUNT', app.cx, app.cy + 225, align='center', size=20, bold=True, font='monospace')
    drawRect(app.cx, app.cy + 225, app.loginW, app.loginH, align='center', fill=None, border='black')

def loginPg_onMousePress(app, mouseX, mouseY):
#RETURNING USERS: 
    if (app.cx + 100 - app.loginW / 2) <= mouseX <= (app.cx + 100 + app.loginW / 2) and (app.cy - 200 - app.loginH / 2) <= mouseY <= (app.cy - 200 + app.loginH / 2):
        app.oldNameTyping = True
        app.oldPasswordTyping = False
        app.newNameTyping = False
        app.newPasswordTyping = False

    if (app.cx + 100 - app.loginW / 2) <= mouseX <= (app.cx + 100 + app.loginW / 2) and (app.cy - 125 - app.loginH / 2) <= mouseY <= (app.cy - 125 + app.loginH / 2):
        app.oldPasswordTyping = True
        app.oldNameTyping = False
        app.newNameTyping = False
        app.newPasswordTyping = False

    if (app.cx - app.loginW / 2) <= mouseX <= (app.cx + app.loginW / 2) and (app.cy - 50 - app.loginH / 2) <= mouseY <= (app.cy - 50 + app.loginH / 2):
        print('Checking login info.')
        if checkLogin(app):
            print('Now navigating to the next pg.')
            setActiveScreen('prefsPg')

#NEW USERS: 
    if (app.cx + 100 - app.loginW / 2) <= mouseX <= (app.cx + 100 + app.loginW / 2) and (app.cy + 75 - app.loginH / 2) <= mouseY <= (app.cy + 75 + app.loginH / 2):
        app.newNameTyping = True
        app.oldNameTyping = False
        app.oldPasswordTyping = False
        app.newPasswordTyping = False

    if (app.cx + 100 - app.loginW / 2) <= mouseX <= (app.cx + 100 + app.loginW / 2) and (app.cy + 150 - app.loginH / 2) <= mouseY <= (app.cy + 150 + app.loginH / 2):
        app.newPasswordTyping = True
        app.oldNameTyping = False
        app.oldPasswordTyping = False
        app.newNameTyping = False

    if (app.cx - app.loginW / 2) <= mouseX <= (app.cx + app.loginW / 2) and (app.cy + 225 - app.loginH / 2) <= mouseY <= (app.cy + 225 + app.loginH / 2):
        User.createNewUser(app.newUsername, app.newPassword)
        resetLoginPg(app)
        

def loginPg_onKeyPress(app,key):
    if app.oldNameTyping:
        if key == 'backspace':
            app.loginUsername = app.loginUsername[:-1]
        else: 
            app.loginUsername += key
    
    if app.oldPasswordTyping:
        if key == 'backspace':
            app.loginPassword = app.loginPassword[:-1]
        else: 
            app.loginPassword += key
    
    if app.newNameTyping: 
        if key == 'backspace':
            app.newUsername = app.newUsername[:-1]
        else: 
            app.newUsername += key
    if app.newPasswordTyping:
        
        if key == 'backspace':
            app.newPassword = app.newPassword[:-1]
            
        else: 
            app.newPassword += key