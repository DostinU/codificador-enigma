print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡ Bienvenido al codificador !!!!!!!!!!!!!!!")
print("Creadores: Dostin Umaña Y Carlos Escobar")
print("Codificador Enigma")

def cifrarTexto(llave, textoACifrar):
    text_codfificado = ''
    abc = lista[0]  # se asume que lista es una matriz y lista[0] es el abecedario
    contadorLlave = 0  # para recorrer la llave

    for pos1 in range(0, len(textoACifrar), 1):
        i = textoACifrar[pos1]

        if i in abc:
            contador1 = 0  # reiniciar para cada letra del texto
    
            for letraAbc in abc:
                if i == letraAbc:
                    columna = contador1
                    letraLlave = llave[contadorLlave % len(llave)] # repite cada letra de la llave para el texto, en resumen se cicla la clave para que haya una letra de la misma para cada letra del texto
                    contador = 0  # reiniciar para cada búsqueda de fila

                    for fila in lista:
                        if letraLlave == fila[0]:
                            text_codfificado += fila[columna]
                            break
                        contador += 1

                    contadorLlave += 1
                    break  # pasamos a la siguiente letra del texto
                contador1 += 1

        else:
            text_codfificado += i # copia todo lo que no sea una letra del abecedario dado
    print(text_codfificado)
    return text_codfificado

# def cifrarTexto(llave,textoACifrar):
    
#     text_codfificado = ''
#     contador = 0
#     contador1 = 0
#     abc = lista[0]
# #Hola
#     for pos1 in range(0,len(textoACifrar),1):
#         i = textoACifrar[pos1]
#         contador1 = 0
#         if i == abc[0][contador1]:
#             columna = contador1
#             print(columna)  
#             for pos in range(0,len(llave),1):
#                 t = llave[pos]
#                 print(t)
#                 if t == abc[contador][0]:
#                     text_codfificado += lista[contador][columna]
#                     pos = contador  
#                     print(text_codfificado)
#                 contador+=1
#                 break
#         contador1+=1      
            
            
# #lemon            
      

#     print(text_codfificado)
#     return text_codfificado

def descifrarTexto(llave, textoAdecifrar):
    texto_descifrado = ''
    abc = lista[0]  # lista[0] es el abecedario
    contadorLlave = 0

    for pos1 in range(len(textoAdecifrar)):
        i = textoAdecifrar[pos1]

        if i in abc:
            letraLlave = llave[contadorLlave % len(llave)]

            for fila in lista:
                if fila[0] == letraLlave:
                    col = 0
                    for letra in fila:
                        if letra == i:
                            letraOriginal = abc[col]
                            texto_descifrado += letraOriginal
                            break
                        col += 1
                    break

            contadorLlave += 1
        else:
            texto_descifrado += i  # copiar tal cual números, espacios, etc.

    print(texto_descifrado)
    return texto_descifrado

#Lista
lista = [
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'],
['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a'],
['c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b'],
['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c'],
['e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd'],
['f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e'],
['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f'],
['h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g'],
['i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'],
['j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'],
['k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
['l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k'],
['m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'],
['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'],
['o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'],
['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o'],
['q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p'],
['r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q'],
['s', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r'],
['t', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's'],
['u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't'],
['v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u'],
['w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v'],
['x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w'],
['y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x'],
['z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v','w','x','y']]


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
        textoACifrar = texto[12:len(texto)]
        cifrarTexto(llave,textoACifrar)

    elif texto[0:12] == "encode-file ":   
        print("Archivo a cifrar")

    elif texto[0:12] == "decode-text ":
        textoAdecifrar = texto[12:len(texto)]
        descifrarTexto(llave, textoAdecifrar)   
        print("Texto a descifrar")

    elif texto[0:12] == "decode-file ":   
        print("Archivo a descifrar")

    else:
        print("ERROR! Expresión no valida")
        

        










