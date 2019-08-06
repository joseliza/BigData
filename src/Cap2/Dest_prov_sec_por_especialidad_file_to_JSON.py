import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1920x1800')
driver = webdriver.Chrome(options = chrome_options)

# Página XX de la especialidad de matemáticas PES
url = "file:///home/joseliza/Descargas/Matematicas-p18.html"
driver.get(url)

# Obtenemos apellidos y nombres de todas las personas en la página
datos = driver.find_elements_by_tag_name("a")

# Los introducimos en una lista llamada nombres (he tenido problemas y por eso la meto en una estructura
# propia de python, no de selenium)
lista = []
for i in datos:
    lista.append(i.text)

# Como en la lista se nos han colocado cuatro tags con nombre "a" (son enlaces al principio de la página),
# los eliminamos:
lista.pop(0)
lista.pop(0)
lista.pop(0)
lista.pop(0)

## PRUEBA PARA LA PRIMERA PERSONA
persona = driver.find_element_by_link_text(lista[0])
## Imprimo apellidos y nombre
print (persona.text)

# Entramos en el enlace que aparece en el nombre de la persona
persona.click()

# Extraemos colectivo
colectivo = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/center[2]/table/tbody/tr/td/em")
## Imprimo colectivo
print (colectivo.text)

# Extraemos tiempo de servicio
tiempo = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/center[3]/table/tbody/tr/td")
## Imprimo tiempo de servicio
print (tiempo.text)

# Extraemos cuerpo
cuerpo = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[2]/center/table/tbody/tr[1]/td")
## Imprimo cuerpo
print (cuerpo.text)

# Extraemos puesto
puesto = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[2]/center/table/tbody/tr[2]/td")
## Imprimo cuerpo
print (puesto.text)

# Extraemos centro
centro = driver.find_elements_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[2]/center/table/tbody/tr[3]/td/font")
## Imprimo centro
for i in centro:
    print ('"' + i.text + '"')



# Abrimos fichero para volcar los datos en él
#f = open("/home/joseliza/Matematicas1.txt", "a")

# count = 0
# # Miramos la información extendida de cada persona (recorremos la lista de personas haciendo click en cada una):
# for nombre in lista:
#     print (len(lista)-count)
#     count += 1
#     persona = driver.find_element_by_link_text(nombre)
#     persona.click()
#     informacion = driver.find_elements_by_xpath("//*[@id='example']/tbody/tr")
#     for extra in informacion:
#         f.write(extra.text + os.linesep)
#     driver.back()

#f.close()





