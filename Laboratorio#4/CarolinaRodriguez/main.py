#Se dan las opciones al usuario
def menu():
 print("1. Contar las letras 'a' en el texto")
 print("2. Reemplazar 'es' por 'ES' en el texto")
 print("3. Convertir el texto en mayúscula")
 print("4. Salir")
#Ciclo para realizar las operaciones acorde a las opciones del menú
while True:
    numero = input("Digite la opción")
    
    #valida si el número es correcto
    if (not(numero.isdigit())):
        print("Digite una opción")
        continue
    option = int(numero)
    
  
    if option is 1:
      #texto a validar
      texto = "San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste"
      #Cuenta la cantidad de veces que se repite la letra deseada
      Cant = texto.count("a")
      #imprime el resultado
      print("La cantidad de letras 'a' es de: " ,Cant)
      
    elif option is 2:
      texto2 = input("Ingrese el texto")
      
     #reemplaza el texto que se indique
      modftexto2 = texto2.replace("es","ES")
      print("Texto modificado: ",modftexto2)
      
    elif option is 3:
      texto3 = input("Ingrese el texto")
      #Convierte todo el texto en mayúscula
      maysctexto3 = texto3.upper()
      print("Texto modificado: ", maysctexto3)
      
    elif option is 4:
      #termina el ciclo
      break
    else:
  #indica si el usario ingresa una opción que no está dentro del menú
      print("Opción no valida")
      
      
      
      