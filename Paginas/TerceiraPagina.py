from tkinter import *
from .PaginaBase import PaginaBase

class TerceiraPagina(PaginaBase):
    def __init__(self, app):
        super().__init__(app.master)
        self.App = app

    def criarPagina(self):
        self.App.limparTela()

        self.Header = Label(text="Portas USB e Saídas de Vídeo")
        self.Header.config(font = ("Courier New", 14))
        self.Header.place(x=170, y=20)

        EntradaUSBVar = StringVar(self.master, " ")
        EntradaUSBVar.trace("w", lambda *args: self.App.salvar('EntradaUSB', EntradaUSBVar))
        self.EntradaUSB = Label(self.master, text="Alguma Porta USB com Defeito?")
        self.EntradaUSB.place(x=15, y=70)
        rbEntradaUSBS = Radiobutton(self.master, text="Sim", variable=EntradaUSBVar, value="Sim")
        rbEntradaUSBS.place(x=220, y=70)
        rbEntradaUSBN = Radiobutton(self.master, text="Não", variable=EntradaUSBVar, value="Não")
        rbEntradaUSBN.place(x=280, y=70)
        self.App.infosTemp.append((self.EntradaUSB, EntradaUSBVar))

        SaidaVideoVar = StringVar(self.master, " ")
        SaidaVideoVar.trace("w", lambda *args: self.App.salvar('SaidaVideo', SaidaVideoVar))
        self.SaidaVideo = Label(self.master, text="Saída de Vídeo com Defeito?")
        self.SaidaVideo.place(x=15, y=120)
        rbSaidaVideoS = Radiobutton(self.master, text="Sim", variable=SaidaVideoVar, value="Sim")
        rbSaidaVideoS.place(x=220, y=120)
        rbSaidaVideoN = Radiobutton(self.master, text="Não", variable=SaidaVideoVar, value="Não")
        rbSaidaVideoN.place(x=280, y=120)
        self.App.infosTemp.append((self.SaidaVideo, SaidaVideoVar))

        # Citação de defeitos encontrados
        self.CiteUSBeVideo = Label(text="Cite Porta e o Defeito Encontrado")
        self.CiteUSBeVideo.place(x=15, y=170)
        entradaCiteUSBVideo = Entry(bd=5)
        entradaCiteUSBVideo.place(x=220, y=170, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('CiteUSBVideo', entradaCiteUSBVideo)).place(x=430, y=170)
        self.App.infosTemp.append((self.CiteUSBeVideo, entradaCiteUSBVideo))

        TecladoVar = StringVar(self.master, " ")
        TecladoVar.trace("w", lambda *args: self.App.salvar('DefeitoTeclado', TecladoVar))
        self.DefeitoTeclado = Label(self.master, text="Defeito no Teclado?")
        self.DefeitoTeclado.place(x=15, y=220)
        rbTecladoS = Radiobutton(self.master, text="Sim", variable=TecladoVar, value="Sim")
        rbTecladoS.place(x=220, y=220)
        rbTecladoN = Radiobutton(self.master, text="Não", variable=TecladoVar, value="Não")
        rbTecladoN.place(x=280, y=220)
        self.App.infosTemp.append((self.DefeitoTeclado, TecladoVar))
        # Programas de teste
        self.TesteTeclado = Button(self.master, text="Teste do Teclado", command=self.Programas.open_teclado)
        self.TesteTeclado.place(x=330, y=220)

        TouchPadVar = StringVar(self.master, " ")
        TouchPadVar.trace("w", lambda *args: self.App.salvar('DefeitoTouchPad', TouchPadVar))
        self.DefeitoTouchPad = Label(self.master, text="Defeito no TouchPad?")
        self.DefeitoTouchPad.place(x=15, y=270)
        rbTouchPadS = Radiobutton(self.master, text="Sim", variable=TouchPadVar, value="Sim")
        rbTouchPadS.place(x=220, y=270)
        rbTouchPadN = Radiobutton(self.master, text="Não", variable=TouchPadVar, value="Não")
        rbTouchPadN.place(x=280, y=270)
        self.App.infosTemp.append((self.DefeitoTouchPad, TouchPadVar))

        # Citação de defeitos encontrados
        self.CiteTecladoTouch = Label(text="Cite o Defeito Encontrado")
        self.CiteTecladoTouch.place(x=15, y=320)
        entradaCiteTecladoTouch = Entry(bd=5)
        entradaCiteTecladoTouch.place(x=220, y=320, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('CiteTecladoTouch', entradaCiteTecladoTouch)).place(x=430, y=320)
        self.App.infosTemp.append((self.CiteTecladoTouch, entradaCiteTecladoTouch))

        self.B1 = Button(self.master, text="Próxima Página", command=self.App.quartaPagina)
        self.B1.place(x=495, y=455)
        
        self.B2 = Button(self.master, text="Página Anterior", command=self.App.segundaPagina)
        self.B2.place(x=15, y=455)