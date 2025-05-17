import os
import platform

def obtener_ruta_escritorio():
    system = platform.system()
    if system == "Windows":
        return os.path.join(os.environ['USERPROFILE'], 'Desktop')
    elif system == "Linux":
        return os.path.join(os.path.expanduser('~'), 'Desktop')
    else:
        raise NotImplementedError(f"sistema operativo no compatible: {system}")

def crear_acceso_directo(nombre, url):
    sistema = platform.system()
    ruta_escritorio = obtener_ruta_escritorio()
    os.makedirs(ruta_escritorio, exist_ok=True)

    if sistema == "Windows":
        contenido = f"[InternetShortcut]\nURL={url}\n"
        archivo = os.path.join(ruta_escritorio, f"{nombre}.url")
        with open(archivo, "w") as f:
            f.write(contenido)
    elif sistema == "Linux":
        contenido = f"""[Desktop Entry]
Version=1.0
Type=Link
Name={nombre}
URL={url}
Icon=web-browser
"""
        archivo = os.path.join(ruta_escritorio, f"{nombre}.desktop")
        with open(archivo, "w") as f:
            f.write(contenido)
        os.chmod(archivo, 0o755)
    else:
        raise NotImplementedError(f"sistema operativo no compatible: {sistema}")

    print(f"acceso directo creado: {archivo}")

crear_acceso_directo("Plantas", "https://github.com/Brayanj20/Plantas")
