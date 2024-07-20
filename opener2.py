import webbrowser  # Módulo para controlar el navegador web
import platform  # Módulo para acceder a los datos del sistema operativo
import time  # Módulo para funciones relacionadas con el tiempo
import subprocess  # Módulo para ejecutar subprocesos del sistema

# Lista de URLs para realizar búsquedas de correos electrónicos
urls_email = [
    "https://emailrep.io/",  # Servicio de reputación de correos electrónicos
    "https://dehashed.com/",  # Motor de búsqueda para datos filtrados
    "https://haveibeenpwned.com/",  # Comprobador de correos electrónicos comprometidos
    "https://epieos.com/",  # Herramienta de OSINT para búsqueda de información personal
    "intelx.io/?s=correo_completo",  # Búsqueda en la base de datos de IntelligenceX
    "https://cybernews.com/personal-data-leak-check/",  # Verificador de filtraciones de datos
    "https://pastebin.com/search?q=correo_completo",  # Búsqueda de correos en Pastebin
    "https://www.secureito.com/",  # Plataforma de seguridad de datos
    "https://yandex.com/search/?text=\"correo_completo\"",  # Búsqueda en Yandex
    "https://emailrep.io/query/correo_completo",  # Consulta en EmailRep
    "https://cavalier.hudsonrock.com/api/json/v2/preview/search-by-login/osint-tools?email=correo_completo",  # Búsqueda en Hudson Rock
    "https://cleantalk.org/email-checker/correo_completo",  # Verificador de correos en CleanTalk
    "https://leakix.net/search?scope=leak&q=\"correo_completo\"",  # Búsqueda de filtraciones en LeakIX
    "https://www.flickr.com/search/people/?q=correo_completo",  # Búsqueda de personas en Flickr
    "https://myspace.com/search/people?q=correo_completo",  # Búsqueda de personas en MySpace
    "https://scamsearch.io/search_report?searchoption=all&search=correo_completo",  # Búsqueda de estafas en ScamSearch
    "https://whoxy.com/search.php?email=correo_completo",  # Búsqueda de registros WHOIS
    "https://whoisology.com/email/correo_completo",  # Búsqueda en WhoiSology
    "https://hunter.io/email-verifier/correo_completo",  # Verificador de correos en Hunter.io
    "https://gmail-osint.activetk.jp/user_correo"  # Búsqueda en la herramienta de Gmail OSINT
]

# Lista de URLs para realizar búsquedas de nombres de usuario
urls_username = [
    "https://namechk.com/",  # Verificador de disponibilidad de nombres de usuario
    "https://checkusernames.com/",  # Verificador de nombres de usuario en múltiples plataformas
    "https://instantusername.com/?q=nombre_usuario",  # Verificador instantáneo de nombres de usuario
    "https://www.google.com/search?q=site:amazon.com+nombre_usuario",  # Búsqueda de nombres de usuario en Amazon
    "https://api.github.com/users/nombre_usuario/events/public",  # Eventos públicos de un usuario en GitHub
    "https://dehashed.com/",  # Motor de búsqueda para datos filtrados
    "https://www.facebook.com/login/identify?ctx=recover",  # Recuperación de cuenta en Facebook
    "https://lookup-id.com/",  # Herramienta de búsqueda de IDs de Facebook
    "https://haveibeenzuckered.com/",  # Comprobador de datos filtrados en Facebook
    "https://whatsmyname.app/",  # Búsqueda de nombres de usuario en múltiples plataformas
    "https://pastebin.com/search?q=nombre_usuario",  # Búsqueda de nombres de usuario en Pastebin
    "https://www.google.com/search?q=\"nombre_usuario\"",  # Búsqueda de nombres de usuario en Google
    "https://www.bing.com/search?q=\"nombre_usuario\"",  # Búsqueda de nombres de usuario en Bing
    "https://yandex.com/search/?text=\"nombre_usuario\"",  # Búsqueda de nombres de usuario en Yandex
    "https://gravatar.com/nombre_usuario",  # Perfil de usuario en Gravatar
    "https://linktr.ee/nombre_usuario",  # Perfil de usuario en Linktree
    "https://twitter.com/nombre_usuario",  # Perfil de usuario en Twitter
    "https://www.facebook.com/nombre_usuario",  # Perfil de usuario en Facebook
    "https://www.instagram.com/nombre_usuario",  # Perfil de usuario en Instagram
    "https://www.tiktok.com/@nombre_usuario",  # Perfil de usuario en TikTok
    "https://www.snapchat.com/add/nombre_usuario",  # Perfil de usuario en Snapchat
    "https://medium.com/@nombre_usuario",  # Perfil de usuario en Medium
    "https://tinder.com/@nombre_usuario",  # Perfil de usuario en Tinder
    "https://www.youtube.com/nombre_usuario",  # Canal de usuario en YouTube
    "https://www.reddit.com/user/nombre_usuario/",  # Perfil de usuario en Reddit
    "https://www.google.com/search?q=\"nombre_usuario@gmail.com\"OR\"nombre_usuario@yahoo.com\"OR\"nombre_usuario@hotmail.com\"OR\"nombre_usuario@protonmail.com\"OR\"nombre_usuario@live.com\"OR\"nombre_usuario@icloud.com\"OR\"nombre_usuario@yandex.com\"OR\"nombre_usuario@gmx.com\"OR\"nombre_usuario@mail.com\"OR\"nombre_usuario@mac.com\"OR\"nombre_usuario@me.com\""  # Búsqueda de correos electrónicos asociados
]

# Detectar el sistema operativo del usuario
system = platform.system()

# Definir la ruta de Google Chrome según el sistema operativo
if system == "Windows":
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"  # Ruta al ejecutable de Chrome en Windows
elif system == "Darwin":  # macOS
    chrome_path = "open -a /Applications/Google\\ Chrome.app %s"
else:
    raise Exception("Sistema operativo no compatible")  # Manejo de error para sistemas no compatibles

# Pedir al usuario que ingrese el correo completo y el nombre de usuario
correo_completo = input("Introduce el correo completo: ")
nombre_usuario = input("Introduce el nombre de usuario: ")
user_correo = correo_completo.split('@')[0]  # Obtener el nombre de usuario del correo (parte antes del @)

# Reemplazar las variables en las URLs con los valores ingresados por el usuario
urls_email = [url.replace("correo_completo", correo_completo).replace("user_correo", user_correo) for url in urls_email]
urls_username = [url.replace("nombre_usuario", nombre_usuario) for url in urls_username]

# Función para abrir URLs en Google Chrome
def abrir_urls(urls):
    """
    Abre una lista de URLs en nuevas pestañas de Google Chrome.
    """
    for url in urls:
        if system == "Windows":
            webbrowser.get(chrome_path).open_new_tab(url)  # Abrir nueva pestaña en Windows
        elif system == "Darwin":
            subprocess.call(chrome_path % url, shell=True)  # Abrir nueva pestaña en macOS
        time.sleep(1)  # Esperar un segundo entre cada apertura de pestaña

# Preguntar al usuario si desea abrir las URLs del grupo 1 (correos electrónicos)
if input("¿Deseas abrir las URLs del grupo 1 (correos electrónicos)? (s/n): ").lower() == 's':
    abrir_urls(urls_email)

# Preguntar al usuario si desea abrir las URLs del grupo 2 (nombres de usuario)
if input("¿Deseas abrir las URLs del grupo 2 (nombres de usuario)? (s/n): ").lower() == 's':
    abrir_urls(urls_username)
