class Huesped:
    codigo_pasajero=''
    rut=''
    nombre=''
    apellido=''
    num_habitacion=0
    precio=0
    cant_dias=0
    tipo_habitacion=''

    def __init__(self):
        self.codigo_pasajero='001'
        self.rut='12345678-0'
        self.nombre='S/N'
        self.apellido='S/A'
        self.num_habitacion=1
        self.precio=35000
        self.cant_dias=1
        self.tipo_habitacion='Simple'

    ### REGLAS DE NEGOCIO

    def setCodigo_pasajero(self,codigo):
        if len(codigo) >=2 and len(codigo) <=15:
            self.codigo_pasajero = codigo
            return True
        else:
            print("Codigo Incorrecto")
            return False


    def setRut(self,rut):
        if len(rut) == 10:
            if rut[0:8].isdigit() and rut[8:9] == '-' and (rut[9:10].isdigit() or rut[9:10].upper() =='K'):
                self.rut = rut
                return True
            else:
                print("Formato Incorrecto 12345678-0/K")
                return False
        else:
            print("Largo del rut Incorrecto")
            return False

    def setPrecio(self,precio):
        if precio >=35000 and precio <=56000:
            self.precio = precio
            return True
        else:
            print("Precio Incorrecto")
            return False

    def setTipo_habitacion(self,tipo):
        if tipo.upper() == 'SIMPLE' or tipo.upper() == 'DOBLE':
            self.tipo_habitacion = tipo
            return True
        else:
            print("Tipo Habitacion incorrecto")
            return False