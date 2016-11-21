"""isdigit() solo nos sirve para detectar enteros
en las cadenas, para los float usamos este."""

def num_valido(s):
    try:
        float(s)
        return True
    except ValueError:
        return False
		
def interpreta_salida(caso_de_prueba): #Traduce la matriz de salidas del conjunto de prueba a letras.

	dic = {0:'d',1:'f',2:'h',3:'j',4:'l',5:'n',6:'p'}

	neurona_activa=0 #Índice de esa neurona.
	valor_neurona_activa=0 #Su valor.
	concluyente=True

	for dato in caso_de_prueba:
		if dato > valor_neurona_activa:
			valor_neurona_activa=dato
			neurona_activa=caso_de_prueba.index(dato)
		
	#Ahora compruebo que no haya repetidos (No sería concluyente el resultado)
	a_batir=max(caso_de_prueba)
	ocurrencias=0
	for elem in caso_de_prueba:
		if elem == a_batir:
			ocurrencias+=1
	if ocurrencias > 1:
		concluyente=False
			
	
	salida_obtenida=dic[neurona_activa]
	if(not concluyente):
		salida_obtenida='*' #Valores repetidos, no concluyente.

	return salida_obtenida