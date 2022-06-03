import os

def borrarPantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

precioGallina=int()
precioPato=int()
precioCodorniz=int()
precioAvestruz=int()
cantidadPedido=int(0)
idDespacho=int()

print("USUARIO")
user=input()
print("CONTRASEÑA")
contra=input()
while contra!="contraseña" or user!="roberto":
    borrarPantalla()
    print("usuario o contraseña incorrectos, intenta nuevamente")
    print("USUARIO")
    user=input()
    print("CONTRASEÑA")
    contra=input()
borrarPantalla()
print("+++++++++++++++++++++++++++++")
print("   BIENVENIDO A ALL EGGS")
print("+++++++++++++++++++++++++++++")
menu=int(input("menu principal: \n 1- ingresar precio de los huevos \n 2- creacion de despacho \n 3- listado de huevos \n 4- listado de despachos \n 0-terminar proceso")) 
while menu != 0:
    if menu == 1:
        borrarPantalla()
        print("++++++++++++++++++++++++++++++++++++++")
        print("    ASIGNACIÓN DE PRECIO HUEVOS")
        print("++++++++++++++++++++++++++++++++++++++")
        print()
        while int(50) > int(precioGallina):
            print()
            print("PRECIO DE HUEVO: GALLINA (MINIMO $50)")
            precioGallina=int(input())
            print()
            print("El precio del huevo de gallina es $",precioGallina)
            borrarPantalla()
        while int(150) > int(precioPato):
            print()
            print("PRECIO DE HUEVO: PATO (MINIMO $150)")
            precioPato=int(input())
            print("++++++++++++++++++++++++++++++++++++++")
            print("    ASIGNACIÓN DE PRECIO HUEVOS")
            print("++++++++++++++++++++++++++++++++++++++")
            print()
            print("El precio del huevo de pato es $",precioPato)
            borrarPantalla()
        while int(50) > int(precioCodorniz):
            print()
            print("PRECIO DE HUEVO: CODORNIZ (MINIMO $50)")
            precioCodorniz=int(input())
            print("++++++++++++++++++++++++++++++++++++++")
            print("    ASIGNACIÓN DE PRECIO HUEVOS")
            print("++++++++++++++++++++++++++++++++++++++")
            print()
            print("El precio del huevo de codorniz es $",precioCodorniz)
            borrarPantalla()
        while int(50) > int(precioAvestruz):
            print()
            print("PRECIO DE HUEVO: AVESTRUZ (MINIMO $800)")
            precioAvestruz=int(input())
            print()
            print("El precio del huevo de avestruz es $",precioAvestruz)
            borrarPantalla()
    elif menu == 2:
        print("++++++++++++++++++++++++++++++")
        print("    CREACION DE DESPACHO")
        print("++++++++++++++++++++++++++++++")
        print()
        print("++++++++++++++++++++++")
        print("   INGRESAR DATOS")
        print("++++++++++++++++++++++")
        print()
        print("RUT DEL CLIENTE(SIN PUNTOS NI GUIÓN)")
        rut=input()
        print()
        print("NOMBRE O RAZÓN SOCIAL")
        razon=input()
        print()
        print("DOMICILIO")
        domicilio=input()
        print()
        print("TIENE CONVENIO?")
        print("Y= SI; N= NO")
        convenio=input()
        convenio=convenio.lower()
        if convenio=="y":
            precioGallina=int(precioGallina) / float(1.10)
            precioPato=int(precioPato) / float(1.10)
            precioCodorniz=int(precioCodorniz) / float(1.10)
            precioAvestruz=int(precioAvestruz) / float(1.10)
        print()
        print("++++++++++++++++++++++")
        print("   TIPO DE HUEVO")
        print("++++++++++++++++++++++")
        print()
        print("a) GALLINA")
        print("b) PATO")
        print("c) CODORNIZ")
        print("d) AVESTRUZ")
        huevoPedido=input()
        huevoPedido=huevoPedido.lower()
        if huevoPedido := "a":
            huevoPedido= "GALLINA"
        elif huevoPedido := "b":
            huevoPedido= "PATO"
        elif huevoPedido := "c":
            huevoPedido= "CODORNIZ"
        elif huevoPedido := "d":
            huevoPedido= "AVESTRUZ"
            
        if huevoPedido:= "GALLINA":
            precioHuevo= int(precioGallina)
        elif huevoPedido:= "PATO":
            precioHuevo=int(precioPato)
        elif huevoPedido:= "CODORNIZ":
            precioHuevo=int(precioCodorniz)
        elif huevoPedido:= "AVESTRUZ":
            precioHuevo=int(precioAvestruz)
        borrarPantalla()
        print()
        while int(cantidadPedido) > int(10000) or int(cantidadPedido) < 50:
            print()
            print("CANTIDAD A PEDIR (minimo de 50 huevos; maximo de 10000 huevos)")
            cantidadPedido=int(input())
        borrarPantalla()
        print()
        print("FECHA COMPROMETIDA")
        print("MES DE DESPACHO")
        mesDespacho=int(input())
        contadorFecha=int(0)
        while contadorFecha !=int(1):
            if mesDespacho== int(2):
                print("FECHA COMPROMETIDA")
                print("DÍA DE DESPACHO (MÁXIMO DÍA 28)")
                diaDespacho=int(input())
                while diaDespacho > int(28):
                    print("fecha incorrecta, ingrese un día posible")
                    print("FECHA COMPROMETIDA")
                    print("DÍA DE DESPACHO (MÁXIMO DÍA 28)")
                    diaDespacho=int(input())
                contadorFecha=contadorFecha+int(1)
            elif mesDespacho== int(1) or int(3) or int(5) or int(7) or int(8)or int(10) or int(12):
                print("FECHA COMPROMETIDA")
                print("DÍA DE DESPACHO (MÁXIMO DÍA 31)")
                diaDespacho=int(input())
                while diaDespacho > int(31):
                    print("fecha incorrecta, ingrese un día posible")
                    print("FECHA COMPROMETIDA")
                    print("DÍA DE DESPACHO (MÁXIMO DÍA 31)")
                    diaDespacho=int(input())
                contadorFecha=contadorFecha+int(1)
            elif mesDespacho== int(4) or int(6)or int(9) or int(11):
                print("FECHA COMPROMETIDA")
                print("DÍA DE DESPACHO (MÁXIMO DÍA 30)")
                diaDespacho=int(input())
                while diaDespacho > int(30):
                    print("fecha incorrecta, ingrese un día posible")
                    print("FECHA COMPROMETIDA")
                    print("DÍA DE DESPACHO (MÁXIMO DÍA 30)")
                    diaDespacho=int(input())
                contadorFecha=contadorFecha+int(1)
        borrarPantalla()
        print("FECHA COMPROMETIDA")
        print("AÑO DE DESPACHO")
        añoDespacho=int(input())
        while int(añoDespacho)<int(2022):
            borrarPantalla()
            print("fecha incorrecta, ingrese un año posible")
            print("FECHA COMPROMETIDA")
            añoDespacho=int(input())
            borrarPantalla()
        idDespacho=int(idDespacho)+1
        print("Registro ingresado correctamente")
        print()
    elif menu == 3:
        borrarPantalla()
        print("+++++++++++++++++++++++")
        print("   LISTA DE HUEVOS")
        print("+++++++++++++++++++++++")
        print()
        print("HUEVOS DISPONIBLES Y PRECIOS:")
        if convenio=="y":
            print(" GALLINA:","$",int(precioGallina)," \n","PATO:","$",int(precioPato)," \n","CODORNIZ:","$",int(precioCodorniz)," \n","AVESTRUZ:","$",int(precioAvestruz))
        elif convenio== "n":
            print(" GALLINA:","$",int(precioGallina)," \n","PATO:","$",int(precioPato)," \n","CODORNIZ:","$",int(precioCodorniz)," \n","AVESTRUZ:","$",int(precioAvestruz))
            print()
    elif menu == 4:
        borrarPantalla()
        if convenio=="y":
            conv="SI"
        elif convenio=="n":
            conv="NO"
        print("++++++++++++++++++++++++++++")
        print("   LISTADO DE DESPACHOS")
        print("++++++++++++++++++++++++++++")
        print()
        print(" rut:",rut,"\n","razón o nombre:",razon, "\n","domicilio:",domicilio, "\n","convenio:",conv, "\n","huevo pedido:",huevoPedido, "\n precio por huevo",precioHuevo,"\n cantidad de huevos:",cantidadPedido,"\n precio por cantidad de huevos:","$",int(cantidadPedido)*int(precioHuevo), "\n","Fecha:",diaDespacho,"/",mesDespacho,"/",añoDespacho,"\n ID de despacho:",idDespacho)
    else:
        print()
        print("por favor digita una opción válida")
    print()
    menu=int(input("menu principal: \n 1- ingresar precio de los huevos \n 2- creacion de despacho \n 3- listado de huevos \n 4- listado de despachos \n 0-terminar proceso")) 
borrarPantalla()
print("++++++++++++++++++++ \n     HASTA LUEGO \n++++++++++++++++++++") 
