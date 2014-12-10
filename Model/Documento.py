#from numpy.core.tests.test_multiarray import x

__author__ = 'Antonio Basilio'
# coding: utf-8
from array import array

class Documento:
    '''
    Classe modelo para a manipulação de arquivos .txt
    '''

    file_path = ""
    Arquivo = None
    Texto = ""
    Palavras = None
    Frequencias = None


    def __init__(self, f):

        self.file_path = f
        self.Palavras = []
        self.Frequencias = dict()

    def abrir(self, mode):
        try:
            self.Arquivo = open(self.file_path, "r")
            return True
        except:
            print ("Ocorreu um erro ao tentar abrir o arquivo!")
            return False


    def fechar(self):
        try:
            self.Arquivo.close()
        except:
            print ("Não foi possível fechar o arquivo! Verifique se o seu sistema está impossibilitando este procedimento.")


    def ler(self):
        if self.Arquivo:
            self.Texto = self.Arquivo.read()
            self.fechar()
            return True
        self.fechar()
        return False


    def separaPalavras(self):

        #Método responsável por separar as palavras do texto, retornando uma lista de palavras soltas

        self.Palavras = self.Texto.split(" ")

    def calculaFrequencia(self):

        #Método responsável por atribuir frequência para as palavras do texto.
        #:return: dict


        for word in self.Palavras:
            if word:
                if word in self.Frequencias:
                    value = self.Frequencias.get(word)
                    self.Frequencias[word] = value+1
                else:
                    self.Frequencias[word] = 1