# 🚀 Guía Rápida de Comandos Git (Git CheatSheet)

> **Más de 35 comandos esenciales que todo desarrollador debe dominar.**

---

## 📁 1. Repositorio (Repository)

Comandos para inicializar, clonar e inspeccionar el estado básico de un repositorio.

| Comando             | Descripción                                                                        | Ejemplo de uso                                      |
| :------------------ | :--------------------------------------------------------------------------------- | :-------------------------------------------------- |
| `git init`          | Inicializa un nuevo repositorio Git local.                                         | `git init`                                          |
| `git clone <url>`   | Clona un repositorio remoto en tu máquina local.                                   | `git clone https://github.com/usuario/proyecto.git` |
| `git status`        | Muestra el estado del directorio de trabajo y del área de preparación (_staging_). | `git status`                                        |
| `git log`           | Muestra el historial completo de commits.                                          | `git log`                                           |
| `git log --oneline` | Muestra el historial de commits resumido en una sola línea por commit.             | `git log --oneline -n 5`                            |

---

## 🌿 2. Ramas (Branching)

Comandos para gestionar ramas, cambiar entre ellas y fusionar cambios.

| Comando                  | Descripción                                                       | Ejemplo de uso                |
| :----------------------- | :---------------------------------------------------------------- | :---------------------------- |
| `git branch`             | Lista todas las ramas locales existentes.                         | `git branch`                  |
| `git branch <nombre>`    | Crea una nueva rama con el nombre especificado.                   | `git branch feature/login`    |
| `git checkout <nombre>`  | Cambia a la rama especificada (comando tradicional).              | `git checkout feature/login`  |
| `git switch <nombre>`    | Cambia a la rama especificada (comando moderno y recomendado).    | `git switch main`             |
| `git merge <nombre>`     | Fusiona la rama especificada dentro de la rama actual.            | `git merge feature/login`     |
| `git rebase <nombre>`    | Aplica los commits de la rama actual sobre la punta de otra rama. | `git rebase main`             |
| `git branch -d <nombre>` | Elimina una rama local de forma segura (si ya fue fusionada).     | `git branch -d feature/login` |

---

## ➕ 3. Área de Preparación (Staging Area)

Comandos para preparar archivos antes de guardarlos en un commit.

| Comando                 | Descripción                                                               | Ejemplo de uso             |
| :---------------------- | :------------------------------------------------------------------------ | :------------------------- |
| `git add .`             | Agrega todos los archivos modificados y nuevos al área de preparación.    | `git add .`                |
| `git add <archivo>`     | Agrega un archivo específico al área de preparación.                      | `git add index.html`       |
| `git add -A`            | Agrega todos los cambios (nuevos, modificados y eliminados).              | `git add -A`               |
| `git restore <archivo>` | Descarta cambios locales en un archivo o lo saca del área de preparación. | `git restore estilos.css`  |
| `git rm <archivo>`      | Elimina un archivo del disco y prepara su eliminación en Git.             | `git rm archivo_viejo.txt` |
| `git rm -r <carpeta>`   | Elimina una carpeta completa de forma recursiva y prepara su eliminación. | `git rm -r temp/`          |

---

## ✅ 4. Confirmaciones (Commits)

Comandos para guardar y gestionar instantáneas de tus cambios en el historial.

| Comando                    | Descripción                                                                       | Ejemplo de uso                                               |
| :------------------------- | :-------------------------------------------------------------------------------- | :----------------------------------------------------------- |
| `git commit -m "mensaje"`  | Guarda los cambios preparados con un mensaje descriptivo.                         | `git commit -m "feat: agregar autenticación con Google"`     |
| `git commit -am "mensaje"` | Prepara archivos ya rastreados y hace commit en un solo paso.                     | `git commit -am "fix: corregir error en cálculo de totales"` |
| `git commit --amend`       | Modifica el último commit (cambiar mensaje o agregar archivos olvidados).         | `git commit --amend -m "feat: nuevo mensaje corregido"`      |
| `git reset --soft HEAD~1`  | Deshace el último commit pero **conserva los cambios** en el área de preparación. | `git reset --soft HEAD~1`                                    |
| `git reset --hard HEAD~1`  | Deshace el último commit y **descarta todos los cambios** definitivamente.        | `git reset --hard HEAD~1`                                    |

---

## ☁️ 5. Repositorios Remotos (Remote)

Comandos para sincronizar y conectar con plataformas como GitHub, GitLab o Bitbucket.

