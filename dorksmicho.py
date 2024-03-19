#run python3 -m pip install googlesearch-python
from google import search

# Lista de dorks
dorks = [
    "site:pastebin.com {usuario} OR {correo}",
    "site:github.com {usuario} OR {correo}",
    "site:pastiebin.com {usuario} OR {correo}",
    "site:hastebin.com {usuario} OR {correo}",
    "site:0bin.net {usuario} OR {correo}",
    "site:ghostbin.com {usuario} OR {correo}",
    "site:justpaste.it {usuario} OR {correo}",
    "site:dpaste.com {usuario} OR {correo}",
    "site:codepad.co {usuario} OR {correo}",
    "site:sourceforge.net {usuario} OR {correo}",
    "site:scribd.com {usuario} OR {correo}",
    "site:slideshare.net {usuario} OR {correo}",
    "site:docs.google.com {usuario} OR {correo}",
    "site:linkedin.com {usuario} OR {correo}",
    "site:facebook.com {usuario} OR {correo}",
    "site:instagram.com {usuario} OR {correo}",
    "site:twitter.com {usuario} OR {correo}",
    "site:reddit.com {usuario} OR {correo}",
    "site:quora.com {usuario} OR {correo}",
    "site:meetup.com {usuario} OR {correo}"
]

# Función para realizar la búsqueda
def buscar_dorks(dorks, usuario, correo):
    resultados = []
    for dork in dorks:
        dork_format = dork.format(usuario=usuario, correo=correo)
        print(f"Buscando: {dork_format}")
        try:
            # Realizar la búsqueda
            for url in search(dork_format, num=5, pause=2):  # Limitar manualmente la cantidad de resultados
                resultados.append(url)
                if len(resultados) >= 5:  # Limitar a 5 resultados
                    break
        except Exception as e:
            print(f"Error en la búsqueda: {e}")
    return resultados

# Función para imprimir los resultados
def imprimir_resultados(resultados):
    if resultados:
        print("Resultados encontrados:")
        for i, url in enumerate(resultados, start=1):
            print(f"{i}. {url}")
    else:
        print("No se encontraron resultados relevantes.")

# Entrada de datos
usuario = input("Ingrese su nombre de usuario: ")
correo = input("Ingrese su correo electrónico: ")

# Ejecutar la búsqueda y mostrar los resultados
resultados = buscar_dorks(dorks, usuario, correo)
imprimir_resultados(resultados)
