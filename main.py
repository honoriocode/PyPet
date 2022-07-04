import sys
import tkinter as tk
from telinhapypet import TelinhaPypet
from pypet import Pypet

sys.setrecursionlimit(3000)

pypet = Pypet()

window = tk.Tk()
telinhapypet = TelinhaPypet(window)
window.geometry('720x480')


window.mainloop()