# **Solución Escaneo Básico de Dependencias**

## **Descripción del problema**
El objetivo de este proyecto es crear un script en Python que lea un archivo `requirements.txt` y detecte si contiene dependencias con versiones inseguras. Esto se realiza mediante la simulación de un escaneo básico de seguridad, comparando las dependencias del archivo contra un diccionario predefinido de paquetes y versiones vulnerables.

---

## **Solución**
El programa está dividido en tres componentes principales: 

1. **Lectura del archivo `requirements.txt`**: Extrae las dependencias y sus versiones.
2. **Verificación de dependencias**: Compara las dependencias del archivo con las versiones inseguras definidas en un diccionario.
3. **Generación de un reporte**: Informa al usuario si existen dependencias inseguras o si todas son seguras.

---

### **Estructura del código**

#### **1. Diccionario de dependencias inseguras**
```python
insecure_packages = {
    "flask": "1.0.2",
    "django": "2.2",
    "requests": "2.19.1"
}
```
Este diccionario contiene los paquetes y las versiones consideradas inseguras.

---

#### **2. Lectura del archivo**
La clase `LectorArchivo` se encarga de leer el archivo `requirements.txt` y extraer las dependencias con sus versiones en formato `(paquete, versión)`.

```python
from typing import List, Tuple

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
```

---

#### **3. Verificación de dependencias**
La clase `VerificadorDependencias` verifica si alguna dependencia coincide con las versiones inseguras del diccionario.

```python
from typing import List, Dict, Tuple

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
```

---

#### **4. Generación de reporte**
La clase `GeneradorReporte` imprime un resumen de las dependencias inseguras encontradas.

```python
class GeneradorReporte:
    @staticmethod
    def generar_reporte(dependencias_inseguras: List[Tuple[str, str, str]]) -> None:
        if not dependencias_inseguras:
            print("¡Todas las dependencias son seguras!")
        else:
            print("Dependencias inseguras encontradas:")
            for paquete, version, version_insegura in dependencias_inseguras:
                print(f"- {paquete}=={version} (versión insegura: {version_insegura})")
```

---

#### **5. Ejecución del script**
El script integra las clases anteriores para realizar el proceso completo de lectura, verificación y reporte.

```python
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
```

---

## **Cómo usar**

### **1. Requisitos previos**
- Python 3.6 o superior.
- Un archivo llamado `requirements.txt` con dependencias en formato `paquete==versión`.

### **2. Ejecución**
1. Guarda el código en un archivo llamado `script.py`.
2. Crea un archivo `requirements.txt` con dependencias, por ejemplo:
   ```
   flask==1.0.2
   django==2.8
   requests==2.19.1
   ```
3. Ejecuta el script desde la terminal.

---

## **Ejemplo de uso**

### Entrada: `requirements.txt`
```
flask==1.0.2
django==2.8
requests==2.19.1
```

### Salida:
```
Dependencias inseguras encontradas:
- flask==1.0.2 (versión insegura: 1.0.2)
- requests==2.19.1 (versión insegura: 2.19.1)
```

---

## **Características clave**
1. **Modularidad**: El código está organizado en clases para facilitar su mantenimiento y escalabilidad.
2. **Validación completa**: Detecta versiones inseguras según un diccionario predefinido.
3. **Reporte claro**: Proporciona un resumen detallado de las dependencias vulnerables.

---
