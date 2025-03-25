from tkinter import *
from Utils.Programas import Programas
from Utils.PCinfo import PCinfo
import threading


class PaginaBase(Frame, Programas, PCinfo):
    def __init__(self, master):
        super().__init__(master)
        self.Programas = Programas()
        self.PcInfo = PCinfo()
        self.Thread = threading.Thread

    

     