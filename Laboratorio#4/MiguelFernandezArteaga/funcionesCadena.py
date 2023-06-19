def contarVocalA():
  #lista con las provicias
  provincias = "San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste"
  lista_provincias = provincias.split("; ")
  #contador para el total de vocal "a" encontradas
  total_a = 0
  #recorremos la lista
  for elemento in lista_provincias:
    #Usando la funcion de la clase String contamos las coincidencias con la vocal "a" 
    vocal_a = elemento.count("a")
    #sumamos al contador, para saber el total general
    total_a += vocal_a     
    print(f"La cantidad de letras 'a' en {elemento} es: {vocal_a}")
  print(f"Para un total de {total_a}")
  
def reemplazarTexto():  
  texto = input("Ingrese un texto: ")
  #Buscar la posición de la palabra "es" en el texto
  posicion = texto.find("es")
  #Devuelve -1 , sino existe coincidencias
  if posicion != -1:
      #La palabra "es" se encontró en el texto
      text_reemplazado = texto.replace("es", "ES")
      print("Texto original:", texto)
      print("Texto modificado:", text_reemplazado)
  else:
      #La palabra "es" no se encontró en el texto
      print("La palabra 'es' no se encuentra en el texto.")

def mayusculas():
  texto = input("Ingrese un texto: ")
  print("Texto original:", texto)
  print("Texto modificado:",texto.upper())

   