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

    def salvar(self, campo, entrada):
        self.infosParaSalvar[campo] = entrada.get()

    def get_entry(self):
        for label, entry in self.infosTemp:
            campo = label.cget('text').split(':')[0]  
            if campo in self.infosParaSalvar:
                self.infosParaSalvar[campo] = entry.get()

    def limparTela(self):
        for i in self.master.winfo_children():
            if i != self.infosParaSalvar:
                i.destroy()

     