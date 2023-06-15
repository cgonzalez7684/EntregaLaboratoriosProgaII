#Encontrar numeros pares

limite=int(input("Ingrese un numero: "))

numerospares=[]

for i in range (1,limite, + 1):
    
     if i % 2 == 0:
         
         numerospares.append(i)
         
print("Numeros pares: ", numerospares)
