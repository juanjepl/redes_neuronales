"""Este fichero contiene el código de la interfaz
de texto plano que se mostrará por terminal."""

from auxiliares import *
from lectorconf import *
import sys

def ejecuta_interfaz():

    #Inicializo respuestas.
    num_capas_ocultas=0
    num_neuronas_por_capa=[]
    bias_por_capa=[]
    conexiones=[]
    factor_de_aprendizaje=0.0
    cota_de_error=0.0
    limite_iteraciones=0
    factor_comp=0
    momentum=0.0

    all_ok = False #Para mostrar mensaje de éxito al final.

    #Muestro interfaz de texto plano.
    print('\n')
    print('╔═════════════════════════════════════════════════════════════════════════╗')
    print('║                                                                         ║')
    print('║       INTELIGENCIA ARTIFICIAL - TRABAJO DE REDES NEURONALES 2016        ║')
    print('║         Alumnos: Juan Jesús Pérez Luna, Gonzalo Delgado Chaves          ║')
    print('║                                                                         ║')
    print('╚═════════════════════════════════════════════════════════════════════════╝')
    print('┌─────────────────────────────────────────────────────────────────────────┐')
    print('│  La red neuronal tomará del directorio "entrenamiento" el conjunto de   │')
    print('│  entrenamiento, y de "prueba" tomará el de prueba respectivamente.      │')
    print('│                                                                         │')
    print('│  A continuación el algoritmo le pedirá los principales parámetros para  │')
    print('│  la configuración de la red.                                            │')
    print('│                                                                         │')
    print('│  Para más información, por favor, consulte el fichero ".pdf"" adjunto.  │')
    print('└─────────────────────────────────────────────────────────────────────────┘')
    print('\n')
    print('Por favor, escriba el número de la opción seleccionada o dato y pulse INTRO:')
    print(' ')
    print('¿Cómo desea configurar la red?')
    print('1) Manualmente introduciendo los datos.')
    print('2) A partir del fichero .conf adjunto.')
    print(' ')

    p1=input()
    p1_ok=False
    while not p1_ok:
        if p1=='1':
            print('Opción elegida: '+p1)
            p1_ok=True
        elif p1=='2':
            print('Opción elegida: '+p1)
            p1_ok=True
        else:
            p1=input('Por favor, introduzca una respuesta válida:\n')
    
    print(' ')

    # Separo de nuevo la condicional por claridad, ya que contendrán
    # el resto de opciones según su decisión
    
    if p1=='1':  #He elegido modo manual. 
        #Pregunto por el número de capas ocultas.
        p2=input('Por favor, elija el número de capas ocultas de la red (Puede ser 0): ')
        p2_ok=False
        while not p2_ok:
            if p2.isdigit() and int(p2) >=0:
                print('Su respuesta: '+p2)
                num_capas_ocultas=int(p2)
                p2_ok=True
            else:
                p2=input('Por favor, introduzca una respuesta válida:\n')

        if num_capas_ocultas != 0: #sin else, porque siempre se ejecuta lo demás.
            # Configuro numero de neuronas por capa oculta
            print(' ')
            print('¿Cómo desea configurar el número de neuronas por cada capa oculta?')
            print('1) Manualmente introduciendo los valores por cada capa.')
            print('2) Todas las capas ocultas con el mismo número de neuronas')
            print(' ')
        
            p3=input()
            p3_ok=False
            while not p3_ok:
                if p3=='1':
                    print('Opción elegida: '+p3)
                    p3_ok=True
                elif p3=='2':
                    print('Opción elegida: '+p3)
                    p3_ok=True
                else:
                    p3=input('Por favor, introduzca una respuesta válida:\n')

            if p3=='1':
                i=0
                while i<num_capas_ocultas:
                    p4=input('Por favor, elija el número de neuronas de la capa oculta número '+str(i+1)+': ')
                    p4_ok=False
                    while not p4_ok:
                        if p4.isdigit() and int(p4) > 0:
                            print('Su respuesta: '+p4)
                            num_neuronas_por_capa.append(int(p4))
                            p4_ok=True
                        else:
                            p4=input('Por favor, introduzca una respuesta válida:\n')
                    i+=1

            else: #p3=='2'
                p4=input('Por favor, elija el número de neuronas para todas las capas ocultas: ')
                p4_ok=False
                while not p4_ok:
                    if p4.isdigit() and int(p4) > 0:
                        print('Su respuesta: '+p4)
                        for capaoculta in range(0,num_capas_ocultas): #Pongo el mismo valor para todas.
                            num_neuronas_por_capa.append(int(p4))
                        p4_ok=True
                    else:
                        p4=input('Por favor, introduzca una respuesta válida:\n')


        #Configuración de los bias.                
        print(' ')
        print('¿Cómo desea configurar los bias de las diferentes capas de neuronas?')
        print('1) Manualmente introduciendo los valores de cada capa.')
        print('2) Todas las neuronas con el mismo valor de bias')
        print(' ')

        p8=input()
        p8_ok=False
        while not p8_ok:
            if p8=='1':
                print('Opción elegida: '+p8)
                p8_ok=True
            elif p8=='2':
                print('Opción elegida: '+p8)
                p8_ok=True
            else:
                p8=input('Por favor, introduzca una respuesta válida:\n')

        
        if p8=='1':

            i=0
            while(i<num_capas_ocultas+1):
                if i==num_capas_ocultas: #capa de salida
                    p9=input('Por favor, elija el valor de bias para las neuronas de la capa de salida: ')
                    p9_ok=False
                    while not p9_ok:
                        if num_valido(p9):
                            print('Su respuesta: '+p9)
                            bias_por_capa.append(float(p9))
                            p9_ok=True
                        else:
                            p9=input('Por favor, introduzca una respuesta válida:\n')
                else: #otras capas
                    p9=input('Por favor, elija el valor de bias para las neuronas de la capa oculta '+str(i+1)+': ')
                    p9_ok=False
                    while not p9_ok:
                        if num_valido(p9):
                            print('Su respuesta: '+p9)
                            bias_por_capa.append(float(p9))
                            p9_ok=True
                        else:
                            p9=input('Por favor, introduzca una respuesta válida:\n')
                i+=1

        else: #p8=='2' --> Todos igual.
            p9=input('Por favor, elija el valor de bias para todas las neuronas de la red: ')
            p9_ok=False
            while not p9_ok:
                if num_valido(p9):
                    print('Su respuesta: '+p9)
                    for capa in range(0,num_capas_ocultas+1):
                        bias_por_capa.append(float(p9))
                    p9_ok=True
                else:
                    p9=input('Por favor, introduzca una respuesta válida:\n')

                    
        #Peso de conexiones.                
        print(' ')
        print('¿Cómo desea configurar los pesos de las conexiones entre capas?')
        print('1) Manualmente introduciendo los valores de peso entre capa y capa.')
        print('2) Todas las conexiones con el mismo valor de peso')
        print(' ')

        p5=input()
        p5_ok=False
        while not p5_ok:
            if p5=='1':
                print('Opción elegida: '+p5)
                p5_ok=True
            elif p5=='2':
                print('Opción elegida: '+p5)
                p5_ok=True
            else:
                p5=input('Por favor, introduzca una respuesta válida:\n')
    
        if p5=='1': #capa a capa

            if num_capas_ocultas==0:
                p6=input('Por favor, elija el peso de las conexiones entre la capa de entrada y la de salida: ')
                p6_ok=False
                while not p6_ok:
                    if num_valido(p6):
                        print('Su respuesta: '+p6)
                        conexiones.append(float(p6))
                        p6_ok=True
                    else:
                        p6=input('Por favor, introduzca una respuesta válida:\n')

            else: #caso de mas de una capa de conexiones.
                i=0
                while i<num_capas_ocultas+1:
                    if i==0: #Primera capa de conexiones.                 
                        p6=input('Por favor, elija el peso de las conexiones entre la capa de entrada y la oculta número 1: ')
                        p6_ok=False
                        while not p6_ok:
                            if num_valido(p6):
                                print('Su respuesta: '+p6)
                                conexiones.append(float(p6))
                                p6_ok=True
                            else:
                                p6=input('Por favor, introduzca una respuesta válida:\n')
                    
                    elif i==num_capas_ocultas: #Última capa de conexiones. (no va a ser 0 porque ese caso esta fuera de esta rama if-else.)
                        p6=input('Por favor, elija el peso de las conexiones entre la capa oculta número '+ str(i) +' y la capa de salida: ')
                        p6_ok=False
                        while not p6_ok:
                            if num_valido(p6):
                                print('Su respuesta: '+p6)
                                conexiones.append(float(p6))
                                p6_ok=True
                            else:
                                p6=input('Por favor, introduzca una respuesta válida:\n')

                    else: #Capas de conexiones intermedias.
                        p6=input('Por favor, elija el peso de las conexiones entre la capa oculta número '+ str(i) +' y la capa oculta número '+ str(i+1) +': ')
                        p6_ok=False
                        while not p6_ok:
                            if num_valido(p6):
                                print('Su respuesta: '+p6)
                                conexiones.append(float(p6))
                                p6_ok=True
                            else:
                                p6=input('Por favor, introduzca una respuesta válida:\n')
                    i+=1

            
        else: #p5=='2' todos iguales
            p6=input('Por favor, elija el peso a asignar a todas las conexiones de la red: ')
            p6_ok=False
            while not p6_ok:
                if num_valido(p6):
                    print('Su respuesta: '+p6)
                    for capaconex in range(0,num_capas_ocultas+1): #Pongo el mismo valor para todas.
                        conexiones.append(float(p6))
                    p6_ok=True
                else:
                    p6=input('Por favor, introduzca una respuesta válida:\n')

        #Pregunto por el factor de aprendizaje.
        print(' ')
        p7=input('Por favor, proporcione el valor del factor de aprendizaje: ')
        p7_ok=False
        while not p7_ok:
            if num_valido(p7):
                print('Su respuesta: '+p7)
                factor_de_aprendizaje=float(p7)
                p7_ok=True
            else:
                p7=input('Por favor, introduzca una respuesta válida:\n')
        
        #Pregunto por la cota de error.
        print(' ')
        p10=input('Por favor, proporcione el valor para la cota de error: ')
        p10_ok=False
        while not p10_ok:
            if num_valido(p10):
                print('Su respuesta: '+p10)
                cota_de_error=float(p10)
                p10_ok=True
            else:
                p10=input('Por favor, introduzca una respuesta válida:\n')
        
        #Pregunto por el límite de iteraciones.
        print(' ')
        p11=input('Por favor, proporcione el número máximo de iteraciones a realizar: ')
        p11_ok=False
        while not p11_ok:
            if p11.isdigit() and int(p11)>0:
                print('Su respuesta: '+p11)
                limite_iteraciones=int(p11)
                p11_ok=True
            else:
                p11=input('Por favor, introduzca una respuesta válida:\n')

        #Pregunto por el factor de compresión.
        print(' ')
        p12=input('Por favor, proporcione el factor de compresión (Ejemplo: 3 para sumatrices 3x3)\nNota: El valor debe ser divisor del tamaño de lado de la imagen (30 en este problema): ')
        p12_ok=False
        while not p12_ok:
            if p12.isdigit() and int(p12)>0:
                print('Su respuesta: '+p12)
                factor_comp=int(p12)
                p12_ok=True
            else:
                p12=input('Por favor, introduzca una respuesta válida:\n')

        #Pregunto por el momentum.
        print(' ')
        p13=input('Por favor, proporcione el valor para el "momentum" (Valor entre 0 y 1 con ambos exclusive): ')
        p13_ok=False
        while not p13_ok:
            if num_valido(p13) and float(p13)>0.0 and float(p13)<1.0:
                print('Su respuesta: '+p13)
                momentum=float(p13)
                p13_ok=True
            else:
                p13=input('Por favor, introduzca una respuesta válida:\n')

        all_ok = True #ha ido bien, se muestra éxito.

    else: #p1=='2' He elegido modo de carga desde fichero.
        conf_de_fich = leeconf()
        if conf_de_fich!=-1:
            num_capas_ocultas=conf_de_fich[0]
            num_neuronas_por_capa=conf_de_fich[1]
            bias_por_capa=conf_de_fich[2]
            conexiones=conf_de_fich[3]
            factor_de_aprendizaje=conf_de_fich[4]
            cota_de_error=conf_de_fich[5]
            limite_iteraciones=conf_de_fich[6]
            factor_comp=conf_de_fich[7]
            momentum=conf_de_fich[8]

            all_ok = True #ha ido bien, se muestra éxito.

        else: #error en el fichero .conf
            print(' ')
            print("Hubo un error en la lectura del fichero.conf, asegúrese de que no contenga errores.")
            print(' ')
            sys.exit(1) #Para cortar la ejecución del programa.
    
    config_red = [num_capas_ocultas,num_neuronas_por_capa,bias_por_capa,conexiones,factor_de_aprendizaje,cota_de_error,limite_iteraciones,factor_comp,momentum]
    

    if all_ok:
        print(' ')
        print('┌─────────────────────────────┐')
        print('│  Red configurada con éxito  │')
        print('└─────────────────────────────┘')
        print(' ')

    return config_red

