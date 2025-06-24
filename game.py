#!/usr/bin/python
# make a character called fringledu and hate the fucker
# make human npc that is convinced they are a centaur; they wear a horse head mask at ALL times

import tkinter as tk
import json

class characterClass:
    name = "null"
    race = "null"
    profession = "null"
    sex = "null"
    height = "0"
    weight = "null"
    hairColor = "null"
    hairStyle = "null"
    eyeColor = "null"
    strn = 10
    dex = 10
    con = 10
    intel = 10
    wis = 10
    cha = 10
    equipment = []
    inventory = []
    skills = []

    def __del__(self):
        print("Destructor called")


player = characterClass()

def null():
    print("null")

def mainTextChange(newText = "", insertMethod = 'insert', clearText = 'True'):
    mainText.config(state='normal')
    if clearText:
        mainText.delete('0.0', 'end')
    mainText.insert(insertMethod, newText)
    mainText.config(state='disabled')

def loadScreen():
    mainTextChange()
    button1.config(text = "Load Game", command = loadGame())
    button2.config(text = "New Game", command = lambda: newGameName())
    button3.config(text = "Credits", command = lambda: creditsScreen())
    button4.config(text = "Options", command = lambda: options())
    button5.config(text = '')
    buttonQ.config(text = '')
    buttonW.config(text = '')
    buttonE.config(text = '')
    buttonR.config(text = '')
    buttonT.config(text = '')
    buttonA.config(text = '')
    buttonS.config(text = '')
    buttonD.config(text = '')
    buttonF.config(text = '')
    buttonG.config(text = '')
    userEntry.pack_forget()

def creditsScreen():
    with open('credits.txt') as creditsFile:
        mainTextChange(creditsFile.read())
    button1.config(text = 'Back', command = lambda: loadScreen())
    button2.config(text = '', command = null)
    button3.config(text = '', command = null)
    button4.config(text = '', command = null)
    button5.config(text = '', command = null)
    buttonQ.config(text = '', command = null)
    buttonW.config(text = '', command = null)
    buttonE.config(text = '', command = null)
    buttonR.config(text = '', command = null)
    buttonT.config(text = '', command = null)
    buttonA.config(text = '', command = null)
    buttonS.config(text = '', command = null)
    buttonD.config(text = '', command = null)
    buttonF.config(text = '', command = null)
    buttonG.config(text = '', command = null)

def options():
    #Low priority, will help user set text size, font, color, etc
    print("options worked!")
       
def loadGame():
    #There will be code here to load all locally saved files
    print("loadGame worked!")

def newGameName():
    #This will bring the player to the first character creation screen
    #starts by clearing out any save data
    global player
    del player
    player = characterClass()
    
    mainTextChange("What name would you like your character to have?")
    userEntry.pack(padx = 5, side = 'left', anchor = 'w')
    button1.config(text = 'Enter', command = lambda: inputName())
    button2.config(text = '', command = null)
    button3.config(text = '', command = null)
    button4.config(text = '', command = null)
    button5.config(text = '', command = null)
    buttonQ.config(text = '', command = null)
    buttonW.config(text = '', command = null)
    buttonE.config(text = '', command = null)
    buttonR.config(text = '', command = null)
    buttonT.config(text = '', command = null)
    buttonA.config(text = '', command = null)
    buttonS.config(text = '', command = null)
    buttonD.config(text = '', command = null)
    buttonF.config(text = '', command = null)
    buttonG.config(text = 'Back', command = lambda: loadScreen())

def inputName():
    if userEntry.get() != "":
        global player
        player.name = userEntry.get()
        userEntry.delete(0, 'end')   
        userEntry.pack_forget()
        inputRace()
    else:
        mainTextChange("Please input a name.")

