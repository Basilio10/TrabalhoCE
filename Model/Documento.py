# from numpy.core.tests.test_multiarray import x

__author__ = 'Antonio Basilio'
# coding: utf-8
from array import array


class Documento:
    """
    Classe modelo para a manipulacao de arquivos .txt
    """
    file_path = ""
    arquivo = None
    texto = ""
    palavras = None
    frequencias = None


    def __init__(self, f):
        self.file_path = f
        self.palavras = array
        self.frequencias = dict()
        self.manager()

    def abrir(self, mode):
        try:
            self.arquivo = open(self.file_path, mode)
            return True
        except:
            print ("Ocorreu um erro ao tentar abrir o arquivo!")
            return False


    def fechar(self):
        try:
            self.arquivo.close()
        except:
            print (
                "Nao foi possivel fechar o arquivo! Verifique se o seu sistema esta impossibilitando este procedimento.")


    def ler(self):
        self.arquivo = open(self.file_path, "r")
        if self.arquivo:
            self.texto = self.arquivo.read()
            self.fechar()
            return True
        self.fechar()
        return False


    def separaPalavras(self):

        #Metodo responsavel por separar as palavras do texto, retornando uma lista de palavras soltas

        self.palavras = self.texto.split(" ")

    def calculaFrequencia(self):

        #Metodo responsavel por atribuir frequencia para as palavras do texto.
        #:return: dict


        for palavra in self.palavras:
            if palavra:
                if palavra in self.frequencias:
                    value = self.frequencias.get(palavra)
                    self.frequencias[palavra] = value + 1
                else:
                    self.frequencias[palavra] = 1

    def getPalavras(self):
        return self.palavras

    def getChaves(self):
        return self.frequencias.keys()

    def getValores(self):
        return self.frequencias.values()

    def getItens(self):
        return self.frequencias.items()

    def manager(self):
        self.ler()
        self.separaPalavras()
        self.calculaFrequencia()

#f = Documento("../data/01/texto1.txt")
#print f.getItens()
