def menu():
    print("#1 Cuntas letras (a) tiene el siguiente texto: "
                  "San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste")
    print("#2 Ingrese un texto que contenga (es) para pasarlo a (ES): ")
    print("#3 Ingrese un texto para devolverlo en Mayusculas: ")
    print("#4 Salir","\n")
    

def programa():
    while True:
        menu()
        opcion = input("Elija una opción del menu: ")
        if (not(opcion.isdigit())):
            print("Opcion invalida debe dijitar un numero","\n")
            continue
        i = int(opcion)
        if i == 1:
            provincias = "San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste"
            print(provincias)
            print("La cantidad de letras (a) que hay en el texto son", provincias.count("a"),"\n")
        elif i ==2:
            texto = input("Ingrese el texto: ")
            print(texto.replace("es", "ES"),"\n")
        elif i ==3:
            texto = input("Ingrese el texto: ")
            print(texto.upper(),"\n")
        elif i == 4:
            break
        else:
                print('Opcion invalida',"\n")
                continue
            
programa()