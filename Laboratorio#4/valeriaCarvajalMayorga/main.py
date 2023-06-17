import funciones    #Importo el módulos de funciones para utilizar las funciones pertenecientes para cada una de las opciones del menú.

print("----Menú de opciones----")
print('Opción #1 ---> Conteo de letras "a" en palabras predeterminadas')
print('Opción #2 ---> Ingrese una palabra para si contiene "es"')
print('Opción #3 ---> Convertir una palabra a mayúscula')
print ('Opción #4 ---> Cerrar')

try:
    while True:
        opc = input("Ingrese a una opción: ")
        if (not(opc.isdigit())):    #Verifico que lo ingresado sea válido en datos enteros.
            print("Por favor ingresar un número")
            continue
        num = int(opc)
        
        if num == 1:
            cadena = "San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste"
            print("Las palabras son: " , cadena)
            lista = funciones.cadena_a_lista(cadena) #Función para convertir una cadena de texto en una lista.
            funciones.conteo_letras_a(lista)  #Funcion para totalizar la cantidad de letras "a" por cada palabra y total.
            
        elif num == 2:
            cadena = input("Ingrese cualquier palabra o frase: ")
            funciones.cambios_es_a_ES(cadena) #Función que reemplaza la sílaba "es" en "ES"
            
        elif num == 3:
           texto = input("Ingrese cualquier palabra o frase: ")
           funciones.cambio_minuscula_a_mayuscula(texto) #Función que cambia el texto ingresado en mayúscula 
           
        elif num == 4:
            break
        else:
            print("Opción no válida, por favor inténtelo de nuevo")
            
except BaseException:
         print("Finalizó el programa por Ctrl + C, cualquier tecla para cerrar ventana...")



         

    
    