from Funciones import contadorA, remplazarES, mayusculas 

def Menu():
    print("Opción 1: averiguar cuantas letras a contienen los nombres de las provincias de Costa Rica")
    print("Opción 2: remplazar un texto donde es pasará a ser ES")
    print("Opción 3: convertir un texto a mayuscula en su totalidad")
    print("Opción 4: salir del menú")
    #Creo un try por si acaso se encuentra alguna excepción a la hora de correr el código
    try:
        #Uso un while para que se repita todas las veces que el usuario quiera
        while True: 
            opc = input("Ingrese el número correspondiente: ")
            #si lo que ingrese el usuario es una letra le dirá que es una opción inválida y reiniciará el ciclo
            if (not(opc.isdigit())):
                print("Opcion inválida")
                continue
            #A i le ingresamos el valor de opc para que opc pase a ser un int
            i = int(opc)
            if i == 1:
                contadorA()
            elif i == 2:
                remplazarES()
            elif i == 3:
                mayusculas()
            #Si el usuario selecciona esta opción se acabará el ciclo
            elif i ==4:
                break
            #Si el usuario ingresa un numéro diferente a los indicados se le dirá que es una opción invalida
            #Y se reiniciaria el ciclo
            else:
                print("Opcion inválida")
                continue     
    except BaseException:
        print("Finalizó el programa, presione cualquier tecla para cerrar la ventana...")
        input()
        
#Aquí ingreso el código de validación para que se reconozca este módulo como el principal
if __name__ == '__main__':
    Menu()