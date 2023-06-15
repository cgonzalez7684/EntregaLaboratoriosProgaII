lado = int(input("Ingrese la longitud del lado del cuadrado: "))

# Variable para controlar el número de asteriscos en cada fila
num_asteriscos = lado

# Bucle while para dibujar el cuadrado
while lado + 1 > 1:     #---->Aquí aumento uno al lado 1, para que existan la misma cantidad de líneas como de asteríscos y que sea simétrico.
    # Imprimir una fila de asteriscos
    print("  *" * num_asteriscos)  #---->Aquí agrego dos espacios antes del asterísco, para dar forma al cuadrado y que no se vea como rectángulo. 

  #  if (lado == 3):
  #      continue     ---->El continue básicamente interrumpe el ciclo si la condición de manera lo que contuna no se ejecuta y el ciclo vuelve a iterar, es decir, vuelve a recorrer desde el inicio.
    
  #  if (lado > 5):
  #       break      ---->El break termina el ciclo si la condición se cumple, de manera que ya no se ejecuta más ya que finaliza el ciclo.
    # Decrementar el valor del lado para la siguiente fila
    lado = lado - 1  # ----> Aquí decrementé ya que la condición del while se enciclaba, además que el ancho del cuadrado debe ser la misma cantidad de línas como de asteríscos.

