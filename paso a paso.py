import sys
despachos={}
despachos_huevos={}
contadorErrores=int(0)
while contadorErrores <= int(3):
    usuario=input("Usuario: ")
    contraseña=input("Contraseña: ")
    if usuario == "usuario" and contraseña == "contraseña":
        contadorErrores=int(4)
    elif usuario != "usuario" or contraseña != "contraseña":
        contadorErrores=contadorErrores+1
        print("Usuario o contraseña incorrectos")
        if contadorErrores==int(3):
            contadorErrores=contadorErrores+1
            sys.exit("ERROR! Intentos agotados")
if contadorErrores==int(3):
    sys.exit("ERROR! Intentos agotados")
elif contadorErrores==int(4):
    print("+++++++++++++++++++++++++++++\n   Bienvenido a ALL EGGS\n+++++++++++++++++++++++++++++")
    menu=int(input("menu principal: \n 1- ingresar precio de los huevos \n 2- creacion de despacho \n 3- listado de huevos \n 4- listado de despachos \n 0-terminar proceso"))
    while menu != 0:
        if menu == 1:
            print('+++++++++++++++++++++++++++\n   Asignación de precios\n+++++++++++++++++++++++++++')
            print()
            precioGallina=input('Ingresar precio por huevo de gallina (Mínimo de $50):')
            while int(precioGallina) < int(50):
                precioGallina=int(input('Ingresar un precio válido por huevo de gallina (Mínimo de $50):'))
            precioPato=input('Ingresar precio por huevo de pato (Mínimo de $150):')
            while int(precioPato) < int(150):
                precioPato=int(input('Ingresar un precio válido por huevo de pato (Mínimo de $150):'))
            precioCodorniz=input('Ingresar precio por huevo de codorníz (Mínimo de $50):')
            while int(precioCodorniz) < int(50):
                precioCodorniz=int(input('Ingresar un precio válido por huevo de codorníz (Mínimo de $50):'))
            precioAvestruz=input('Ingresar precio por huevo de avestrúz (Mínimo de $800):')
            while int(precioAvestruz) < int(800):
                precioAvestruz=int(input('Ingresar un precio válido por huevo de avestrúz (Mínimo de $800):'))
            print('------------------\nPrecios: \n1-Gallina:',precioGallina,'\n2-Pato:',precioPato,'\n3-Codorníz:',precioCodorniz,'\n4-Avestrúz:',precioAvestruz,'\n------------------')
        elif menu == 2:
            print('+++++++++++++++++++++++++')
            print('   Datos de despacho')
            print('+++++++++++++++++++++++++')
            print()
            rut=int(input('Rut (Sin puntos ni guón):'))
            despachos['rut']=rut
            nombre=input('Nombre o razón social:')
            despachos['nombre']=nombre
            domicilio=input('Datos de domicilio:')
            despachos['domicilio']=domicilio
            convenio=input('Tiene algún tipo de convenio?\n1(SI)/2(NO):')
            if convenio=='1':
                precioGallina=int(precioGallina) / float(1.10)
                precioPato=int(precioPato) / float(1.10)
                precioCodorniz=int(precioCodorniz) / float(1.10)
                precioAvestruz=int(precioAvestruz) / float(1.10)
            elif convenio=='2':
                precioGallina=int(precioGallina)
                precioPato=int(precioPato)
                precioCodorniz=int(precioCodorniz)
                precioAvestruz=int(precioAvestruz)
            print('++++++++++++++++++++++++++')
            print('   Fecha comprometida')
            print('++++++++++++++++++++++++++')
            año=int(input('Año comprometido:'))
            while año <= int(2022):
                print('Ingresar un año válido (2023 en adelante)')
                año=int(input('Año comprometido:'))
            despachos['año']=año
            mes=int(input('mes comprometido:'))
            while int(13)<= mes:
                print('Ingresar un mes válido (hasta diciempre-12-)')
                mes=int(input('Mes comprometido:'))
            despachos['mes']=mes
            dia=int(input('Día comprometido:'))
            while int(29)<= dia:
                print('Ingresar un día válido (hasta el día 28)')
                dia=int(input('Día comprometido:'))
            despachos['dia']=dia
            print('++++++++++++++++++++++++\n   Huevos requeridos\n++++++++++++++++++++++++')
            huevoPedido=input("1) Gallina \n2) Pato \n3) Codorníz \n4) Avestrúz")
            if huevoPedido := "1":
                huevoPedido= "Gallina"
                precioHuevo=int(precioGallina)
            elif huevoPedido := "2":
                huevoPedido= "Pato"
                precioHuevo=int(precioPato)
            elif huevoPedido := "3":
                huevoPedido= "Codorníz"
                precioHuevo=int(precioCodorniz)
            elif huevoPedido := "4":
                huevoPedido= "Avestrúz"
                precioHuevo=int(precioAvestruz)
            cantidadPedido=int()
            while int(cantidadPedido) > int(10000) or int(cantidadPedido) < int(50):
                print()
                cantidadPedido=int(input("CANTIDAD A PEDIR (minimo de 50 huevos; maximo de 10000 huevos)"))
            huevoTotal=int(cantidadPedido)*int(precioHuevo)
            despachos_huevos['Tipo de huevo:']=huevoPedido
            despachos_huevos['Precio del huevo:']=precioHuevo
            despachos_huevos['Cantidad de huevos:']=cantidadPedido
            despachos_huevos['Precio total:']=huevoTotal
        elif menu == 3:
            print("+++++++++++++++++++++++")
            print("   Lista de huevos")
            print("+++++++++++++++++++++++")
            print()
            print("Huevos disponibles y precios:\n")
            print('----------------\n GALLINA:',"$",int(precioGallina)," \n","PATO:","$",int(precioPato)," \n","CODORNIZ:","$",int(precioCodorniz)," \n","AVESTRUZ:","$",int(precioAvestruz),'\n----------------')
        elif menu == 4:
            print()
            print('+++++++++++++++++++++++++++++ \n   Listado de despachos \n+++++++++++++++++++++++++++++')
            print()
            print(despachos)
            print(despachos_huevos)
            print()
        else:
            print('Digitar un valor válido')
        menu=int(input("menu principal: \n 1- ingresar precio de los huevos \n 2- creacion de despacho \n 3- listado de huevos \n 4- listado de despachos \n 0-terminar proceso"))
    print("==============Gracias==============\n============Hasta luego============")
    sys.exit("Sistema ha finalizado")
