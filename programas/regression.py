#Fazer um programa que dado uma função linear, vai criar um training set para o programa achar a função de volta.
import random
import matplotlib.pyplot as plt
import numpy as np

T = 6.3 #Tamanho
I = random.randrange(-10, 10) #Inclinacao
pontosX = []
pontosY = []

def f(x,erro):
    return I*x+erro

for i in range(10):
    xi = random.uniform(-T, T)
    e = random.gauss(0, 4) #erro
    pontosX.append(xi) 
    pontosY.append(f(xi,e))

def estimar_coeficiente(x,y):
    tamanho = np.size(x)
    media_x = np.mean(x)
    media_y = np.mean(y)
    #Calculando o desvio
    x = np.array(x)
    y = np.array(y)
    desvio_xy = np.sum(x*y) - media_y*media_x*tamanho
    desvio_xx = np.sum(x*x) - (media_x**2)*tamanho
    coef_Reg = desvio_xy / desvio_xx
    ajuste = media_y - media_x*coef_Reg
    return (ajuste, coef_Reg)


def erro_min(pontosX, pontosY):
    tetha = 0
    lista_erros=[]
    for i in range(len((pontosX))):
        E = 0 #erro total
        tetha = pontosY[i]/pontosX[i]
        for i in range(len((pontosX))):
            E += (pontosX[i]*tetha - pontosY[i])**2
        lista_erros.append(E)
    temp = min(lista_erros) #achar menor elemento da lista
    res = [i for i, j in enumerate(lista_erros) if j == temp] #achar posicao do menor elemento
    tetha = pontosY[res[0]]/pontosX[res[0]]
    return tetha

#def regression(pontos):
    #Pegar a derivada
    #Fazer ela ser minimizada (ir para 0)
    


inclinacao = erro_min(pontosX, pontosY)
plt.plot(pontosX,pontosY, 'o') #Azul
print(pontosX)
b,a = estimar_coeficiente(pontosX, pontosY)
plt.plot([-5,5],[-a*5+b,a*5+b]) #Laranja
#plt.plot([-5,5],[-5*I,5*I]) #verde
plt.show()

