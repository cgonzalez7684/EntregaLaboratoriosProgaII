#Funcion para verificar si el numero es par
def es_par(numero):
    for i in range(1, numero):
        if numero % 2 == 0:
            return True
    return False

#Lectura para saber el limete a evaluar de numero pares
limite = int(input("Ingrese el límite para evaluar números pares: "))

#Un ciclo para mostrar cuales numeros son pares 
for num in range(1, limite + 1):
    if es_par(num):
        print("El Numero",num,"es par")
        
        