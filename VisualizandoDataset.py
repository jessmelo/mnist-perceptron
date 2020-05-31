import numpy as np
import matplotlib.pyplot as plt

image_size = 28 # width and length
no_of_different_labels = 10 #  i.e. 0, 1, 2, 3, ..., 9
image_pixels = image_size * image_size
data_path = "C:/Users/Jess/Documents/USP/2020.1/IA/Conjuntos MNIST/"

test_data = np.loadtxt(data_path + "mnist_teste.csv", 
                       delimiter=",") 
print(test_data[:10])

print(test_data[test_data==255])
print(test_data.shape)

fac = 0.99 / 255
test_imgs = np.asfarray(test_data[:, 1:]) * fac + 0.01

for i in range(10):
    img = test_imgs[i].reshape((28,28))
    plt.imshow(img, cmap="Greys")
    plt.show()
