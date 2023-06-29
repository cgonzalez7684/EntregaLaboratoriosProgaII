arrayOfFruits = []

def addFruit():
    nameOfFruit = input('Por favor ingrese el nombre de una fruta\n')

    arrayOfFruits.append(nameOfFruit)
    
    print('La fruta ', nameOfFruit,' fue agregada de forma exitosa\n')
    
def showInventory():
    print('La frutas del inventario son : \n')
    
    for currentFruit in arrayOfFruits:
        print(currentFruit)
        
def searchFruitByName():
    countFruit = 0
    
    nameOfFruit = input('Ingrese el nombre de la fruta que desea buscar\n')
    
    for currentFruit in arrayOfFruits:
        if(currentFruit == nameOfFruit):
            countFruit += 1
            
    if(countFruit == 0):
        print('La fruta no esta en el inventario\n')
    else:
        print('La fruta si esta en el inventario\n')

def calculateQuantityOfFruits():
    print('La cantidad de frutas es de : ', len(arrayOfFruits))
 
def deleteFruit():  
    finalArrayOfFruits = []
    countQuantityOfFruistEliminated = 0
    
    nameOfFruit = input('Ingrese el nombre de la fruta que desea eliminar: ')
    
    print('La cantidad de ', nameOfFruit, ' es de ', arrayOfFruits.count(nameOfFruit))
    
    quantityOfFruitToDelete = int(input('Ingrese la cantidad de frutas que desea eliminar: '))
    
    for currentFruit in arrayOfFruits:
        if(currentFruit != nameOfFruit):
            finalArrayOfFruits.append(currentFruit)
        elif(countQuantityOfFruistEliminated < quantityOfFruitToDelete):
            countQuantityOfFruistEliminated += 1
        else:
            finalArrayOfFruits.append(currentFruit)
            
    arrayOfFruits.clear()     
    
    for currentfinalFruit in finalArrayOfFruits:
        arrayOfFruits.append(currentfinalFruit)
        
    print('La fruta ', nameOfFruit, ' fue eliminada de forma exitosa ', arrayOfFruits)

def menu():
    menuOption = ""
    
    while menuOption != '6':
        menuOption = input('\n\nSeleccione una opcion: \n 1. Agregar fruta \n 2. Mostrar inventario \n 3. Buscar fruta por nombre \n 4. Obtener total de frutas \n 5. Eliminar fruta por nombre\n 6. Salir\n\n ')
    
        if(menuOption == '1'):
            addFruit()
        elif(menuOption == '2'):
            showInventory()
        elif(menuOption == '3'):
            searchFruitByName()
        elif(menuOption == '4'):
            calculateQuantityOfFruits()
        elif(menuOption == '5'):
            deleteFruit()
        else:
            break

menu()