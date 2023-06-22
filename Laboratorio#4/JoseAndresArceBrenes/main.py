# Menú del programa
print ("Opcion #1: Ver la cantidad de letras 'a' en las palabras 'San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste' ")
print ("Opcion #2: Reemplazar las palabras del texto digitado de 'es' a 'ES'")
print ("Opcion #3: Reemplazar las letras del texto que se digitaron a mayuscula")
print ("Opcion #4: Salir")

#While para crear el menú
while True:
    tecla =input("Digite opcion: ")
    if (not(tecla.isdigit())):
        print("Debe digitar un número")
        continue
    #Opcion 1
    i = int (tecla)
    if i == 1:
        txt1 = "San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste"
        CantidadLetrasA = txt1.count("a") #Utilización de un count para contar las letras 'a'
        print ("La cantidad de letras 'a' en el texto es ",CantidadLetrasA)
    #Opcion 2
    elif i == 2: 
        text2 = input ("Ingresa un texto: ")
        new_text2 = text2.replace("es","ES") #Utilizacion de un replace para hacer el cambio de letras
        print ("Texto modificado ",new_text2)
    #Opcion 3
    elif i== 3:
        text3 = input("Ingresa un texto: ")
        text3_mayus = text3.upper() #Utilizacion de un upper para hacer mayuscula el texto
        print ("Texto en mayusculas: ", text3_mayus)
    #Opcion 4
    elif i == 4:
        break
    #Opcion en caso de error del usuario
    else:
        print ("Opcion no valida")
        continue 