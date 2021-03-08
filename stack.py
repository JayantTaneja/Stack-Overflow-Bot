import webbrowser as wb
from tkinter import Tk

def bot():
    ques=Tk().clipboard_get()

    url="https://stackoverflow.com/search?q={}".format(ques)

    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

    wb.get(chrome_path).open(url)