def menu():
    # menú
    print("Ingrese una de las siguientes opciones:")
    print("Opcion 1: Poder determinar de la cadena de texto, cuantas letras ´a´ se tienen 'San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste'" )
    print("Opcion 2: Determinar de un valor de texto ingresado por el usuario si se encuentra el texto “es” para que el mismo sea remplazado en el valor original por “ES” ")
    print("Opcion 3: Retornar el de un texto ingresado por el usuario, el mismo pero todo en mayúscula.")
    print("Opcion 4: Cerrar el programa")

    
    try:
        while True: 
            tecla = input("Digite una opción: ")
            
            if (not(tecla.isdigit())):
                print('Debe digitar un numero')
                continue
            i = int(tecla)

            # opción de dividir la cadena y contar las "a"
            if i == 1:
                cadena = "San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste"
                cadena.split(";")
                
                #Se cuentan las A
                contador = cadena.count("a")
                
                print(f'La letra "a" se repite: {contador} veces'  )   
                
            #creamos la segunda opción para buscar y reemplazar "es"
            elif i == 2:
                
                cadena = input ("Ingrese un texto: ") 
                
                if cadena.find("es"):

                    #reemplazamos "es"
                    cadena = cadena.replace("es","ES")
                    print("El texto sería: " ,cadena)
                else:
                    print("No existe las letras 'es' en el texto")
                
            #creamos la tercera opción par convertir la frase a mayúscula              
            elif i==3:
                cadena = input ("Ingrese un texto a convertir: ") 
                
                if cadena:

                    #Se convierte a mayuscula
                    cadena = cadena.upper()
                    print (cadena)
                else:
                    print("Ingrese el texto a convertir")

            #Opción cuatro para salir del programa
            elif i==4:
                break
            
            #Si no seleccionamos una opción continúa el programa
            else:
                print("Opción inválida")
                continue 
            
    except BaseException:
        print("Finalizó el programa, cualquier tecla para cerrar ventanda...")
        input()
        #Mostrar un mensaje de error al usuario "Favor contacar admistrador..."
        #Registrar error en bitacora txt / registrado bd (el momento/usuario/error tecnico / los datos)
        #Notifación error

if __name__ == '__main__':
    menu()