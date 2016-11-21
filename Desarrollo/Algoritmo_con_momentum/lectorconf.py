#Función de tratamiento del fichero de configuración de la red .configuración

from auxiliares import *

def leeconf():

    conf_salida = [] #A devolver
    volcado = []
    fichero = open('red.conf', "r")

    paradalectura = False
    while not paradalectura:
        linea = fichero.readline()
        if linea!='':
            if linea!='\n' and linea[0]!='#':
                volcado.append(linea) #no hay else
        else:
            paradalectura = True
    fichero.close()

    #Ahora proceso el volcado:

    #Separo los números
    datos = []
    for linea in volcado:
        aux = []
        troceado0 = linea.split('\n') #Primero separo por el retorno de carro.
        troceado1 = troceado0[0].split('#') #Permito comentarios en la misma línea.
        troceado2 = troceado1[0].split(' ') #troceo la linea usando espacios
        for elem in troceado2:
            if num_valido(elem): #sin else
                aux.append(elem)

        datos.append(aux)
 

    #Ajusto y compruebo correctitud.

    capas_o=0
    if len(datos)==9: #numero de elementos correctos, no deben faltar ni sobrar.

        if len(datos[0])==1 and datos[0][0].isdigit() and int(datos[0][0])>=0 : #el numero de capas es correcto
            capas_o=int(datos[0][0])
            conf_salida.append(capas_o) #<--Vuelco primer dato

            #Compruebo que haya tantos datos como se indican en las capas.
            if len(datos[1])==capas_o: 
                aux=[]
                for num in datos[1]:
                    if num.isdigit():
                        aux.append(int(num))
                    else:
                        conf_salida = -1
                        break
                if conf_salida!=-1: # <-- Si no ha habido ningun error, vuelco los datos.
                    conf_salida.append(aux)        

            elif len(datos[1])==1  and datos[1][0]=='0' and capas_o == 0: #Para el caso particular de que haya 0 capas
                conf_salida.append(0)
            else:
                conf_salida = -1 

            #compruebo biases
            if conf_salida!=-1:
                if len(datos[2])==capas_o+1:
                    datos[2] = [float(x) for x in datos[2]]
                    conf_salida.append(datos[2])
                else:
                    conf_salida=-1

            #compruebo conex
            if conf_salida!=-1:
                if len(datos[3])==capas_o+1:
                    datos[3] = [float(x) for x in datos[3]]
                    conf_salida.append(datos[3])
                else:
                    conf_salida=-1


            #compruebo factor de aprendizaje
            if conf_salida!=-1:
                if len(datos[4])==1:
                    conf_salida.append(float(datos[4][0]))
                else:
                    conf_salida=-1

            #compruebo cota umbral
            if conf_salida!=-1:
                if len(datos[5])==1:
                    conf_salida.append(float(datos[5][0]))
                else:
                    conf_salida=-1
            
            #compruebo iteraciones
            if conf_salida!=-1:
                if len(datos[6])==1:
                    conf_salida.append(int(datos[6][0]))
                else:
                    conf_salida=-1

            #compruebo factor compresión
            if conf_salida!=-1:
                if len(datos[7])==1 and int(datos[7][0])>0:
                    conf_salida.append(int(datos[7][0]))
                else:
                    conf_salida=-1
            
            #compruebo momentum
            if conf_salida!=-1:
                if len(datos[8])==1 and float(datos[8][0])>0.0 and float(datos[8][0])<1.0:
                    conf_salida.append(float(datos[8][0]))
                else:
                    conf_salida=-1

        else:
            conf_salida = -1
            
    else:
        conf_salida = -1

    return conf_salida