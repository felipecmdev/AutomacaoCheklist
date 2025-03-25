from tkinter import *
from .PaginaBase import PaginaBase

class SetimaPagina(PaginaBase):
    def __init__(self, app):
        super().__init__(app.master)
        self.App = app

    def criarPagina(self):
        self.App.limparTela()

        self.Header = Label(text="Stress CPU")
        self.Header.config(font = ("Courier New", 14))
        self.Header.place(x=170, y=20)

        StressCPUVar = StringVar(self.master, " ")
        StressCPUVar.trace("w", lambda *args: self.App.salvar('StressCPU', StressCPUVar))
        self.StressCPU = Label(self.master, text="Stress CPU?")
        self.StressCPU.place(x=15, y=70)
        rbS = Radiobutton(self.master, text="Sim", variable=StressCPUVar, value="Sim")
        rbS.place(x=220, y=70)
        rbN = Radiobutton(self.master, text="Não", variable=StressCPUVar, value="Não")
        rbN.place(x=280, y=70)
        self.App.infosTemp.append((self.StressCPU, StressCPUVar))
        # Programas de teste
        self.TesteStressCPU = Button(self.master, text="Teste de Stress CPU", command=self.run_cpuMEM_test_thread)
        self.TesteStressCPU.place(x=330, y=70)
        self.CPUinfo = Button(self.master, text="CPU Info.", command=self.run_cpuInfo_thread)
        self.CPUinfo.place(x=470, y=70)

        self.CPUTempMin = Label(text="CPU Temp. Mínima")	
        self.CPUTempMin.place(x=15, y=120)
        entradaCPUTempMin = Entry(bd=5)
        entradaCPUTempMin.place(x=220, y=120, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('CPUTempMin', entradaCPUTempMin)).place(x=430, y=120)
        self.App.infosTemp.append((self.CPUTempMin, entradaCPUTempMin))
        
        self.CPUTempMax = Label(text="CPU Temp. Máxima")
        self.CPUTempMax.place(x=15, y=170)
        entradaCPUTempMax = Entry(bd=5)
        entradaCPUTempMax.place(x=220, y=170, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('CPUTempMax', entradaCPUTempMax)).place(x=430, y=170)
        self.App.infosTemp.append((self.CPUTempMax, entradaCPUTempMax))

        self.CPUTempMd = Label(text="CPU Temp. Média")
        self.CPUTempMd.place(x=15, y=220)
        entradaHorasLigado = Entry(bd=5)
        entradaHorasLigado.place(x=220, y=220, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('CPUTempMd', entradaHorasLigado)).place(x=430, y=220)
        self.App.infosTemp.append((self.CPUTempMd, entradaHorasLigado))

        DefeitoCPUVar = StringVar(self.master, " ")
        DefeitoCPUVar.trace("w", lambda *args: self.App.salvar('DefeitoCPU', DefeitoCPUVar))
        self.DefeitoCPU = Label(self.master, text="Defeito na CPU?")
        self.DefeitoCPU.place(x=15, y=270)
        rbDefeitoCPUS = Radiobutton(self.master, text="Sim", variable=DefeitoCPUVar, value="Sim")
        rbDefeitoCPUS.place(x=220, y=270)
        rbDefeitoCPUN = Radiobutton(self.master, text="Não", variable=DefeitoCPUVar, value="Não")
        rbDefeitoCPUN.place(x=280, y=270)
        self.App.infosTemp.append((self.DefeitoCPU, DefeitoCPUVar))
        
        self.B1 = Button(self.master, text="Próxima Página", command=self.App.oitavaPagina)
        self.B1.place(x=495, y=455)
        
        self.B2 = Button(self.master, text="Página Anterior", command=self.App.sextaPagina)
        self.B2.place(x=15, y=455)

    def run_cpuMEM_test_thread(self):
        self.Thread(target=self.Programas.open_cpuMEM).start()

    def run_cpuInfo_thread(self):
        self.Thread(target=self.Programas.open_cpuInfo).start()