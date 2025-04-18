print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡ Bienvenido al codificador !!!!!!!!!!!!!!!")
print("Creadores: Dostin Umaña Y Carlos Escobar")
print("Codificador Enigma")


while True:
    texto = input("codificador >> ").lower().strip()
    print(texto)
    if texto == "quit":
        print("Saliendo ... \nGracias por usar nuestro codificador")
        break
    elif texto[0:7] == "setkey ":
        llave = texto[7:len(texto)]
        numeros = "0123456789"
        hay_numero = False #Validación del setkey
        for i in llave:
            for n in numeros:
                if i == n:
                    hay_numero = True
                    break
        if hay_numero == False:
            print("LLave Aceptada")
        else:
            print("ERROR! Expresión no valida") 
     

    elif texto[0:12] == "encode-text ":
        print("Texto a cifrar")

    elif texto[0:12] == "encode-file ":   
        print("Archivo a cifrar")

    elif texto[0:12] == "decode-text ":   
        print("Texto a descifrar")

    elif texto[0:12] == "decode-file ":   
        print("Archivo a descifrar")

    else:
        print("ERROR! Expresión no valida")
        


    



