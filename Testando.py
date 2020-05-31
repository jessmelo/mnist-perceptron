import numpy as np
import matplotlib.pyplot as plt

# #importanto os csv's
# data = np.loadtxt('Conjuntos MNIST/mnist_teste.csv', dtype = float, delimiter = ',')
# # y = np.asarray(data[1:, 0:1], dtype='float')
# # X = np.asarray(data[1:,1:], dtype='float')

# print(data)
#pré-processamento

# def pre_processamento(data):
#     line = float
#     for a in np.nditer(data):
#         line = float(a) / 255
#         data[data.index(a)] = line
#     return data

# def pre_processamento(data):
#     line = float
#     for a in np.nditer(data):
#         a = float(a) / 255
#         print(a)

def pre_processamento(data):
    line = float
    rows = data.shape[0]
    cols = data.shape[1]
    for x in range(0, rows):
        for y in range(0, cols):
            line = data[x,y] / 255
            data[x, y] = line
    return data

    # for i, label in enumerate(labels_class):
    #  labels_class[i] = 1 if (label == classifier) else 0

teste = np.loadtxt('Conjuntos MNIST/mnist_teste.csv', dtype = float, delimiter = ',')
print(teste)
print(pre_processamento(teste))
# def pre_processamento(data):
#     with open('mnist_teste.csv') as file:
#         line = file.readline()
#     print("leu arquivo")
#     line = line.split(',')
#     for line in data
#         line[i] = float(line[i]) / 255
