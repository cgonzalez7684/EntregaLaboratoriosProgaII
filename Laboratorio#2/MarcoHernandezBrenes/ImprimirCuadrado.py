lado = int(input("Ingrese la longitud del lado del cuadrado: "))

# Variable para controlar el número de asteriscos en cada fila
num_asteriscos = lado

# Bucle while para dibujar el cuadrado
for i in range(lado):
    # Imprimir una fila de asteriscos
    print("*" * num_asteriscos)

    if (i == 2): #Aqui en este caso, utilize numero 2 por que si el usuario basado en la logica un cuadrado deberia tener minimo dos lineas 
        continue  #Aqui esta la explicacion https://www.digitalocean.com/community/tutorials/how-to-use-break-continue-and-pass-statements-when-working-with-loops-in-python-3-es
          
    
    if (i == lado - 1):
        break
    # Decrementar el valor del lado para la siguiente fila
# El comando "break" se usa para salir del bucle actual antes de que se complete.  Basicamente el  "break" se activara en la ultima iteración del bucle, 
# es decir, cuando "i" sea igual a "lado - 1". 
#Pero la verdad , ya que estamos en la ultima iteración del bucle, "break" no tiene realmente un efecto en la salida del código. 


######## CODIGO MALO #######
## Explicandolo: 

#lado = int(input("Ingrese la longitud del lado del cuadrado: "))
# Variable para controlar el número de asteriscos en cada fila
#num_asteriscos = lado

# Bucle while para dibujar el cuadrado
#while lado > 1:
    # Imprimir una fila de asteriscos
#    print("*" * num_asteriscos)

#    if (lado == 3): ====>  El comando "continue" esta dentro de un condicional que comprueba si "lado" es igual a 3. 
# En este caso, si el usuario introduce un numero mayor que 3, nunca va a pegar esta  condición y entonces el  "continue" nunca se ejecutara, creo que basado en la logica deberia ser minimo 2, por que ya 
# una linea de asteriscos es dada 
#        continue        
    
#    if (lado > 5): ===> Esto tampoco tiene sentido, por que  el comando "break"  se activara si el  "lado" es mayor que 5, dicendo
#  interrumpiendo el bucle y evitando que se dibuje un cuadrado completo si el lado es mayor que 5, en otras palabras, nos contradecimos
#        break
# Decrementar el valor del lado para la siguiente fila
#    lado = lado + 1 ===> Esto tampoco tiene sentido para mi, por que incrementar? podria resultar en un bucle infinito si el usuario introduce un numero mayor que 1.




