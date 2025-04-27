import os #mapea las rutas del directorio de tus archivos
print("¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡ Bienvenido al codificador !!!!!!!!!!!!!!!")
print("Creadores: ")
print("24000286 - Dostin Umaña - Sección BN")
print("24001994 - Carlos Escobar - Sección BN")

print("Codificador Enigma")

def quitarTilde(textoUsuario): #La función recibe el texto del usuario y le quita las tildes
    tildes = "áéíóúÁÉÍÓÚ"
    letras = "aeiouAEIOU"
    textoModificado = ""

    for l in textoUsuario:
        if l == "\\":
            textoModificado += "\\" + l
        elif l in tildes:
            pos = tildes.index(l)
            letra = letras[pos]  # Reemplaza la letra tildada con la letra sin tilde
            textoModificado += "\\" + letra  # Reemplaza la letra tildada con \ + letra   
        else:
            textoModificado += l  # Conserva la letra original si no tiene tilde  # Imprime el texto modificado
    return textoModificado

def agregarTilde(textoDecifrado): #Sirve para cuando codificamos y revisa si antes de una vocal hay una \ y si existe la diagnal la cambia por una vocal y 
    tildes = "áéíóúÁÉÍÓÚ"         # en dado caso sean \\ elimina una de las \ y deja solo una, luego especifica que la siguiente letra no lleva tilde.
    letras = "aeiouAEIOU"
    texto_modificado = ""
    saltarTilde = False  # Nuevo indicador

    i = 0
    while i < len(textoDecifrado): #Hola \\a
        l = textoDecifrado[i]

        if l == "\\":
            # Verificar si hay dos barras invertidas seguidas
            if i + 1 < len(textoDecifrado) and textoDecifrado[i + 1] == "\\": #Evaluamos si la siguiente posicion es una diagonal
                texto_modificado += "\\"  # Agrega solo una barra
                saltarTilde = True  # Indicar que no se debe poner tilde a la siguiente letra
                i += 2  # Saltar las dos barras
                continue
            else:
                # Solo una barra, se manejará en el siguiente paso
                texto_modificado += "\\"
                i += 1
                continue

        if texto_modificado and texto_modificado[-1] == "\\" and not saltarTilde: #and not " Si tilde es igual a falso"
            if l in letras:
                pos = letras.index(l)
                letra = tildes[pos]  # Reemplaza la letra sin tilde con la letra tildada
                texto_modificado = texto_modificado[:-1] + letra  # Reemplaza la barra + letra tildada
            else:
                texto_modificado += l 
        else: # si saltar Tilde es igual a verdadero: solo se copia la letra
            texto_modificado += l 

        saltarTilde = False  # Reiniciar el indicador
        i += 1

    return texto_modificado


def codificarTexto(llave, textoSinTilde): #Le asigna un valor de la llave a cada letra del texto y en base a estos dos busca la fila y columna de la matriz donde coincidan las posiciones de las dos letras.
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


def mayuscula(textocifrado, textoSinTilde): #Compara el texto cifrado con el texto sin cifrar, para encontrar en que posicion se encuentra una mayuscula y si la encuentra la coloca en el texto cifrado
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



def descifrarTexto(llave, textoUsuario): #Con la posicion de la llave que es la fila busca la letra del texto codificado en esa fila y luego con ese indice busca en las columnas
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

