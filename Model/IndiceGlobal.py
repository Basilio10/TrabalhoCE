
__author__ = 'Vinícius e Antonio'

from Documento import Documento

class IndiceGlobal:
    Documentos = []
    Distancias = [[]]


    #Monta o índice global
    #Deve receber como parâmetro uma lista de documentos
    def montaIndice(self, documentos):

        #Verifica se o parâmetro é uma lista
        if isinstance(documentos, list):
            self.Documentos = documentos

    def calculaDistancias(self):
        qtdDocumentos = len(self.Documentos)
        i = 0
        j = 0

        self.criaMatriz(qtdDocumentos)

        while i < qtdDocumentos:
            while j < qtdDocumentos:
                self.calculaDistancias(i,j)

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
            if not (palavra in palavrasDocB):
                distancia += pow(freqB[palavra], 2)

    def criaMatriz(self, tam):
        self.Distancias = [[0 for x in range(tam)] for x in range(tam)]



