"""Funcion para contar la letra 'a' en el texto"""
def contarLetras(etiqueta):
    
    print("Se va a deternar cuantas letras hay en las palabras San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste\n")
    """Se utiliza el metedo '.count' para contar las letras 'a'"""
    letras=etiqueta.count('a')
    
    print("La cantidad de letras en total son: ", letras)
    
"""Funcion para reemplazar el texto 'es' por el 'ES'"""
def validarEs(texto):
    """Se utiliza el metodo '.replace' para remplazar el texto 'es' por el 'ES'"""
    palabras=texto.replace("es", "ES")
    print("Se imprime el texto: \n", palabras)
    
"""Funcion para retornar el texto en mayuscula"""
def retornarM(palabra):
    """Se utiliza el metodo 'upper' para retornar todo el texto en mayuscula"""
    mayuscula=palabra.upper
    print("Se imprime el texto: \n", mayuscula)

opc=0
while (opc!=4):
    """Se utiliza un menu para facilitar al usuario la opcion a escoger"""
    menu=(input('''********MENU********
    Seleccione la opcion a elegir
    1-Contar letras a de provincias
    2-Validar si se encuentra el texto es
    3-Retornar el texto ingresado en mayuscula 
    4-Salir
    ''' ))
    """Se utiliza el metodo 'isdigit' para validar que el texto ingresado sea un valor numerico"""
    if (not(menu.isdigit())):
        print("Debe digitar un numero")
        continue
    i = int(menu)
    if i == 1:
        etiqueta="San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste"
        print(contarLetras(etiqueta))
    elif i==2:
        texto=input("Ingrese una oracion para determinar si cuenta con el texto es\n")
        print(validarEs(texto))
    elif i==3:
        palabra=input("Ingrese un texto para que se retorne en mayusculas\n")
        print(retornarM(palabra))
    elif i==4:
        print("Nos vemos")
        opc=4
    else:
        print("Valor ingresado no valido")
        continue
        