import webbrowser
import platform
import time
import subprocess

# Nuevos enlaces que se abrirán en Google Chrome
urls = [
    "https://namechk.com/",
    "https://intelx.io/",
    "https://checkusernames.com/",
    "https://instantusername.com/",
    "https://www.google.com/search?q=site:amazon.com+%3Cusername%3E",
    "https://api.github.com/users/%3Cusername%3E/events/public",
    "https://www.secureito.com/"
    "https://www.gotinder.com/@%3Cusername%3E",
    "https://www.skymem.info/",
    "https://emailrep.io/",
    "https://www.mailboxvalidator.com/plans#bulk",
    "https://www.vigilante.pw/",
    "https://www.vigilante.pw/",
    "https://haveibeenpwned.com/",
    "https://www.facebook.com/public?query=email@gmail.com&nomc=0",
    "https://www.facebook.com/login/identify?ctx=recover",
    "https://lookup-id.com/",
    "https://www.facebook.com/login/identify",
    "https://epieos.com/",
    "https://haveibeenzuckered.com/",
    "https://whatsmyname.app/",
    "https://cybernews.com/personal-data-leak-check/",
    "https://pastebin.com/",
    "https://www.google.com.mx/",
    "https://duckduckgo.com/",
    "https://www.bing.com/",
    "https://www.facebook.com/",
    "https://twitter.com/"   
]

# Detectar el sistema operativo
system = platform.system()

# Definir la ruta de Google Chrome según el sistema operativo
if system == "Windows":
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # Ruta al ejecutable de Chrome en Windows
elif system == "Darwin":  # macOS
    chrome_path = "open -a /Applications/Google\ Chrome.app %s"
else:
    raise Exception("Sistema operativo no compatible")

# Abrir cada URL en una nueva pestaña de Google Chrome
for url in urls:
    if system == "Windows":
        webbrowser.get(chrome_path).open_new_tab(url)
    elif system == "Darwin":
        subprocess.call(chrome_path % url, shell=True)
    time.sleep(1)  # Esperar un segundo entre cada apertura de pestaña
