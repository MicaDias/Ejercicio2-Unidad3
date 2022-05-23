import csv,numpy as np
from Flor import Flor
from ManejadorRamo import ManejadorRamo
class ManejadorFlor:
    __dimension=0
    __cantidad=0
    __incremento=0
    __flores=None
    def __init__(self,dimension=0,incremento=5):
        self.__flores=np.empty(dimension,dtype=Flor)
        self.__cantidad=0
        self.__dimension=dimension
        self.__incremento=incremento
    def agregarFlor(self,flor):
        if self.__cantidad==self.__dimension:
            self.__dimension+=self.__incremento
            self.__flores.resize(self.__dimension)
        self.__flores[self.__cantidad]=flor
        self.__cantidad+=1

    def cargarArchivo(self):
        archivo=open("flores.csv")
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
            nombre=fila[0]
            color=fila[1]
            descripcion=fila[2]
            flor=Flor(nombre,color,descripcion)
            self.agregarFlor(flor)
        archivo.close()
    def mostrasFlores(self):
        for i in range(self.__cantidad):
            print(self.__flores[i])
    def buscarFlor(self,num):
        i=0
        bandera=True
        resultado=-1
        while i<self.__cantidad and bandera:
            if self.__flores[i].verificarNumero(num):
                bandera=not bandera
                resultado=self.__flores[i]
            
            i+=1
        return resultado
    def cantidad(self):
        return self.__cantidad
    def buscarFlorRamo(self,num):
        i=0
        bandera=True
        resultado=-1
        while i<self.__cantidad and bandera:
            if self.__flores[i].verificarNumero(num):
                bandera=not bandera
            else:
                i+=1
        if not bandera:
            resultado=i
        return resultado
    def mostrasFloresRamo(self,num):
        pos=self.buscarFlorRamo(num)
        if pos!=-1:
            print(self.__flores[pos])
        else:
            print("No se encontro el numero")
    def redimensionar(self):
        self.__flores.resize(self.__dimension)
    def verificarDimension(self):
        if self.__dimension!=self.__cantidad:
            self.__dimension=self.__cantidad
            self.redimensionar()
    def ordenarArreglo(self):
        for i in range(self.__cantidad):
            min=i
            for j in range(i+1,self.__cantidad):
                if self.__flores[j].numero()<self.__flores[min].numero():
                    min=j
            aux=self.__flores[i]
            self.__flores[i]=self.__flores[min]
            self.__flores[min]=aux
    def floresVendidas(self,manejadorRamo): 
        print("******Flores mas vendidas******")
        self.verificarDimension()
        cantidad=0
        if self.__cantidad>5:
            cantidad=5
        else:
            cantidad=self.__cantidad
        for i in range(self.__cantidad):
            cantidadMaxima=manejadorRamo.maximaCantidad(i+1)
            self.__flores[i].setCantidad(cantidadMaxima)
            self.__flores[::-1].sort()  
        i=0
        bandera=True
        while i<cantidad and bandera:
            if self.__flores[i].getCantidad()==0:
                bandera=False
            else:
                print(self.__flores[i])
                i+=1
        self.ordenarArreglo()