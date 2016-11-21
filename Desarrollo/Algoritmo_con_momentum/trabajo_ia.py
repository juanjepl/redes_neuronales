""" Trabajo para la asignatura de IA del curso 2015-16 por los alumnos
    Juan Jesús Pérez Luna y Gonzalo Delgado Chaves"""


import time
from clases import *
from interfaz import *
from inicializa import * 
from retroprop import *  


## Ejecución.
"""Obtengo los parámetros de configuración
para la red neuronal a través de la información
recibida de la interfaz de usuario"""
config_red = ejecuta_interfaz()

"""Le paso como parámetro la configuración de red, y
me devuelve la arquitectura de la red neuronal ya inicializada"""
red_neuronal_inicial = inicializa_red(config_red)

# Arquitectura de la red
lista_perceptrones = red_neuronal_inicial[0]
conjunto_entrenamiento = red_neuronal_inicial[1]
conjunto_prueba = red_neuronal_inicial[2]
factor_aprendizaje = red_neuronal_inicial[3]

cota_umbral = config_red[5]
lim_iteraciones = config_red[6]
factor_momentum = config_red[7]


msg_procesando() #Muestro mensaje de carga.
#Start crono
tiempo_inicial = time.clock()


#### Comienza la ejecución del algoritmo de retropropagación.

iteracion_actual = 0
cota_error = 1.0 #Inicializamos a un valor igual o mayor que la cota escogida para garantizar el primer pase.


while cota_error > cota_umbral and iteracion_actual < lim_iteraciones:
	sumas_errores_en_cada_it = 0.0
	
	for par_imagen_solucion in conjunto_entrenamiento:

		suma_errores = 0.0 # Aquí se hará el sumatorio del error de cada ejemplo de entrenamiento, para hacer la media.
		
		#### Ejecucion de fase hacia adelante.
		resultado_frontal = frontal(par_imagen_solucion, lista_perceptrones)

		#### Calculo de errores
		diferencia_soluciones=[]
		i=0
		while(i<len(resultado_frontal)):
			diferencia_soluciones.append((par_imagen_solucion[1][i]-resultado_frontal[i])**2)
			i+=1
		
		suma_cuadrados = 0.0
		for cuadrad in diferencia_soluciones: #sumo los cuadrados
			suma_cuadrados += cuadrad

		suma_errores=(1/len(resultado_frontal)) * suma_cuadrados #Termino la fórmula del error cuadrático aplicado a las salidas.
		#### Propagación de error hacia atrás.
		if iteracion_actual == 0:
			actualiza_pesos(par_imagen_solucion, lista_perceptrones, factor_aprendizaje)
		else:
			actualiza_pesos_con_momentum(par_imagen_solucion, lista_perceptrones, factor_aprendizaje, factor_momentum)

		sumas_errores_en_cada_it+=suma_errores

	print('Iteración '+str(iteracion_actual+1)+' completada.')
	iteracion_actual+=1
	cota_error = (1/len(conjunto_entrenamiento)) * sumas_errores_en_cada_it
	
#### Obtenemos los pesos tras haber entrenado la red.

print('\n')
print('Red entrenada tras '+str(iteracion_actual)+' iteraciones. Evaluando conjunto de prueba.')


# Hago el barrido frontal paralelo de las pruebas --------------------------

res_ejec_conj_pruebas = frontal_paralelo(conjunto_prueba,lista_perceptrones)

# Interpreto los resultados y los muestro por pantalla ---------------------

#ajusto formato.
aux_sol_esperadas=[]
for solu in conjunto_prueba:
	aux_sol_esperadas.append(solu[1])


i=0
resultados_obtenidos = []
resultados_esperados = []
for cada_solucion in res_ejec_conj_pruebas:
	resultados_obtenidos.append(interpreta_salida(cada_solucion))
	resultados_esperados.append(interpreta_salida(aux_sol_esperadas[i])) 
	i+=1

msg_resultados(resultados_obtenidos, resultados_esperados)

tiempo_final = time.clock()
print(' ')
print('    Tiempo de ejecución: '+str(tiempo_final)+ ' segundos.')
print(' ')

volcado_pesos(lista_perceptrones)