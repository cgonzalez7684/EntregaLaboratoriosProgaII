def count_letras():
    chain= "San Jose; Cartago; Puntarenas; Heredia; Limon; Alajuela; Guanacaste"
    contador = chain.count('a')
    print(f"La cadena tiene {contador}letras 'a'.")

def replace_es():
    texto= input("Por favor, ingrese el texto")
    textomod = texto.replace("es", "ES")
    print("texto original: ", texto)
    print("Texto modificado: ", textomod)
    
def convertir_mayus():
    texto = input("Ingrese un texto: ")
    textomayus = texto.upper()
    print("Texto en mayúsculas:", textomayus)
    
while True:
    print("---menu---")
    print("1. contar letras a en ")    
    print("2. reemplazar texto")
    print("3. Convertir a mayusculas")
    print("4.salir")
    
    opcion= input("ingrese la opcion: ")
    
    if opcion == "1":
        count_letras()
    elif opcion == "2":
        replace_es()
    elif opcion == "3":
        convertir_mayus()
    elif opcion == "4":
        print ("Hasta pronto")
        break
    else: 
        print("opcion no valida, ingrese una opcion valida")    
    
#las funciones del inicio designan las tareas especificas que su utilizaran en el menu,
#dentro de cada funcion se indica al usuario, que ingrese la opcion para iniciar 
#la funcion, para esto, mediante el while true, iniciamos el menu tipo consola
#este va a iterar en bucle las opciones siempre y cuando el usuario ingrese una opcion valida
#si se elige la opcion 4, el programa rompe el bucle y se cierra
