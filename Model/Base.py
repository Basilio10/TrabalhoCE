from Documento import Documento

__author__ = 'Antonio Basilio e Vinicius'

from array import array

class Base:
    """
    Classe responsavel por gerenciar os arquivos de entrada
    """
    arquivosTest = None
    arquivosTrain = None
    test = None
    train = None
    arquivo = None
    pathArquivosTest = ""
    pathArquivosTrain = ""

    def __init__(self, pathTest, pathTrain):
        self.arquivosTest = array
        self.arquivosTrain = array
        self.test = []
        self.train = []
        self.pathArquivosTest = pathTest
        self.pathArquivosTrain = pathTrain
        self.manager()

    def lerArquivo(self, path):
        """
        Metodo responsavel por ler um arquivo
        """
        texto = array
        textoFinal = array
        try:
            self.arquivo = open(path, "r")
            if self.arquivo:
                texto = self.arquivo.readlines()
                self.arquivo.close()
                return texto
        except:
            print ("Ocorreu um erro ao tentar ler o arquivo!")
            return False


    def listaTest(self):
        """
        le o arquivo que contem os arquivos test que deverao ser lidos
        """
        self.arquivosTest = self.lerArquivo(self.pathArquivosTest)

    def listaTrain(self):
        """
        le o arquivo que contem os arquivos train que deverao ser lidos
        """
        self.arquivosTrain = self.lerArquivo(self.pathArquivosTrain)


    def montaTest(self):
        """
        #Monta uma lista com os documentos test
        """
        for path in self.arquivosTest:
            caminho = path.split(" ")
            D = Documento("../" + caminho[0])
            self.test.append(D)

    def montaTrain(self):
        """
        #Monta uma lista com os documentos train
        """
        for path in self.arquivosTrain:
            caminho = path.split(" ")
            D = Documento("../" + caminho[0])
            D.setClasse(caminho[1])
            self.train.append(D)

    def manager(self):
        """
        Manager da classe
        """
        self.listaTest()
        self.listaTrain()
        self.montaTest()
        self.montaTrain()

    def getTest(self):
        return self.test


    def getTrain(self):
        return self.train


