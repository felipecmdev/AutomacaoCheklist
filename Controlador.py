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
from threading import Thread
from ModCL.CriarDoc import CriarDoc

class Controlador:
    def __init__(self):
        self.master = Tk()
        self.master.geometry("400x500")
        self.master.minsize(600, 500)
        self.master.maxsize(600, 500)
        self.master.resizable(width=False, height=False)
        self.infosTemp = []
        self.infosParaSalvar = {
            'Nome': '', 'DataH': '', 'MarcaModelo': '', 'Serial': '', 'SO': '',
            'DanoTela': '', 'DanoMoldura': '', 'DanoPalmrest': '', 'DanoDeadPixels': '', 'DanoDobradica': '', 'DanoTampa': '', 'CiteCarcaca': '',
            'EntradaUSB': '', 'SaidaVideo': '', 'CiteUSBVideo': '', 'DefeitoTeclado': '', 'DefeitoTouchPad': '', 'CiteTecladoTouchPad': '',
            'DefeitoSpeaker': '', 'DefeitoCam': '', 'DefeitoMic': '', 'CiteAWM': '', 'DefeitoRede': '', 'DefeitoWifi': '', 'CiteRede': '',
            'DefeitoAlimentacao': '', 'DefeitoFonte': '', 'CiteFonte': '', 'DefeitoBateria': '', 'CapFabrica': '', 'CapAtual': '', 'QtCiclos': '', 'CiteBateria': '',
            'DefeitoDisco': '', 'DefeitoSaude': '', 'DiscoTemp': '', 'HorasLigado': '', 'ModDisc': '', 'CiteDisco': '',
            'StressCPU': '', 'CPUTempMin': '', 'CPUTempMax': '', 'CPUTempMd': '', 'DefeitoCPU': '',
            'StressGPU': '', 'GPUTempMin': '', 'GPUTempMax': '', 'GPUTempMd': '', 'DefeitoGPU': '',
            'TesteMem': '', 'VIDCore': '', 'QTMem': '', 'DefeitoPlacaMae': '', 'DefeitoBios': '', 'DefeitoMem': '', 'CiteCPUGPUMem': '', 'OBS': ''
        }

        # Iniciando com a primeira página
        self.primeiraPagina()

    def primeiraPagina(self):
        self.paginaAtual = PrimeiraPagina(self)
        self.paginaAtual.criarPagina()

    def segundaPagina(self):
        self.paginaAtual = SegundaPagina(self)
        self.paginaAtual.criarPagina()

    def terceiraPagina(self):
        self.paginaAtual = TerceiraPagina(self)
        self.paginaAtual.criarPagina()

    def quartaPagina(self):
        self.paginaAtual = QuartaPagina(self)
        self.paginaAtual.criarPagina()

    def quintaPagina(self):
        self.paginaAtual = QuintaPagina(self)
        self.paginaAtual.criarPagina()

    def sextaPagina(self):
        self.paginaAtual = SextaPagina(self)
        self.paginaAtual.criarPagina()

    def setimaPagina(self):
        self.paginaAtual = SetimaPagina(self)
        self.paginaAtual.criarPagina()

    def oitavaPagina(self):
        self.paginaAtual = OitavaPagina(self)
        self.paginaAtual.criarPagina()

    def nonaPagina(self):
        self.paginaAtual = NonaPagina(self)
        self.paginaAtual.criarPagina()

    def ultimaPagina(self):
        self.paginaAtual = UltimaPagina(self)
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
        Thread(target=doc.salvarDoc, args=(self.infosParaSalvar, novo_nome_arquivo)).start()