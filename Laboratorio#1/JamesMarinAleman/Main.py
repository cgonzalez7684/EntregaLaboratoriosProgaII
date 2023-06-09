'''funcion para verificar si el numero es par'''
def es_par (numero): 
   if num < 2 : 
       return False
   for i in range(2,numero):
        if numero % 2 == 1 :
            return False
   return True
    


#inicio del programa
Limite = int(input("Favor ingrese un limite para evaluar los números pares: "))

print("Los numeros pares de ",Limite ,"son: ")
# 1-limite
for num in range ( 0, Limite + 1):        
    if es_par(num):                                               #llamamos a la funcion si esta devuelve True se imprime 
        print(num)
    


###Version corta###
"""
limite = int(input('Por favor, ingrese el límite para sacar sus números pares: '))
for i in range(limite + 1):
    if i % 2 == 0:
        print(i)
"""