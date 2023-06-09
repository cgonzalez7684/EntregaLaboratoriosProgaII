def imprimir_numeros_pares(limite):
    for i in range(2, limite + 1, 2):
        print(i)
        
def main():
    limite = int(input("Ingrese el límite para evaluar números pares: "))
    imprimir_numeros_pares(limite)       

if _name_ == "_main_":
    main()