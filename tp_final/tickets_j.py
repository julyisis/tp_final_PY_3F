"""
TICKETSSe ha pedido crear un modulo para generar tickets que contenga lo 
siguiente:Un menú con 3 opciones - Alta ticket , Leer ticket , Salir.Alta 
ticket : nombre, sector,asunto, problema. Al terminar de ingresar el ticket 
se deberá mostrar por pantalla el mismo,sumándose el numero de ticket (que 
sera un numero random entre 1000,9999) y una leyenda que pida acordarse del
numero, un menu que nos pregunte si deseamos crear otro ticket, en caso de 
ser no, que nos regrese al menu principal, de lo contrario que nos regrese a 
la pantalla de alta.leer ticket: número ticket al ingresar el numero nos 
mostrara por pantalla el ticket almacenado debajo del mismo aparece una 
leyenda que nos preguntara si deseamos leer otro ticket, teniendo la 
funcionalidad similar a la anteriormente mencionada.Salir : el programa 
finaliza y se cierra pidiéndonos una confirmacion
"""

import pickle, sys, os, random

# Diccionario para almacenar los tickets
tickets = {}
def limpiar_pantalla():
    if os.name == 'nt':  # Para Windows
        os.system('cls')
    else:  # Para Linux
        os.system('clear')

def generar_numero_ticket():
    return random.randrange(1000, 9999)

def guardar_ticket(ticket, numero_ticket):
    nombre_archivo = f"ticket_{numero_ticket}.pkl"
    with open(nombre_archivo, "wb") as f:
        pickle.dump(ticket, f)

def cargar_ticket(numero_ticket):
    nombre_archivo = f"ticket_{numero_ticket}.pkl"
    if os.path.isfile(nombre_archivo):
        with open(nombre_archivo, "rb") as f:
            return pickle.load(f)
    else:
        return None

def alta_ticket():
    print("\nIngrese los datos para Generar un nuevo Ticket")
    nombre = input("Ingrese su Nombre: ")
    sector = input("Ingrese su Sector: ")
    asunto = input("Ingrese Asunto: ")
    mensaje = input("Ingrese un Mensaje: ")

    numero_ticket = generar_numero_ticket()
    ticket = {
        "nombre": nombre,
        "sector": sector,
        "asunto": asunto,
        "mensaje": mensaje
    }
    guardar_ticket(ticket, numero_ticket)
    limpiar_pantalla()
    print("="*40)
    print(f"{'Se generó el siguiente Ticket':^40}")
    print("="*40)
    print(f"    Su nombre: {nombre}    N°Ticket: {numero_ticket}")
    print(f"    Sector: {sector}")
    print(f"    Asunto: {asunto}")
    print(f"    Mensaje: {mensaje}")
    print("\n\t  Recordar su número de Ticket")
   
    otro = input("\nDesea generar un nuevo Ticket? (s/n): ").lower()
    if otro == 's':
        alta_ticket()
    elif otro == 'n':
        main()
    else:
        print("Opción no válida. Saliendo...")
    return

def leer_ticket():
    limpiar_pantalla()
    print("--- Leer Ticket ---")
    numero_ticket = int(input("Número de ticket: "))
    ticket = cargar_ticket(numero_ticket)
    if ticket:
        limpiar_pantalla()
        print("="*40)
        print(f"{'Ticket Encontrado':^40}")
        print("="*40)
        print(f"""Su nombre: {ticket['nombre']}    N°Ticket: {numero_ticket}""")
        print(f"""Sector: {ticket['sector']}""")
        print(f"""Asunto: {ticket['asunto']}""")
        print(f"\nMensaje: {ticket['mensaje']}")
        
    else:
        print("\nTicket no encontrado.")


    otro = input("""
Desea leer otro Ticket? (s/n): """).lower()
    if otro == 's':
        leer_ticket()
    elif otro == 'n':
        main()
    else:
        print("Opción no válida. Saliendo...")
    return

def menu():
    limpiar_pantalla()
    print("""   Hola bienvenido al sistema de Tickets
                    
1 - Generar un Nuevo Ticket
2 - Leer un Ticket
3 - Salir""")
    opcion = input("Seleccione: ")
    return opcion

def main():
    opcion = menu()
    if opcion == '1':
        alta_ticket()
    elif opcion == '2':
        leer_ticket()
    elif opcion == '3':
        fin = input("Estás seguro que quiere salir? (s/n) ")
        if fin == 'n':
            main()
        elif fin == 's':
            print("Saliendo...")
    return

if __name__ == "__main__":
    main()