llave = ""
while True:
    texto = input("codificador >> ").strip()
    if texto == "quit":
        print("Saliendo ... \nGracias por usar nuestro codificador")
        break
    elif texto[0:7] == "setkey ":
        llave = texto[7:len(texto)]
        espacio = " "
        if espacio in llave:
            print("ERROR! Expresion no valida") 
        else:    
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
        if llave != "":
            textoUsuario = texto[12:len(texto)] #se guarda unicamente el texto dado al usuario 
            textoSinTilde = quitarTilde(textoUsuario).strip() #se llama a la funcion de quitar tildes para quitar las tildes del texto
            textocifrado = codificarTexto(llave,textoSinTilde) #se llama a la funcion de cifrado para cifrar el texto sin tildes
            cifrado_mayuscula = mayuscula(textocifrado,textoSinTilde ) #se llama a la funcion de mayuscula para que el cifrado mantenga las mayusculas y minusculas del texto original
            print("resultado >>", cifrado_mayuscula)
        else:   
            print("Error debe definir una llave.") 

    elif texto[0:12] == "decode-text ":
        if llave != "":
            textoAdecifrar = texto[12:len(texto)] #se guarda unicamente el texto codificado dado por el usuario
            textoDecifrado = descifrarTexto(llave,textoAdecifrar) #Se manda a llamar a la función decifrarTexto y decifra el texto dado por el usuario
            textoConMayuscula = mayuscula(textoDecifrado, textoAdecifrar) # Compara el texto decifrado con el texto dado por el usuario
            textoConTilde = agregarTilde(textoConMayuscula) # verifica el texto y si tiene un back slash antes de una vocal le pone una tilde.
            print("resultado >> ",textoConTilde)
        else:   
            print("Error debe definir una llave.")    

    elif texto[0:12] == "encode-file ":
        if llave != "":
            restante = texto[12:len(texto)]
            for i in restante:
                if i == " ":
                    posEspacio = restante.index(i) #posicion donde se encuentra le espacio
                    llave1 = restante[0:posEspacio]
                    archivo = restante[(posEspacio+1):len(restante)]
                    break
                else:
                    llave1 = llave
                    archivo = texto[12:len(texto)]   

            if os.path.exists(archivo):    #Sirve para comprobar si el archivo existe en tu disco
                file = open(archivo,"rt",encoding="utf-8") # se investio el "encoding = utf-8" el cual es para indicar que es el estándar para caracteres como á, é, í, ó, ú, ñ, etc.             
                leerLineas = file.read()  #lee todas las lineas pero no las guardar en lista
                archivoSinTilde = quitarTilde(leerLineas)
                archivoCodificado = codificarTexto(llave1,archivoSinTilde)
                archivoConMayuscula = mayuscula(archivoCodificado,archivoSinTilde) #Archivo codificado
                file.close()
                archivo1 = archivo[0:-3] + "gcf"
                file2 = open(archivo1,"w",encoding="utf-8")#Creamos Archivo y escribimos en el
                file2.write(archivoConMayuscula)
                file2.close()
                print("resultado >> archivo codificado en",archivo1)
            else:
                print(f"ERROR! {archivo} no existe.") 
            
        else:   
            print("Error debe definir una llave.") 

    elif texto[0:12] == "decode-file ":
        if llave != "":
            restante = texto[12:len(texto)]
            for i in restante:
                if i == " ":
                    posEspacio = restante.index(i) #posicion donde se encuentra le espacio
                    llave1 = restante[0:posEspacio]
                    archivo = restante[(posEspacio+1):len(restante)]
                    break
                else:
                    llave1 = llave
                    archivo = texto[12:len(texto)]
            if os.path.exists(archivo):
                file = open(archivo,"r",encoding="utf-8") #Abrimos archivo para poder leerlo
                leerLineas = file.read()
                archivoDecifrado = descifrarTexto(llave1,leerLineas)
                archivoConMayusculas = mayuscula(archivoDecifrado,leerLineas)
                archivoConTildes = agregarTilde(archivoConMayusculas)
                file.close()

                archivo1 = archivo[0:-4] + "-decoded.txt"
                file2 = open(archivo1,"w",encoding="utf-8")#Creamos Archivo y escribimos en el
                file2.write(archivoConTildes)
                file2.close()
                print("resultado >> archivo decodificado en",archivo1)
            else:
                print(f"ERROR! {archivo} no existe.") 

        else:   
            print("Error debe definir una llave.")     

    else:
        print("ERROR! Expresión no valida")

#Ssxo Zfrpc! Gprsc 5 Zlc\ggPfpmg





 
