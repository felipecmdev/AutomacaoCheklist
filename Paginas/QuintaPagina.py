from tkinter import *
from .PaginaBase import PaginaBase
from threading import Thread

class QuintaPagina(PaginaBase):
    def __init__(self, master, pc_info, app, threading):
        super().__init__(master)
        self.App = app
        self.Pc_info = pc_info
        self.Thread = threading
        self.threading = Thread()

    def criarPagina(self):
        self.App.limparTela()

        self.Header = Label(text="Bateria e Fonte")
        self.Header.config(font = ("Courier New", 14))
        self.Header.place(x=170, y=20)

        AlimentacaoVar = StringVar(self.master, " ")
        AlimentacaoVar.trace("w", lambda *args: self.App.salvar('DefeitoAlimentacao', AlimentacaoVar))
        self.DefeitoAlimentacao = Label(self.master, text="Defeito na Alimentação?")
        self.DefeitoAlimentacao.place(x=15, y=70)
        rbAlimentacaoS = Radiobutton(self.master, text="Sim", variable=AlimentacaoVar, value="Sim")
        rbAlimentacaoS.place(x=220, y=70)
        rbAlimentacaoN = Radiobutton(self.master, text="Não", variable=AlimentacaoVar, value="Não")
        rbAlimentacaoN.place(x=280, y=70)
        self.App.infosTemp.append((self.DefeitoAlimentacao, AlimentacaoVar))

        FonteVar = StringVar(self.master, " ")
        FonteVar.trace("w", lambda *args: self.App.salvar('DefeitoFonte', FonteVar))
        self.DefeitoFonte = Label(self.master, text="Defeito na Fonte?")
        self.DefeitoFonte.place(x=15, y=120)
        rbFonteS = Radiobutton(self.master, text="Sim", variable=FonteVar, value="Sim")
        rbFonteS.place(x=220, y=120)
        rbFonteN = Radiobutton(self.master, text="Não", variable=FonteVar, value="Não")
        rbFonteN.place(x=280, y=120)
        self.App.infosTemp.append((self.DefeitoFonte, FonteVar))

        self.CiteFonte = Label(text="Cite os Problemas")
        self.CiteFonte.place(x=15, y=170)
        entradaCiteFonte = Entry(bd=5)
        entradaCiteFonte.place(x=220, y=170, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('CiteFonte', entradaCiteFonte)).place(x=430, y=170)
        self.App.infosTemp.append((self.CiteFonte, entradaCiteFonte))

        BateriaVar = StringVar(self.master, " ")
        BateriaVar.trace("w", lambda *args: self.App.salvar('DefeitoBateria', BateriaVar))
        self.DefeitoBateria = Label(self.master, text="Defeito na Bateria?")
        self.DefeitoBateria.place(x=15, y=220)
        rbBateriaS = Radiobutton(self.master, text="Sim", variable=BateriaVar, value="Sim")
        rbBateriaS.place(x=220, y=220)
        rbBateriaN = Radiobutton(self.master, text="Não", variable=BateriaVar, value="Não")
        rbBateriaN.place(x=280, y=220)
        self.App.infosTemp.append((self.DefeitoBateria, BateriaVar))
        self.TesteBateria = Button(self.master, text="Teste da Bateria", command=self.run_battery_test_thread)
        self.TesteBateria.place(x=330, y=220)

        self.CapFabrica = Label(text="Cap. de Fábrica")
        self.CapFabrica.place(x=15, y=270)
        entradaCapFabrica = Entry(bd=5)
        entradaCapFabrica.place(x=220, y=270, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('CapFabrica', entradaCapFabrica)).place(x=430, y=270)
        self.App.infosTemp.append((self.CapFabrica, entradaCapFabrica))

        self.CapAtual = Label(text="Cap. Atual")
        self.CapAtual.place(x=15, y=320)
        entradaCapAtual = Entry(bd=5)
        entradaCapAtual.place(x=220, y=320, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('CapAtual', entradaCapAtual)).place(x=430, y=320)
        self.App.infosTemp.append((self.CapAtual, entradaCapAtual))

        self.QtCiclos = Label(text="Ciclos")
        self.QtCiclos.place(x=15, y=370)
        entradaCiclos = Entry(bd=5)
        entradaCiclos.place(x=220, y=370, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('QtCiclos', entradaCiclos)).place(x=430, y=370)
        self.App.infosTemp.append((self.QtCiclos, entradaCiclos))
        
        self.CiteBateria = Label(text="Cite Problemas")
        self.CiteBateria.place(x=15, y=420)
        entradaCiteBateria = Entry(bd=5)
        entradaCiteBateria.place(x=220, y=420, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('CiteBateria', entradaCiteBateria)).place(x=430, y=420)
        self.App.infosTemp.append((self.CiteBateria, entradaCiteBateria))

        self.B1 = Button(self.master, text="Próxima Página", command=self.App.sextaPagina)
        self.B1.place(x=495, y=455)
        
        self.B2 = Button(self.master, text="Página Anterior", command=self.App.quartaPagina)
        self.B2.place(x=15, y=455)

    def run_battery_test_thread(self):
        Thread(target=self.Programas.open_battery).start()