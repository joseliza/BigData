import json
# importar el módulo pyplot
import matplotlib.pyplot as plt

with open('../../data/Aemet/Granada.json') as fich:
    datos_grx = json.load(fich)

with open('../../data/Aemet/Sevilla.json') as fich:
    datos_svq = json.load(fich)

print(len(datos_grx))
print(len(datos_svq))

grx_temp = []
grx_date = []
svq_temp = []
svq_date = []
count = 1

for elemento in datos_grx:
    if 'tmax' in elemento:
        grx_temp.append(float(elemento['tmax'].replace(',','.')))
        grx_date.append(elemento['fecha'])

for elemento in datos_svq:
    if 'tmax' in elemento:
        svq_temp.append(float(elemento['tmax'].replace(',','.')))
        svq_date.append(elemento['fecha'])


plt.plot(grx_date, grx_temp)
plt.plot(svq_date, svq_temp)
plt.xlabel('fecha')
plt.ylabel('temperatura')
plt.show()