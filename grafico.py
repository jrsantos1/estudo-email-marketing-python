from turtle import color
from matplotlib import colors
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display


dados = pd.read_excel('dados.xlsx')
display(dados)

list_x = []
list_y = []
colors = []


if dados[dados['var'] > 0]['var'].count() > 0:
    var = dados[dados['var'] > 0]['var'].count()
    list_y.append(var)
    list_x.append('VaR 1')
    colors.append('blue')

if dados[dados['varAlerta2'] > 0]['varAlerta2'].count() > 0:
    varAlerta2 = dados[dados['varAlerta2'] > 0]['varAlerta2'].count()
    list_y.append(varAlerta2)
    list_x.append('VaR 2')
    colors.append('yellow')

if dados[dados['varAlerta3'] > 0]['varAlerta3'].count() > 0:
    varAlerta3 = dados[dados['varAlerta3'] > 0]['varAlerta3'].count()
    list_y.append(varAlerta3)
    list_x.append('VaR 3')
    colors.append('red')

if dados[dados['stress'] > 0]['stress'].count() > 0:
    stress = dados[dados['stress'] > 0]['stress'].count()
    list_y.append(stress)
    list_x.append('Stress 1')
    colors.append('blue')

if dados[dados['stressAlerta2'] > 0]['stressAlerta2'].count() > 0:
    stressAlerta2 = dados[dados['stressAlerta2'] > 0]['stressAlerta2'].count()
    list_y.append(stressAlerta2)
    list_x.append('Stress 2')
    colors.append('yellow')

if dados[dados['stressAlerta3'] > 0]['stressAlerta3'].count() > 0:
    stressAlerta3 = dados[dados['stressAlerta3'] > 0]['stressAlerta3'].count()
    list_y.append(stressAlerta3)
    list_x.append('Stress 3')
    colors.append('red')

if dados[dados['liquidez'] > 0]['liquidez'].count() > 0:
    liquidez = dados[dados['liquidez'] > 0]['liquidez'].count()
    list_y.append(liquidez)
    list_x.append('Liquidez 1')
    colors.append('blue')

if dados[dados['liquidezAlerta2'] > 0]['liquidezAlerta2'].count() > 0:
    liquidezAlerta2 = dados[dados['liquidezAlerta2'] > 0]['liquidezAlerta2'].count()
    list_y.append(liquidezAlerta2)
    list_x.append('Liquidez 2')
    colors.append('yellow')

if dados[dados['liquidezAlerta3'] > 0]['liquidezAlerta3'].count() > 0:
    liquidezAlerta3 = dados[dados['liquidezAlerta3'] > 0]['liquidezAlerta3'].count()
    list_y.append(liquidezAlerta3)
    list_x.append('Liquidez 3')
    colors.append('red')


y = np.array(list_y)
x = np.array(list_x)
fig = plt.bar(x,y, color=colors)
plt.title("Alertas Por Métrica")
plt.xlabel('Métrica')
plt.ylabel('Quantidade de ALertas')
plt.bar_label(fig)
plt.savefig('teste.jpg', format='jpg')
plt.show()

