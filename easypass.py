from Tkinter import *

debugMode = False
sourceFileName = ""
randomSiteUrl = "http://www.random.org/integers/?num=30&min=1&max=6&col=5&base=10&format=plain&rnd=new"
diceWords = ['ERROR','ERROR','ERROR','ERROR','ERROR','ERROR']
diceWordsCount = len( diceWords )
diceWordsResult = ""
wordListLang = "en"

mainWindow = Tk()
mainWindow.title("Diceware lookup")
mainWindow.minsize(200,200)
mainWindow.geometry("400x410-260+35")
# geometry: x-size 'x' y-size '+-' x-position '+-' y-position

# START: def matchup

def matchup(argFileName):

    global debugMode
    global sourceFileName
    global diceWords
    global diceWordsCount
    global diceWordsResult

    sourceFileName = argFileName
    wordList = open('wordlist.txt', 'r')
    sourceFile = open(sourceFileName+".txt", 'r+')

    fileValues = sourceFile.readlines()
    if debugMode:
        print("fileValues as the result of file.readlines() :")
        print( str(fileValues) )
        print("\n")
    
    for n1 in range(len(fileValues)):
        if debugMode:
            print("fileValues[" + str(n1) + "] with value '" + str( fileValues[n1] ) + "'" )
        fileValues[n1] = fileValues[n1].rstrip("\n")
        if debugMode:
            print( "set to value '" + str( fileValues[n1] ) + "'" )
            print("\n")
    
    if debugMode:
        print("START: matching wordListValues to fileValues and setting diceWords")
        print("\n")
    
    wordListValues = wordList.readlines()
    
    if debugMode:
        print("wordListValues as the result of wordList.readlines() :")
        print( str( fileValues[0:10] ) )
        print("\n\n")
    
    for n2 in range( len( wordListValues ) ):
        if debugMode:
            print("wordListValues[" + str(n2) + "] with value '" + str( wordListValues[n1] ) + "'")
        wordListValues[n2] = wordListValues[n2].rstrip("\n")
        if debugMode:
            print( "set to value '" + str( wordListValues[n2] ) + "'" )
            print("\n")
        currentIndex = wordListValues[n2].split("\t", -1)[0]
        currentValue = wordListValues[n2].split("\t", -1)[1]
        if debugMode:
            print( "currentIndex = " + str( currentIndex ) )
            print( "currentValue = " + str( currentValue ) )
            print("\n")
        if fileValues.count( currentIndex ) != 0 :
            dwIndex = fileValues.index( currentIndex )
            diceWords[dwIndex] = currentValue

    sourceFile.close()
    wordList.close()
    
    for n3 in range( diceWordsCount ):
        diceWordsResult = diceWordsResult + str( diceWords[n3] )
        if n3 != diceWordsCount - 1:
            diceWordsResult = diceWordsResult + " "

    if debugMode:
        print( str( diceWords ) )
    print( diceWordsResult )

    resultValue.set( "" )
    resultValue.set( diceWordsResult )

# END: def matchup
       

# Define callback functions for specific events

def callbackLangSelected():
    global wordListLang
    wordListLang = langSelectorValue.get()

def callbackOkButtonClicked():
    if debugMode:
        print("OK button clicked")
        print("\n")
    matchup( fileNameEntryValue.get() )

def callbackSaveToFileButtonClicked():
    global sourceFileName
    global diceWordsResult
    resultFile = open( sourceFileName + "_result.txt", 'w')
    resultFile.write( diceWordsResult )
    resultFile.close()

def callbackCloseButtonClicked():
    mainWindow.destroy()


# Set up the GUI

labeledGroupLang = LabelFrame(master=mainWindow, text="Wordlist language", padx=5, pady=5)
labeledGroupLang.pack(padx=10, pady=10)

langSelectorValue = StringVar()
langSelectorRadioEn = Radiobutton(master=labeledGroupLang, text="English", variable=langSelectorValue, value="en", command=callbackLangSelected, state=ACTIVE)
langSelectorRadioEn.pack()
langSelectorRadioHu = Radiobutton(master=labeledGroupLang, text="Hungarian", variable=langSelectorValue, value="hu", command=callbackLangSelected, state=DISABLED)
langSelectorRadioHu.pack()
langSelectorRadioEn.select()

labeledGroupFile = LabelFrame(master=mainWindow, text="File", padx=5, pady=5)
labeledGroupFile.pack(padx=10, pady=10)

Label(master=labeledGroupFile, text="Enter filename for the DICE file (.txt extension):").pack()

fileNameEntryValue = StringVar()
fileNameEntryField = Entry(master=labeledGroupFile, width=70, textvariable=fileNameEntryValue)
fileNameEntryValue.set("dice_1")
fileNameEntryField.pack()

separator1 = Frame(master=labeledGroupFile, height=2, bd=1, relief=SUNKEN)
separator1.pack(fill=X, padx=5, pady=5)

okButton = Button(master=labeledGroupFile, width=70, text="OK", command=callbackOkButtonClicked)
okButton.pack()

labeledGroupResult = LabelFrame(master=mainWindow, text="Result", padx=5, pady=5)
labeledGroupResult.pack(padx=10, pady=10)

resultValue = StringVar()
resultField = Entry(master=labeledGroupResult, width=70, textvariable=resultValue)
resultValue.set("")
resultField.pack()

labeledGroupActions = LabelFrame(master=mainWindow, text="Actions", padx=5, pady=5)
labeledGroupActions.pack(padx=10, pady=10)

saveToFileButton = Button(master=labeledGroupActions, width=70, text="Save to file", command=callbackSaveToFileButtonClicked)
saveToFileButton.pack()

separator2 = Frame(master=labeledGroupActions, height=2, bd=1, relief=SUNKEN)
separator2.pack(fill=X, padx=5, pady=5)

closeButton = Button(master=labeledGroupActions, width=70, text="Close", command=callbackCloseButtonClicked)
closeButton.pack()

# Start the application

mainWindow.mainloop()
fileNameEntryField.focus_set()
