from tkinter import *
from .PaginaBase import PaginaBase

class SextaPagina(PaginaBase):
    def __init__(self, master, pc_info, app, threading):
        super().__init__(master)
        self.App = app
        self.Pc_info = pc_info
        self.Threading = threading

    def criarPagina(self):
        self.App.limparTela()

        self.Header = Label(text="Disco")
        self.Header.config(font = ("Courier New", 14))
        self.Header.place(x=170, y=20)

        DiscoVar = StringVar(self.master, " ")
        DiscoVar.trace("w", lambda *args: self.App.salvar('DefeitoDisco', DiscoVar))
        self.DefeitoDisco = Label(self.master, text="Defeito no(s) Disco(s)?")
        self.DefeitoDisco.place(x=15, y=70)
        rbDiscoS = Radiobutton(self.master, text="Sim", variable=DiscoVar, value="Sim")
        rbDiscoS.place(x=220, y=70)
        rbDiscoN = Radiobutton(self.master, text="Não", variable=DiscoVar, value="Não")
        rbDiscoN.place(x=280, y=70)
        self.App.infosTemp.append((self.DefeitoDisco, DiscoVar))
        # Programas de teste
        self.TesteDisco = Button(self.master, text="Teste do Disco", command=self.run_disco_test_thread)
        self.TesteDisco.place(x=330, y=70)

        self.DefeitoSaude = Label(text="Status de Saúde")    
        self.DefeitoSaude.place(x=15, y=120)
        entradaSaude = Entry(bd=5)
        entradaSaude.place(x=220, y=120, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('DefeitoSaude', entradaSaude)).place(x=430, y=120)
        self.App.infosTemp.append((self.DefeitoSaude, entradaSaude))
        
        self.DiscoTemp = Label(text="DiscoTemp")
        self.DiscoTemp.place(x=15, y=170)
        entradaDiscoTemp = Entry(bd=5)
        entradaDiscoTemp.place(x=220, y=170, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('DiscoTemp', entradaDiscoTemp)).place(x=430, y=170)
        self.App.infosTemp.append((self.DiscoTemp, entradaDiscoTemp))

        self.HorasLigado = Label(text="Horas Ligado")
        self.HorasLigado.place(x=15, y=220)
        entradaHorasLigado = Entry(bd=5)
        entradaHorasLigado.place(x=220, y=220, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('HorasLigado', entradaHorasLigado)).place(x=430, y=220)
        self.App.infosTemp.append((self.HorasLigado, entradaHorasLigado))

        self.ModDisc = Label(text="Modelo do Disco")
        self.ModDisc.place(x=15, y=270)
        entradaModDisco = Entry(bd=5)
        entradaModDisco.place(x=220, y=270, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('ModDisc', entradaModDisco)).place(x=430, y=270)
        self.App.infosTemp.append((self.ModDisc, entradaModDisco))

        self.CiteDisco = Label(text="Cite os Problemas")
        self.CiteDisco.place(x=15, y=320)
        entradaCiteDisco = Entry(bd=5)
        entradaCiteDisco.place(x=220, y=320, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('CiteDisco', entradaCiteDisco)).place(x=430, y=320)
        self.App.infosTemp.append((self.CiteDisco, entradaCiteDisco))
        
        self.B1 = Button(self.master, text="Próxima Página", command=self.App.setimaPagina)
        self.B1.place(x=495, y=455)

        self.B2 = Button(self.master, text="Página Anterior", command=self.App.quintaPagina)
        self.B2.place(x=15, y=455)

    def run_disco_test_thread(self):
       self.Thread(target=self.Programas.open_disco).start()
