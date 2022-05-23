from Flor import Flor
class Ramo:
    __tamaño=''
    __flores=[]
    def __init__(self,tamaño=''):
        self.__tamaño=tamaño
        self.__flores=[]
    def agregarFlor(self,flor):
        if type(flor)==Flor:
            self.__flores.append(flor)
        else:
            print("No se agrego")
    def verificarTamaño(self,tamaño):
        resultado=False
        if self.__tamaño==tamaño:
            resultado=True
        return resultado
    def buscarFlor(self,num):
        i=0
        resultado=False
        bandera=True
        longitud=len(self.__flores)
        while i<longitud and bandera:
            if self.__flores[i].verificarNumero(num):
                bandera=not bandera
                resultado=True
            else:
                i+=1
        return resultado
    def contarFlores(self,num):
        cantidad=0
        for i in range(len(self.__flores)):
            if self.__flores[i].verificarNumero(num):
                cantidad+=1
        return cantidad