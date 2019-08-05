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

# Obtenemos nombres y apellidos de todas las personas en la página
datos = driver.find_elements_by_tag_name("a")

# Los introducimos en una lista llamada nombres
lista = []
for i in datos:
    lista.append(i.text)



# Como en la lista se nos han colocado cuatro tags con nombre "a" enlaces al principio, los eliminamos:
lista.pop(0)
lista.pop(0)
lista.pop(0)
lista.pop(0)

# Abrimos fichero para volcar los datos en él
f = open("/home/joseliza/Matematicas1.txt", "a")

count = 0
# Miramos la información extendida de cada persona (recorremos la lista de personas haciendo click en cada una):
for nombre in lista:
    print (len(lista)-count)
    count += 1
    persona = driver.find_element_by_link_text(nombre)
    persona.click()
    informacion = driver.find_elements_by_xpath("//*[@id='example']/tbody/tr")
    for extra in informacion:
        f.write(extra.text + os.linesep)
    driver.back()

f.close()





