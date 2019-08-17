import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1920x1800')
driver = webdriver.Chrome(options = chrome_options)

# Página XX de la especialidad de matemáticas PES
url = "file:///home/joseliza/Descargas/Matematicas-p19.html"
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

# Abrimos fichero para volcar los datos en él
f = open("/home/joseliza/Matematicas1.json", "a")

## Escribo apertura de corchete (debo hacerlo sólo si acabo de crear el fichero o si estaba vacío)
## Por hacer
f.write("[")

count = 0
# Miramos la información extendida de cada persona (recorremos la lista de personas haciendo click en cada una):
for nombre in lista:
    print (len(lista)-count)
    count += 1

    # Escribo llave de apertura de campo
    f.write("{")

    persona = driver.find_element_by_link_text(nombre)
    # Escribo apellidos y nombre en archivo
    f.write ("Persona:"+'"'+persona.text+'",')

    # Entramos en el enlace que aparece en el nombre de la persona
    ##persona.click()

    # Extraemos colectivo
    colectivo=persona
    ##colectivo = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/center[2]/table/tbody/tr/td/em")
    # Escribo colectivo en archivo
    f.write ("Colectivo:"+'"'+colectivo.text+'",')

    # Extraemos tiempo de servicio
    tiempo=persona
    ##tiempo = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div[1]/div/div[2]/center[3]/table/tbody/tr/td")
    # Escribo tiempo de servicio en archivo
    f.write ("Tiempo:"+'"'+tiempo.text+'",')

    # Extraemos cuerpo
    cuerpo=persona
    ##cuerpo = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[2]/center/table/tbody/tr[1]/td")
    # Escribo cuerpo en archivo
    f.write ("Cuerpo:"+'"'+cuerpo.text+'",')

    # Extraemos puesto
    puesto=persona
    ##puesto = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[2]/center/table/tbody/tr[2]/td")
    # Escribo puesto en archivo
    f.write ("Puesto:"+'"'+puesto.text+'",')

    # Extraemos centro
    centro=persona
    ##centro = driver.find_elements_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div[2]/div/div[2]/center/table/tbody/tr[3]/td/font")
    # Escribo centro en archivo
    ##for i in centro:
    ##    f.write ("Centro:"+'"' + i.text + '"' + os.linesep)

    # Escribo llave de cierre de campo
    ## La coma no se escribe si es la última llave. Esto queda por hacer
    f.write("},")

    # Vuelvo a página anterior (lista de personas)
    #driver.back()

## Escribo cierre de corchete (debo hacerlo sólo si acabo de crear el fichero o si estaba vacío)
## Por hacer
f.write("]")
f.close()





