lado = int (input (" Ingrese la longitud del cuadrado: "))
 
 # Variable para controlar el numero de asteriscos 
num_asteriscos = lado

# Bucle while para dibujar el cuadrado
while lado > 1:
      # Imprimir fila de asteriscos
      print("*" * num_asteriscos)
    
      if (lado == 3):
          continue
      
      if (lado > 5):
          break
    
      # Decretar el valor del lado para la otra fila
      lado = lado + 1
        
    
