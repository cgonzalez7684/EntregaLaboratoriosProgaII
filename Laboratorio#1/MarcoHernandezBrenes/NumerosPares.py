# Aqui voy a solicitar al usuario por el limite que ella o el quiera poner , que nos diga el numero
# input() es una función incorporada en Python que recibe la entrada del usuario. Explicaion aqui ==> https://www.knowledgehut.com/blog/programming/user-input-in-python 
# En ese link mencionan que el  input() siempre devuelve una cadena de texto (string), por lo que necesito convertirla a un número entero (integer) 
# para poder realizar operaciones matemáticas con ella. Eso es lo que hace int() que es el que puse antes del 'input'
limite = int(input('Por favor, ingrese el límite: '))

# Tengo que usar un bucle for para iterar desde 0 hasta el límite
for i in range(limite + 1):
    # Aqui estoy iniciando un bucle for. En Python, un bucle for se usa para iterar sobre una secuencia (que puede ser una lista, una tupla,
    # un diccionario, un conjunto o una cadena). Aui esta la explicacion ---> https://j2logo.com/bucle-for-en-python/
    
    # En este caso, estamos utilizando la función range()
    # para generar una secuencia de números desde 0 hasta el número ingresado por el usuario (limite + 1 )
    # Este Link explica muy bien como usarlo: https://cosasdedevs.com/posts/range-python/ 
    
    
    if i % 2 == 0:
        # Aqui utilizo  el operador de módulo % para determinar si el número actual i es par. 
        # El operador de módulo devuelve el residuo de la división entre dos números. Si un número es divisible por 2 sin dejar residuo (es decir, i % 2 es igual a 0), entonces es par.
        # Si es par, lo imprimo
        print(i)
   # Entonces  si el número es par, lo imprimimos en la consola con la función print().
   # Este ciclo se repite para cada número desde 0 hasta el límite ingresado por el usuario.
   
   