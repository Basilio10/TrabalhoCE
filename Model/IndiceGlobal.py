from Documento import Documento
__author__ = 'Vinicius e Antonio'



class IndiceGlobal:
    documentos = None
    distancias = None
    qtdDocumentos = None

    def __init__(self, docs):
        self.documentos = docs
        self.distancias = [[]]
        self.qtdDocumentos = 0
        self.manager()

    #Monta o indice global
    #Deve receber como parametro uma lista de documentos
    #def montaIndice(self, documentos):

        #Verifica se o parametro eh uma lista
     #   if isinstance(documentos, list):
      #      self.documentos = documentos

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
        freqA = self.documentos[a].frequencias
        freqB = self.documentos[b].frequencias

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

    def manager(self):
        self.calculaDistancias()
        self._criaMatriz(self.qtdDocumentos)



