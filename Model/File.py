from numpy.core.tests.test_multiarray import x

__author__ = 'Antonio Basilio'
# coding: utf-8
from array import array

class File:
    '''
    Classe modelo para a manipulação de arquivos .txt
    '''

    file_path = ""
    file = file
    text = ""
    words = array
    frequency = dict()


    def __init__(self, f):

        self.file_path = f

    def open_file(self, mode):
        try:
            self.file = open(self.file_path)
            return True
        except:
            print "Ocorreu um erro ao tentar abrir o arquivo!"
            return False


    def close_file(self):
        try:
            self.file.close()
        except:
            print "Não foi possível fechar o arquivo! Verifique se o seu sistema está impossibilitando este procedimento."


    def read_file(self):
        self.file = open(self.file_path, "r")
        if self.file:
            self.text = self.file.read()
            self.close_file()
            return True
        self.close_file()
        return False


    def broken_words(self):
        '''
        Método responsável por separar as palavras do texto, retornando uma lista de palavras soltas
        '''
        self.words = self.text.split(" ")

    def words_frequency(self):
        '''
        Método responsável por atribuir frequência para as palavras do texto.
        :return: dict
        '''

        for word in self.words:
            if word:
                if word in self.frequency:
                    value = self.frequency.get(word)
                    self.frequency[word] = value+1
                else:
                    self.frequency[word] = 1



f = File("../Articles/teste.txt")
f.read_file()
f.broken_words()
f.words_frequency()




