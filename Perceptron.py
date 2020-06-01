import numpy as np
import random as rd

class Perceptron:

	# definindo numero de epocas e bias 
	epocas = 50
	bias = 1.0 		
	perceptrons = 10

	# importando os datasets com pickle
	import pickle 
	with open("C:/Users/Jess/github/mnist-perceptron/pickled_mnist.pkl", "rb") as fh:
		data = pickle.load(fh)

	treino = data[0]
	teste = data[1]

	# embaralhando os dados
	def shuffle_dataset(data):
		shuffle_dataset = data
	    np.random.shuffle(shuffle_dataset)
	    return shuffle_dataset

	# print(teste)

	# treino_embaralhado = teste  # make a copy
	# np.random.shuffle(treino_embaralhado)
	# print("treino embaralhado:")
	# print(treino_embaralhado)

	# print(treino)

	# teste_embaralhado = teste  # make a copy
	# np.random.shuffle(teste_embaralhado)
	# print("teste embaralhado:")
	# print(teste_embaralhado)

	# gerando os pesos aleatorios para as 785 entradas
	def random_weights():
		weights = np.zeros(785)
		for i, j in enumerate(weights):
			weights[i] = rd.uniform(-0.5, 0.5)
		return weights

	# print(random_weights())

	# soma ponderada das entradas
	# def net_input(amostras, pesos):
	# 	taxa_aprendizado = 0.01
	# 	net = 0
	# 	erro = 0
	# 	pesos = random_weights()
	# 	for linha in range(amostras.shape[0]):
	# 		rotulo = amostras[linha, 0]
	# 		for j in range(amostras.shape[1]-1):
	# 			net += pesos[j+1] * amostras[linha][j+1]
	# 		net_sum = pesos[0] * bias + net
	# 		saida = check_result(rotulo, net_sum) # t_k
	# 		if(net_sum > 0):
	# 			y_k = 1
	# 		else:
	# 			y_k = 0
	# 		if(saida != 1):
	# 			pesos[0] = pesos[0] + taxa_aprendizado * (saida - y_k) * bias
	# 			for j in range(amostras.shape[1]-1):
	# 				pesos[j+1] = pesos[j+1] + taxa_aprendizado * (saida - y_k) * amostras[linha][j+1]
	# 	return net

	# confere resultado
	def check_result(resultado_esperado, label_amostra):
		if (resultado_esperado == label_amostra):
			return 1
		else:
			return 0

	# treina perceptron
	def train_perceptron():

		taxa_aprendizado = 0.01 # taxa inicial
		dados_embaralhados = shuffle_dataset(treino) # embaralhando os dados de treinamento

		amostras = dados_embaralhados
		pesos = random_weights()

		for i in range(epocas):
			net = 0
			erro = 0
			for linha in range(amostras.shape[0]):
				rotulo = amostras[linha, 0]
				for j in range(amostras.shape[1]-1):
					net += pesos[j+1] * amostras[linha][j+1]
				net_sum = pesos[0] * bias + net
				saida = check_result(rotulo, net_sum) # t_k
				if(net_sum > 0):
					y_k = 1
				else:
					y_k = 0
				if(saida != 1):
					pesos[0] = pesos[0] + taxa_aprendizado * (saida - y_k) * bias
					for j in range(amostras.shape[1]-1):
						pesos[j+1] = pesos[j+1] + taxa_aprendizado * (saida - y_k) * amostras[linha][j+1]

		
			
	# serao treinados dez perceptrons um para cada digito

