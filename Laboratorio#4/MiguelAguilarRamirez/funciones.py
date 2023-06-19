def menu():
    print("#1 Cuntas letras (a) tiene el siguiente texto: "
                  "San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste")
    print("#2 Ingrese un texto que contenga (es) para pasarlo a (ES): ")
    print("#3 Ingrese un texto para devolverlo en Mayusculas: ")
    print("#4 Salir","\n")
    

def programa():
    while True:
        menu() #aquí se hace el llamado a la funcion de un pequeño menu que se crea 
        opcion = input("Elija una opción del menu: ")
        if (not(opcion.isdigit())): # se utiliza esta funcion para verificar que se ingresen numeros y cadenas de texto
            print("Opcion invalida debe dijitar un numero","\n")
            continue 
        i = int(opcion)
        if i == 1:
            provincias = "San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste"
            print(provincias)
            print("La cantidad de letras (a) que hay en el texto son", provincias.count("a"),"\n") # metodo par contar la cantidad de veses que coincida el parametro que le enviemos
        elif i ==2:
            texto = input("Ingrese el texto: ")
            print(texto.replace("es", "ES"),"\n") # uso este metodo para remplazar un fragmento de la cadena por otra dada
        elif i ==3:
            texto = input("Ingrese el texto: ")
            print(texto.upper(),"\n") # aqui uamos este metodo par convertir todo a mayuscula
        elif i == 4:
            break
        else:
                print('Opcion invalida',"\n")
                continue
            
