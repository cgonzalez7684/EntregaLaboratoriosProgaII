arrayOfPlanes = []

def addPlane():
    nameOfPlane = input('Por favor ingrese el nombre de un Avion\n')

    arrayOfPlanes.append(nameOfPlane)
    
    print('El avion ', nameOfPlane,' fue agregado de forma exitosa\n')
    
def showInventory():
    print('Los aviones del inventario son : \n')
    
    for currentPlane in arrayOfPlanes:
        print(currentPlane)
        
def searchPlaneByName():
    countPlane = 0
    
    nameOfPlane = input('Ingrese el numero de vuelo que desea buscar\n')
    
    for currentPlane in arrayOfPlanes:
        if(currentPlane == nameOfPlane):
            countPlane += 1
            
    if(countPlane == 0):
        print('El avion no esta en la lista\n')
    else:
        print('El avion si esta en la lista\n')

def calculateQuantityOfPlanes():
    print('La cantidad de aviones es de : ', len(arrayOfPlanes))
 
def deletePlane():  
    finalArrayOfPlanes = []
    countQuantityOfPlanesEliminated = 0
    
    nameOfPlane = input('Ingrese el nombre del avion que desea eliminar: ')
    
    print('La cantidad de ', nameOfPlane, ' es de ', arrayOfPlanes.count(nameOfPlane))
    
    quantityOfPlanesToDelete = int(input('Ingrese la cantidad de aviones que desea eliminar: '))
    
    for currentPlane in arrayOfPlanes:
        if(currentPlane != nameOfPlane):
            finalArrayOfPlanes.append(currentPlane)
        elif(countQuantityOfPlanesEliminated < quantityOfPlanesToDelete):
            countQuantityOfPlanesEliminated += 1
        else:
            finalArrayOfPlanes.append(currentPlane)
            
    arrayOfPlanes.clear()     
    
    for currentfinalPlane in finalArrayOfPlanes:
        arrayOfPlanes.append(currentfinalPlane)
        
    print('El avion ', nameOfPlane, ' fue eliminado de forma exitosa ', arrayOfPlanes)

def menu():
    menuOption = ""
    
    while menuOption != '6':
        menuOption = input('\n\nSeleccione una opcion: \n 1. Agregar avion a la lista \n 2. Mostrar lista \n 3. Buscar avion por numero de vuelo \n 4. Obtener total de aviones en lista de espera\n 5. Eliminar avion por nombre\n 6. Salir\n\n ')
    
        if(menuOption == '1'):
            addPlane()
        elif(menuOption == '2'):
            showInventory()
        elif(menuOption == '3'):
            searchPlaneByName()
        elif(menuOption == '4'):
            calculateQuantityOfPlanes()
        elif(menuOption == '5'):
            deletePlane()
        else:
            break

menu()