print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡ Bienvenido al codificador !!!!!!!!!!!!!!!")
print("Creadores: Dostin Umaña Y Carlos Escobar")
print("Codificador Enigma")

lista = [['a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'],
['b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a'],
['c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b'],
['d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c'],
['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d'],
['g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','f'],
['h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','f','g'],
['i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','f','g','h'],
['j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','f','g','h','i'],
['k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','f','g','h','i','j'],
['l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','f','g','h','i','j','k'],
['m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','f','g','h','i','j','k','l'],
['n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','f','g','h','i','j','k','l','m'],
['o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','f','g','h','i','j','k','l','m','n'],
['p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','f','g','h','i','j','k','l','m','n','o'],
['q','r','s','t','u','v','w','x','y','z','a','b','c','d','f','g','h','i','j','k','l','m','n','o','p'],
['r','s','t','u','v','w','x','y','z','a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q'],
['s','t','u','v','w','x','y','z','a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r'],
['t','u','v','w','x','y','z','a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s'],
['u','v','w','x','y','z','a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t'],
['v','w','x','y','z','a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u'],
['w','x','y','z','a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v'],
['x','y','z','a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w'],
['y','z','a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x'],
['z','a','b','c','d','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y']]

while True:
    texto = input("codificador >> ").lower().strip()
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
        







