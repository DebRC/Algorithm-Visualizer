import random
import time
from tkinter import *
from Codes.Main_Window import Window
from threading import *

class START(Thread):
    def run(self):
        root=Tk()
        Window(root)
        root.mainloop()