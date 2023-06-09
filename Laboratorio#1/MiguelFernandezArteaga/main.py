"""
Verifica si un número es par.

Args:
numero (int): El número a verificar.

Returns:
bool: True si el número es par, False si es impar.
"""
def es_par(numero):
  # Si el modulo de 2 es igual a 0, el numero es par.
  if numero % 2 == 0:
    return True
  else:
    return False

# Funcion para imprimir los numeros
def imprimir_pares():
  # Se toma el limite, numerico a analizar
  limite = int(input("Ingrese el límite para evaluar números pares: "))
  print(f"Números pares hasta el límite {limite}:")
  # Usamos un ciclo para imprimir los numeros en pantalla 
  for num in range(2, limite + 1):
    # Se llama la funcion para determinar si el numero es par
    if es_par(num):
      print(num)

# Se llama la rutina de imprimir los numeros      
imprimir_pares()