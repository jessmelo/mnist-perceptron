import numpy as np
    
# importando os datasets

dir_path = "C:/Users/Jess/Documents/USP/2020.1/IA/Conjuntos MNIST/"
# treino = np.loadtxt(dir_path + '/mnist_treinamento.csv', dtype = float, delimiter = ',')
# teste2 = np.loadtxt(dir_path + '/mnist_teste.csv', dtype = float, delimiter = ',')

# usando o pickle para rodar mais rapido

import pickle

# with open("C:/Users/Jess/github/mnist-perceptron/pickled_mnist.pkl", "bw") as fh:
# 	data = (
#         treino, 
#         teste)
# 	pickle.dump(data, fh)

with open("C:/Users/Jess/github/mnist-perceptron/pickled_mnist.pkl", "rb") as fh:
	data = pickle.load(fh)

treino = data[0]
teste = data[1]

# embaralhando os dados
from random import shuffle 

def shuffle_dataset(data):
    shuffle_dataset = np.random.shuffle(data)
    print(shuffle_dataset)

print(teste)

teste_embaralhado = teste  # make a copy
shuffle_dataset = np.random.shuffle(teste_embaralhado)
print("proximo")
print(teste_embaralhado)
