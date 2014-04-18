easypass
========

A simple program to create passphrases from diceware wordlists.

Title
=====

Version 1.0 written in Python

Description
===========

The first working version of this program.

It is written in python 3.4 and requires the Python34 (CPython) runtime environment to be installed.

It uses an external "wordlist.txt" file containing a standard English diceware wordlist. The attached .zip file contains the binaries, this "wordlist.txt" file and a sample text file for creating a passphrase (explained in the next paragraph).

To use it, you need to create a text file (.txt !) with seven rows, six of which contain a five-digit random number featuring only the numbers 1 through 6. When you launch the program you have to enter the path to this text file (using the same folder for both the file and the program executable is preferred, since then you only have to enter the filename). When entering the path omit the .txt extension since that will be added by the program.

If you launch the .py (Python source) or .pyc (Python compiled binary) files you get the GUI and the console both, so I recommend the .pyw (Python consoleless source) which only gives you the GUI.