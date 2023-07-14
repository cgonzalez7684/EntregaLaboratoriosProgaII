#Establecer para agregar un avion en la lista de espera
def add_avion(waitin_list, flying_number):
    waitin_list.append(flying_number)
    
    print("Avion será agregado en la lista.")


#Establecer la conexion para mostrar la lista de espera
def show_list(waitin_list):
    if len(waitin_list) ==0:
        
        print("La lista está vacia.")
    else:
        print("Lista de espera de aviones.")
        for i , airplane in enumerate(waitin_list, start=1):
            print(f"{i}. Avión {airplane}")
            

#Establecer la eliminación de un avion en la lista de espera
def eliminate_plane(waitin_list, flying_number):
    if flying_number in waitin_list:
        waitin_list.remove(flying_number)
        
        print(" Este avion ha sido eliminado en la lista de espera.")
        
    else:
        print("Avión no se encuentra en la lista de espera.")
        
#Establecer de encontrar aviones en la lista de espera
def search_plane(waitin_list, flying_number):
     if flying_number in waitin_list:
        position = waitin_list.index(flying_number) + 1
        print(f"El avión {flying_number} se encuentra en la posición {position} de la lista de espera.")
     else:
        print(" El avión no  se encontrado en la lista de espera.")
        
#Establecer la cantidad de aviones en la lista de espera
def show_amount (waitin_list)
    amount= len (waitin_list)
    
    print("La cantidad de aviones en la lista de espera")