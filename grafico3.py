from turtle import color
from matplotlib import colors
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display


dados_main = pd.read_excel('dadosGrafico.xlsx')
##display(dados_main)

controles = ['BVAR', 'TE', 'VAR', 'STRESS']

list_x = []
list_y = []
cores_alerts = ['blue', 'yellow', 'red']
list_cores = []

# for i in range(1,3):
#     print(i)
#
# quit()

for i, v in enumerate(controles):
    for index in range(1,4):

        # filtrar tipo de controle
        filtro = dados_main['Controle'] == v
        dados_gerados = dados_main[filtro]
        
        if dados_gerados[dados_gerados['NivelAlerta'] == index]['NivelAlerta'].count() > 0:
            #somar quantidade de alertas por tipo de controle
            qtd_alertas = dados_gerados[dados_gerados['NivelAlerta'] == index]['NivelAlerta'].count()
            legenda = v + ' ' + str(index)
            list_x.append(legenda)
            list_y.append(qtd_alertas)
            list_cores.append(cores_alerts[index - 1])


plt.figure(figsize=(14,7))
y = np.array(list_y)
x = np.array(list_x)
fig = plt.bar(x,y, color = list_cores)
plt.title("Alertas Por Métrica")
plt.xlabel('Métrica')
plt.ylabel('Quantidade de ALertas')
plt.bar_label(fig)
plt.savefig('teste.jpg', format='jpg')
plt.show()

