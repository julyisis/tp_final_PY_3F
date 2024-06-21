import secrets, string, sys

# diccionario adjuntado por el profesor donde cada valor tendra una cadena, es decir letras tiene una cadena del alfabeto en mayusculas y minusculas, numeros tiene la cadena de numeros del 0 al 9 y lo mismo con caracteres

diccionario = {
  'letras': string.ascii_letters,
  'numeros': string.digits,
  'caracteres': string.punctuation
}

def generar_contraseña(tipos, longitud=12):
    caracteres = ''.join(diccionario[tipo] for tipo in tipos)
    return ''.join(secrets.choice(caracteres) for _ in range(longitud))

def menu():
    print("""
    -----------Welcome-----------
    Generador de Contraseñas V0.1
    »•----------------(☼_☼)----------------•«
    Seleccione una de las siguientes opciones:
    » 1. Generar contraseña solo de Letras.
    » 2. Generar contraseña solo de números.
    » 3. Generar contraseña Letras y Números.
    » 4. Generar contraseña Letras, Números y Caracteres.
    » 0. Salir.
    """)
    
    opcion = input("Escriba la opción seleccionada: ")
    return opcion

def main():
    while True:
        opcion = menu()
        if opcion == '0':
            print("Saliendo...")
            break
        elif opcion == '1':
            tipos = ['letras']
        elif opcion == '2':
            tipos = ['numeros']
        elif opcion == '3':
            tipos = ['letras', 'numeros']
        elif opcion == '4':
            tipos = ['letras', 'numeros', 'caracteres']
        else:
            print("Opción no válida, intente de nuevo.")
            continue
        
        longitud = int(input("Ingrese el número de longitud de la contraseña: "))
        contraseña = generar_contraseña(tipos, longitud)
       
       
        print(f"""
              
              »»»»»»»»»»» CONTRASEÑA GENERADA: {contraseña} »»»»»»»»»»»""")

if __name__ == "__main__":
    main()
