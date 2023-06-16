def conteo_letras_a (args):
    contador=0
    for i in range(len(args)):
        contador += args [i].count("a")
        print('Cantidad de "a" en la palabra "', args[i],'" es: ', args [i].count("a"))
    print('Total de letras "a" es: ', contador)
    
def cadena_a_lista (enunciado):
    lista = enunciado.split(sep="; ")
    return lista

def cambios_es_a_ES (cadena):
    print(cadena.replace("es", "ES"))
    
def cambio_minuscula_a_mayuscula (texto):
    print(texto.upper())
    
