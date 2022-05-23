from Ramo import Ramo

class ManejadorRamo:
    __listaRamos=[]
    
    def __init__(self):
        self.__listaRamos=[]
    def agregarRamo(self,ramo):
        if type(ramo)==Ramo:
            self.__listaRamos.append(ramo)
        else:
            print("No se pudo agregar")
    def buscarRamo(self,tamaño,manejador):
        
        longitud=len(self.__listaRamos)
        cantidad=manejador.cantidad()
        for i in range(cantidad):
            bandera=True
            j=0
            while j<longitud and bandera:
                
                if self.__listaRamos[j].verificarTamaño(tamaño):
                    if self.__listaRamos[j].buscarFlor(i+1):
                        bandera=not bandera
                j+=1
            if not bandera:
                manejador.mostrasFloresRamo(i+1)
    def maximaCantidad(self,num):
        maximaCantidad=0
        for i in range(len(self.__listaRamos)):
            cantidad=self.__listaRamos[i].contarFlores(num)
            if cantidad>maximaCantidad:
                maximaCantidad=cantidad
        return maximaCantidad