#Fazer um programa que dado uma função linear, vai criar um training set para o programa achar a função de volta.
import random
import matplotlib.pyplot as plt
import numpy as np

T = 5 #Tamanho
I = random.randrange(-10, 10) #Inclinacao
pontos = [[],[]]

for i in range(10):
    xi = random.uniform(-T, T)
    e = random.gauss(0, 1) #erro
    pontos[0].append(xi) 
    pontos[1].append(xi*I + e)

def regression(pontos):
    tetha = 0
    lista_erros=[]
    for i in range(len((pontos[0]))):
        E = 0 #erro total
        tetha = pontos[1][i]/pontos[0][i]
        for i in range(len((pontos[0]))):
            E += (pontos[0][i]*tetha - pontos[1][i])**2
        lista_erros.append(E)
    temp = min(lista_erros) #achar menor elemento da lista
    res = [i for i, j in enumerate(lista_erros) if j == temp] #achar posicao do menor elemento
    tetha = tetha = pontos[1][res[0]]/pontos[0][res[0]]
    return tetha



inclinacao = regression(pontos)
plt.plot(pontos[0],pontos[1], 'o')
plt.plot([-5,5],[-5*inclinacao,5*inclinacao])
plt.show()

