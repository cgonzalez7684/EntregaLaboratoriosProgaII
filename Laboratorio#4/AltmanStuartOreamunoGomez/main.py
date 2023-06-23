import funciones
print("Menú de opciones")
print("Opcion #1: Contador de letras a")
print("Opcion #2: Ingresar palabra que contenga 'es' en ella")
print("Opcion #3: Convertidor a mayuscula")
print("Opcion #4: Salir")    
try:
    while True:
        teclado = input("Ingrese la opcion deseada: ")
        if (not(teclado.isdigit())): #Se evalua si lo ingresado por el usuario es un numero o no
            print("Digite el numero correspondiente")
            continue
        i = int(teclado)
            
        if i == 1:
            frase = "San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste"
            print("Oracion: ")
            print(frase)
            print("El total de 'a' es de: ")
            funciones.Contador_A(frase) #Se llama al metodo Contador_A para realizar le recuento de strings "a"
                
        elif i == 2:
            texto = input("Escribra cualquier palabra o frase que contenga 'es': ")
            print("Original: ")
            print(texto)
            print("Correción: ")
            funciones.Cambio_ES(texto) #Se llama al metodo Cambio_ES para reemplazar el string "es" por "ES"
        elif i == 3:
            mensaje = input("Ingrese cualquier oracion: ")
            print("Original: ")
            print(mensaje)
            print("Corrección: ")
            funciones.Mayusculas(mensaje) #Se llama al metodo Mayusculas para cambiar el string ingresado de minuscula a mayuscula
        elif i == 4:
            print("Cerrando...")
            print("Programa cerrado")
            break
        else:
            print("Opcion invalida. Intentelo de nuevo")  
except BaseException: #En caso de cualquier error inesperado a la hora de ejecutar el programa
    print("Error catastrofico. Favor llamar a su administrador")