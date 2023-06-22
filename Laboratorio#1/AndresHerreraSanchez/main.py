# Programa de consola para imprimir números pares hasta un límite dado por el usuario

# Función para imprimir números pares hasta el límite especificado
def imprimir_numeros_pares(numero):
   if numero < 2:
       return False 
   for i in range(2, numero):
       if numero % i == 0:
           return False
       return True
# Función principal del programa
limite = int(input("Ingresa el limite para evaluar los numeros  primos: "))
# Iniciar el programa
for num in range (2, limite + 1):
    if imprimir_numeros_pares(num):
        print(num)
    