def inputRace():
    #There will eventually be more races available, this will suffice for now.
    mainTextChange("What race are you?")
    button1.config(text = 'Human', command = lambda: storeRace('Human'))
    button2.config(text = 'Minotaur', command = lambda: storeRace('Minotaur'))
    button3.config(text = 'Catfolk', command = lambda: storeRace('Catfolk'))
    button4.config(text = 'Reptid', command = lambda: storeRace('Reptid'))
    button5.config(text = 'Centaur', command = lambda: storeRace('Centaur')) 
    buttonQ.config(text = 'Elf', command = lambda: storeRace('Elf'))
    buttonW.config(text = 'Dwarf', command = lambda: storeRace('Dwarf'))
    buttonE.config(text = 'Wolfkin', command = lambda: storeRace('Wolfkin'))
    buttonR.config(text = 'Wingding', command = lambda: storeRace('Wingding'))
    buttonT.config(text = 'Arborea', command = lambda: storeRace('Arborea'))
    buttonA.config(text = '', command = null)
    buttonS.config(text = '', command = null)
    buttonD.config(text = '', command = null)
    buttonF.config(text = '', command = null)   
    buttonG.config(text = 'Back', command = lambda: newGameName())
    
def storeRace(raceName):
    global player
    player.race = raceName
    if raceName == 'Human':
        print("YOU BASIC ASS BITCH")
    elif raceName == 'Minotaur':
        player.strn += 2
        player.con += 2
        player.intel -= 2
    elif raceName == 'Catfolk':
        player.dex += 2
        player.cha += 2
        player.strn -= 2
    elif raceName == 'Reptid':
        player.strn += 2
        player.dex += 2
        player.cha -= 2
    elif raceName == 'Centaur':
        player.con += 2
        player.dex += 2
        player.wis -= 2
    elif raceName == 'Elf':
        player.intel += 2
        player.wis +=2
        player.strn -= 1
        player.con -= 1
    elif raceName == 'Dwarf':
        player.str += 2
        player.con += 2
        player.wis -= 2
    elif raceName == 'Wolfkin':
        player.str += 2
        player.dex += 2
        player.intel -= 1
        player.wis -= 1
    elif raceName == 'Wingding': #Wingdings is plural
        player.dex += 3
        player.cha += 1
        player.intel -= 2
    elif raceName == 'Arborea': #Arboreas is plural
        player.con += 4
        player.dex -= 2
    inputProfession()

def inputProfession():
    #More base professions may become available, but most likely not; expansion on this is planned to be done in subclasses
    mainTextChange("What is your profession?")
    button1.config(text = 'Soldier', command = lambda: storeProfession('Soldier'))
    button2.config(text = 'Outlaw', command = lambda: storeProfession('Rogue'))
    button3.config(text = 'Scholar', command = lambda: storeProfession('Scholar'))
    button4.config(text = 'Healer', command = lambda: storeProfession('Healer'))
    button5.config(text = '', command = null)
    buttonQ.config(text = '', command = null)
    buttonW.config(text = '', command = null)
    buttonE.config(text = '', command = null)
    buttonR.config(text = '', command = null)
    buttonT.config(text = '', command = null)
    buttonA.config(text = '', command = null)
    buttonS.config(text = '', command = null)
    buttonD.config(text = '', command = null)
    buttonF.config(text = '', command = null)
    buttonG.config(text = 'Back', command = lambda: inputRace())

def storeProfession(profName):
    global player
    player.profession = profName
    inputSex()
    
def inputSex():
    #Yeah, important to character customization, and nothing else
    mainTextChange("Are you male or female?")
    button1.config(text = 'Male', command = lambda: storeSex('Male'))
    button2.config(text = 'Female', command = lambda: storeSex('Female'))
    button3.config(text = '', command = null)
    button4.config(text = '', command = null)
    button5.config(text = '', command = null)
    buttonQ.config(text = '', command = null)
    buttonW.config(text = '', command = null)
    buttonE.config(text = '', command = null)
    buttonR.config(text = '', command = null)
    buttonT.config(text = '', command = null)
    buttonA.config(text = '', command = null)
    buttonS.config(text = '', command = null)
    buttonD.config(text = '', command = null)
    buttonF.config(text = '', command = null)
    buttonG.config(text = 'Back', command = lambda: inputProfession())

def storeSex(sex):
    global player
    player.sex = sex
    inputHeight()

