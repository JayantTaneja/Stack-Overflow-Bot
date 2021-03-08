from docopt import docopt
import webbrowser as wb
from tkinter import Tk

def bot():
    ques=Tk().clipboard_get()

    url="https://stackoverflow.com/search?q={}".format(ques)

    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    wb.get(chrome_path).open(url)


usage = '''

StackOverFlow Bot

Usage:
  stack run
  stack help

'''
args = docopt(usage)

if args['run']:
    
    bot()

if args['help']:

    print("-----------------------------------------------------------------------\n\t\t\t\tWelcome !!")
    print("-----------------------------------------------------------------------\nThis bot is aimed to make your life easier by automatically searching")
    print("clipboard text on stackoverflow")

    print("\nHere is how to use this bot:\n")

    print("1) Simply copy an error message")
    print("2) Type 'stack run' in your terminal")
