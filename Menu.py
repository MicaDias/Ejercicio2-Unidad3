from Ramo import Ramo
class Menu:
    __opciones={}
    def __init__(self):
        self.__opciones={
            1:self.opcion1,
            2:self.opcion2,
            3:self.opcion3,
            4:self.salir
        }
    def lanzarMenu(self,manejador,manejadorRamo):
        #Menu opciones
        i=len(self.__opciones)
        opcion=0
        while(i!=opcion):
            print('Menu:')
            print('-Ingrese 1:Registrar Ramo.')
            print('-Ingrese 2: Mostrar el nombre de las 5 flores mas vendidas.')
            print('-Ingrese 3: Mostrar flores.')
            print('-Ingrese 4 para salir.')
            opcion=self.cargarNumeroEntero('Ingrese opcion:\n')
            ejecutar=self.__opciones.get(opcion,self.error)
            if opcion>0 and opcion<5:
                ejecutar(manejador,manejadorRamo)
            else:
                ejecutar()
    def opcion1(self,manejador,manejadorRamo):
        tamaño=''
        print("TAMAÑO DE RAMOS: 1)-chico, 2)-mediano, 3)-grande.")
        op=self.cargarNumeroEntero('Ingrese un numero: ')
        
        if op>0 and op<4:
            if op==1:
                tamaño='chico'
            elif op==2:
                tamaño='mediano'
            else:
                tamaño='grande'
            ramo=Ramo(tamaño)
            bandera=True
            while bandera:
                manejador.mostrasFlores()
                
                valor=input("Ingrese el numero de flor  o t para terminar:")
                if valor=='t':
                    bandera=False
                else:

                    try:
                        valor=int(valor)
                    except ValueError:
                     print("Debe ingresar un numero entero")
                    else:
                        flor=manejador.buscarFlor(valor)
                        ramo.agregarFlor(flor)
            manejadorRamo.agregarRamo(ramo)
        else:
            print("No corresponde a ningun tamaño")
    def opcion2(self,manejador,manejadorRamo):
        manejador.floresVendidas(manejadorRamo)
    def opcion3(self,manejador,manejadorRamo):
        tamañoBuscar=input("Ingresar un tamaño de Ramo(chico-mediano-grande):")
        manejadorRamo.buscarRamo(tamañoBuscar,manejador)
       
    def cargarNumeroEntero(self,mensaje='Ingrese valor:'):
        numero=None
        bandera=True
        while bandera:
            try:
                numero=int(input(mensaje))
            except ValueError:
                print('ERROR: Se debe ingresar un numero entero.')
            else:
                bandera=False
        return numero
 
    def error(self):
        #Mensaje cuando ingresa opcion incorrecta
        print('Opción incorrecta')
    def salir(self):
        #Mensaje cuando decide salir
        print('Se cerro el menú')