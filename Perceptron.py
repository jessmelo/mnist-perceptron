import numpy as np
import random as rd

epocas = 50

# importando os datasets
dir_path = "C:/Users/Jess/Documents/USP/2020.1/IA/Conjuntos MNIST/"
treino = np.loadtxt(dir_path + '/mnist_treinamento.csv', dtype = float, delimiter = ',')
teste = np.loadtxt(dir_path + '/mnist_teste.csv', dtype = float, delimiter = ',')

# embaralhando os dados

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
	for i in amostras[]:
		for j in amostras:
			net += pesos[j] * amostras[i][j]
	return net

