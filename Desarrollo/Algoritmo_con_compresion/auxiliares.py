"""isdigit() solo nos sirve para detectar enteros
en las cadenas, para los float usamos este."""

def num_valido(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def comprimir_vector_imagen(vect,factor,tam_l):

    
    solucion_matriz=[]
    solucion_vector=[] 
    m=[] 
    # Convierto a formato matricial (no una fila sola)
    i=0
    while i<len(vect):
        fila=vect[i:i+tam_l]
        m.append(fila)
        i+=tam_l

    m_comprimida = []
    #Índices i_principio, i_final, j_principio, j_final... proceso las submatrices.
    i_p=0
    i_f=factor
    while i_p<len(m):
        fila_comprimida = []
        j_p=0
        j_f=factor
        while j_p<tam_l:
            suma_submatriz=0
            for fila in m[i_p:i_f]: #recorro las filas seleccionadas
                suma_subfila=0
                for celda in fila[j_p:j_f]: #recorro las celdas del trozo de fila seleccionado.
                    suma_subfila+=celda
                suma_submatriz+=suma_subfila
                
            if suma_submatriz >= ((factor*factor)/2): #1 si es la mitad o superior
                fila_comprimida.append(1)
            else:
                fila_comprimida.append(0)

            j_p+=factor
            j_f+=factor
            
        m_comprimida.append(fila_comprimida)
        i_p+=factor
        i_f+=factor

        #Asigno la version comprimida.
        solucion_matriz=m_comprimida

    #Vuelvo a convertir la solucion de forma matricial a un único vector.
    for fila in solucion_matriz:
        for celda in fila:
            solucion_vector.append(celda)
    
    return solucion_vector


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