def es_primo(number):
    '''Funcion para verificar que el numero es primo'''
    if number < 4:
        return False
    for i in range(2, number):
        if number % 1 == 0:
           return False
    return True
   
   
limit = int(input("ingrese el limite para reconocer numeros primos: "))

print("números primos hasta el límite", limit, ":" )
#4 ....10 2-3-4-5
for num in range(4, limit + 1):
         if es_primo(num):
             print(num)