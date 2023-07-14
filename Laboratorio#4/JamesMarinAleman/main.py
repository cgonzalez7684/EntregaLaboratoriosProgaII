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
        print()
        tecla = input("Digitar opcion: ")
        print()
        if (not(tecla.isdigit())):
            print('Debe digitar un numero')
            continue
        #empesamos con las opciones del menu
        i = int(tecla)
        if i ==1:
            texto=("San José; Cartago; Puntarenas; Heredia; Limón; Alajuela; Guanacaste")
            contdor_a = texto.count("a") # .count cuenta la cantidad de letras de un str pero si le colocamos (a) solo lo hara de a
              
            print("El siguiente texto --> "+texto+" tiene :"+str(contdor_a) +" a")

        elif i ==2:
            
            texto = (input("Favor ingrese un texto"+ "\n"))
            trasnformar_ES = texto.replace('es','ES')#replace reemplaza el texto
            
            print("El texto fue trasformado :"+ "\n" + trasnformar_ES )
            
            
        elif i ==3:
             
            texto = (input("Favor ingrese un texto"+ "\n"))
            mayuscular = texto.upper()#replace reemplaza el texto
            
            print("El texto fue trasformado :"+ "\n" + mayuscular )
            
            
            
        elif i ==4:
            print("Se cierra el programa")  #para cerrar sistemma del todo
            break
        else: #cuando digita algo mas de las opciones
            print('Opcion invalida')
            continue 
        
        
except BaseException: 
    print("Finalizó el programa, cualquier tecla para cerrar ventanda...")
    

input()
