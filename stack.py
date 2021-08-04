from docopt import docopt
import webbrowser as wb
from tkinter import Tk

def bot(args):
    ques=Tk().clipboard_get()

    if args['<g>']:
        url="https://www.google.com/search?q={}".format(ques)
    else:
        url="https://stackoverflow.com/search?q={}".format(ques)

    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    wb.get(chrome_path).open(url)


usage = '''

StackOverFlow Bot

Usage:
  stack run [<g>]
  stack help

'''
args = docopt(usage)

if args['run']:

    try:
        bot(args)
    except:
        print(usage)

if args['help']:

    print("-----------------------------------------------------------------------\n\t\t\t\tWelcome !!")
    print("-----------------------------------------------------------------------\nThis bot is aimed to make your life easier by automatically searching")
    print("clipboard text on stackoverflow")

    print("\nHere is how to use this bot:\n")

    print("1) Simply copy an error message")
    print("2) Type 'python stack run' in your terminal")
