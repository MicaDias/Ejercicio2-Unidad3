class Flor:
    __numero=0
    __numeroFlor=0
    __nombre=''
    __color=''
    __descripcion=''
    __cantidad=0
    @classmethod
    def getNumero(cls):
        cls.__numero+=1
        return cls.__numero
    def __init__(self,nombre='',color='',descripcion='',cantidad=0):
        self.__numeroFlor=self.getNumero()
        self.__nombre=nombre
        self.__color=color
        self.__descripcion=descripcion
        self.__cantidad=cantidad
    def __str__(self):
        return '{}, {},color:{}'.format(self.__numeroFlor,self.__nombre,self.__color,self.__descripcion)
    
    def verificarNumero(self,num):
        resultado=False
        if self.__numeroFlor==num:
            resultado=True
        return resultado
    def getNombre(self):
        return self.__nombre
    def setCantidad(self,cantidad):
        self.__cantidad=cantidad
    def getCantidad(self):
        return self.__cantidad
    def __gt__(self,otro):
        resultado=False
        if type(otro)==Flor:
            resultado=self.__cantidad>otro.getCantidad()
        return resultado
    def numero(self):
        return self.__numeroFlor