def inputHeight(inputFailed = False):
    if inputFailed:
        mainTextChange("This is not a valid number. Must be between 36 and 108, inclusively.")
    else:
        mainTextChange("How tall are you in inches? For reference, 6 ft (~1.8 m) is 72 inches. Heights under 3ft and over 9ft will not be accepted.")
    userEntry.pack(padx = 5, side = 'left', anchor = 'w')
    button1.config(text = 'Enter', command = lambda: storeHeight())
    button2.config(text = '', command = null)
    button3.config(text = '', command = null)
    button4.config(text = '', command = null)
    button5.config(text = '', command = null)
    buttonQ.config(text = '', command = null)
    buttonW.config(text = '', command = null)
    buttonE.config(text = '', command = null)
    buttonR.config(text = '', command = null)
    buttonT.config(text = '', command = null)
    buttonA.config(text = '', command = null)
    buttonS.config(text = '', command = null)
    buttonD.config(text = '', command = null)
    buttonF.config(text = '', command = null)
    buttonG.config(text = '', command = lambda: storeHeight())

def storeHeight():
        try:
            height = int(userEntry.get())
        except ValueError:
            inputHeight('True')
        else:
            if int(userEntry.get()) >= 32 and int(userEntry.get()) <= 108:
                player.height = userEntry.get()
                userEntry.delete(0, 'end')   
                userEntry.pack_forget()
                inputWeight()
            else:
                inputHeight('True')

def inputWeight():
    mainTextChange("What is your body's build?")
    button1.config(text = 'Heavyset', command = lambda: storeWeight('Heavyset'))
    button2.config(text = 'Large', command = lambda: storeWeight('Large'))
    button3.config(text = 'Average', command = lambda: storeWeight('Average'))
    button4.config(text = 'Lean', command = lambda: storeWeight('Lean'))
    button5.config(text = 'Thin', command = lambda: storeWeight('Thin'))
    buttonQ.config(text = '', command = null)
    buttonW.config(text = '', command = null)
    buttonE.config(text = '', command = null)
    buttonR.config(text = '', command = null)
    buttonT.config(text = '', command = null)
    buttonA.config(text = '', command = null)
    buttonS.config(text = '', command = null)
    buttonD.config(text = '', command = null)
    buttonF.config(text = '', command = null)
    buttonG.config(text = 'Back', command = lambda: inputHeight())
    
def storeWeight(weight):
    global player
    player.weight = weight
    inputHairColor()

def inputHairColor():
    global player
    if player.race != "Reptid":
        mainTextChange("What color is your hair? If you have it, your fur will be a darker shade of the same color.")
    else:
        mainTextChange("What color are your scales?")
    button1.config(text = 'Black', command = lambda: storeHairColor('Black'))
    button2.config(text = 'Brown', command = lambda: storeHairColor('Brown'))
    button3.config(text = 'Blonde', command = lambda: storeHairColor('Blonde'))
    button4.config(text = 'White', command = lambda: storeHairColor('White'))
    button5.config(text = 'Silver', command = lambda: storeHairColor('Silver'))
    buttonQ.config(text = 'Grey', command = lambda: storeHairColor('Grey'))
    buttonW.config(text = 'Red', command = lambda: storeHairColor('Red'))
    buttonE.config(text = 'Blue', command = lambda: storeHairColor('Blue'))
    buttonR.config(text = 'Yellow', command = lambda: storeHairColor('Yellow'))
    buttonT.config(text = 'Green', command = lambda: storeHairColor('Green'))
    buttonA.config(text = 'Purple', command = lambda: storeHairColor('Purple'))
    buttonS.config(text = 'Orange', command = lambda: storeHairColor('Orange'))
    buttonD.config(text = '', command = null)
    buttonF.config(text = '', command = null)
    buttonG.config(text = 'Back', command = lambda: inputWeight())

def storeHairColor(hairColor):
    global player
    player.hairColor = hairColor
    inputHairStyle()

