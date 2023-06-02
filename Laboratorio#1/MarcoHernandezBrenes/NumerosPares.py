# Primero, solicitamos al usuario que ingrese un número
# En la primera línea, estamos solicitando al usuario que introduzca un número. input() es una función incorporada en Python que recibe la entrada del usuario.
# Sin embargo, input() siempre devuelve una cadena de texto (string), por lo que necesitamos convertirla a un número entero (integer) 
# para poder realizar operaciones matemáticas con ella. Eso es lo que hace int().
limite = int(input('Por favor, ingrese el límite: '))

# Utilizamos un bucle for para iterar desde 0 hasta el límite
for i in range(limite + 1):
    # Usamos la operación de módulo para comprobar si el número es par
    # En esta línea, estamos iniciando un bucle for. En Python, un bucle for se usa para iterar sobre una secuencia (que puede ser una lista, una tupla,
    # un diccionario, un conjunto o una cadena). En este caso, estamos utilizando la función range()
    # para generar una secuencia de números desde 0 hasta el número ingresado por el usuario (limite + 1, porque range() es exclusivo en el límite superior).
    
    if i % 2 == 0:
        # En esta parte, estamos utilizando el operador de módulo % para determinar si el número actual i es par. 
        # El operador de módulo devuelve el residuo de la división entre dos números. Si un número es divisible por 2 sin dejar residuo (es decir, i % 2 es igual a 0), entonces es par.
        # Si es par, lo imprimimos
        print(i)
   # Finalmente, si el número es par, lo imprimimos en la consola con la función print().
   # Este ciclo se repite para cada número desde 0 hasta el límite ingresado por el usuario, comprobando si cada número es par y, en caso afirmativo, imprimiéndolo.
   
   