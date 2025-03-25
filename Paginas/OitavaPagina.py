from tkinter import *
from .PaginaBase import PaginaBase

class OitavaPagina(PaginaBase):
    def __init__(self, master, pc_info, app):
        super().__init__(master)
        self.App = app
        self.Pc_info = pc_info

    def criarPagina(self):
        self.App.limparTela()

        self.Header = Label(text="Stress GPU")
        self.Header.config(font = ("Courier New", 14))
        self.Header.place(x=170, y=20)

        StressGPUVar = StringVar(self.master, " ")
        StressGPUVar.trace("w", lambda *args: self.App.salvar('StressGPU', StressGPUVar))
        self.StressGPU = Label(self.master, text=" Stress GPU?")
        self.StressGPU.place(x=15, y=70)
        rbStressGPUS = Radiobutton(self.master, text="Sim", variable=StressGPUVar, value="Sim")
        rbStressGPUS.place(x=220, y=70)
        rbStressGPUN = Radiobutton(self.master, text="Não", variable=StressGPUVar, value="Não")
        rbStressGPUN.place(x=280, y=70)
        self.App.infosTemp.append((self.StressGPU, StressGPUVar))
        # Programas de teste
        self.TesteStressGPU = Button(self.master, text="Teste de Stress GPU", command=self.run_gpuStress_test_thread)
        self.TesteStressGPU.place(x=330, y=70)
        self.GPUinfo = Button(self.master, text="GPU Info.", command=self.run_cpuInfo_thread)
        self.GPUinfo.place(x=470, y=70)

        self.GPUTempMin = Label(text="GPU Temp. Mínima")	
        self.GPUTempMin.place(x=15, y=120)
        entradaGPUTempMin = Entry(bd=5)
        entradaGPUTempMin.place(x=220, y=120, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('GPUTempMin', entradaGPUTempMin)).place(x=430, y=120)
        self.App.infosTemp.append((self.GPUTempMin, entradaGPUTempMin))
        
        self.GPUTempMax = Label(text="GPU Temp. Máxima")
        self.GPUTempMax.place(x=15, y=170)
        entradaGPUTempMax = Entry(bd=5)
        entradaGPUTempMax.place(x=220, y=170, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('GPUTempMax', entradaGPUTempMax)).place(x=430, y=170)
        self.App.infosTemp.append((self.GPUTempMax, entradaGPUTempMax))

        self.GPUTempMd = Label(text="GPU Temp. Média")
        self.GPUTempMd.place(x=15, y=220)
        entradaHorasLigado = Entry(bd=5)
        entradaHorasLigado.place(x=220, y=220, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('GPUTempMd', entradaHorasLigado)).place(x=430, y=220)
        self.App.infosTemp.append((self.GPUTempMd, entradaHorasLigado))

        DefeitoGPUVar = StringVar(self.master, " ")
        DefeitoGPUVar.trace("w", lambda *args: self.App.salvar('DefeitoGPU', DefeitoGPUVar))
        self.DefeitoGPU = Label(self.master, text="Defeito na GPU?")
        self.DefeitoGPU.place(x=15, y=270)
        rbDefeitoGPUS = Radiobutton(self.master, text="Sim", variable=DefeitoGPUVar, value="Sim")
        rbDefeitoGPUS.place(x=220, y=270)
        rbDefeitoGPUN = Radiobutton(self.master, text="Não", variable=DefeitoGPUVar, value="Não")
        rbDefeitoGPUN.place(x=280, y=270)
        self.App.infosTemp.append((self.DefeitoGPU, DefeitoGPUVar))
                
        self.B1 = Button(self.master, text="Página Anterior", command=self.App.setimaPagina)
        self.B1.place(x=15, y=455)

        self.B2 = Button(self.master, text="Próxima Página", command=self.App.nonaPagina)
        self.B2.place(x=495, y=455)   

    def run_gpuStress_test_thread(self):
        self.Thread(target=self.Programas.open_gpuStress).start()
    
    def run_cpuInfo_thread(self):
        self.Thread(target=self.Programas.open_cpuInfo).start()