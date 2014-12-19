from array import array
from Base import Base
from Documento import Documento
from IndiceGlobal import IndiceGlobal

__author__ = 'Antonio Basilio'


class Controlador:
    """
    Quase um main
    """
    B = Base("../data/02-test.txt", "../data/02-train.txt")

    #docs = [Documento("../data/01/texto1.txt"), Documento("../data/01/texto1.txt"), Documento("../data/01/texto2.txt"), Documento("../data/01/texto3.txt"), Documento("../data/01/texto4.txt")]

    #colocar o gettest e o gettrain em uma lista unica

    #IG = IndiceGlobal(docs)
    IG = IndiceGlobal(B.getTest(), B.getTrain())
    #print IG.distancias
    #print IG.indice
