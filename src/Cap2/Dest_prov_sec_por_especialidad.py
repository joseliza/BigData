#from selenium.webdriver.support.ui import Select
from selenium import webdriver

driver = webdriver.Chrome()
url = "http://www.juntadeandalucia.es/educacion/vscripts/dgprh/efectivos/Sp2019/"
driver.get(url)

# Consulta por cuerpo y puesto. Debemos introducir los datos en las variables.
cuer = "590" # 590 --> Secundaria
pues = "00590006" # 00590006 --> Matemáticas
ord = "SI" # SI --> Orden de adjudicación, NO --> Orden alfabético

cuerpo = driver.find_element_by_name("CUERPO")
cuerpo.send_keys(cuer)
#puesto = Select(driver.find_element_by_name("Puesto"))
#puesto.select_by_index(2)
orden = driver.find_element_by_name("APA")
orden.send_keys(ord)

#acepta_centro = driver.find_element_by_xpath("/html/body/div[3]/div/div[3]/div[2]/form/div[2]/input")
#acepta_centro.click()

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





