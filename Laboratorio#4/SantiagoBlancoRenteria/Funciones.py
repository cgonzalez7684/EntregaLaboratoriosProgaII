#Función para averiguar cuantas letras "a" hay en el texto requerido
def contadorA():
    provincias = "San José; Cartago; Puntarenas; Heredia; Limon; Alajuela; Guanacaste" 
    #Con el método count() podemos encontrar un determinado caracter y contar cuantas veces aparece
    #Utilicé count con "a" y "A" porque en "pa" no contaba la primera "A" de Alajuela
    pa = provincias.count("a")
    pA = provincias.count("A")
    #Acá le mostré en pantalla al usuario las provincias para que él mismo pudiera contar también
    print(provincias)
    #En este print nada mas sume la cuentas de los caracteres "a" y "A" para que me diera el resultado correcto
    print("La cantidad de letras ''a'' que tienen en conjunto estas provinicas es de: " , (pa + pA))
    
#Función para remplazar en cualquier texto "es" por "ES"
def remplazarES():
    #Le pido al usuario que ingrese el texto
    texto = (input("Ingrese un texto con la palabra es: "))
    #Utilizo el método replace() para remplazar "es" por "ES" 
    txt = texto.replace("es","ES")
    print(txt)

#Función para cambiar cualquier texto a mayúscula en su totalidad
def mayusculas():
    #Le pido al usuario que ingrese el texto
    texto = (input("Ingrese un texto: "))
    #Utilizo el método upper() para cambiar todo el texto a mayúscula
    txt = texto.upper()
    print (txt)