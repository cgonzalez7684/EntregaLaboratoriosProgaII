#Funcion para contar la letra 'a' en el texto
def ContadorLetras(Contar):
    print("Las 'a' de las provincias: San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste\n")
    #Se utiliza .count para contar la vocal a
    vocal=Contar.count('a')
    #Parametro para imprimir las A contadas
    print("La cantidad de letras en total son: ", vocal)
    
#Funcion para reemplazar  'es' por el 'ES'
def Cambiaes(Palabra):
    #Se utiliza el replace para remplazar el las letras
    Letras=Palabra.replace("es", "ES")
    #Parametro para imprimir las letras en Mayusculas
    print("Letras en Mayuscula: \n", Letras)
    
#Funcion para retornar el texto en mayuscula
def TextoMayuscula(texto):
    #Se utiliza el metodo 'upper' para retornar todo el texto en mayuscula
    Mayuscula=texto.upper
    #Parametro para imprimir el texto en Mayusculas
    print("Se imprime el texto: \n", Mayuscula)

while True:
    #Parametro para imprimir un menu 
    menu=(input('''----------MENU----------\n
    Seleccione una opcion: \n
    1-Contar vocal 'a' de las provincias de Costa Rica.\n
    2-Validar si se encuentra 'es' en un texto.\n
    3-Regresar Texto en mayuscula.\n
    4-Salir\n
    --------------------------\n''' ))
    #Se utiliza 'isdigit' para validar que el texto ingresado sea un numero
    if (not(menu.isdigit())):
        print("Escoga numero por favor:")
        continue
    i = int(menu)
    if i == 1:
        Contar="San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste"
        print(ContadorLetras(Contar))
    elif i==2:
        Palabra=input("Ingrese una oracion para determinar si cuenta con el texto es\n")
        print(Cambiaes(Palabra))
    elif i==3:
        texto=input("Ingrese un texto para que se retorne en mayusculas\n")
        print(TextoMayuscula(texto))
    elif i==4:
        print("Gracias!!!")
        break
    else:
        print("Favor ingrese un numero del 1 al 4")
        continue
    
    #Prueba 