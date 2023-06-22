def main():
    
    print ("Opcion #1: Determinar cuantas letras ‘a’ se tienen San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste ")
    print ("Opcion #2: Determinar si se encuentra el texto “es” para que el mismo sea remplazado en el valor original por “ES”")
    print ("Opcion #3: Retornar el texto ingresado, todo en mayúscula.")
    
while True:
    tecla = input("Digitar opcion")
    #aplicamos el metodo isdigit para determinar si el texto ingresado es un dato numerico
    if (not(tecla.isdigit())):
        print("Debes digitar un numero")
        continue
    #Menú del usuario
    i = int(tecla)
    if i == 1:
        palabras = "San José,Cartago,Puntarenas,Heredia,Limon,Alajuela,Guanacaste"
        Cantidadletras = palabras.count("a") # contador de las letras a
        print("La cantdad de letras (a) es"" ", palabras)
    elif i==2:
        texto = input ("ingrese el texto")
        textoModificado = texto.replace ("es","ES")#modificador de palabras
        print("textoreemplazado"" ",textoModificado)    
    elif i==3:
        texto2 = input("ingrese el texto")
        texto2mayuscula = texto2.upper()#modificador de texto
        print("Texto en mayuscula"" ",texto2mayuscula)
    elif i==4:
        break    
    else:
        print("Opcion no valida")
        continue    