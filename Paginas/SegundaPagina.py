from tkinter import *
from .PaginaBase import PaginaBase

class SegundaPagina(PaginaBase):
    def __init__(self, master, pc_info, app):
        super().__init__(master)
        self.App = app
        self.Pc_info = pc_info

    def criarPagina(self):
        self.App.limparTela()
        self.Header = Label(text="Tela e Carcaça")
        self.Header.config(font=("Courier New", 14))
        self.Header.place(x=170, y=20)

        # Dano na Tela
        DanoTelaVar = StringVar(self.master, " ")
        DanoTelaVar.trace("w", lambda *args: self.App.salvar('DanoTela', DanoTelaVar))
        self.DanoTela = Label(self.master, text="Dano Físico na Tela?")
        self.DanoTela.place(x=15, y=70)
        rbDanoTelaS = Radiobutton(self.master, text="Sim", variable=DanoTelaVar, value="Sim")
        rbDanoTelaS.place(x=220, y=70)
        rbDanoTelaN = Radiobutton(self.master, text="Não", variable=DanoTelaVar, value="Não")
        rbDanoTelaN.place(x=280, y=70)
        self.App.infosTemp.append((self.DanoTela, DanoTelaVar))

        # Moldura da Tela
        MolduraVar = StringVar(self.master, " ")
        MolduraVar.trace("w", lambda *args: self.App.salvar('DanoMoldura', MolduraVar))
        self.DanoMoldura = Label(self.master, text="Moldura da tela com defeito?")
        self.DanoMoldura.place(x=15, y=120)
        rbMolduraS = Radiobutton(self.master, text="Sim", variable=MolduraVar, value="Sim")
        rbMolduraS.place(x=220, y=120)
        rbMolduraN = Radiobutton(self.master, text="Não", variable=MolduraVar, value="Não")
        rbMolduraN.place(x=280, y=120)
        self.App.infosTemp.append((self.DanoMoldura, MolduraVar))

        # Palmrest
        PalmrestVar = StringVar(self.master, " ")
        PalmrestVar.trace("w", lambda *args: self.App.salvar('DanoPalmrest', PalmrestVar))
        self.DanoPalmrest = Label(self.master, text="Palmrest com defeito?")
        self.DanoPalmrest.place(x=15, y=170)
        rbPalmrestS = Radiobutton(self.master, text="Sim", variable=PalmrestVar, value="Sim")
        rbPalmrestS.place(x=220, y=170)
        rbPalmrestN = Radiobutton(self.master, text="Não", variable=PalmrestVar, value="Não")
        rbPalmrestN.place(x=280, y=170)
        self.App.infosTemp.append((self.DanoPalmrest, PalmrestVar))

        # Dead Pixels
        DeadPixelsVar = StringVar(self.master, " ")
        DeadPixelsVar.trace("w", lambda *args: self.App.salvar('DanoDeadPixels', DeadPixelsVar))
        self.DanoDeadPixels = Label(self.master, text="Dead pixels, manchas ou linhas?")
        self.DanoDeadPixels.place(x=15, y=220)
        rbDeadPixelsS = Radiobutton(self.master, text="Sim", variable=DeadPixelsVar, value="Sim")
        rbDeadPixelsS.place(x=220, y=220)
        rbDeadPixelsN = Radiobutton(self.master, text="Não", variable=DeadPixelsVar, value="Não")
        rbDeadPixelsN.place(x=280, y=220)
        self.App.infosTemp.append((self.DanoDeadPixels, DeadPixelsVar))
        # Programas de teste
        self.TesteTela = Button(self.master, text="Teste de tela", command=self.Programas.open_monitor)
        self.TesteTela.place(x=330, y=220)

        # Dobradiça
        DobradicaVar = StringVar(self.master, " ")
        DobradicaVar.trace("w", lambda *args: self.App.salvar('DanoDobradica', DobradicaVar))
        self.DanoDobradica = Label(self.master, text="Dobradiça com defeito?")
        self.DanoDobradica.place(x=15, y=270)
        rbDobradicaS = Radiobutton(self.master, text="Sim", variable=DobradicaVar, value="Sim")
        rbDobradicaS.place(x=220, y=270)
        rbDobradicaN = Radiobutton(self.master, text="Não", variable=DobradicaVar, value="Não")
        rbDobradicaN.place(x=280, y=270)
        self.App.infosTemp.append((self.DanoDobradica, DobradicaVar))

        # Tampa Inferior ou Traseira
        TampaVar = StringVar(self.master, " ")
        TampaVar.trace("w", lambda *args: self.App.salvar('DanoTampa', TampaVar))
        self.DanoTampa = Label(self.master, text="Tampa inferior ou traseira com defeito?")
        self.DanoTampa.place(x=15, y=320)
        rbTampaS = Radiobutton(self.master, text="Sim", variable=TampaVar, value="Sim")
        rbTampaS.place(x=220, y=320)
        rbTampaN = Radiobutton(self.master, text="Não", variable=TampaVar, value="Não")
        rbTampaN.place(x=280, y=320)
        self.App.infosTemp.append((self.DanoTampa, TampaVar))

        self.CiteCarcaca = Label(text="Cite os Problemas")
        self.CiteCarcaca.place(x=15, y=370)
        entradaCiteCarcaca = Entry(bd=5)
        entradaCiteCarcaca.place(x=150, y=370, width=200)
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('CiteCarcaca', entradaCiteCarcaca)).place(x=360, y=370)
        self.App.infosTemp.append((self.CiteCarcaca, entradaCiteCarcaca))

        # Botões de Navegação
        self.B1 = Button(self.master, text="Próxima Página", command=self.App.terceiraPagina)
        self.B1.place(x=495, y=455)

        self.B2 = Button(self.master, text="Página Anterior", command=self.App.primeiraPagina)
        self.B2.place(x=15, y=455)