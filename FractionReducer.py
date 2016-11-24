#Created by Gilbert Lam
#November 23, 2016
#This program simplifies fractions submitted by the user

from tkinter import *

mainWindow = Tk()

answerString = StringVar()
def calculate():
	stringInput = userInput.get().split("/")
	denom = int(stringInput[1])
	numer = int(stringInput[0])
	pos = True
	if denom == 0:
		answerString.set("Invalid Fraction!")
	else:
		if denom < 0 and numer > 0:
			denom = denom * -1
			pos = False
		elif numer < 0 and denom > 0:
			numer = numer * -1
			pos = False
		
		elif numer < 0 and denom < 0:
			denom = denom * -1
			numer = numer * -1

		if denom > numer:
			for i in range (numer, 0 , -1):
				if numer % i == 0 and denom % i == 0:
					numer = int(numer / i)
					denom = int(denom / i)
					comFac = i
					break
		else:
			for i in range (denom, 0 , -1):
				if numer % i == 0 and denom % i == 0:
					numer = int(numer / i)
					denom = int(denom / i)
					comFac = i
					break
					
		if denom == 1 and pos == True:
			answerString.set(numer)
		elif denom == 1 and pos == False:
			answerString.set(numer * -1)
		elif pos == False:
			tempString = (-1 * numer, "/",denom)
			answerString.set(tempString)
		else:
			tempString = (numer,"/",denom)
			answerString.set(tempString)
	


userPrompt = Label(mainWindow, text = "Enter a fraction here:")
userPrompt.pack()

userInput = Entry(mainWindow)
userInput.pack()

answerLabel = Label(mainWindow, text = "Calculated Result:")
answerLabel.pack()

calculatedResult = Entry(mainWindow, textvariable = answerString)
calculatedResult.pack()

submitButton = Button(mainWindow, text="Calculate!", command = calculate)
submitButton.pack()

quitButton = Button(mainWindow, text="Quit!", command = quit)
quitButton.pack()

mainWindow.mainloop()