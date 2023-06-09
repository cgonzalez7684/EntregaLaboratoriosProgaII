        #Esto lo que hace es definir el limite de cuantos numeros pares se buscan 

def imprimir_numeros_pares(limite):
    for i in range(2, limite + 1, 2):
        print(i)
        
        #Esta clase lo que hace es imprimir en la consola el mensaje para que el usuario cuente la cantidad de numeros pares hasta el numero ingresado

def main():
    limite = int(input("Ingrese el límite para evaluar números pares: "))
    imprimir_numeros_pares(limite)       
        

#verifica que el programa se puede ejecutar, de poder ser ejecutado,
#llama a la función main() para iniciar la ejecución del programa.
if __name__ == "__main__":
    main()