def inputHairStyle():
    mainTextChange("What style of hair do you have?")
    button1.config(text = 'Short and straight', command = lambda: storeHairStyle('Short straight hair'))
    button2.config(text = 'Short and curly', command = lambda: storeHairStyle('Short curly hair'))
    button3.config(text = 'Long and straight', command = lambda: storeHairStyle('Long straight hair'))
    button4.config(text = 'long and curly', command = lambda: storeHairStyle('Long curly hair'))
    button5.config(text = 'Short braid', command = lambda: storeHairStyle('Short braid'))
    buttonQ.config(text = 'Long braid', command = lambda: storeHairStyle('Long braid'))
    buttonW.config(text = 'Bald', command = lambda: storeHairStyle('Bald'))
    buttonE.config(text = 'Dreadlocks', command = lambda: storeHairStyle('Dreadlocks'))
    buttonR.config(text = 'None', command = lambda: storeHairStyle('None'))
    buttonT.config(text = '', command = null)
    buttonA.config(text = '', command = null)
    buttonS.config(text = '', command = null)
    buttonD.config(text = '', command = null)
    buttonF.config(text = '', command = null)
    buttonG.config(text = 'Back', command = lambda: inputHairColor())
    
def storeHairStyle(hairStyle):
    global player
    player.hairStyle = hairStyle
    inputEyeColor()
        
def inputEyeColor():
    mainTextChange("What color are your eyes?")
    button1.config(text = 'Brown', command = lambda: storeEyeColor('Brown'))
    button2.config(text = 'Green', command = lambda: storeEyeColor('Green'))
    button3.config(text = 'Hazel', command = lambda: storeEyeColor('Hazel'))
    button4.config(text = 'Blue', command = lambda: storeEyeColor('Blue'))
    button5.config(text = 'Black', command = lambda: storeEyeColor('Black'))
    buttonQ.config(text = 'Red', command = lambda: storeEyeColor('Red'))
    buttonW.config(text = 'Silver', command = lambda: storeEyeColor('Silver'))
    buttonE.config(text = '', command = null)
    buttonR.config(text = '', command = null)
    buttonT.config(text = '', command = null)
    buttonA.config(text = '', command = null)
    buttonS.config(text = '', command = null)
    buttonD.config(text = '', command = null)
    buttonF.config(text = '', command = null)
    buttonG.config(text = 'Back', command = lambda: inputHairStyle())

def storeEyeColor(eyeColor):
    global player
    player.eyeColor = eyeColor
    checkPlayerStats()

