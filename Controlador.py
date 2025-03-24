from tkinter import *
from Paginas.PrimeiraPagina import PrimeiraPagina
from Paginas.SegundaPagina import SegundaPagina
from Paginas.TerceiraPagina import TerceiraPagina
from Paginas.QuartaPagina import QuartaPagina
from Paginas.QuintaPagina import QuintaPagina
from Paginas.SextaPagina import SextaPagina
from Paginas.SetimaPagina import SetimaPagina
from Paginas.OitavaPagina import OitavaPagina
from Paginas.NonaPagina import NonaPagina
from Paginas.UltimaPagina import UltimaPagina
from Utils.Programas import Programas
from Utils.PCinfo import PCinfo
from threading import Thread
from ModCL.CriarDoc import CriarDoc

class Controlador:
    def __init__(self):
        self.master = Tk()
        self.master.geometry("400x500")
        self.master.minsize(600, 500)
        self.master.maxsize(600, 500)
        self.master.resizable(width=False, height=False)
        self.Programas = Programas()
        self.PcInfo = PCinfo()
        self.Thread = Thread()
        self.infosTemp = []
        self.infosParaSalvar = {
            'Nome': '', 'Data': '', 'Modelo': '', 'Serial': '', 'SO': '',
            'DanoTela': '', 'Moldura': '', 'Palmrest': '', 'DeadPixels': '', 'Dobradica': '', 'Tampa': '', 'CiteCarcaca': '',
            'EntradaUSB': '', 'SaidaVideo': '', 'CiteUSBVideo': '', 'Teclado': '', 'TouchPad': '', 'CiteTecladoTouchPad': '',
            'Speaker': '', 'Cam': '', 'Mic': '', 'CiteAWM': '', 'Rede': '', 'Wifi': '', 'CiteRede': '',
            'Alimentacao': '', 'Fonte': '', 'CiteFonte': '', 'Bateria': '', 'CapFabrica': '', 'CapAtual': '', 'QtCiclos': '', 'CiteBateria': '',
            'Disco': '', 'Saude': '', 'DiscoTemp': '', 'HorasLigado': '', 'ModDisco': '', 'CiteDisco': '',
            'StressCPU': '', 'CPUTempMin': '', 'CPUTempMax': '', 'CPUTempMd': '', 'DefeitoCPU': '',
            'StressGPU': '', 'GPUTempMin': '', 'GPUTempMax': '', 'GPUTempMd': '', 'DefeitoGPU': '',
            'VIDCore': '', 'QTMem': '', 'DefeitoPlacaMae': '', 'DefeitoBios': '', 'DefeitoMem': '', 'CiteCPUGPUMem': '', 'OBS': ''
        }

        # Iniciando com a primeira página
        self.primeiraPagina()

    def primeiraPagina(self):
        self.paginaAtual = PrimeiraPagina(self.master, self.PcInfo, self)
        self.paginaAtual.criarPagina()

    def segundaPagina(self):
        self.paginaAtual = SegundaPagina(self.master, self.PcInfo, self)
        self.paginaAtual.criarPagina()

    def terceiraPagina(self):
        self.paginaAtual = TerceiraPagina(self.master, self.PcInfo, self)
        self.paginaAtual.criarPagina()

    def quartaPagina(self):
        self.paginaAtual = QuartaPagina(self.master, self.PcInfo, self)
        self.paginaAtual.criarPagina()

    def quintaPagina(self):
        self.paginaAtual = QuintaPagina(self.master, self.PcInfo, self, self.Thread)
        self.paginaAtual.criarPagina()

    def sextaPagina(self):
        self.paginaAtual = SextaPagina(self.master, self.PcInfo, self, self.Thread)
        self.paginaAtual.criarPagina()

    def setimaPagina(self):
        self.paginaAtual = SetimaPagina(self.master, self.PcInfo, self, self.Thread)
        self.paginaAtual.criarPagina()

    def oitavaPagina(self):
        self.paginaAtual = OitavaPagina(self.master, self.PcInfo, self, self.Thread)
        self.paginaAtual.criarPagina()

    def nonaPagina(self):
        self.paginaAtual = NonaPagina(self.master, self.PcInfo, self)
        self.paginaAtual.criarPagina()

    def ultimaPagina(self):
        self.paginaAtual = UltimaPagina(self.master, self.PcInfo, self)
        self.paginaAtual.criarPagina()

    def salvar(self, campo, entrada):
        self.infosParaSalvar[campo] = entrada.get()

    def get_entry(self):
        for label, entry in self.infosTemp:
            campo = label.cget('text').split(':')[0]
            if campo in self.infosParaSalvar:
                self.infosParaSalvar[campo] = entry.get()

    def limparTela(self):
        for i in self.master.winfo_children():
            i.destroy()

    def salvarDocumento(self, novo_nome_arquivo):
        doc = CriarDoc()
        doc.salvarDoc(self.infosParaSalvar, novo_nome_arquivo)