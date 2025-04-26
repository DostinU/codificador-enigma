print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡ Bienvenido al codificador !!!!!!!!!!!!!!!")
print("Creadores: Dostin Umaña Y Carlos Escobar")
print("Codificador Enigma")

def quitarTilde(textoUsuario):
    tildes = "áéíóúÁÉÍÓÚ"
    letras = "aeiouAEIOU"
    texto_modificado = ""

    for l in textoUsuario:
        if l in tildes:
            pos = tildes.index(l)
            letra = letras[pos]  # Reemplaza la letra tildada con la letra sin tilde
            texto_modificado += "\\" + letra  # Reemplaza la letra tildada con \ + letra
        else:
            texto_modificado += l  # Conserva la letra original si no tiene tilde  # Imprime el texto modificado
    return texto_modificado

def agregarTilde(textoDecifrado):
    tildes = "áéíóúÁÉÍÓÚ"
    letras = "aeiouAEIOU"
    texto_modificado = ""

    for l in textoDecifrado:
        if l == "\\":
            pass  # Ignora el carácter '\'

        if texto_modificado and texto_modificado[-1] == "\\":
            pos = letras.index(l)
            letra = tildes[pos]  # Reemplaza la letra sin tilde con la letra tildada
            texto_modificado = texto_modificado[:-1] + letra  # Reemplaza la letra sin tilde con \ + letra tildada
        else:
            texto_modificado += l  # Conserva la letra original si no tiene tilde
            texto_modificado += l  # Conserva la letra original si no tiene tilde 
    return texto_modificado

def codificarTexto(llave, textoSinTilde):
    textoSinTilde = textoSinTilde.lower()  # se guarda el texto dado al usuario en minuscula
    texto_codfificado = ''
    abc = lista[0]  # se asume que lista es una matriz y lista[0] es para buscar la columna en la lista 
    contadorLlave = 0  # para recorrer la llave

    for pos1 in range(0, len(textoSinTilde), 1):
        i = textoSinTilde[pos1]

        if i in abc:
            contador1 = 0  # reiniciar para cada letra del texto
    
            for letraAbc in abc:
                if i == letraAbc:
                    columna = contador1
                    letraLlave = llave[contadorLlave % len(llave)] # repite cada letra de la llave para el texto, en resumen se cicla la clave para que haya una letra de la misma para cada letra del texto
                    contador = 0  # reiniciar para cada búsqueda de fila

                    for fila in lista:
                        if letraLlave == fila[0]:
                            texto_codfificado += fila[columna]
                            break
                        contador += 1

                    contadorLlave += 1
                    break  # pasamos a la siguiente letra del texto
                contador1 += 1

        else:
            texto_codfificado += i # copia todo lo que no sea una letra del abecedario dado
    return texto_codfificado


def mayuscula(textocifrado, textoSinTilde):
    textocifrado1 = ""
    for l in range(len(textoSinTilde)):
        if textoSinTilde[l] == "\\":
            pass
        if textoSinTilde[l].isupper():
            textocifrado1 += textocifrado[l].upper()
        elif textoSinTilde[l].islower():
            textocifrado1 += textocifrado[l].lower()
        else:
            textocifrado1 += textocifrado[l]
    return textocifrado1



def descifrarTexto(llave, textoUsuario):
    texto_descifrado = ''
    abc = lista[0]  # lista[0] es el abecedario
    contadorLlave = 0
    textoUsuario = textoUsuario.lower()  # se guarda el texto dado al usuario en minuscula

    for pos1 in range(len(textoUsuario)):
        i = textoUsuario[pos1]

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

    return texto_descifrado


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
    texto = input("codificador >> ").strip()
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
        textoUsuario = texto[12:len(texto)] #se guarda unicamente el texto dado al usuario 
        textoSinTilde = quitarTilde(textoUsuario).strip() #se llama a la funcion de quitar tildes para quitar las tildes del texto
        textocifrado = codificarTexto(llave,textoSinTilde) #se llama a la funcion de cifrado para cifrar el texto sin tildes
        cifrado_mayuscula = mayuscula(textocifrado,textoSinTilde ) #se llama a la funcion de mayuscula para que el cifrado mantenga las mayusculas y minusculas del texto original
        print("resultado >>", cifrado_mayuscula)

    elif texto[0:12] == "decode-text ":
        textoAdecifrar = texto[12:len(texto)] #se guarda unicamente el texto codificado dado por el usuario
        textoDecifrado = descifrarTexto(llave, textoAdecifrar) #Se manda a llamar a la función decifrarTexto y decifra el texto dado por el usuario
        textoConMayuscula = mayuscula(textoDecifrado, textoAdecifrar) # Compara el texto decifrado con el texto dado por el usuario
        textoConTilde = agregarTilde(textoConMayuscula) # verifica el texto y si tiene un back slash antes de una vocal le pone una tilde.
        print("resultado >> ",textoConTilde)


    elif texto[0:12] == "encode-file ":   
        print("Archivo a cifrar")

    elif texto[0:12] == "decode-file ":   
        print("Archivo a descifrar")

    else:
        print("ERROR! Expresión no valida")