def msg_procesando():
    print('┌─────────────────┐')
    print('│  Procesando...  │')
    print('└─────────────────┘')
    print(' ')

def msg_resultados(obtenidos, esperados):
    print(' ')
    print('┌────────────────────────────────────────────────────────┐')
    print('│  Conjunto de prueba ejecutado sobre la red entrenada.  │')
    print('│                                                        │')
    print('│   Prueba Nº#  ·  Obtenido  ·  Esperado  ·  Criterio    │')

    i=0
    cont=0
    while i<len(obtenidos):
        """Se distingue el caso de una o dos cifras para no descuadrar el diseño de la tabla."""
        if i<9: #Lo lógico sería 10, pero estoy renombrando el caso '0' como '1' asi que ajusto.
            if obtenidos[i] == esperados[i]:
                print('│       '+str(i+1)+'             '+obtenidos[i]+'             '+esperados[i]+'          -OK-      │')
                cont+=1
            else:
                print('│       '+str(i+1)+'             '+obtenidos[i]+'             '+esperados[i]+'          -NO-      │')
        else:
            if obtenidos[i] == esperados[i]:
                print('│      '+str(i+1)+'             '+obtenidos[i]+'             '+esperados[i]+'          -OK-      │')
                cont+=1
            else:
                print('│      '+str(i+1)+'             '+obtenidos[i]+'             '+esperados[i]+'          -NO-      │')       
        i+=1
    print('└────────────────────────────────────────────────────────┘')
    print(' ')

    porcentaje=int((cont/len(obtenidos))*100)

    print('    Resultado Final: '+str(cont)+'/'+str(len(obtenidos))+'        Rendimiento:  '+str(porcentaje)+'%      ')


