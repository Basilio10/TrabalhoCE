from array import array
from Base import Base
from Documento import Documento
from IndiceGlobal import IndiceGlobal

__author__ = 'Antonio Basilio e Vinicius'


class Controlador:

    B = Base("../data/02-test.txt", "../data/02-train.txt")
    IG = IndiceGlobal(B.getTest(), B.getTrain())
    IG.calculaIndices()
    IG.imprimeRecomendacao()

