"""Este fichero contiene los métodos relativos al algoritmo
de retropropagación: fase de barrido hacia adelante y fase de actualización de pesos."""

from clases import *

#### Función que realiza el barrido frontal para un único ejemplo, pensado para ejecución secuencial con conjunto de entrenamiento.
def frontal(par_imagen_solucion, lista_perceptrones): #Tanto la red de conexiones como la función de activación son parte de lista_perceptrones.

	solucion = []

	# 1) Asigno los valores de salida a las neuronas de la capa inicial.
	i=0
	while i<len(par_imagen_solucion[0]): # [0] se refiere a la parte del par que contiene los pixeles de la imagen.
		lista_perceptrones[0][i].salida=par_imagen_solucion[0][i] # asigno el valor del pixel a la salida de cada neurona de la primera capa.
		i+=1
  
	# 2) Calculo salidas del resto de capas.
	i=0
	while i<len(lista_perceptrones)-1: #Hay un bloque menos de conexiones que de capas.
		for percep in lista_perceptrones[i+1]: #Me salto la primera capa y comienzo en la siguiente
			aux_calc = 0 #Almaceno los resultados parciales de cada conex a esa neurona.
			for conex in percep.conex_in:
				aux_calc += conex.peso*lista_perceptrones[i][conex.idx_in].salida #Esto es el sumatorio de wi*xi de cada entrante.
			percep.salida = percep.activa(aux_calc + (-1)*percep.bias)
		i+=1
   
	# 3) Devuelvo la solución.
	for percep in lista_perceptrones[len(lista_perceptrones)-1]:
		solucion.append(percep.salida)
		
	return solucion

	
#### Función que realiza un barrido frontal para todo un conjunto, a efectos de mostrar la salida de la red.	
def frontal_paralelo(conjunto_entrenamiento, lista_perceptrones):

    #Aquí se guarda el conjunto completo de soluciones.
	resultado_ejecucion_hacia_adelante = []
	
	for par_imagen_solucion in conjunto_entrenamiento:
		sol_caso_particular = []

		# 1) Asigno los valores de salida a las neuronas de la capa inicial.
		i=0
		while i<len(par_imagen_solucion[0]): # [0] se refiere a la parte del par que contiene los pixeles de la imagen.
			lista_perceptrones[0][i].salida=par_imagen_solucion[0][i] # asigno el valor del pixel a la salida de cada neurona de la primera capa.
			i+=1
	  
		# 2) Calculo salidas del resto de capas.
		i=0
		while i<len(lista_perceptrones)-1: #Hay un bloque menos de conexiones que de capas.
			for percep in lista_perceptrones[i+1]: #Me salto la primera capa y comienzo en la siguiente
				aux_calc = 0 #Almaceno los resultados parciales de cada conex a esa neurona.
				for conex in percep.conex_in:
					aux_calc += conex.peso * lista_perceptrones[i][conex.idx_in].salida #esto es el sumatorio de wi*xi de cada entrante.
				percep.salida = percep.activa(aux_calc + (-1)*percep.bias)
			i+=1
	   
		# 3) Almaceno las soluciones de este par.
		for percep in lista_perceptrones[len(lista_perceptrones)-1]:
			sol_caso_particular.append(percep.salida)
			
		resultado_ejecucion_hacia_adelante.append(sol_caso_particular)
		
	return resultado_ejecucion_hacia_adelante
	
	
#### Función que actualiza los pesos hacia atrás en función del error cometido.
def actualiza_pesos(par_imagen_solucion, lista_perceptrones, factor_aprendizaje):

	# 1) Asigno un delta_i de error a cada perceptrón de salida.
	for percep in lista_perceptrones[len(lista_perceptrones)-1]: #Trabajamos con la capa de salida.
		percep.delta = percep.salida * (1-percep.salida) * (par_imagen_solucion[1][percep.idx]-percep.salida)
		aux = factor_aprendizaje * (-1) * percep.delta
		percep.bias += aux
		percep.momentum = aux
		
	
	# 2) Por cada capa anterior a la salida, asigno un delta_j a sus perceptrones y actualizo sus pesos.
	l=len(lista_perceptrones)-2 #Comienza en la capa anterior a la salida.
	
	while l>=0:	
		if l>0: #Si no nos encontramos en la capa de entrada, es necesario calcular deltas nuevos.
			for percep in lista_perceptrones[l]: #Por cada perceptrón de la capa...
				aux_calc = 0 #Resultado parcial para la implementación de delta_j.
				for conex in percep.conex_out:
					aux_calc += conex.peso * lista_perceptrones[l+1][conex.idx_out].delta
				percep.delta = percep.salida * (1-percep.salida) * aux_calc #Esto es el g'(inj) * suma(wji)*delta_i.
		
		#Calculamos los pesos actualizados.
		for percep in lista_perceptrones[l]:
			x = factor_aprendizaje * (-1) * percep.delta
			percep.bias += aux
			percep.momentum = aux
			for conex in percep.conex_out:
				aux = factor_aprendizaje * percep.salida * lista_perceptrones[l+1][conex.idx_out].delta
				conex.peso += aux #Esto es el wji <- wji + eta + aj + delta_i.
				conex.momentum = aux
		l-=1
		
def actualiza_pesos_con_momentum(par_imagen_solucion, lista_perceptrones, factor_aprendizaje, factor_momentum):

	# 1) Asigno un delta_i de error a cada perceptrón de salida.
	for percep in lista_perceptrones[len(lista_perceptrones)-1]: #Trabajamos con la capa de salida.
		percep.delta = percep.salida * (1-percep.salida) * (par_imagen_solucion[1][percep.idx]-percep.salida)
		aux = factor_aprendizaje * (-1) * percep.delta
		percep.bias += aux + (factor_momentum*percep.momentum)
		percep.momentum = aux
	
	# 2) Por cada capa anterior a la salida, asigno un delta_j a sus perceptrones y actualizo sus pesos.
	l=len(lista_perceptrones)-2 #Comienza en la capa anterior a la salida.
	
	i=1
	while l>=0:	
		if l>0: #Si no nos encontramos en la capa de entrada, es necesario calcular deltas nuevos.
			for percep in lista_perceptrones[l]: #Por cada perceptrón de la capa...
				aux_calc = 0 #Resultado parcial para la implementación de delta_j.
				for conex in percep.conex_out:
					aux_calc += conex.peso * lista_perceptrones[l+1][conex.idx_out].delta
				percep.delta = percep.salida * (1-percep.salida) * aux_calc #Esto es el g'(inj) * suma(wji)*delta_i.
		
		#Calculamos los pesos actualizados.
		for percep in lista_perceptrones[l]:
			x = factor_aprendizaje * (-1) * percep.delta
			percep.bias += x + (factor_momentum*percep.momentum)
			percep.momentum = x
			for conex in percep.conex_out:
				aux = factor_aprendizaje * percep.salida * lista_perceptrones[l+1][conex.idx_out].delta
				conex.peso += aux + (factor_momentum*conex.momentum) #Esto es el wji <- wji + eta + aj + delta_i.
				conex.momentum = aux
			i+=1
		l-=1