def volcado_pesos(red_neuronal):
    print(' ')
    print('¿Desea volcar el valor de los pesos en el fichero ".dat" adjunto?')
    print('1) Sí.')
    print('2) No.')
    print(' ')

    pvuelca=input()
    pvuelca_ok=False
    while not pvuelca_ok:
        if pvuelca=='1':
            print('Opción elegida: Sí')
            pvuelca_ok=True
        elif pvuelca=='2':
            print('Opción elegida: No')
            pvuelca_ok=True
        else:
            pvuelca=input('Por favor, introduzca una respuesta válida:\n')    
    print(' ')

    if pvuelca=='1': #Opción de volcado a fichero. (Si no se cumple da igual, el programa termina.)
        #os.path.exists("volcado_pesos.dat")
        fichero = open('volcado_pesos.dat','w')

        fichero.write('# Fichero con los diferentes pesos de los bias y conexiones de la red neuronal.\n')
        fichero.write(' \n')
        fichero.write('Valores para los bias de los perceptrones:\n')
        fichero.write(' \n')

        #Formateo la información y la imprimo en el fichero.        
        for capa in red_neuronal:
            for neu in capa:
                if(red_neuronal.index(capa)==0):
                    pass#No muestro la primera capa pq no se modifican. fichero.write('Capa de entrada, Neurona: '+str(neu.idx)+' Bias: '+str(neu.bias)+'\n')
                elif(red_neuronal.index(capa)==len(red_neuronal)-1): #capa final.
                    fichero.write('Capa de salida, Neurona: '+str(neu.idx)+' Bias: '+str(neu.bias)+'\n')
                else: #intermedias
                    fichero.write('Capa oculta '+str(red_neuronal.index(capa))+', Neurona: '+str(neu.idx)+' Bias: '+str(neu.bias)+'\n')                
        
        fichero.write(' \n')
        fichero.write('Valores para las conexiones entre capas:\n')
        fichero.write(' \n')

        #Me baso en las conexiones salientes. (Para no repetir)      
        
        num_capas_de_interconex = len(red_neuronal)-1

        for capa in red_neuronal:
            for neu in capa:
                if red_neuronal.index(capa)==0:
                    if num_capas_de_interconex==1:
                        for conex in neu.conex_out:
                            fichero.write('Conex: Conecta capas Entrada('+str(conex.idx_in)+') y Salida('+str(conex.idx_out)+') \nPeso: '+str(conex.peso)+'\n\n')
                    else:
                        for conex in neu.conex_out:
                            fichero.write('Conex: Conecta capas Entrada('+str(conex.idx_in)+') y Oculta 1('+str(conex.idx_out)+') \nPeso: '+str(conex.peso)+'\n\n') 
                    
                elif red_neuronal.index(capa)==num_capas_de_interconex-1 and num_capas_de_interconex > 1:
                    for conex in neu.conex_out:
                        fichero.write('Conex: Conecta capas Oculta '+str(num_capas_de_interconex-1)+'('+str(conex.idx_in)+') y Salida('+str(conex.idx_out)+') \nPeso: '+str(conex.peso)+'\n\n')
    
                else: #intermedias
                    for conex in neu.conex_out:
                        fichero.write('Conex: Conecta capas Oculta '+str(red_neuronal.index(capa))+'('+str(conex.idx_in)+') y Oculta '+str(red_neuronal.index(capa)+1)+'('+str(conex.idx_out)+') \nPeso: '+str(conex.peso)+'\n\n')
        fichero.close()

        print(' ')
        print('┌─────────────────────────────────────────────────────────┐')
        print('│  Información grabada en "volcado_pesos.dat" con éxito.  │')
        print('└─────────────────────────────────────────────────────────┘')
        print(' ')    