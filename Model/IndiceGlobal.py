from Model import Documento
__author__ = 'Vinícius e Antonio'



class IndiceGlobal:
    Documentos = None
    Distancias = None

    def __init__(self):
        self.Documentos = []
        self.Distancias = [[]]

    #Monta o índice global
    #Deve receber como parâmetro uma lista de documentos
    def montaIndice(self, documentos):

        #Verifica se o parâmetro é uma lista
        if isinstance(documentos, list):
            self.Documentos = documentos

    def calculaDistancias(self):
        qtdDocumentos = len(self.Documentos)
        i = 0

        self._criaMatriz(qtdDocumentos)

        while i < qtdDocumentos - 1:
            j = 1
            while j < qtdDocumentos:
                self._calculaDistancias(i,j)
                j += 1

            i += 1

    def _calculaDistancias(self, a, b):
        freqA = self.Documentos[a].Frequencias
        freqB = self.Documentos[b].Frequencias

        palavrasDocA = self.Documentos[a].Palavras
        palavrasDocB = self.Documentos[b].Palavras

        distancia = 0

        for palavra in palavrasDocA:

            if palavra in freqB:
                distancia += pow(freqA[palavra] - freqB[palavra], 2)

            else:
                distancia += pow(freqA[palavra], 2)

        for palavra in palavrasDocB:
            if not (palavra in freqA):
                distancia += pow(freqB[palavra], 2)

        self.Distancias[a][b] = distancia
        self.Distancias[b][a] = distancia

    def _criaMatriz(self, tam):
        self.Distancias = [[0 for x in range(tam)] for x in range(tam)]




