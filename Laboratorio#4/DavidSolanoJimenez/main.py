def Main():    #menu
    print("Opcion #1: Determinar cuantas veces aparece una letra en el texto.")   
    print("Opcion #2: Si se encuentra 'es' reemplace x 'ES'.")
    print("Opcion #3: Retornar el texto en mayuscula.")
    print("Opcion #4: Salir")
    
    try:
        while True:
            tecla = input("Digite numero de opcion: ")
            if not tecla.isdigit():
                print('Debe ser un numero')
                continue
            i = int(tecla)
            if i == 1:
                texto = "San Jose; Cartago; Puntarenas; Heredia; Limon; Alajuela; Guanacaste"            
                print("El total de 'a' en el texto son: ", texto.lower().count('a'))    #se evalua el texto para contar las a, se pone lower para contar todas las A
            elif i == 2:
                textoIngresado = input("ingrese el texto a evaluar: ") #se solicita el texto a evaluar
                textoModifi = textoIngresado.replace('es','ES') #se cambia la variable a UPPER si es que exite en el texto ingresado.
                print("El texto modificado es: ", textoModifi)  
            elif i == 3:
                textoIngresado = input("ingrese el texto a evaluar: ")
                textoUpper = textoIngresado.upper() #se realiza el cambio a UPPERCASE
                print("El texto modificado es: ", textoUpper)
                print()
            elif i == 4:
                break
            else:
                print("Opcion invalida")
                continue
    except BaseException:
        print("Finalizo el programa, pulse tecla para cerrar")
        input()        
        
if __name__ == '__main__':
    Main()
