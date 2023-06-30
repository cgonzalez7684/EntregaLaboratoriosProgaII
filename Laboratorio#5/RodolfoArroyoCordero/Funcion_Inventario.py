#Variable para contar el total de las frutas 
Frutas_en_Inventario = 0


#Variable para el inventario es vector
Inventario=[]

#Funcion para agregar frutas en el Inventario
def Agregar_Fruta():
    print("Desea Agregar una Fruta al Inventario")
    Fruta=input()
    Inventario.append(Fruta.lower())
 
#Funcion para Buscar una fruta en el Invemtario
def Buscar_Fruta_por_Fruta():
    print("Digite la Fruta a buscar...")
    Fruta = input().lower()
    if Fruta in Inventario:
        print(f'{Fruta} - Ya se encuenta en el Inventario')
    else:
        print(f'{Fruta} - No se encuenta en el Inventario')
 
#Funcion para eliminar frutas del Inventario     
def Eliminar_Fruta():
    print(f'El total de Frutas en el Inventario es:{Frutas_en_Inventario}, desea eliminar alguna fruta del Inventario? SI/NO')
    opcion = input()
    if opcion.upper() == 'Y':
        print("Digite el nombre de la fruta que desee eliminar del inventario")
        Fruta = input()
        Inventario.remove(Fruta.lower())

#Funcion para mostrar todas las frutas del Inventario
def Mostrar_Inventario():
    [print(Fruta) for Fruta in Inventario ]

#  Funcio para Calcular el total de Frutas en Inventario  
def Calcular_Total_Frutas():
    Frutas_en_Inventario = len(Inventario)  
    print(f'El Total de las frutas en inventario es: {Frutas_en_Inventario}') 