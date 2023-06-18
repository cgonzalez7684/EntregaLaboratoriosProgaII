#import funciones as fn
import funciones

#opciones de menu
print("Opcion #1 ---> Determinar 'a' en cadenas de texto")
print("Opcion #2 ---> Reemplezar 'es' por 'EZ' ")
print("Opcion #3 ---> Reemplazar ''") 
    
#se interpreta como un hacer si o si 
try:
    #while para hacer que si ingresa algo que no sea una letra vuelva a digitar una de las opciones
    while True:
        tecla = input("Digitar opcion: ")
        if (not(tecla.isdigit())):
            print('Debe digitar un numero')
            continue
        #empesamos con las opciones del menu
        i = int(tecla)
        if i ==1:
            texto=("San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste")
            
            x = texto.count("a")
            
            print (texto)
            
            
            
            
        elif i ==2:
            
            print(" opcion 2 ")
            
        elif i ==3:
            
            print(" opcion 3 ")
            
        elif i ==4:
            print("Se cierra el programa")  #para cerrar sistemma del todo
            break
        else: 
            print('Opcion invalida')
            continue 
        
        
except BaseException: 
    print("Finalizó el programa, cualquier tecla para cerrar ventanda...")
    

input()
