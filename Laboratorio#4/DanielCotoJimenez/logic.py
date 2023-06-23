#creamos un menu para el usuario
def menu():
    #le damos a elegir 4 opciones, sino coincide con alguna de estas. Pedira por una opcion valida
    while True:
        print("Menú:")
        print("1. Detectar caracteres")
        print("2. Detectar ES")
        print("3. Retornar texto en mayuscula")
        print("4. Salir")

        opcion = input("Selecciona una opcion: ")
        #aprovechamos para poner la logica en la opcion #1, ya que es poca cantidad de codigo.
        if opcion == '1':
            print("Has seleccionado la opcion 1")
            #creamos la funcion  para saber cuantos caracteres 'a' tiene la cadena
            def contadorDeCarater():
                cadena = "San Jose; Cartago; Puntarenas; Heredia; Limon; Alajuela; Guanacaste"
                cantidad_de_a = cadena.count('a')
                print("La cantidad de letras 'a' en la cadena es:", cantidad_de_a)

        elif opcion == '2':
            print("Has seleccionado la opcion 2")
            #creamos un metodo para saber si contiene 'es' si lo tiene. Lo cambia por el 'ES' deseado
            def dectarEs():
                texto = input("Ingresa un valor de texto: ")
                if "es" in texto:
                    texto_modificado = texto.replace("es", "ES")
                    print("Texto modificado:", texto_modificado)
                else:
                    print("El texto no contiene 'es'")


        elif opcion == '3':
            print("Has seleccionado la opcion 3")
            #Usamos el metodo ".upper para transformar el texto"
            def convertirMayusculas():
                texto = input("Ingresa un valor de texto: ")
                texto_en_mayusculas = texto.upper()
                print("Texto en mayusculas:", texto_en_mayusculas)


        elif opcion.lower() == 'salir':
            print("Saliendo del programa...")
            break

        else:
            print("Opcion invalida. Por favor, selecciona una opcion valida.")









