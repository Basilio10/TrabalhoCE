from Base import Base
from Documento import Documento
from IndiceGlobal import IndiceGlobal

__author__ = 'Antonio Basilio'


class Controlador:
    """
    Quase um main
    """
    B = Base("../data/01-test.txt", "../data/01-train.txt")
    IG = IndiceGlobal(B.getTrain())
    print IG.distancias
