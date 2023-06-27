from Huesped import *

def ingresarHuesped(arreglo_huesped):
    pasajero = Huesped()

    c = False
    while c == False:
        c = pasajero.setCodigo_pasajero(input("Ingrese Codigo pasajero:"))

    c = False
    while c == False:
        c = pasajero.setRut(input("Ingrese rut:"))

    c = False
    while c == False:
       try:
           c = pasajero.setPrecio(int(input("Ingrese Precio")))
       except BaseException as error:
           print(f"Error: {error}")

    c = False
    while c == False:
        c = pasajero.setTipo_habitacion(input("Ingrese Tipo Habitacion"))

    pasajero.nombre = input("Ingrese Nombre Pasajero")
    pasajero.apellido = input("Ingrese Apellido Pasajero")
    try:
        pasajero.num_habitacion = int(input("Ingrese Numero Habitacion"))
    except BaseException as error:
        print(f"Error: {error}")
    try:
        pasajero.cant_dias = int(input("Ingrese Cantidad de dias"))
    except BaseException as error:
        print(f"Error: {error} ")
    arreglo_huesped.apped(pasajero)
    print("Pasajero Registrado....")




def buscarHuesped(arreglo_huesped):
    pass
    codigo_pasajero = input("Ingrese Codigo pasajero a buscar")
    flag = False
    for pasajero in arreglo_huesped:
        if pasajero.codigo_pasajero = codigo:
            flag = True
            print("Datos")
            print(f"Codigo Pasajero: {codigo}")
            print(f"Rut: {rut}")
            print(f"Nombre: {nombre}")
            print(f" Apellido {apellido}")
            print(f"")
            print(f"")

###############################################

arreglo_huesped = np.array([])
ciclo = True




while ciclo:
    print("Menu Hotel Continental")
    print("1) Ingresar Huesped")
    print("2) Buscar Huesped")
    print("3) Listados")
    print("4) Salir")
    try:
        op=int(input("Seleccione (1/4): "))
        match op:
            case 1:
                arreglo_huesped = ingresarHuesped(arreglo_huesped)
            case 2:
                print("Buscar Huesped")
                buscarHuesped (arreglo_huesped)
            case 3:
                print("Listados")

    except BaseException as error:
        print(f"Error: {error}")