# funcion que me permite saber si el numero es par
def numero_par(numero):
    for i in range(1,numero):
       if numero % 2 == 0:
           return True
       return False
   

#Ingreso de dato para evaluar si es par o no 
evaluacion_limite = int(input("Ingrese un numero limite para evaluar: "))

#impresion del recorrido que me dice cual es par
for num in range(1, evaluacion_limite + 1):
    if numero_par(num):
        print("Numero par", num)
    
    