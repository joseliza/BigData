import csv

# Las filas se tratan como listas
# with open('../../data/Cap1/subvenciones.csv', encoding='latin1') as fichero_csv:
#     lector = csv.reader(fichero_csv)
#     next(lector, None)  # Se salta la cabecera
#     importe_total = 0
#     for linea in lector:
#         importe = float(linea[2])
#         importe_total = importe_total + importe
#     print(importe_total)

# Las filas se tratan como diccionarios

with open('../../data/Cap1/subvenciones.csv', encoding='latin1') as fichero_csv:
    dic_lector = csv.DictReader(fichero_csv)
    asocs = {}
    for linea in dic_lector:
        centro = linea['Asociación']
        print(centro)