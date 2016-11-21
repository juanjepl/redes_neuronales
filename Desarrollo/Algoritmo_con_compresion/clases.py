"""Este fichero contiene las definiciones de
clases y funciones que utilizará el algorimo"""

import math #Es usado por el sigmoide

# Clases Perceptron y conexion

class Perceptron(object):
	def __init__(self,idx,bias):
		self.idx = idx #Índice dentro de su capa, con el objetivo de acceder directamente
		self.bias = bias
		self.salida = 0 # Provisionalmente a cero hasta que la activación se calcule
		self.conex_in = []
		self.conex_out = []
		self.delta = 0.0
		
	def activa(self, input):
		return 1 / (1 + math.exp(-input))
    
	def __str__(self):
		return "Perceptron: "+ str(self.idx) +" bias: "+ str(self.bias) +" salida: "+ str(self.salida)

    
class Conexion(object):
    def __init__(self,peso,idx_in,idx_out):
        self.peso = peso
        self.idx_in = idx_in
        self.idx_out = idx_out
    
    def __str__(self):
        return 'Interconecta neuronas: '+ str(self.idx_in) + ' y '+ str(self.idx_out) + ' Peso: ' + str(self.peso)    