import csv

with open('../../data/Cap1/subvenciones.csv', encoding='latin1') as fichero_csv:
    lector = csv.reader(fichero_csv)
    next(lector, None)  # Se salta la cabecera
    importe_total = 0
    for linea in lector:
        importe_str = linea[2]
        importe = float(importe_str)
        importe_total = importe_total + importe
    print(importe_total)