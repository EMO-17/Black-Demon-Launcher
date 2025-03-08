import minecraft_launcher_lib
import subprocess

#variables..
# Diretorio de instalacion..
minecraft_directory = minecraft_launcher_lib.utils.get_minecraft_directory()

version_minecraft = "fabric-loader-0.16.10-1.17.1"


#Barra de carga...
current_max = 0

def set_status(status: str):
    print(status)


def set_progress(progress: int):
    if current_max != 0:
        print(f"{progress}/{current_max}")


def set_max(new_max: int):
    global current_max
    current_max = new_max

callback = {
    "setStatus": set_status,
    "setProgress": set_progress,
    "setMax": set_max
}



#funciones de intalacion...
def instalar_version():
    #instalar version de minecraft...
    minecraft_launcher_lib.install.install_minecraft_version(version_minecraft, minecraft_directory, callback=callback)

def instalar_version_fabric():
    #instalar version de minecraft con fabric...
    minecraft_launcher_lib.fabric.install_fabric(version_minecraft, minecraft_directory, callback=callback)


#funciones de ejecucion...
def ejecutar():
    print("Ejecutando..")

    #options = minecraft_launcher_lib.utils.generate_test_options()
    options = {
        "username": "EMO_17",
        "uuid": "The UUID",
        "token": "The acces token"
        }

    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(version_minecraft,minecraft_directory, options)

    subprocess.run(minecraft_command, cwd=minecraft_directory)


def verificar_versiones():
    # Obtener las versiones instaladas
    installed_versions = minecraft_launcher_lib.utils.get_installed_versions(minecraft_directory)

    # Imprimir las versiones instaladas
    print("Versiones de Minecraft instaladas:")
    for version in installed_versions:
        print(version)









#Interfaz del emulador ...

print("Que accion realisaras?")
print("  1) Intalar una version...")
print("  2) Intalar fabric")
print("  3) Ejecutar una version...")

op = input(">>> ")


try:
    op = int(op)

    if op == 1:
        version_minecraft=input("Que version deseas intalar? :")
        instalar_version()

    elif op == 2:
        version_minecraft=input("A que version de minecraft deseas instarle el fablric? :")
        instalar_version_fabric()

    elif op == 3:
        verificar_versiones()
        version_minecraft=input("Que version de minecraft deseas ejecutar? (Ej: 1.17.1) :")
        ejecutar()

    else:
        print("No elegiste nada....",op)

except ValueError:
    print("Entrada no válida. Por favor, ingresa un número.")
