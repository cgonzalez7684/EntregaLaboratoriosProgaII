selectedOption = 0

while(selectedOption != 4):
    selectedOption = int(input("\n(1) Cuatro letras 'a'\n(2)Valor de texto ingresado por el usuario\n(3)Retorno de texto\n(4) Salir \n\n"))
    
    if(selectedOption == 1):
        word = "San Jose;Cartago;Puntarenas;Heredia;Limon;Alajuela;Guanacaste"
        
        print("La letra 'a' se repite ", word.count('a'), " veces")
    elif(selectedOption == 2):
        phrase = input("Ingrese el valor de texto: \n")
        arrayOfWords = phrase.split(" ")
        newPhrase = ""

        for currentWord in arrayOfWords:
            i = 0
            while i < len(currentWord):
                if(currentWord[i:(i + 2)] == "es"):
                    newPhrase += currentWord[i:(i + 2)].upper()
                    i += 2
                else:
                    newPhrase += currentWord[i:(i + 1)]
                    i += 1
                
        print("data", newPhrase)
    elif(selectedOption == 3):
        print("phrase ", input("Ingrese el valor de texto: \n").upper())