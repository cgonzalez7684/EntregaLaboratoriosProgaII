def conteo_letras_a (args): 
    contador=0
    for i in range(len(args)):      #Ciclo for para recorre cada uno de los elementos de la lista
        contador += args [i].count("a") #Variable contadora para acumular la cantidad de "a" en cada uno de los elementos y totalizar.
        print('Cantidad de "a" en la palabra "', args[i],'" es: ', args [i].count("a"))
    print('Total de letras "a" es: ', contador)
    
def cadena_a_lista (enunciado): #Función para convertir una cadena de texto en una lista con la función split.
    lista = enunciado.split(sep="; ") #El sep = ';' indica el separador de la cadena para crear elementos de manera indexada cada vez que se lee un ";".
    return lista

def cambios_es_a_ES (cadena):
    print(cadena.replace("es", "ES")) #Reemplazo de sílaba "es" por "ES"
    
def cambio_minuscula_a_mayuscula (texto):
    print(texto.upper())    #Función "upper" para cambiar a mayúsculas.
    
