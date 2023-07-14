import funciones as fn #llamo a las funciones y las llamo fn


#Creamos el menu 
print("Opcion #1 ---> Agregar Avion")
print("Opcion #2 ---> Mostrar lista de aviones")
print("Opcion #3 ---> Eliminar avion cuando despego")
print("Opcion #4 ---> Mostrar avion y mostrar su posicion en la lista") 
print("Opcion #5 ---> Mostrar Aviones en espera") 
print("Opcion #6 ---> Cerrar")


#hacemos que se ejecute
# 
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
            fn.agregar_avion() 
            
            
        elif i==2:
            print("Opcion : ",i)
            fn.Mostrar_avion()
 
        elif i==3:
            print("Opcion : ",i)
            fn.eliminar_avion()
        
        
        elif i==4:
            print("Opcion : ",i)
            fn.buscar_avion()
        
        elif i==5:
            print("Opcion : ",i)
            fn.calcular_vuelos()
        
        
        elif i ==6:
            print("Se cierra el programa")  #para cerrar sistemma del todo
            break
        else: #cuando digita algo mas de las opciones
            print('Opcion invalida')
            continue 
        
        
        
        
except BaseException:
    print("Finalizó el programa, cualquier tecla para cerrar ventanda...")
    input()
        
input()
    