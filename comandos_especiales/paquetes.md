# 🐍 Gestión de Paquetes en Python

Entornos virtuales y dependencias en Python.

---

## 1. Gestión con `pip`

### Listar e Inspeccionar

| Comando                   | Descripción                                                                                   |
| :------------------------ | :-------------------------------------------------------------------------------------------- |
| `pip list`                | Muestra todos los paquetes instalados y sus versiones en el entorno actual.                   |
| `pip list --outdated`     | Muestra solo los paquetes instalados que tienen versiones más recientes disponibles.          |
| `pip list --uptodate`     | Lista los paquetes que están en su última versión.                                            |
| `pip list --user`         | Lista únicamente los paquetes instalados a nivel de usuario (fuera de root/env).              |
| `pip list --not-required` | Muestra paquetes instalados que**no** son dependencia de ningún otro paquete (paquetes raíz). |
| `pip freeze`              | Genera una lista formateada en formato`paquete==versión` (ideal para exportar).               |
| `pip show <paquete>`      | Muestra información detallada de un paquete (ubicación, dependencias, autor, licencia).       |
| `pip show -f <paquete>`   | Muestra los detalles y**todos los archivos** instalados por el paquete.                       |
| `pip check`               | Verifica si hay incompabilidades o dependencias faltantes entre paquetes instalados.          |

### Instalación

```bash
# Instalación básica de la última versión
pip install nombre_paquete

# Instalar versión específica
pip install nombre_paquete==2.4.0

# Instalar versión mínima o máxima requerida
pip install "nombre_paquete>=1.5,<2.0"

# Instalar múltiples paquetes a la vez
pip install requests pandas numpy
```

### Desinstalación

```bash
# Desinstalar un paquete (pedirá confirmación)
pip uninstall nombre_paquete

# Desinstalar sin pedir confirmación (-y / --yes)
pip uninstall nombre_paquete -y

# Desinstalar múltiples paquetes
pip uninstall paquete1 paquete2 paquete3

# Desinstalar TODOS los paquetes listados en un archivo
pip uninstall -r requirements.txt -y
```

### Actualización

```bash
# Actualizar pip a su última versión
python -m pip install --upgrade pip

# Actualizar un paquete específico
pip install --upgrade nombre_paquete

# Actualizar a una versión específica o superior
pip install -U "nombre_paquete>=3.0"
```

### Manejo de `requirements.txt`

```bash
# Exportar todos los paquetes instalados al archivo
pip freeze > requirements.txt

# Instalar todas las dependencias listadas en el archivo
pip install -r requirements.txt

# Ignorar dependencias ya instaladas durante la lectura del archivo
pip install -r requirements.txt --upgrade
```

---

## 2. Entornos Virtuales (`venv`)

Es una buena práctica **nunca** instalar paquetes en el Python global del sistema. Utiliza entornos virtuales.

### Crear y actualizar

```bash
# 1. Crear entorno virtual (nombre común: .venv o venv)
python -m venv .venv

# 2. Activar el entorno virtual:
# En Linux / macOS (Bash / Zsh):
source .venv/bin/activate

# En Windows (Command Prompt):
.venv\\Scripts\\activate.bat

# En Windows (PowerShell):
.venv\\Scripts\\Activate.ps1

# 3. Desactivar el entorno (igual en todos los sistemas)
deactivate
```

### Verificar el Entorno Activo

```bash
# Verificar la ruta del ejecutable de Python activo
which python   # Linux / macOS
where python   # Windows (CMD / PowerShell)
```

---

> 💡 **Consejo:** Mantén siempre un archivo `.gitignore` configurado para ignorar las carpetas de entornos virtuales (`.venv/`, `venv/`, `env/`) en tus repositorios.
> """
