#Menu

print("Opcion #1: Contar la cantidad de letras 'a' (San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste)")
print("opcion #2: Remplazar las letras 'es' por 'ES' ")
print("Opcion #3: Remplazar el texto a letras en mayuscula")
print("Opcion #4: Salir del menu")

while True:
    
    tecla= input("Digite la opcion que desea: ")
    if(not(tecla.isdigit())):
        print("Digite un numero")
        continue
    i = int(tecla)
    
    if i == 1:
        texto1 = "San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste"
        cantletraA = texto1.count("a")
        print("La cantidad de letras 'a' son:",cantletraA)
        
    elif i ==2:
        texto2 = input("Ingrese un texto: ")
        nuevotexto = texto2.replace("es", "ES")
        print("Modificacion: ", nuevotexto)
        
    elif i ==3 :
        texto3 = input("Ingrese un texto: ")
        mayus = texto3.upper()
        print("Texto en mayuscula: ", mayus)
        
    elif i ==4 :
        break 
    
    input()