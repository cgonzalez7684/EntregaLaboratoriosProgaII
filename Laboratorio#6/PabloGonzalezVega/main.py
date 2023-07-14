comparador: int= 9
lista = []

while 1< comparador: 
 entrada= input("sistema de control de aeropuerto, si desea terminar operaciones intruduzca 1, si desea agregar un avión a la lista, 2, eliminar un avión, 3, buscar un avión en la lista, 4, y visualizar la cantidad de aviones en la lista 5 ") 

 comparador= int(entrada)
 print ("Operaciones terminadas")
 
 if comparador == 2:
     print ("intruduzca número de vuelo del avión")
     avion = input()
     
     lista.append(avion)
     print ("vuelo ", avion, " agregado")
     
 elif comparador == 3:
     print ("intruduzca número de vuelo a eliminar")
     avion = input()
     if avion in lista:
      lista.remove(avion)
      print ("vuelo ", avion, " eliminado")
     else:
      print ("el vuelo no existe")
      
 elif comparador == 4:
     print ("intruduzca número de vuelo que desea buscar")
     avion = input()
     
     
     posicion = lista.index (avion)  
     if avion in lista:
      print ("El vuelo", avion, "esta en la posicion", posicion)
     else:
       print ("el vuelo no existe")
       
 else:
    contador = len(lista)
    print (contador)
    
 
 
     