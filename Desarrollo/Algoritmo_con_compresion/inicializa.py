# Fichero que contiene la inicialización de la red neuronal.

from auxiliares import *
from lectorpgm import *
from clases import *
import sys


def inicializa_red(conf):
	red_neuronal = [] # Información de salida

    # Parámetros de inicialización.
	"""Entradas manuales --------------------"""
	perceptrones_entrada=900
	perceptrones_salida=7
	lado=30 #Fijo por el problema a resolver.
	"""--------------------------------------"""

	"""Modificación automatica según factor -"""
	bloque=conf[7] #Factor de compresión: 3=submatrices 3x3 (tiene que ser divisor de 'lado')
	if lado%bloque==0: #Es divisor correcto
		perceptrones_entrada=perceptrones_entrada//(bloque*bloque)
	else:
		print(' ')
		print("El factor de compresión no cumple las restricciones establecidas para el problema.")
		print(' ')
		sys.exit(1) #Para cortar la ejecución del programa.
	"""--------------------------------------"""

	num_capas_ocultas=conf[0]
	num_neu_capa_oculta=conf[1]
	bias_capas=conf[2]
	peso_conex=conf[3]
	factor=conf[4]

    #Variables auxiliares
	total_capas=num_capas_ocultas+2
	total_capas_conex=num_capas_ocultas+1
	ind_ult_capa_conex=num_capas_ocultas

    #Conjuntos
	conjunto_entrenamiento=[]
	conjunto_prueba=[]

    #Neuronas
	perceptrones=[]

    #----------- Inicializo los perceptrones de la red ----------------

    #### Inicializo la capa de perceptrones de entrada.
	idx=0 #Para el idx de los perceptrones. (Identifica el índice dentro de su capa.)
	i=0
	aux_entrada=[]
	while i<perceptrones_entrada:    
		percep = Perceptron(idx,0) #La capa de entrada no usa bias útil (de ahí el 0).
		aux_entrada.append(percep)
		i += 1
		idx += 1
	perceptrones.append(aux_entrada)

    #### Inicializo las capas de perceptrones intermedias (ocultas).
	i=0
	while i<num_capas_ocultas: #no entrará si no hay capas ocultas.
		idx=0 #Para el idx de los perceptrones.
		j=0
		aux_oculta=[]
		while j<num_neu_capa_oculta[i]:
			percep = Perceptron(idx,bias_capas[i])
			aux_oculta.append(percep)
			j+=1
			idx+=1 #Incremento el identificador.
		perceptrones.append(aux_oculta) # antes de machacar la capa con la siguiente oculta, la añado.
		i+=1    

    #### Inicializo la capa de perceptrones de salida.
	idx=0 #Para el idx de los perceptrones.
	i=0
	aux_salida=[]
	while i<perceptrones_salida:
		percep = Perceptron(idx,bias_capas[ind_ult_capa_conex])
		aux_salida.append(percep)
		i+=1
		idx+=1
	perceptrones.append(aux_salida)

    #----------- Inicializo las conexiones de la red ----------------
	""" Por cada neurona, almaceno la conexion como entrante o saliente"""

	i=0
	while i<total_capas_conex:
		j=0
		while j<len(perceptrones[i]): #Recorro el numero total de perceptrones de esa capa.
			k=0
			while k<len(perceptrones[i+1]): #Recorro por cada perceptron de la capa, todos los de la siguiente.
				conex = Conexion(peso_conex[i],perceptrones[i][j].idx,perceptrones[i+1][k].idx) #creo la conexion
				perceptrones[i][j].conex_out.append(conex) #almaceno la conexion como saliente en la capa actual.
				perceptrones[i+1][k].conex_in.append(conex) #almaceno la conexion como entrante en la siguiente capa.
				k+=1
			j+=1
		i+=1

    #----------- Leo conjuntos de entrenamiento y prueba ----------------        

    #Entrenamiento

	conjunto_entrenamiento.append([leepgm('entrenamiento/1.pgm'),[1,0,0,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/2.pgm'),[0,1,0,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/3.pgm'),[0,0,1,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/4.pgm'),[0,0,0,1,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/5.pgm'),[0,0,0,0,1,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/6.pgm'),[0,0,0,0,0,1,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/7.pgm'),[0,0,0,0,0,0,1]])

	conjunto_entrenamiento.append([leepgm('entrenamiento/8.pgm'),[1,0,0,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/9.pgm'),[0,1,0,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/10.pgm'),[0,0,1,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/11.pgm'),[0,0,0,1,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/12.pgm'),[0,0,0,0,1,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/13.pgm'),[0,0,0,0,0,1,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/14.pgm'),[0,0,0,0,0,0,1]])

	conjunto_entrenamiento.append([leepgm('entrenamiento/15.pgm'),[1,0,0,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/16.pgm'),[0,1,0,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/17.pgm'),[0,0,1,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/18.pgm'),[0,0,0,1,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/19.pgm'),[0,0,0,0,1,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/20.pgm'),[0,0,0,0,0,1,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/21.pgm'),[0,0,0,0,0,0,1]])

	conjunto_entrenamiento.append([leepgm('entrenamiento/22.pgm'),[1,0,0,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/23.pgm'),[0,1,0,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/24.pgm'),[0,0,1,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/25.pgm'),[0,0,0,1,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/26.pgm'),[0,0,0,0,1,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/27.pgm'),[0,0,0,0,0,1,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/28.pgm'),[0,0,0,0,0,0,1]])

	conjunto_entrenamiento.append([leepgm('entrenamiento/29.pgm'),[1,0,0,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/30.pgm'),[0,1,0,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/31.pgm'),[0,0,1,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/32.pgm'),[0,0,0,1,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/33.pgm'),[0,0,0,0,1,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/34.pgm'),[0,0,0,0,0,1,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/35.pgm'),[0,0,0,0,0,0,1]])

	conjunto_entrenamiento.append([leepgm('entrenamiento/36.pgm'),[1,0,0,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/37.pgm'),[0,1,0,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/38.pgm'),[0,0,1,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/39.pgm'),[0,0,0,1,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/40.pgm'),[0,0,0,0,1,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/41.pgm'),[0,0,0,0,0,1,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/42.pgm'),[0,0,0,0,0,0,1]])

	conjunto_entrenamiento.append([leepgm('entrenamiento/43.pgm'),[1,0,0,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/44.pgm'),[0,1,0,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/45.pgm'),[0,0,1,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/46.pgm'),[0,0,0,1,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/47.pgm'),[0,0,0,0,1,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/48.pgm'),[0,0,0,0,0,1,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/49.pgm'),[0,0,0,0,0,0,1]])    

	conjunto_entrenamiento.append([leepgm('entrenamiento/50.pgm'),[1,0,0,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/51.pgm'),[0,1,0,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/52.pgm'),[0,0,1,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/53.pgm'),[0,0,0,1,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/54.pgm'),[0,0,0,0,1,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/55.pgm'),[0,0,0,0,0,1,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/56.pgm'),[0,0,0,0,0,0,1]])

	conjunto_entrenamiento.append([leepgm('entrenamiento/57.pgm'),[1,0,0,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/58.pgm'),[0,1,0,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/59.pgm'),[0,0,1,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/60.pgm'),[0,0,0,1,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/61.pgm'),[0,0,0,0,1,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/62.pgm'),[0,0,0,0,0,1,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/63.pgm'),[0,0,0,0,0,0,1]])

	conjunto_entrenamiento.append([leepgm('entrenamiento/64.pgm'),[1,0,0,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/65.pgm'),[0,1,0,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/66.pgm'),[0,0,1,0,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/67.pgm'),[0,0,0,1,0,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/68.pgm'),[0,0,0,0,1,0,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/69.pgm'),[0,0,0,0,0,1,0]])
	conjunto_entrenamiento.append([leepgm('entrenamiento/70.pgm'),[0,0,0,0,0,0,1]])  

    #Prueba

	conjunto_prueba.append([leepgm('prueba/1.pgm'),[1,0,0,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/2.pgm'),[0,1,0,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/3.pgm'),[0,0,1,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/4.pgm'),[0,0,0,1,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/5.pgm'),[0,0,0,0,1,0,0]])
	conjunto_prueba.append([leepgm('prueba/6.pgm'),[0,0,0,0,0,1,0]])
	conjunto_prueba.append([leepgm('prueba/7.pgm'),[0,0,0,0,0,0,1]])

	conjunto_prueba.append([leepgm('prueba/8.pgm'),[1,0,0,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/9.pgm'),[0,1,0,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/10.pgm'),[0,0,1,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/11.pgm'),[0,0,0,1,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/12.pgm'),[0,0,0,0,1,0,0]])
	conjunto_prueba.append([leepgm('prueba/13.pgm'),[0,0,0,0,0,1,0]])
	conjunto_prueba.append([leepgm('prueba/14.pgm'),[0,0,0,0,0,0,1]])

	conjunto_prueba.append([leepgm('prueba/15.pgm'),[1,0,0,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/16.pgm'),[0,1,0,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/17.pgm'),[0,0,1,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/18.pgm'),[0,0,0,1,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/19.pgm'),[0,0,0,0,1,0,0]])
	conjunto_prueba.append([leepgm('prueba/20.pgm'),[0,0,0,0,0,1,0]])
	conjunto_prueba.append([leepgm('prueba/21.pgm'),[0,0,0,0,0,0,1]])

	conjunto_prueba.append([leepgm('prueba/22.pgm'),[1,0,0,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/23.pgm'),[0,1,0,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/24.pgm'),[0,0,1,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/25.pgm'),[0,0,0,1,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/26.pgm'),[0,0,0,0,1,0,0]])
	conjunto_prueba.append([leepgm('prueba/27.pgm'),[0,0,0,0,0,1,0]])
	conjunto_prueba.append([leepgm('prueba/28.pgm'),[0,0,0,0,0,0,1]])

	conjunto_prueba.append([leepgm('prueba/29.pgm'),[1,0,0,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/30.pgm'),[0,1,0,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/31.pgm'),[0,0,1,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/32.pgm'),[0,0,0,1,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/33.pgm'),[0,0,0,0,1,0,0]])
	conjunto_prueba.append([leepgm('prueba/34.pgm'),[0,0,0,0,0,1,0]])
	conjunto_prueba.append([leepgm('prueba/35.pgm'),[0,0,0,0,0,0,1]])

	conjunto_prueba.append([leepgm('prueba/36.pgm'),[1,0,0,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/37.pgm'),[0,1,0,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/38.pgm'),[0,0,1,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/39.pgm'),[0,0,0,1,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/40.pgm'),[0,0,0,0,1,0,0]])
	conjunto_prueba.append([leepgm('prueba/41.pgm'),[0,0,0,0,0,1,0]])
	conjunto_prueba.append([leepgm('prueba/42.pgm'),[0,0,0,0,0,0,1]])

	conjunto_prueba.append([leepgm('prueba/43.pgm'),[1,0,0,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/44.pgm'),[0,1,0,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/45.pgm'),[0,0,1,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/46.pgm'),[0,0,0,1,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/47.pgm'),[0,0,0,0,1,0,0]])
	conjunto_prueba.append([leepgm('prueba/48.pgm'),[0,0,0,0,0,1,0]])
	conjunto_prueba.append([leepgm('prueba/49.pgm'),[0,0,0,0,0,0,1]])    

	conjunto_prueba.append([leepgm('prueba/50.pgm'),[1,0,0,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/51.pgm'),[0,1,0,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/52.pgm'),[0,0,1,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/53.pgm'),[0,0,0,1,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/54.pgm'),[0,0,0,0,1,0,0]])
	conjunto_prueba.append([leepgm('prueba/55.pgm'),[0,0,0,0,0,1,0]])
	conjunto_prueba.append([leepgm('prueba/56.pgm'),[0,0,0,0,0,0,1]])

	conjunto_prueba.append([leepgm('prueba/57.pgm'),[1,0,0,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/58.pgm'),[0,1,0,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/59.pgm'),[0,0,1,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/60.pgm'),[0,0,0,1,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/61.pgm'),[0,0,0,0,1,0,0]])
	conjunto_prueba.append([leepgm('prueba/62.pgm'),[0,0,0,0,0,1,0]])
	conjunto_prueba.append([leepgm('prueba/63.pgm'),[0,0,0,0,0,0,1]])

	conjunto_prueba.append([leepgm('prueba/64.pgm'),[1,0,0,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/65.pgm'),[0,1,0,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/66.pgm'),[0,0,1,0,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/67.pgm'),[0,0,0,1,0,0,0]])
	conjunto_prueba.append([leepgm('prueba/68.pgm'),[0,0,0,0,1,0,0]])
	conjunto_prueba.append([leepgm('prueba/69.pgm'),[0,0,0,0,0,1,0]])
	conjunto_prueba.append([leepgm('prueba/70.pgm'),[0,0,0,0,0,0,1]])
	
	#-------------------- MODIFICACIÓN ------------------------------
	for par_img_solucion in conjunto_entrenamiento:
		par_img_solucion[0]=comprimir_vector_imagen(par_img_solucion[0],bloque,lado)

	for par_img_solucion in conjunto_prueba:
		par_img_solucion[0]=comprimir_vector_imagen(par_img_solucion[0],bloque,lado)
    #----------------------------------------------------------------

    #Asigno la arquitectura
	red_neuronal.append(perceptrones)
	red_neuronal.append(conjunto_entrenamiento)
	red_neuronal.append(conjunto_prueba)
	red_neuronal.append(factor)
	
	return red_neuronal