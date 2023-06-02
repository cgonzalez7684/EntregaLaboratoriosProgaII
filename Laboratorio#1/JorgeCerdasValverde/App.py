#variable limite, solicitamos al usuario que ingrese el numero limite
limite = int(input("Por favor, ingrese el numero limite que desea calcular los numeros pares: "))

def even(limite):
    #Definimos la funcion que busca los numeros pares y los imprime a la consola
    for i in range(1, limite):
        if i % 2 == 0:
            print(f"Numero par: {i}")

#Invocamos la funcion que busca los numeros pares en base al limite
even(limite)