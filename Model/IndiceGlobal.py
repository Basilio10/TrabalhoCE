from Documento import Documento
__author__ = 'Vinicius e Antonio'



class IndiceGlobal:
    documentos = None
    distancias = None
    qtdDocumentos = None
    palavrasGlobal = None
    #qtdPalavras = None
    indice = None
    qtdtest = None
    test = None
    train = None

    def __init__(self, docs, train):
        self.test = docs
        self.train = train
        self.documentos = self.test + self.train
        self.distancias = [[]]
        self.qtdDocumentos = 0
        #self.qtdPalavras = 0
        self.indice = []
        self.qtdtest = len(docs)
        self.manager()

    #Monta o indice global
    #Deve receber como parametro uma lista de documentos
    #def montaIndice(self, documentos):

        #Verifica se o parametro eh uma lista
     #   if isinstance(documentos, list):
      #      self.documentos = documentos

    #def calculaNumeroPalavras(self):
     #   for d in self.documentos:
            

    def calculaDistancias(self):
        self.qtdDocumentos = len(self.documentos)
        i = 0

        self._criaMatriz(self.qtdDocumentos)

        while i < self.qtdDocumentos - 1:
            j = 1
            while j < self.qtdDocumentos:
                self._calculaDistancias(i,j)
                j += 1

            i += 1

    def _calculaDistancias(self, a, b):
        freqA = self.documentos[a].indice
        freqB = self.documentos[b].indice

        palavrasDocA = self.documentos[a].palavras
        palavrasDocB = self.documentos[b].palavras

        distancia = 0

        for palavra in palavrasDocA:

            if palavra in freqB:
                distancia += pow(freqA[palavra] - freqB[palavra], 2)

            else:
                distancia += pow(freqA[palavra], 2)

        for palavra in palavrasDocB:
            if not (palavra in freqA):
                distancia += pow(freqB[palavra], 2)

        self.distancias[a][b] = distancia
        self.distancias[b][a] = distancia

    def _criaMatriz(self, tam):
        self.distancias = [[0 for x in range(tam)] for x in range(tam)]


    #Metodo que gera a saida
    def indiceDocumentos(self):
        i = 0
        for doc in self.test:
            qt = 0
            arquivo = str(doc.file_path)
            distancia = self.distancias[i]
            for dis in distancia:
                if qt < self.qtdtest:
                    distancia.pop(qt)
                    qt += 1

            dist_original = distancia[:]
            #remover os de test da lista
            distancia.sort()
            #print distancia
            menor = []

            for j in distancia:
                if j != 0:
                    if len(menor) < 2:
                        menor.append(dist_original.index(j))

            #escreve a classe no arquivo
            print "\n##############################"
            doc.setClasse(self.train[menor[0]].classe)
            print doc.file_path + " -> " + doc.classe
            print "------------------------------"
            print "TEXTOS MAIS PARECIDOS"
            print "------------------------------"
            lista = [self.train[menor[0]].file_path, dist_original[menor[0]], doc.classe.rstrip()]
            print lista
            self.indice.append(lista)
            lista = [self.train[menor[1]].file_path, dist_original[menor[1]], doc.classe.rstrip()]
            print lista
            self.indice.append(lista)
            i += 1


    def manager(self):
        self.calculaDistancias()
        #print self.distancias
        self.indiceDocumentos()




