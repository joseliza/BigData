from selenium import webdriver
driver = webdriver.Chrome()
url = "file:///home/joseliza/Descargas/41700415.html"
driver.get(url)

# Consulta por centro. Debemos introducir el código en la variable cod.
# centro = driver.find_element_by_name("CENADJ")
# cod = "41700415"
# centro.send_keys(cod)
# acepta_centro = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[2]/form/div[2]/input")
# acepta_centro.click()

# Obtenemos nombres y apellidos de todas las personas
datos = driver.find_elements_by_xpath("//*[@id='example']/tbody/tr/td/a")
# Los introducimos en una lista llamada nombres
lista = []
for i in datos:
    lista.append(i.text)

# Miramos la información extendida de cada persona (recorremos la lista de personas haciendo click en cada una):
for nombre in lista:
    persona = driver.find_element_by_link_text(nombre)
    persona.click()
    informacion = driver.find_elements_by_xpath("//*[@id='example']/tbody/tr")
    for extra in informacion:
        print(extra.text)
    driver.back()





