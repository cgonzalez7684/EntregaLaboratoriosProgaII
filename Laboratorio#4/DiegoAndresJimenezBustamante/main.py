#Se imprimen las opciones para el usuario
print("Opcion #1: Ver la cantidad de letras 'a' en el texto: San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste")
print("Opcion #2: Reemplazar las palabras del texto digitado de 'es' a 'ES'")
print("Opcion #3: Reemplazar las letras del texto digitado a mayusculas")
print("Opcion #4: Salir")    
#Se hace un ciclo para hacer el menú
while True: 
            tecla = input("Digitar opcion: ")
            if (not(tecla.isdigit())):
                print('Debe digitar un numero')
                continue
            i = int(tecla)
            if i == 1:
                #Se ingresa el texto para contar la cantidad de letras "a"
                txt1 = "San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste"
                #Se una el metodo count
                CantidadLetrasA = txt1.count("a")
                #Se imprime la cantidad de letras "a"
                print("La cantidad de letras 'a' en el texto: San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste es",CantidadLetrasA)
            elif i==2:
                #Se le pide al usuario ingresar el texto
                txt2 = input("Ingresa un texto: ")
                #Se utiliza el metodo replace para reemplazar letras en el texto
                nuevo_txt = txt2.replace("es", "ES")
                #Se imprime el texto original y el texto modificado
                print("Texto modificado:", nuevo_txt)
            elif i==3:
                #Se le pide al usuario ingresar el texto
                txt3 = input("Ingresa un texto: ")
                #Se utiliza el metodo upper para que todo el texto se convierta a mayusculas
                texto_mayusculas = txt3.upper()
                #Se imprime el texto modificado
                print("Texto en mayúsculas:", texto_mayusculas)
            elif i==4:
                break
            else:
                print('Opcion invalida')
                continue 