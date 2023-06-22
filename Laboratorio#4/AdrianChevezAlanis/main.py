print ("Opcion #1: indentificar cantidad de letras 'a' ")
print ("opcion #2: reemplazar las palabras del texto de 'es' a 'ES' ")
print ("opcion #3: reemplazar las letras del texto a mayuscula")

while True:

        tecla = input ("Digite el numero de opcion que desea realizar: ")
        if(not(tecla.isdigit())):
         print("Digite el numero de la opcion a ejecutar: ")
         continue
        i = int(tecla)
        if i == 1:
           text1 ="San Jose,Cartago,Puntarenas,Heredia,Limon,Guanacaste,Puntarenas"
           CanLetrasA=text1.count('a')
           print("el total de letras 'a' en los siguientes nombres:San Jose,Cartago,Puntarenas,Heredia,Limon,Guanacaste,Puntarenas son",CanLetrasA)
        elif i==2:
                txt2 = input("Digita un texto: ")
                nuevo_txt = txt2.replace("es", "ES")
                print("Texto cambiado:", nuevo_txt)
        elif i==3:
                txt3 = input("Digita un texto: ")
                texto_mayusculas = txt3.upper()
                print("Texto en mayúsculas:", texto_mayusculas)
        elif i==4:
                break
        else:
                print('Opcion incorrecta')
                continue 