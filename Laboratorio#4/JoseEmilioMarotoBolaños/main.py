print("opcion #1: Ver las cantidades de letras 'a' en el texto: San Jose, Cartago, Puntarenas, Heredia, Limon, Alajuela, Guanacaste")
print("opcion #2: Remplaza las palabras del texto digitados de 'es' a 'Es'")
print("opcion #3: Remplaza las letras del texto que se digitaron en mayusculas")
print("opcion #4: Menu salir")

while True:
        tecla = input("digite opcion: ")
        if (not(tecla.isdigit())):
            print('Tiene que digitar un numero')
            continue
        i = int(tecla)
        if i == 1:
            texto1 = "San Jose, Cartago, Puntarenas, Heredia, Limon, Alajuela, Guanacaste"
            CantidadLetrasA = texto1.count("a")
            print("Las cantidades de letras 'a' en el texto: San Jose, Cartago, Puntarenas, Heredia, Limon, Alajuela, Guanacaste es",CantidadLetrasA)
        elif i == 2:
            texto2 = input("Ingrese un texto: ")
            nuevo_texto = texto2.replace("es", "Es")
            print("Texto modificado: ", nuevo_texto)
        elif i == 3:
            texto3 = input("Ingrese un texto: ")
            texto_mayusculas = texto3.upper()
            print("Texto en mayusculas: ", texto_mayusculas)
        elif i == 4:
            break
        else:
            print('opcion invalida')
            continue