from tkinter import *
from .PaginaBase import PaginaBase

class UltimaPagina(PaginaBase):
    def __init__(self, master, pc, app):
        super().__init__(master)
        self.App = app
        self.PcInfo = pc

    def criarPagina(self):
        self.App.limparTela()

        self.Header = Label(text="Salvar no Documento")
        self.Header.config(font=("Courier New", 14))
        self.Header.place(x=170, y=20)

        self.NomeArquivoLabel = Label(text="Nome do Arquivo:")
        self.NomeArquivoLabel.place(x=15, y=70)
        self.NomeArquivoEntry = Entry(bd=5)
        self.NomeArquivoEntry.place(x=150, y=70, width=200)

        Button(self.master, text="Salvar", command=self.salvarDocumento).place(x=360, y=70)

        self.B1 = Button(self.master, text="Página Anterior", command=self.App.nonaPagina)
        self.B1.place(x=15, y=455)

    def salvarDocumento(self):
        nome_arquivo = self.NomeArquivoEntry.get()
        if not nome_arquivo.endswith('.docx'):
            nome_arquivo += '.docx'
        self.App.salvarDocumento(nome_arquivo)

        caminho_completo = f"C:/Automação Checklist/{nome_arquivo}"
        self.App.salvarDocumento(caminho_completo)