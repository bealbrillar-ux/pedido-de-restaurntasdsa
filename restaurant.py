
import os
os.system("cls")

x = True
nombre = ""
rut = ""
suma_precio = 0
hamburger = False
pizza = False
ensalada = False
rutt = False
pedido = False

#nombre y rut
while len(nombre) < 3 or len(nombre) > 20:
    nombre = str(input("Ingrese su nombre (Maximo 20 caracteres):"))
try:
    rut_provisorio = int(input("Desea ingresar rut?: (1).Si (2).NO \n"))
    if rut_provisorio == 1 :
        while len(rut) > 8 or len(rut) <= 0:
            rutt =True
            rut =str(input("Ingrese su rut (Maximo 8 caracteres): "))
    else:
        print("Rut no ingresado")
except:
    print("ingrese los datos correctamente")


#menu
while x:
    print("\n--Menú--\n1. Agregar pedido \n2. Ver resumen \n3. Descargar boleta \n4. Salir")

    try:
        eleccion = int(input("Ingrese elección: "))
        if eleccion == 1:
            pedido = True
            comida = 0
            print("\n--Menú de comida--\n1. Hamburgesa ($5000) \n2. Pizza ($8000) \n3. Ensalada ($4000)")
            while comida < 1 or comida > 3:
                try:
                    comida = int(input("Ingrese su opcion de comida: "))
                    cantidad = int(input("ingrese la cantidad: "))
                    if comida == 1:
                        hamburger = True
                        cantidad_hmg = cantidad
                        suma_precio += (5000 * cantidad)
                    elif comida == 2:
                        pizza = True
                        cantidad_pizza = cantidad
                        suma_precio += (8000 * cantidad)
                    elif comida == 3:
                        ensalada = True
                        canidad_ensalada = cantidad
                        suma_precio += (4000 * cantidad)
                    else:
                        print("Opcion no valida, intente denuevo")
                except:
                    print("Datos mal ingresados, intende denuevo")
        elif eleccion == 2:
            if pedido:
                print("------RESUMEN--------")
                print(f"Nombre:{nombre}")
                if rutt:
                    print(f"Rut:{rut}")
                if hamburger:
                    print(f"hamburgesa: {cantidad_hmg}")
                if pizza:
                    print(f"pizza: {cantidad_pizza}")
                if ensalada:
                    print(f"ensalada. {canidad_ensalada}")
                print(f"TOTAL: {suma_precio}")
            else:
                print("No existe pedido aún")
        elif eleccion == 3:
            if pedido:
                with open("boleta.txt", "w") as archivo:
                    archivo.write("------BOLETA--------\n")
                    archivo.write(f"Nombre:{nombre}\n")
                    if rutt:
                        archivo.write(f"Rut:{rut}\n")
                    if hamburger:
                        archivo.write(f"hamburgesa: {cantidad_hmg}\n")
                    if pizza:
                        archivo.write(f"pizza: {cantidad_pizza}\n")
                    if ensalada:
                        archivo.write(f"ensalada. {canidad_ensalada}\n")
                    archivo.write(f"TOTAL: {suma_precio}")
            else:
                print("No existe pedido aún")
        elif eleccion == 4:
            print("Gracias por su visita")
            break
        else:
            print("Opcion no valida, intente denuevo")
    except:
        print("Datos mal ingresados, intende denuevo")

