from tkinter import *
from .PaginaBase import PaginaBase

class UltimaPagina(PaginaBase):
    def __init__(self, app):
        super().__init__(app.master)
        self.App = app

    def criarPagina(self):
        self.App.limparTela()

        self.Header = Label(text="Salvar no Documento")
        self.Header.config(font=("Courier New", 14))
        self.Header.place(x=170, y=20)

        self.OBS = Label(text="Observações:")
        self.OBS.place(x=15, y=70)
        entradaOBS = Entry(bd=5)
        entradaOBS.place(x=150, y=70, width=200) 
        Button(self.master, text="Salvar", command=lambda: self.App.salvar('OBS', entradaOBS)).place(x=360, y=70)
        self.App.infosTemp.append((self.OBS, entradaOBS))

        self.NomeArquivoLabel = Label(text="Nome do Arquivo:")
        self.NomeArquivoLabel.place(x=15, y=120)
        self.NomeArquivoEntry = Entry(bd=5)
        self.NomeArquivoEntry.place(x=150, y=120, width=200)

        Button(self.master, text="Salvar", command=self.salvarDocumento).place(x=360, y=120)

        self.B1 = Button(self.master, text="Página Anterior", command=self.App.nonaPagina)
        self.B1.place(x=15, y=455)

    def salvarDocumento(self):
        nome_arquivo = self.NomeArquivoEntry.get()
        if not nome_arquivo.endswith('.docx'):
            nome_arquivo += '.docx'
        self.App.salvarDocumento(nome_arquivo)

        caminho_completo = f"C:/AutomacaoChecklist/{nome_arquivo}"
        self.App.salvarDocumento(caminho_completo)