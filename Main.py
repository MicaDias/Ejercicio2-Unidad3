from ManejadorFlor import ManejadorFlor
from ManejadorRamo import ManejadorRamo
from Ramo import Ramo
from Menu import Menu
if __name__=='__main__':
    cant=0
    bandera=True
    while bandera:
        try:
            cant=int(input("Ingrese la cantidad de flores:"))
        except ValueError:
            print("Ingrese un numero entero")
        else:
            bandera=False
    manejadorFlores=ManejadorFlor(cant,5)
    manejadorFlores.cargarArchivo()
    manejadorRamo=ManejadorRamo()
    menu=Menu()
    menu.lanzarMenu(manejadorFlores,manejadorRamo)
    