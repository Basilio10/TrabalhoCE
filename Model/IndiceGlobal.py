from Documento import Documento
from Base import Base
import random
__author__ = 'Vinicius e Antonio Basilio'



class IndiceGlobal:
    lista_train = None
    lista_test = None
    lista_distancias = None
    lista_relacao = None

    def __init__(self, lista_test, lista_train):
        self.lista_test = lista_test
        self.lista_train = lista_train
        self.lista_distancias = []
        self.lista_relacao = []

    def calculaIndice(self, docA, docB):
        """
        Metodo responsavel por calcular a frequencia entre dois documentos
        :param docA: documento test
        :param docB: documento train
        :return: d: int
        """
        d = 0
        for palavra in docA.indice:
            if palavra in docB.indice:
                d += (docA.indice[palavra] - docB.indice[palavra]) ** 2
            else:
                d += docA.indice[palavra]**2

        for palavra in docB.indice:
            if not palavra in docA.indice:
                d += docB.indice[palavra]**2
        return d

    def calculaIndices(self):
        """
        Metodo responsavel por calcular todas as frequencias entre todos os documentos
        :return:
        """
        lista_d = []
        for docA in self.lista_test:
            for docB in self.lista_train:
                lista_d.append(self.calculaIndice(docA, docB))
            novaLista = lista_d[:]
            lista_d = []
            self.lista_distancias.append(novaLista)
        #print self.lista_distancias


    def imprimeRecomendacao(self):
        """
        Metodo responsavel por imprimir na tela o resultado do programa
        :return:
        """
        menor = []
        i = 0
        for valor in self.lista_distancias:
            menor = []
            distancia_temp = valor[:]
            distancia_temp.sort()
            for v in distancia_temp:
                if v != 0:
                    if len(menor) < 2:
                        menor.append(valor.index(v))

            self.lista_test[i].setClasse(self.lista_train[menor[0]].classe)
            print "##############################"
            print self.lista_test[i].file_path + " -> " + self.lista_test[i].classe.rstrip()
            print "------------------------------"
            print "TEXTOS MAIS PARECIDOS"
            print "------------------------------"
            for m in menor:
                print self.lista_train[m].file_path + " " + str(self.lista_distancias[i][m])

            print "------------------------------"
            print "TEXTOS ALEATORIOS DA MESMA CLASSE"
            print "------------------------------"
            ale = 0
            while ale < 2:
                numero = random.randrange(0, len(self.lista_train)-1);
                if self.lista_train[numero].classe == self.lista_train[i].classe:
                    print self.lista_train[numero].file_path + " " + str(self.lista_distancias[i][numero])
                    ale += 1
            print "\n"

            i += 1











