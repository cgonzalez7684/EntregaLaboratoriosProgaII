# Laboratorio 4
import funcionesCadena

def Main():
    try:
        while True:
            print("\nMenu")
            print("Opcion #1: Conteo de las vocales (a)")
            print("Opcion #2: Reemplazar texto (es - ES)")
            print("Opcion #3: Convertir a Mayusculas")
            print("Opcion #4: Salir del sistema \n") 
            tecla = input("Digitar opcion: ")
            if (not(tecla.isdigit())):
                print('Debe digitar un numero')
                continue
            i = int(tecla)
            if i == 1:
                funcionesCadena.contarVocalA()
            elif i==2:
                funcionesCadena.reemplazarTexto()                         
            elif i==3:
                funcionesCadena.mayusculas()                         
            elif i==4:
                break                
            else:
                print('Opcion invalida')
                continue 
    except BaseException:
        print("Finalizó el programa, cualquier tecla para cerrar ventanda...")
        input()
if __name__ == '__main__':
    Main()
    