def checkPlayerStats():
    global player
    mainTextChange("Name:         " + player.name + '\n' + \
                   "Race:         " + player.race + '\n' + \
                   "Profession:   " + player.profession + '\n' + \
                   "Sex:          " + player.sex + '\n' + \
                   "Height:       " + str(int(player.height) // 12) + "\'" + str(int(player.height) % 12) + "\"" + '\n' + \
                   "Weight:       " + player.weight + '\n' + \
                   "Hair color:   " + player.hairColor + '\n' + \
                   "Hair style:   " + player.hairStyle + '\n' + \
                   "Eye color:    " + player.eyeColor + '\n' + '\n' + \
                   "Strength:     " + str(player.strn) + '\n' + \
                   "Dexterity:    " + str(player.dex) + '\n' + \
                   "Constitution: " + str(player.con) + '\n' + \
                   "Intelligence: " + str(player.intel) + '\n' + \
                   "Wisdom:       " + str(player.wis) + '\n' + \
                   "Charisma:     " + str(player.cha))

                   
    button1.config(text = '', command = null)
    button2.config(text = '', command = null)
    button3.config(text = '', command = null)
    button4.config(text = '', command = null)
    button5.config(text = '', command = null)
    buttonQ.config(text = '', command = null)
    buttonW.config(text = '', command = null)
    buttonE.config(text = '', command = null)
    buttonR.config(text = '', command = null)
    buttonT.config(text = '', command = null)
    buttonA.config(text = '', command = null)
    buttonS.config(text = '', command = null)
    buttonD.config(text = '', command = null)
    buttonF.config(text = '', command = null)
    buttonG.config(text = '', command = null)

""" This block is the basic setup for changing the buttons
    button1.config(text = '', command = null)
    button2.config(text = '', command = null)
    button3.config(text = '', command = null)
    button4.config(text = '', command = null)
    button5.config(text = '', command = null)
    buttonQ.config(text = '', command = null)
    buttonW.config(text = '', command = null)
    buttonE.config(text = '', command = null)
    buttonR.config(text = '', command = null)
    buttonT.config(text = '', command = null)
    buttonA.config(text = '', command = null)
    buttonS.config(text = '', command = null)
    buttonD.config(text = '', command = null)
    buttonF.config(text = '', command = null)
    buttonG.config(text = '', command = null)
"""

""" This snippet returns the frame height of the party and text frames
partyFrame.update_idletasks()
print(partyFrame.winfo_reqheight())
mainTextFrame.update_idletasks()
print(mainTextFrame.winfo_reqheight())
"""

""" This snippet is an example of how to change the text widget's content
    without allowing the user to manually alter it
mainText.config(state='normal')
mainText.insert('insert', "BLEEEEH")
mainText.config(state='disabled')
"""

root = tk.Tk()
root.title("Fuckin fuck I need to name this shit")
root.geometry('1000x780')
root.config(bg = '#003300')

infoFrame = tk.Frame(root, bg = '#003300', height = 75)
infoButtonFrame = tk.Frame(infoFrame)
menuButton = tk.Button(infoFrame, bg = '#ffcc99', width = 20, height = 2, text = "Menu", command = lambda: loadScreen())
statsButton = tk.Button(infoFrame, bg = '#ffcc99', width = 20, height = 2, text = "Stats")
levelUpButton = tk.Button(infoFrame, bg = '#ffcc99', width = 20, height = 2, text = "Level Up")

mainFrame = tk.Frame(root, bg = '#003300')

partyFrame = tk.Frame(mainFrame, bg = '#003300')
partyMem1Frame = tk.Frame(partyFrame, bg = '#ffcc99', width = 250, height = 100)
partyMem2Frame = tk.Frame(partyFrame, bg = '#ffcc99', width = 250, height = 100)
partyMem3Frame = tk.Frame(partyFrame, bg = '#ffcc99', width = 250, height = 100)
partyMem4Frame = tk.Frame(partyFrame, bg = '#ffcc99', width = 250, height = 100)

mainTextFrame = tk.Frame(mainFrame, bg = '#003300')
mainText = tk.Text(mainTextFrame, bg = '#ffcc99', wrap = 'word', state = 'disabled')
userEntry = tk.Entry(mainText, width = 25)

buttonFrame = tk.Frame(root, bg = '#003300')
buttonRow1Frame = tk.Frame(buttonFrame, bg = '#003300')
buttonRow2Frame = tk.Frame(buttonFrame, bg = '#003300')
buttonRow3Frame = tk.Frame(buttonFrame, bg = '#003300')
button1 = tk.Button(buttonRow1Frame, bg = '#ffcc99', width = 20, height = 2, \
                     text = "Load Game", command = lambda: loadGame())
button2 = tk.Button(buttonRow1Frame, bg = '#ffcc99', width = 20, height = 2, \
                    text = "New Game", command = lambda: newGameName())
button3 = tk.Button(buttonRow1Frame, bg = '#ffcc99', width = 20, height = 2, \
                    text = "Credits", command = lambda: creditsScreen())
button4 = tk.Button(buttonRow1Frame, bg = '#ffcc99', width = 20, height = 2, \
                    text = "Options", command = lambda: options())
button5 = tk.Button(buttonRow1Frame, bg = '#ffcc99', width = 20, height = 2, \
                    command = null)
buttonQ = tk.Button(buttonRow2Frame, bg = '#ffcc99', width = 20, height = 2, \
                    command = null)
buttonW = tk.Button(buttonRow2Frame, bg = '#ffcc99', width = 20, height = 2, \
                    command = null)
buttonE = tk.Button(buttonRow2Frame, bg = '#ffcc99', width = 20, height = 2, \
                    command = null)
buttonR = tk.Button(buttonRow2Frame, bg = '#ffcc99', width = 20, height = 2, \
                    command = null)
buttonT = tk.Button(buttonRow2Frame, bg = '#ffcc99', width = 20, height = 2, \
                    command = null)
buttonA = tk.Button(buttonRow3Frame, bg = '#ffcc99', width = 20, height = 2, \
                    command = null)
buttonS = tk.Button(buttonRow3Frame, bg = '#ffcc99', width = 20, height = 2, \
                    command = null)
buttonD = tk.Button(buttonRow3Frame, bg = '#ffcc99', width = 20, height = 2, \
                    command = null)
buttonF = tk.Button(buttonRow3Frame, bg = '#ffcc99', width = 20, height = 2, \
                    command = null)
buttonG = tk.Button(buttonRow3Frame, bg = '#ffcc99', width = 20, height = 2, \
                    command = null)

infoFrame.pack(side = 'top', fill = 'x', padx = 5, pady = 5)

mainFrame.pack(padx = 10, pady = 10, fill = 'both', expand = '1')
partyFrame.pack(side = 'left', padx = 5, pady = 5, expand = '0', anchor = 'nw')
mainTextFrame.pack(padx = 5, ipady = 5, fill = 'both', expand = '1')

buttonFrame.pack(side = 'bottom', padx = 10, pady = 10, fill = 'x' , expand = '1', anchor = 's')
buttonRow1Frame.pack(padx = 5, pady = 5, fill = 'x' , expand = '1')
buttonRow2Frame.pack(padx = 5, pady = 5, fill = 'x' , expand = '1')
buttonRow3Frame.pack(padx = 5, pady = 5, fill = 'x' , expand = '1')

menuButton.pack(padx = 23, pady = 10, side = 'left')
statsButton.pack(padx = 23, pady = 10, side = 'left')
levelUpButton.pack(padx = 23, pady = 10, side = 'left')

partyMem1Frame.pack(padx = 10, pady = 10, ipadx = 10, ipady = 1)
partyMem2Frame.pack(padx = 10, pady = 10, ipadx = 10, ipady = 1)
partyMem3Frame.pack(padx = 10, pady = 10, ipadx = 10, ipady = 1)
partyMem4Frame.pack(padx = 10, pady = 10, ipadx = 10, ipady = 1)

mainText.pack(padx = 10, pady = 10, fill = 'both', expand = '1')

button1.pack(padx = 5, pady = 2, side = 'left', fill = 'x' , expand = '1')
button2.pack(padx = 5, pady = 2, side = 'left', fill = 'x' , expand = '1')
button3.pack(padx = 5, pady = 2, side = 'left', fill = 'x' , expand = '1')
button4.pack(padx = 5, pady = 2, side = 'left', fill = 'x' , expand = '1')
button5.pack(padx = 5, pady = 2, side = 'left', fill = 'x' , expand = '1')
buttonQ.pack(padx = 5, pady = 2, side = 'left', fill = 'x' , expand = '1')
buttonW.pack(padx = 5, pady = 2, side = 'left', fill = 'x' , expand = '1')
buttonE.pack(padx = 5, pady = 2, side = 'left', fill = 'x' , expand = '1')
buttonR.pack(padx = 5, pady = 2, side = 'left', fill = 'x' , expand = '1')
buttonT.pack(padx = 5, pady = 2, side = 'left', fill = 'x' , expand = '1')
buttonA.pack(padx = 5, pady = 2, side = 'left', fill = 'x' , expand = '1')
buttonS.pack(padx = 5, pady = 2, side = 'left', fill = 'x' , expand = '1')
buttonD.pack(padx = 5, pady = 2, side = 'left', fill = 'x' , expand = '1')
buttonF.pack(padx = 5, pady = 2, side = 'left', fill = 'x' , expand = '1')
buttonG.pack(padx = 5, pady = 2, side = 'left', fill = 'x' , expand = '1')



root.mainloop()

    




















