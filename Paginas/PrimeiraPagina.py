from tkinter import *
from .PaginaBase import PaginaBase

class PrimeiraPagina(PaginaBase):
    def __init__(self, app):
        super().__init__(app.master)
        self.App = app

    def criarPagina(self):
        self.App.limparTela()
        
        self.Header = Label(text="Descrição do Dispositivo")
        self.Header.config(font = ("Courier New", 14))
        self.Header.place(x=170, y=20)

        # Nome
        self.Nome = Label(text="Nome do Técnico:")
        self.Nome.place(x=15, y=70)
        entradaNome = Entry(bd=5)
        entradaNome.place(x=150, y=70, width=200)
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('Nome', entradaNome)).place(x=360, y=70)
        self.App.infosTemp.append((self.Nome, entradaNome))

        # Data 
        self.DataH = Label(text="Data da Vistoria:")
        self.DataH.place(x=15, y=120)
        entradaData = Entry(bd=5)
        entradaData.insert(0, self.PcInfo.DataHoje())
        self.App.infosParaSalvar['DataH'] = entradaData.get()
        entradaData.place(x=150, y=120, width=200)  
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('DataH', entradaData)).place(x=360, y=120)
        self.App.infosTemp.append((self.DataH, entradaData))

        # Modelo 
        self.MarcaModelo = Label(text="Modelo:")
        self.MarcaModelo.place(x=15, y=170)
        entradaModelo = Entry(bd=5)
        entradaModelo.place(x=150, y=170, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('MarcaModelo', entradaModelo)).place(x=360, y=170)
        self.App.infosTemp.append((self.MarcaModelo, entradaModelo))

        # Número de Série
        self.Serial = Label(text="Série:")
        self.Serial.place(x=15, y=220)
        entradaSerial = Entry(bd=5)
        entradaSerial.insert(0, self.PcInfo.SerialNumber())
        self.App.infosParaSalvar['Serial'] = entradaSerial.get()
        entradaSerial.place(x=150, y=220, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('Serial', entradaSerial)).place(x=360, y=220)
        self.App.infosTemp.append((self.Serial, entradaSerial))

        ConfProblemaVar = StringVar(self.master, " ")
        ConfProblemaVar.trace("w", lambda *args: self.App.salvar('ConfProblema', ConfProblemaVar))
        self.ConfProblema = Label(self.master, text="Ocorreu Problema Durante a Conf.?")
        self.ConfProblema.place(x=15, y=270)
        rbConfProblemaS = Radiobutton(self.master, text="Sim", variable=ConfProblemaVar, value="Sim")
        rbConfProblemaS.place(x=220, y=270)
        rbConfProblemaN = Radiobutton(self.master, text="Não", variable=ConfProblemaVar, value="Não")
        rbConfProblemaN.place(x=280, y=270)
        self.App.infosTemp.append((self.ConfProblema, ConfProblemaVar))

        # Versão do Sistema Operacional
        self.SO = Label(text="Versão S.O:")
        self.SO.place(x=15, y=320)
        entradaSO = Entry(bd=5)
        entradaSO.insert(0, self.PcInfo.Winver())
        self.App.infosParaSalvar['SO'] = entradaSO.get()
        entradaSO.place(x=150, y=320, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('SO', entradaSO)).place(x=360, y=320)
        self.App.infosTemp.append((self.SO, entradaSO))
        
        self.CiteSO = Label(text="Cite os Problemas")
        self.CiteSO.place(x=15, y=370)
        entradaCiteSO = Entry(bd=5)
        entradaCiteSO.place(x=150, y=370, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('CiteSO', entradaCiteSO)).place(x=360, y=370)
        self.App.infosTemp.append((self.CiteSO, entradaCiteSO))

        self.B1 = Button(self.master, text="Próxima Página", command=self.App.segundaPagina)
        self.B1.place(x=495, y=455)