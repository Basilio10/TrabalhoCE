# from numpy.core.tests.test_multiarray import x

__author__ = 'Antonio Basilio e Vinicius'
# coding: utf-8
from array import array


class Documento:
    """
    Classe modelo para o documento
    """
    file_path = ""
    arquivo = None
    texto = ""
    palavras = None
    indice = None
    classe = ""


    def __init__(self, f):
        self.file_path = f
        self.palavras = array
        self.indice = dict()
        self.manager()


    def abrir(self, mode):
        """
        Metodo responsavel por abrir o arquivo
        """
        try:
            self.arquivo = open(self.file_path, mode)
            return True
        except:
            print ("Ocorreu um erro ao tentar abrir o arquivo!")
            return False


    def fechar(self):
        """
        Metodo responsavel por fechar o arquivo
        """
        try:
            self.arquivo.close()
        except:
            print (
                "Nao foi possivel fechar o arquivo! Verifique se o seu sistema esta impossibilitando este procedimento.")


    def ler(self):
        """
        Metodo responsavel por ler o arquivo
        """
        self.arquivo = open(self.file_path, "r")
        if self.arquivo:
            self.texto = self.arquivo.read()
            self.fechar()
            return True
        self.fechar()
        return False


    def setClasse(self, classe):
        self.classe = classe


    def separaPalavras(self):
        """
        Metodo responsavel por separar as palavras do texto, retornando uma lista de palavras soltas
        """
        self.palavras = self.texto.split(" ")

    def calculaFrequencia(self):
        """
        Metodo responsavel por atribuir frequencia para as palavras do texto.
        :return: dict
        """
        for palavra in self.palavras:
            if palavra:
                if palavra in self.indice:
                    value = self.indice.get(palavra)
                    self.indice[palavra] = value + 1
                else:
                    self.indice[palavra] = 1

    def getPalavras(self):
        return self.palavras

    def getChaves(self):
        return self.indice.keys()

    def getValores(self):
        return self.indice.values()

    def getItens(self):
        return self.indice.items()

    def manager(self):
        """
        manager da classe
        """
        self.ler()
        self.separaPalavras()
        self.calculaFrequencia()
