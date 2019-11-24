#!/usr/bin/env python3

# imports #
import tkinter as Tk
from tkinter import ttk

# -------------------------------------------------------------------- #
# constants #

IS_DEBUG_MODE = True

# -------------------------------------------------------------------- #
# variables #

source_file_name = ""
source_dice_ids = []

dice_words = ["ERROR"]
dice_words_count = len(dice_words)
dice_words_result = ""

# wordListLang = "en"
#randomSiteUrl = "http://www.random.org/integers/?num=30&min=1&max=6&col=5&base=10&format=plain&rnd=new"

# -------------------------------------------------------------------- #
# functions #

def debug(message):
    global IS_DEBUG_MODE

    if IS_DEBUG_MODE:
        print(message)

# START: def lookup

def lookup():

    global source_dice_ids
    global dice_words
    global dice_words_count
    global dice_words_result

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
        dice_words_result = dice_words_result + str( diceWords[n3] )
        if n3 != diceWordsCount - 1:
            dice_words_result = dice_words_result + " "

    if debugMode:
        print( str( diceWords ) )
    print( dice_words_result )

    resultValue.set( "" )
    resultValue.set( dice_words_result )

# END: def lookup

# START: def display_result

def display_result():
    var_result.set(dice_words_result)

# END: def display_result

# START: getters and setters

def get_source_file_path():
    global source_file_name
    return "data/{0}.txt".format(source_file_name)

def set_source_file_name(arg_source_file_name):
    global source_file_name
    source_file_name = arg_source_file_name
    debug("source_file_name = {0}".format(source_file_name))

def get_result_file_path():
    global source_file_name
    return "output/{0}-result.txt".format(source_file_name)

# END: getters and setters

# -------------------------------------------------------------------- #
# callbacks #

def action_load_file():
    global source_dice_ids

    set_source_file_name(var_filename.get())
    source_lines = []

    try:
        source_file = open(get_source_file_path(), 'r+')
    except IOError:
        print('error, file not found')
    else:
        with source_file:
            for line in source_file:
                source_lines.append(line.strip())

    source_dice_ids = source_lines

    debug(source_dice_ids)

    #lookup()

    display_result()

    button_save_to_file.state(["!disabled"])

def action_save_to_file():
    global dice_words_result

    try:
        resultFile = open(get_result_file_path(), 'w')
    except IOError:
        print('error, file could not be opened for writing')
    else:
        with resultFile:
            resultFile.write(dice_words_result)

# -------------------------------------------------------------------- #
# set up the GUI #

# root #
root = Tk.Tk()
root.title("easypass")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.bind('<Return>', action_load_file)

# bound variables #
var_filename = Tk.StringVar()
var_filename.set("dice-sample")
var_result = Tk.StringVar()

# main frame #
frame_main = ttk.Frame(root, padding="3 3 12 12")
frame_main.grid(column=0, row=0)
for row in range(0,1):
    frame_main.columnconfigure(row, weight=1)
for col in range(0,4):
    frame_main.rowconfigure(col, weight=1)

# row 1 #
ttk.Label(frame_main, text="File:").grid(column=1, row=1, padx=5, pady=5)
entry_filename = ttk.Entry(frame_main, width=15, textvariable=var_filename)
entry_filename.grid(column=2, row=1, padx=5, pady=5)
ttk.Label(frame_main, text=".txt").grid(column=3, row=1, padx=5, pady=5)
ttk.Button(frame_main, text="Load", command=action_load_file).grid(column=4, row=1, padx=5, pady=5)

# row 2 #
ttk.Label(frame_main, text="Result:").grid(column=1, row=2, padx=5, pady=5)
ttk.Label(frame_main, textvariable=var_result).grid(column=2, row=2, columnspan=2, padx=5, pady=5)
button_save_to_file = ttk.Button(frame_main, text="Save to file", command=action_save_to_file)
button_save_to_file.grid(column=4, row=2, padx=5, pady=5)
button_save_to_file.state(["disabled"])

# main program loop #
entry_filename.focus()
debug("Debug mode is on")
root.mainloop()

# -------------------------------------------------------------------- #
