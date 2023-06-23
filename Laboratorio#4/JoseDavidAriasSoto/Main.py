app_running = True

print("Ingrese una de las siguientes opciones:")
print("Opcion 1: Poder determinar de la cadena de texto, cuantas letras ‘a’ se tienen 'San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste'")
print("Opcion 2: Determinar de un valor de texto ingresado por el usuario si se encuentra el texto “es” para que el mismo sea remplazado en el valor original por “ES” ")
print("Opcion 3: Retornar el de un texto ingresado por el usuario, el mismo pero todo en mayúscula.")
print("Opcion 4: Cancelar el programa")

cadena_texto = "San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste"

while app_running:
    option = input("Ingrese la opción: ")

    if option == "1":
        contador = sum(s.count("a") for s in cadena_texto.split(";"))
        print(f"El caracter 'a' aparece: {contador} veces")

    elif option == "2":
        texto = input("Ingrese el texto: ")
        texto = texto.replace("es", "ES")
        print(texto)

    elif option == "3":
        texto = input("Ingrese el texto: ")
        print(texto.upper())

    elif option == "4":
        print("Terminando el programa")
        app_running = False

    else:
        print("Ingrese una opción válida o ingrese la opción '4' para terminar el programa")
