import funciones 

def menu():
    #Se crea el menú
    
    try:
        while True: 
            print("Ingrese una de las siguientes opciones:")
            print("Opcion 1: Agregar una fruta" )
            print("Opcion 2: Mostrar inventario")
            print("Opcion 3: Buscar frutas por nombre")
            print("Opcion 4: Calcular el total de frutas")
            print("Opcion 5: Eliminar frutas")
            print("Opcion 6: Salir del programa")
            tecla = input("Digite una opción: \n")
            
            if (not(tecla.isdigit())):
                print('Debe digitar un numero')
                continue
            
            i = int(tecla)
            
            #Se crean las opciones ys e ingresa a la función correspondiente
            if i == 1:
                print ("Ingresaste la opción 1: Agregar una fruta \n")
                funciones.agregar_fruta() 
                
                
            elif i == 2:
                print ("Ingresaste la opción 2: Mostrar inventario \n")
                funciones.mostrar_inventario()

            
            
            elif i==3:
                print ("Ingresaste la opción 3: Buscar frutas por nombre \n")
                funciones.buscar_fruta_por_nombre()
                
                
            elif i==4: 
                print ("Ingresaste la opción 4: Calcular el total de frutas \n") 
                funciones.calcular_total_frutas()
                
            elif i==5: 
                print ("Ingresaste la opción 5: Eliminar frutas") 
                funciones.eliminar_fruta()

            #Opción 5 para salir del programa
            elif i==6:
                break
            
            #Si no se selecciona una opción continúa el programa
            else:
                print("Opción inválida")
                continue 
                
    except BaseException:
        print("Finalizó el programa, cualquier tecla para cerrar ventana...")
        input()
        #Mostrar un mensaje de error amigable al usuario "Favor contacar admistrador..."
        #Registrar error en bitacora txt / registrado bd (el momento/usuario/error tecnico / los datos)
        #Notifación error

if __name__ == '__main__':
    menu()