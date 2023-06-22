

def main():
 
        print ("opcion #1: mostrar las cantidades de letras 'a' en el texto: San Jose, Cartago, Puntarenas, Heredia, Limon, Alajuela, Guanacaste")
        print ("opcion #2: Remplazar las palabras del texto digitados de 'es' a 'Es'")
        print ("opcion #3: Remplazar las letras del texto que se digitaron en mayusculas")
        print ("opcion #4: Menu salir")

while True:
        tecla = input("digite opcion: ")
        #se forma el metodo isdigit para determinar si el texto agregado es un dato numerico
        if (not(tecla.isdigit())):
            print('Tiene que digitar un numero')
            continue
        i = int(tecla)
        if i == 1:
            texto1 = "San Jose, Cartago, Puntarenas, Heredia, Limon, Alajuela, Guanacaste"
            CantidadLetrasA = texto1.count("a")# reconocimiento de contador de la letra (a)
            print("Las cantidades de letras 'a' en el texto: San Jose, Cartago, Puntarenas, Heredia, Limon, Alajuela, Guanacaste es",CantidadLetrasA)
        elif i == 2:
            texto2 = input("Ingrese un texto: ")
            nuevo_texto = texto2.replace("es", "Es") #modificador de palabras
            print("Texto modificado: ", nuevo_texto)
        elif i == 3:
            texto3 = input("Ingrese un texto: ")
            texto_mayusculas = texto3.upper() #modificador de texto
            print("Texto en mayusculas: ", texto_mayusculas)
        elif i == 4:
            break
        else:
            print('opcion invalida')
            continue