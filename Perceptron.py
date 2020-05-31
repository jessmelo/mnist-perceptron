import numpy as np
import random as rd
import Datasets as ds 

class Perceptron:

	# definindo numero de epocas e bias 
	self.epocas = 50
	self.bias = 1.0 		

	# gerando os pesos aleatorios para as 785 entradas
	def random_weights():
		weights = np.zeros(785)
		for i, j in enumerate(weights):
			weights[i] = rd.uniform(-0.5, 0.5)
		return weights

	print(random_weights())

	# soma ponderada das entradas
	def net_input(amostras):
		net = 0
		pesos = random_weights()
		for i in amostras.shape[0]:
			for j in amostras:
				net += pesos[j] * amostras[i][j]
		return net


	# serao treinados dez perceptrons um para cada digito

