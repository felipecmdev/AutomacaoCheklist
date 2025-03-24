from tkinter import *
from .PaginaBase import PaginaBase

class QuartaPagina(PaginaBase):
    def __init__(self, master, pc_info, app):
        super().__init__(master)
        self.App = app
        self.Pc_info = pc_info

    def criarPagina(self):
        self.App.limparTela()

        self.Header = Label(text="Microfone, Câmera e Alimentação")
        self.Header.config(font = ("Courier New", 14))
        self.Header.place(x=170, y=20)

        SpeakerVar = StringVar(self.master, " ")
        SpeakerVar.trace("w", lambda *args: self.App.salvar('DefeitoSpeaker', SpeakerVar))
        self.DefeitoSpeaker = Label(self.master, text="Defeito no Speaker?")
        self.DefeitoSpeaker.place(x=15, y=70)
        rbSpeakerS = Radiobutton(self.master, text="Sim", variable=SpeakerVar, value="Sim")
        rbSpeakerS.place(x=220, y=70)
        rbSpeakerN = Radiobutton(self.master, text="Não", variable=SpeakerVar, value="Não")
        rbSpeakerN.place(x=280, y=70)
        self.App.infosTemp.append((self.DefeitoSpeaker, SpeakerVar))
        # Programas de teste
        self.TesteSpeaker = Button(self.master, text="Teste do Speaker", command=self.Programas.open_speaker)
        self.TesteSpeaker.place(x=330, y=70)

        CamVar = StringVar(self.master, " ")
        CamVar.trace("w", lambda *args: self.App.salvar('Cam', CamVar))
        self.Cam = Label(self.master, text="Defeito na Câmera?")
        self.Cam.place(x=15, y=120)
        rbCamS = Radiobutton(self.master, text="Sim", variable=CamVar, value="Sim")
        rbCamS.place(x=220, y=120)
        rbCamN = Radiobutton(self.master, text="Não", variable=CamVar, value="Não")
        rbCamN.place(x=280, y=120)
        self.App.infosTemp.append((self.Cam, CamVar))
        # Programas de teste
        self.TesteCam = Button(self.master, text="Teste da Câmera", command=self.Programas.open_cam)
        self.TesteCam.place(x=330, y=120)

        MicVar = StringVar(self.master, " ")
        MicVar.trace("w", lambda *args: self.App.salvar('DefeitoMic', MicVar))
        self.DefeitoMic = Label(self.master, text="Defeito no Microfone?")
        self.DefeitoMic.place(x=15, y=170)
        rbMicS = Radiobutton(self.master, text="Sim", variable=MicVar, value="Sim")
        rbMicS.place(x=220, y=170)
        rbMicN = Radiobutton(self.master, text="Não", variable=MicVar, value="Não")
        rbMicN.place(x=280, y=170)
        self.App.infosTemp.append((self.DefeitoMic, MicVar))
        # Programas de teste
        self.TesteMic = Button(self.master, text="Teste do Microfone", command=self.Programas.open_mic)
        self.TesteMic.place(x=330, y=170)

        self.CiteAWM = Label(text="Cite os Problemas")
        self.CiteAWM.place(x=15, y=220)
        entradaCiteAWM = Entry(bd=5)
        entradaCiteAWM.place(x=220, y=220, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('CiteAWM', entradaCiteAWM)).place(x=430, y=220)
        self.App.infosTemp.append((self.CiteAWM, entradaCiteAWM))

        RedeVar = StringVar(self.master, " ")
        RedeVar.trace("w", lambda *args: self.App.salvar('DefeitoRede', RedeVar))
        self.DefeitoRede = Label(self.master, text="Defeito na Entrada de Rede?")
        self.DefeitoRede.place(x=15, y=270)
        rbRedeS = Radiobutton(self.master, text="Sim", variable=RedeVar, value="Sim")
        rbRedeS.place(x=220, y=270)
        rbRedeN = Radiobutton(self.master, text="Não", variable=RedeVar, value="Não")
        rbRedeN.place(x=280, y=270)
        self.App.infosTemp.append((self.DefeitoRede, RedeVar))

        WifiVar = StringVar(self.master, " ")
        WifiVar.trace("w", lambda *args: self.App.salvar('DefeitoWifi', WifiVar))
        self.DefeitoWifi = Label(self.master, text="Defeito na Entrada de Wifi?")
        self.DefeitoWifi.place(x=15, y=320)
        rbWifiS = Radiobutton(self.master, text="Sim", variable=WifiVar, value="Sim")
        rbWifiS.place(x=220, y=320)
        rbWifiN = Radiobutton(self.master, text="Não", variable=WifiVar, value="Não")
        rbWifiN.place(x=280, y=320)
        self.App.infosTemp.append((self.DefeitoWifi, WifiVar))

        self.CiteRede = Label(text="Cite os Problemas")
        self.CiteRede.place(x=15, y=370)
        entradaCiteRede = Entry(bd=5)
        entradaCiteRede.place(x=220, y=370, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('CiteRede', entradaCiteRede)).place(x=430, y=370)
        self.App.infosTemp.append((self.CiteRede, entradaCiteRede))

        self.B1 = Button(self.master, text="Próxima Página", command=self.App.quintaPagina)
        self.B1.place(x=495, y=455)

        self.B2 = Button(self.master, text="Página Anterior", command=self.App.terceiraPagina)
        self.B2.place(x=15, y=455)