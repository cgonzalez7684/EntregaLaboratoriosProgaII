#Variable de control de tipo buleana 
app_running = True
#Imprimimos las opciones
print("Ingrese una de las siguientes opciones:")
print("Opcion 1: Poder determinar de la cadena de texto, cuantas letras ‘a’ se tienen 'San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste'")
print("Opcion 2: Determinar de un valor de texto ingresado por el usuario si se encuentra el texto “es” para que el mismo sea remplazado en el valor original por “ES” ")
print("Opcion 3: Retornar el de un texto ingresado por el usuario, el mismo pero todo en mayúscula.")
print("Opcion 4: Cancela el programa")

cadena_texto = "San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste"

#Ciclo while loop que controla la ejecucion del programa siempre y cuando app_running sea verdadero
while app_running:
    #Solicitamos una de las opciones al usuario
    option = input("Ingrese la opcion:")
    if option == "1": 
        #Transformamos la cadena de caracteres a una lista
        #ya siendo una lista vamos a iterar la lista con cada palabra y evaluar si la letra 'a' esta presente
        #Si, la letra 'a' esta presente incrementamos el contador.
        lista_cadena_testo = cadena_texto.split(";")
        contador = 0
        for s in lista_cadena_testo:
            contador += s.count("a")
        print(f"El caracter 'a' aparece: {contador} de veces")
    if option == "2":
        texto = input("Ingrese el texto:")
        #Si en el text se encuentra la palabra 'es'
        #Replazamos el texto usando el metodo replace
        if texto.find("es"):
            texto = texto.replace("es", "ES")
            print(texto)
        else:
            print("'es' no fue encontrado")
    if option == "3":
        texto = input("Ingrese el texto")
        #utilizamos el metodo upper para cambiar todas las palabras a mayusculas
        if texto:
            print(texto.upper())
        else:
            print("Ingrese un texto")
            texto = input()
    if option == "4":
        print("Terminando el programa")
        app_running = False
    else:
        print("Ingrese una opcion o ingrese la opcion '4' para terminar el programa")