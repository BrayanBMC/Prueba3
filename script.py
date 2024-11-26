from typing import List, Dict, Tuple

# Diccionario de versiones inseguras
insecure_packages = {
    "flask": "1.0.2",
    "django": "2.2",
    "requests": "2.19.1"
}

class LectorArchivo:

    @staticmethod
    def leer_requerimientos(ruta_archivo: str) -> List[Tuple[str, str]]:
        dependencias = []
        try:
            with open(ruta_archivo, "r") as archivo:
                for linea in archivo:
                    if "==" in linea:  
                        paquete, version = linea.strip().split("==")
                        dependencias.append((paquete, version))
        except FileNotFoundError:
            raise FileNotFoundError(f"El archivo {ruta_archivo} no existe.")
        return dependencias

class VerificadorDependencias:
    def __init__(self, paquetes_inseguros: Dict[str, str]):
        self.paquetes_inseguros = paquetes_inseguros

    def verificar_dependencias(self, dependencias: List[Tuple[str, str]]) -> List[Tuple[str, str, str]]:

        inseguras = []
        for paquete, version in dependencias:
            if paquete in self.paquetes_inseguros:
                version_insegura = self.paquetes_inseguros[paquete]
                if version == version_insegura:
                    inseguras.append((paquete, version, version_insegura))
        return inseguras

class GeneradorReporte:
    @staticmethod
    def generar_reporte(dependencias_inseguras: List[Tuple[str, str, str]]) -> None:
        if not dependencias_inseguras:
            print("¡Todas las dependencias son seguras!")
        else:
            print("Dependencias inseguras encontradas:")
            for paquete, version, version_insegura in dependencias_inseguras:
                print(f"- {paquete}=={version} (versión insegura: {version_insegura})")

def main():
    ruta_archivo = "requirements.txt"
    try:
        dependencias = LectorArchivo.leer_requerimientos(ruta_archivo)
        
        verificador = VerificadorDependencias(insecure_packages)
        dependencias_inseguras = verificador.verificar_dependencias(dependencias)

        GeneradorReporte.generar_reporte(dependencias_inseguras)
    except Exception as e:
        print(f"Error: {e}")

main()