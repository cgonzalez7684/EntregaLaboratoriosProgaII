def imprimir_etiqueta(valores):
    for valor in valores:
        print (valor)
        
if __name__ == "__main__":
    valores = [1, 2, 3, 4, 5] 
    imprimir_etiqueta(valores)
            #la funcion imprimir_etiqueta recibe el argumento valores, esto se encarga de la impresion de cada uno de los valores en la lista
            #el codigo principal verifica que el codigo sea ejecutatdo fcorrectamente utilizando el "if__name==__main__"asegurando que el codigo se ejecute desde el programa
            #imprimir_etiqueta(valores) toma la lista de la linea de codigo de arriba valores=[1, 2, 3, 4, 5] y la imprime