 #Menu de opciones para el usuario

    #Prueba el codigo y en caso de error finaliza la ejecucion del codigo
try:
        #mientras se cumpla correctamente las opciones que se le brinden al usuario el codigo estara en bucle
        while True:
            print("\nElija una de las siguientes opciones para ejecutar la opcion elegida\n"
          "\n 1.Cuantas letras ""A"" hay en alguna de las 7 provincias de Costa Rica "
          "\n 2.Escriba un texto y la palabra ""es"" sera remplazada por ""ES"" "
          "\n 3.Escriba un texto y este se le devolvera en mayuscula "
          "\n 4.Salir del programa")
            
            opc=input("\ndigite una opcion: ")
            #En caso de dijitar uan letra mostrara un error
            if (not(opc.isdigit())):
                print("Debe digitar un numero ")
                continue
            nop=int(opc)
            #Opcion 1 provincias de costarica
            if nop ==1:
                print("Cuantas letras ""A"" hay en alguna de las 7 provincias de Costa Rica ")
                #contador de letras
                from collections import Counter
                #entrada dada por el usuario
                prov=input(str("\nEscriba el nombre de una provincia de Costa Rica "))
                #contador
                Counter = Counter(prov)
                #salida con el contador, suma las A mayusculas y minisculas segun corresponda
                print("\nLa cantidad de ""A"" que hay en "+ prov + " es",  Counter["a"] + Counter["A"])  
            #opcion 2 es Mayuscula
            elif nop ==2:
                print("\nLa palabra ""es"" sera remplazada por ""ES"" ")
                #entrada del usuario
                ences=input("\nEscriba un texto ")
                #remplaza es por ES
                encES=ences.replace("es", "ES")
                #imprime el resultado
                print(encES)
            #opcion 3 entrada en mayuscula
            elif nop==3:
                print("\nSe le devolvera el texto ingresado en mayuscula ")
                text=input("\nEscriba un texto: ")
                #se usa la funcuion upper para pasar la entrada de texto a mayuscula
                mayus=text.upper()
                print(mayus)
            #opcion 4 salida
            elif nop==4:
                print("\nSaliendo del programa")
                break
            #en caso de ingresar un numero diferente a 1,2,3 o 4
            else:
                print("\nOpcion invalida")
                continue
#en caso de error muestra lo siguiente
except BaseException:
        print("\nFinalizo el programa, presione una tecla para cerrar la ventana ")
        input()
        
        ##end
