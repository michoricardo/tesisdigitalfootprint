import webbrowser
import platform
import time
import subprocess

# Nuevos enlaces que se abrirán en Google Chrome

# Grupo 1: URLs para correos electrónicos
urls_email = [
    "https://emailrep.io/",
    "https://dehashed.com/",
    "https://haveibeenpwned.com/",
    "https://epieos.com/",
    "intelx.io/?s=correo_completo",
    "https://cybernews.com/personal-data-leak-check/",
    "https://pastebin.com/search?q=correo_completo",
    "https://www.secureito.com/",
    "https://yandex.com/search/?text=\"correo_completo\"",
    "https://emailrep.io/query/correo_completo",
    "https://cavalier.hudsonrock.com/api/json/v2/preview/search-by-login/osint-tools?email=correo_completo",
    "https://cleantalk.org/email-checker/correo_completo",
    "https://leakix.net/search?scope=leak&q=\"correo_completo\"",
    "https://www.flickr.com/search/people/?q=correo_completo",
    "https://myspace.com/search/people?q=correo_completo",
    "https://scamsearch.io/search_report?searchoption=all&search=correo_completo",
    "https://whoxy.com/search.php?email=correo_completo",
    "https://whoisology.com/email/correo_completo",
    "https://hunter.io/email-verifier/correo_completo",
    "https://gmail-osint.activetk.jp/user_correo"
]

# Grupo 2: URLs para nombres de usuario
urls_username = [
    "https://namechk.com/",
    "https://checkusernames.com/",
    "https://instantusername.com/?q=nombre_usuario",
    "https://www.google.com/search?q=site:amazon.com+nombre_usuario",
    "https://api.github.com/users/nombre_usuario/events/public",
    "https://dehashed.com/",
    "https://www.facebook.com/login/identify?ctx=recover",
    "https://lookup-id.com/",
    "https://haveibeenzuckered.com/",
    "https://whatsmyname.app/",
    "https://pastebin.com/search?q=nombre_usuario",
    "https://www.google.com/search?q=\"nombre_usuario\"",
    "https://www.bing.com/search?q=\"nombre_usuario\"",
    "https://yandex.com/search/?text=\"nombre_usuario\"",
    "https://gravatar.com/nombre_usuario",
    "https://linktr.ee/nombre_usuario",
    "https://twitter.com/nombre_usuario",
    "https://www.facebook.com/nombre_usuario",
    "https://www.instagram.com/nombre_usuario",
    "https://www.tiktok.com/@nombre_usuario",
    "https://www.snapchat.com/add/nombre_usuario",
    "https://medium.com/@nombre_usuario",
    "https://tinder.com/@nombre_usuario",
    "https://www.youtube.com/nombre_usuario",
    "https://www.reddit.com/user/nombre_usuario/",
    "https://www.google.com/search?q=\"nombre_usuario@gmail.com\"OR\"nombre_usuario@yahoo.com\"OR\"nombre_usuario@hotmail.com\"OR\"nombre_usuario@protonmail.com\"OR\"nombre_usuario@live.com\"OR\"nombre_usuario@icloud.com\"OR\"nombre_usuario@yandex.com\"OR\"nombre_usuario@gmx.com\"OR\"nombre_usuario@mail.com\"OR\"nombre_usuario@mac.com\"OR\"nombre_usuario@me.com\""
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

# Pedir input al usuario
correo_completo = input("Introduce el correo completo: ")
nombre_usuario = input("Introduce el nombre de usuario: ")
user_correo = correo_completo.split('@')[0]

# Reemplazar las variables en las URLs
urls_email = [url.replace("correo_completo", correo_completo).replace("user_correo", user_correo) for url in urls_email]
urls_username = [url.replace("nombre_usuario", nombre_usuario) for url in urls_username]

# Función para abrir URLs en Google Chrome
def abrir_urls(urls):
    for url in urls:
        if system == "Windows":
            webbrowser.get(chrome_path).open_new_tab(url)
        elif system == "Darwin":
            subprocess.call(chrome_path % url, shell=True)
        time.sleep(1)  # Esperar un segundo entre cada apertura de pestaña

# Preguntar al usuario si desea abrir URLs del grupo 1
if input("¿Deseas abrir las URLs del grupo 1 (correos electrónicos)? (s/n): ").lower() == 's':
    abrir_urls(urls_email)

# Preguntar al usuario si desea abrir URLs del grupo 2
if input("¿Deseas abrir las URLs del grupo 2 (nombres de usuario)? (s/n): ").lower() == 's':
    abrir_urls(urls_username)
