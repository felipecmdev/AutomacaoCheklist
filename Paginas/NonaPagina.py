from tkinter import *
from .PaginaBase import PaginaBase

class NonaPagina(PaginaBase):
    def __init__(self, master, pc_info, app):
        super().__init__(master)
        self.App = app
        self.Pc_info = pc_info

    def criarPagina(self):
        self.App.limparTela()

        self.Header = Label(text="Memória")
        self.Header.config(font = ("Courier New", 14))
        self.Header.place(x=170, y=20)

        self.VIDCore = Label(text="VID Core:")	
        self.VIDCore.place(x=15, y=70)
        entradaVIDCore = Entry(bd=5)
        entradaVIDCore.place(x=220, y=70, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('VIDCore', entradaVIDCore)).place(x=430, y=70)
        self.App.infosTemp.append((self.VIDCore, entradaVIDCore))
        
        self.QtMem = Label(text="Quantidade de Memória:")
        self.QtMem.place(x=15, y=120)
        entradaQtMem = Entry(bd=5)
        entradaQtMem.place(x=220, y=120, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('QtMem', entradaQtMem)).place(x=430, y=120)
        self.App.infosTemp.append((self.QtMem, entradaQtMem))

        DefeitoPlacaMaeVar = StringVar(self.master, " ")
        DefeitoPlacaMaeVar.trace("w", lambda *args: self.App.salvar('DefeitoPlacaMae', DefeitoPlacaMaeVar))
        self.DefeitoPlacaMae = Label(self.master, text="Defeito na Placa Mãe?")
        self.DefeitoPlacaMae.place(x=15, y=170)
        rbDefeitoPlacaMaeS = Radiobutton(self.master, text="Sim", variable=DefeitoPlacaMaeVar, value="Sim")
        rbDefeitoPlacaMaeS.place(x=220, y=170)
        rbDefeitoPlacaMaeN = Radiobutton(self.master, text="Não", variable=DefeitoPlacaMaeVar, value="Não")
        rbDefeitoPlacaMaeN.place(x=280, y=170)
        self.App.infosTemp.append((self.DefeitoPlacaMae, DefeitoPlacaMaeVar))
        
        DefeitoBiosVar = StringVar(self.master, " ")
        DefeitoBiosVar.trace("w", lambda *args: self.App.salvar('DefeitoBios', DefeitoBiosVar))
        self.DefeitoBios = Label(self.master, text="Defeito na Bios?")
        self.DefeitoBios.place(x=15, y=220)
        rbDefeitoBiosS = Radiobutton(self.master, text="Sim", variable=DefeitoBiosVar, value="Sim")
        rbDefeitoBiosS.place(x=220, y=220)
        rbDefeitoBiosN = Radiobutton(self.master, text="Não", variable=DefeitoBiosVar, value="Não")
        rbDefeitoBiosN.place(x=280, y=220)
        self.App.infosTemp.append((self.DefeitoBios, DefeitoBiosVar))
        
        DefeitoMemVar = StringVar(self.master, " ")
        DefeitoMemVar.trace("w", lambda *args: self.App.salvar('DefeitoMem', DefeitoMemVar))
        self.DefeitoMem = Label(self.master, text="Defeito na memória?")
        self.DefeitoMem.place(x=15, y=270)
        rbDefeitoMemS = Radiobutton(self.master, text="Sim", variable=DefeitoMemVar, value="Sim")
        rbDefeitoMemS.place(x=220, y=270)
        rbDefeitoMemN = Radiobutton(self.master, text="Não", variable=DefeitoMemVar, value="Não")
        rbDefeitoMemN.place(x=280, y=270)
        self.App.infosTemp.append((self.DefeitoMem, DefeitoMemVar))

        self.CiteCPUGPUMem = Label(text="Cite os Problemas")
        self.CiteCPUGPUMem.place(x=15, y=320)
        entradaCiteCPUGPUMem = Entry(bd=5)
        entradaCiteCPUGPUMem.place(x=220, y=320, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('CiteCPUGPUMem', entradaCiteCPUGPUMem)).place(x=430, y=320)
        self.App.infosTemp.append((self.CiteCPUGPUMem, entradaCiteCPUGPUMem))

        self.OBS = Label(text="Observações:")
        self.OBS.place(x=15, y=370)
        entradaOBS = Entry(bd=5)
        entradaOBS.place(x=220, y=370, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('OBS', entradaOBS)).place(x=430, y=370)
        self.App.infosTemp.append((self.OBS, entradaOBS))
                
        self.B1 = Button(self.master, text="Próxima Página", command=self.App.ultimaPagina)
        self.B1.place(x=495, y=455) 

        self.B2 = Button(self.master, text="Página Anterior", command=self.App.oitavaPagina)
        self.B2.place(x=15, y=455)