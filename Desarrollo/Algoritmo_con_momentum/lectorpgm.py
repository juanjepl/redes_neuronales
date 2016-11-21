"""La funcion le la imagen en formato pgm y devuelve un vector de
0's y 1's directamente ya procesados"""

def leepgm(ruta_fichero):
    archivo = open(ruta_fichero, "r")
    it1 = archivo.readline() # Ignoro primera linea de tipo
    it2 = archivo.readline() # Ignoro segunda linea de comentario
    it3 = archivo.readline() # Ignoro tercera linea de tamaño
    it4 = archivo.readline() # Ignoro cuarta linea de 255 que indica...
    
    out = []
    bucl = True
    while(bucl):
        linealeida = archivo.readline()
        if linealeida != '':
            lineaprocesada = linealeida.replace('\n','')
            numeroprocesado = int(lineaprocesada)//255    # Convierto a 0's y 1's
            out.append(numeroprocesado) #elimino el salto de carro de cada cadena.
        else:
            bucl = False
        
    archivo.close()

    #print(len(out)) # Para probar el tamaño de la muestra
    return out