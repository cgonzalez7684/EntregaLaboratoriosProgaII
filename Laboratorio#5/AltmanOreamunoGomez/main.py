import funciones

    
try:
    while True: #se crea el ciclo para que la funciona se ejecute hasta que el usuario desee terminar el programa
        print("Opcion #1 Agregar fruta")
        print("Opcion #2 Mostrar Inventario")
        print("Opcion #3 Buscar fruta por nombre")
        print("Opcion #4 Calcular total frutas") 
        print("Opcion #5 Eliminar fruta")
        print()
        Opcion = input("Digite una opcion: ")
        print()
        
        #mensaje de error por si el usuario digita algo que no sea un numero
        if (not(Opcion.isdigit())):
            print('Favor digite un numero')
            continue
        
        
        i = int(Opcion)
        
        if i==1:
            print("Opcion : ",i)
            funciones.agregar_fruta() #se llama a la funcion agregar_fruta
            
        elif i==2:
            print("Opcion : ",i)
            funciones.mostrar_frutas() #se llama a la funcion mostrar_frutas
 
        elif i==3:
            print("Opcion : ",i)
            funciones.buscar_frutas() #se llama a la funcion buscar_frutas
            
        elif i==4:
            print("Opcion : ",i)
            funciones.calcular_frutas() #se llama a la funcion calcula_frutas
            
            
        elif i==5:
            print("Opcion : ",i)
            funciones.eliminar_fruta() #se llama a la funcion eliminar_fruta         
      
        
        else:
            print('Opcion incorrecta')
            continue 
    
        
    
except BaseException:
    print("Error en el sistema, favor contactar a su administrador")

    