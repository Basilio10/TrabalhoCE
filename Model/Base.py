from Documento import Documento

__author__ = 'Antonio Basilio'

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

    #le o arquivo que contem os arquivos que deverao ser lidos
    def listaTest(self):
        self.arquivosTest = self.lerArquivo(self.pathArquivosTest)

    def listaTrain(self):
        self.arquivosTrain = self.lerArquivo(self.pathArquivosTrain)

    #cria uma lista com os documentos
    def montaTest(self):
        for path in self.arquivosTest:
            caminho = path.split(" ")
            D = Documento("../" + caminho[0])
            self.test.append(D)

    def montaTrain(self):
        for path in self.arquivosTrain:
            caminho = path.split(" ")
            D = Documento("../" + caminho[0])
            self.train.append(D)

    def manager(self):
        self.listaTest()
        self.listaTrain()
        self.montaTest()
        self.montaTrain()

    def getTest(self):
        return self.test


    def getTrain(self):
        return self.train


#B = Base("../data/01-test.txt", "../data/01-train.txt")
#print B.getTest()
#print B.getTrain()


