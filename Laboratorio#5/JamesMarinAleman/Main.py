import funciones as fn   #llamo a las funciones y las llamo fn

'''
import time
print ("Bienvenido al sistema de inventario de la tienda")
for letra in "cargado... /n":
    time.sleep(0.3)  # espera 2 segundos entre cada print()
    (print(letra))time
'''

#Creamos el menu 
print("Opcion #1 ---> Agregar fruta")
print("Opcion #2 ---> Mostrar Inventario")
print("Opcion #3 ---> Buscar fruta por nombre")
print("Opcion #4 ---> calcular total frutas") 
print("Opcion #5 ---> Eliminar fruta") 
   
#hacemos que se ejecute
try:
    while True: #para eviatar errores
        print()
        tecla = input("Digite una opcion: ")
        print()
        
        #pequeño if para que no de error cuando no selecciona un #N
        if (not(tecla.isdigit())):
            print('Debe digitar un numero')
            continue
        
        #ahora si empezamos con el if del menu
        i = int(tecla)
        
        if i==1:
            print("Opcion : ",i)
            fn.agregar_fruta()
            
        elif i==2:
            print("Opcion : ",i)
            fn.Mostrar_Frutas()
 
        elif i==3:
            print("Opcion : ",i)
            fn.buscar_frutas()
            
        elif i==4:
            print("Opcion : ",i)
            fn.calcular_frutas()
            
            
        elif i==5:
            print("Opcion : ",i)
            fn.eliminar_fruta()            
      
        
        else: #cuando digita algo mas de las opciones
            print('Opcion invalida')
            continue 
    
        
    
except BaseException:
    print("Finalizó el programa, cualquier tecla para cerrar ventanda...")
    input()
        
input()
    