| Comando                       | Descripción                                                                  | Ejemplo de uso                                              |
| :---------------------------- | :--------------------------------------------------------------------------- | :---------------------------------------------------------- |
| `git remote -v`               | Lista los servidores remotos configurados y sus URLs.                        | `git remote -v`                                             |
| `git remote add origin <url>` | Vincula el repositorio local con un repositorio remoto llamado `origin`.     | `git remote add origin https://github.com/usuario/repo.git` |
| `git fetch`                   | Descarga el historial y ramas del remoto sin fusionar cambios.               | `git fetch origin`                                          |
| `git pull`                    | Descarga y fusiona automáticamente los cambios del remoto en la rama actual. | `git pull origin main`                                      |
| `git push`                    | Sube tus commits locales al repositorio remoto.                              | `git push`                                                  |
| `git push -u origin <rama>`   | Sube la rama al remoto y establece el rastreo predeterminado (_upstream_).   | `git push -u origin feature/login`                          |
| `git push --tags`             | Sube todas las etiquetas (_tags_) locales al repositorio remoto.             | `git push --tags`                                           |

---

## 🕒 6. Historial y Cambios Temporales (History & Stash)

Comandos para inspeccionar diferencias y guardar cambios temporales sin hacer commit.

| Comando             | Descripción                                                                               | Ejemplo de uso      |
| :------------------ | :---------------------------------------------------------------------------------------- | :------------------ |
| `git diff`          | Muestra las diferencias entre los archivos modificados y el último commit.                | `git diff`          |
| `git diff --staged` | Muestra las diferencias de los archivos que ya están en el área de preparación.           | `git diff --staged` |
| `git show <commit>` | Muestra los detalles y cambios específicos de un commit.                                  | `git show a1b2c3d`  |
| `git reflog`        | Muestra el registro histórico de todas las acciones y movimientos de `HEAD`.              | `git reflog`        |
| `git stash`         | Guarda temporalmente los cambios no confirmados y limpia el espacio de trabajo.           | `git stash`         |
| `git stash pop`     | Recupera y aplica los últimos cambios guardados en el _stash_, eliminándolos de la lista. | `git stash pop`     |
| `git stash list`    | Muestra la lista de todos los cambios guardados en el _stash_.                            | `git stash list`    |

---

## 🏷️ 7. Etiquetas (Tags)

Comandos para marcar versiones y puntos importantes en el historial (ej. versiones de lanzamiento).

| Comando                        | Descripción                                                 | Ejemplo de uso                                             |
| :----------------------------- | :---------------------------------------------------------- | :--------------------------------------------------------- |
| `git tag`                      | Lista todas las etiquetas existentes.                       | `git tag`                                                  |
| `git tag <nombre>`             | Crea una etiqueta ligera en el commit actual.               | `git tag v1.0.0`                                           |
| `git tag -a <nombre> -m "msg"` | Crea una etiqueta anotada con mensaje y datos del autor.    | `git tag -a v1.0.0 -m "Versión 1.0 lista para producción"` |
| `git show <tag>`               | Muestra la información y detalles asociados a una etiqueta. | `git show v1.0.0`                                          |
| `git push --tags`              | Envía todas las etiquetas locales al repositorio remoto.    | `git push --tags`                                          |

---

## ⚙️ 8. Varios y Configuración (Miscellaneous)

Herramientas para configuración global, limpieza y mantenimiento.

| Elemento / Comando               | Descripción                                                                       | Ejemplo de uso                                          |
| :------------------------------- | :-------------------------------------------------------------------------------- | :------------------------------------------------------ |
| `.gitignore`                     | Archivo de texto para indicar a Git qué archivos o carpetas ignorar.              | Contenido: `node_modules/`, `.env`, `dist/`             |
| `git config --global user.name`  | Configura el nombre del autor para todos los commits en el sistema.               | `git config --global user.name "Tu Nombre"`             |
| `git config --global user.email` | Configura el correo electrónico asociado a tus commits.                           | `git config --global user.email "tu_email@ejemplo.com"` |
| `git config --list`              | Muestra toda la configuración actual de Git.                                      | `git config --list`                                     |
| `git clean -fd`                  | Elimina archivos y directorios no rastreados (_untracked_) del proyecto.          | `git clean -fd`                                         |
| `git gc`                         | Ejecuta el recolector de basura (_garbage collection_) y optimiza el repositorio. | `git gc`                                                |
