# Guía de Etiquetas HTML5

> **Resumen de referencia rápida**: Catálogo con wlas etiquetas esenciales de HTML5 para estructuración semántica, SEO y desarrollo web moderno.

---

## 1. Estructura del Documento (`Document Structure`)

Etiquetas fundamentales que definen el documento, sus metadatos e importación de recursos globales.

| Etiqueta       | Descripción                                                                                               | Ejemplo de Uso                                             |
| :------------- | :--------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------- |
| `<!DOCTYPE>` | Declara el tipo de documento y la versión de HTML (HTML5).                                                | `<!DOCTYPE html>`                                        |
| `<html>`     | Elemento raíz que envuelve todo el contenido del documento HTML.                                          | `<html lang="es">...</html>`                             |
| `<head>`     | Contenedor de metadatos, configuración técnica y enlaces a recursos externos.                            | `<head>...</head>`                                       |
| `<title>`    | Define el título del documento (visible en la pestaña del navegador y en SEO).                           | `<title>Mi Página Web</title>`                          |
| `<base>`     | Especifica la URL base y/o destino para todos los enlaces relativos del documento.                         | `<base href="https://example.com/">`                     |
| `<link>`     | Vincula recursos externos al documento (hojas de estilo CSS, favicon, fuentes).                            | `<link rel="stylesheet" href="estilos.css">`             |
| `<meta>`     | Proporciona metadatos del documento (juego de caracteres, viewport, descripción SEO).                     | `<meta charset="UTF-8">`                                 |
| `<style>`    | Permite insertar reglas y estilos CSS internos dentro del documento.                                       | `<style> body { margin: 0; } </style>`                   |
| `<script>`   | Define o enlaza código JavaScript ejecutado del lado del cliente.                                         | `<script src="app.js"></script>`                         |
| `<noscript>` | Define contenido alternativo para mostrar cuando el navegador no soporta o tiene JavaScript deshabilitado. | `<noscript>Activa JavaScript para continuar.</noscript>` |

---

## 2. Secciones Semánticas (`Sections`)

Elementos estructurales clave para definir la arquitectura del contenido y mejorar la accesibilidad y el SEO.

| Etiqueta      | Descripción                                                                                                        | Ejemplo de Uso                              |
| :------------ | :------------------------------------------------------------------------------------------------------------------ | :------------------------------------------ |
| `<body>`    | Contiene todo el contenido visible de la página web.                                                               | `<body>...</body>`                        |
| `<header>`  | Representa la cabecera introductoria de la página o de una sección (logos, títulos, navegación).                | `<header><h1>Título</h1></header>`       |
| `<nav>`     | Define una sección que contiene enlaces principales de navegación.                                                | `<nav><a href="#inicio">Inicio</a></nav>` |
| `<main>`    | Especifica el contenido principal y exclusivo del documento (único por página).                                   | `<main>...</main>`                        |
| `<section>` | Define una sección temática genérica dentro de un documento.                                                     | `<section><h2>Servicios</h2></section>`   |
| `<article>` | Representa contenido autónomo, independiente y reutilizable (noticia, post, widget).                               | `<article><h2>Post</h2></article>`        |
| `<aside>`   | Representa contenido complementario o lateral relacionado indirectamente con el principal (barra lateral, widgets). | `<aside><p>Dato curioso</p></aside>`      |
| `<footer>`  | Define el pie de página de un documento o sección (copyright, términos, enlaces).                                | `<footer>&copy; 2026 Empresa</footer>`    |
| `<address>` | Proporciona información de contacto del autor o propietario del documento o artículo.                             | `<address>contacto@dominio.com</address>` |

---

## 3. Contenido de Texto y Formato (`Text Content`)

Etiquetas utilizadas para estructurar, jerarquizar y dar significado semántico al texto.

| Etiqueta            | Descripción                                                                                      | Ejemplo de Uso                                          |
| :------------------ | :------------------------------------------------------------------------------------------------ | :------------------------------------------------------ |
| `<h1>` a `<h6>` | Encabezados de diferentes niveles de jerarquía (del más importante`h1` al menor `h6`).      | `<h1>Título Principal</h1>`                          |
| `<p>`             | Define un párrafo de texto.                                                                      | `<p>Este es un párrafo explicativo.</p>`             |
| `<br>`            | Inserta un salto de línea simple.                                                                | `Línea 1<br>Línea 2`                                |
| `<hr>`            | Representa un cambio temático o una línea divisoria horizontal entre contenidos.                | `<hr>`                                                |
| `<pre>`           | Muestra texto preformateado respetando espacios y saltos de línea originales.                    | `<pre>Texto   con   espacios</pre>`                   |
| `<blockquote>`    | Define una cita extensa en bloque proveniente de otra fuente externa.                             | `<blockquote>Cita textual...</blockquote>`            |
| `<q>`             | Define una cita corta en línea (generalmente renderizada entre comillas).                        | `<q>Ser o no ser</q>`                                 |
| `<cite>`          | Define el título de una obra creativa (libro, película, canción, investigación).              | `<cite>Cien años de soledad</cite>`                  |
| `<code>`          | Define un fragmento de código de computadora en línea.                                          | `<code>console.log()</code>`                          |
| `<em>`            | Define texto con énfasis estructural (usualmente en cursiva; cambia la entonación).             | `<em>Importante destacar</em>`                        |
| `<strong>`        | Define texto con alta importancia, seriedad o urgencia (usualmente en negrita).                   | `<strong>Atención requerida</strong>`                |
| `<small>`         | Define texto secundario o de menor tamaño (letra chica, avisos legales, copyright).              | `<small>Términos aplicables</small>`                 |
| `<mark>`          | Define texto marcado o resaltado por relevancia en el contexto de consulta.                       | `<mark>resultado clave</mark>`                        |
| `<abbr>`          | Define una abreviatura o acrónimo (se puede complementar con el atributo`title`).              | `<abbr title="HyperText Markup Language">HTML</abbr>` |
| `<time>`          | Define una fecha, hora o duración precisa en formato legible por máquinas.                      | `<time datetime="2026-08-29">29 de agosto</time>`     |
| `<bdi>`           | Aísla una porción de texto para que su dirección bidireccional no afecte al texto circundante. | `<bdi>اسم المستخدم</bdi>`                  |
| `<bdo>`           | Sobrescribe de forma explícita la dirección de lectura del texto actual (`ltr` o `rtl`).    | `<bdo dir="rtl">Texto invertido</bdo>`                |

---

## 4. Enlaces y Multimedia (`Links & Media`)

Etiquetas para conectar documentos e incrustar medios visuales, auditivos e interactivos.

| Etiqueta      | Descripción                                                                                         | Ejemplo de Uso                                                           |
| :------------ | :--------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------- |
| `<a>`       | Define un hipervínculo hacia otra página, recurso o sección interna.                              | `<a href="https://example.com">Visitar</a>`                            |
| `<img>`     | Incrusta una imagen en el documento.                                                                 | `<img src="foto.jpg" alt="Descripción">`                              |
| `<map>`     | Define un mapa de imagen con zonas interactivas/clicables.                                           | `<map name="zonas">...</map>`                                          |
| `<area>`    | Define un área interactiva específica dentro de un mapa de imagen (`<map>`).                     | `<area shape="rect" coords="0,0,50,50" href="link.html" alt="Zona 1">` |
| `<audio>`   | Incrusta contenido de audio o pistas sonoras.                                                        | `<audio src="audio.mp3" controls></audio>`                             |
| `<source>`  | Especifica múltiples recursos multimedia alternativos para`<video>`, `<audio>` o `<picture>`. | `<source src="clip.webm" type="video/webm">`                           |
| `<track>`   | Especifica pistas de texto cronometradas (subtítulos, descripciones) para medios audiovisuales.     | `<track src="sub.vtt" kind="subtitles" srclang="es">`                  |
| `<video>`   | Incrusta un reproductor y contenido de video en la página.                                          | `<video src="video.mp4" controls></video>`                             |
| `<picture>` | Contenedor para múltiples fuentes de imagen adaptativas según resolución o formato.               | `<picture><source ...><img></picture>`                                 |
| `<embed>`   | Incrusta contenido o aplicaciones externas independientes (plugins, interactivos).                   | `<embed src="archivo.swf">`                                            |
| `<iframe>`  | Incrusta un marco en línea que aloja otro documento HTML externo.                                   | `<iframe src="https://example.com"></iframe>`                          |
| `<object>`  | Incrusta un recurso multimedia u objeto externo (PDF, SVG, applets).                                 | `<object data="archivo.pdf" type="application/pdf"></object>`          |
| `<param>`   | Define parámetros de inicialización para un elemento`<object>`.                                  | `<param name="autoplay" value="true">`                                 |

---

## 5. Listas (`Lists`)

Estructuras para agrupar elementos relacionados en listas ordenadas, no ordenadas o de definición.

| Etiqueta | Descripción                                                                            | Ejemplo de Uso                                     |
| :------- | :-------------------------------------------------------------------------------------- | :------------------------------------------------- |
| `<ul>` | Define una lista no ordenada (con viñetas por defecto).                                | `<ul><li>Elemento</li></ul>`                     |
| `<ol>` | Define una lista ordenada (secuencia numerada o alfabética).                           | `<ol><li>Paso 1</li></ol>`                       |
| `<li>` | Representa un elemento individual dentro de una lista (`<ul>` o `<ol>`).            | `<li>Elemento de lista</li>`                     |
| `<dl>` | Define una lista de descripciones o términos y sus definiciones.                       | `<dl><dt>Término</dt><dd>Definición</dd></dl>` |
| `<dt>` | Define el término o nombre a describir dentro de una lista de descripción (`<dl>`). | `<dt>HTML</dt>`                                  |
| `<dd>` | Proporciona la descripción o valor correspondiente al término`<dt>`.                | `<dd>Lenguaje de marcado...</dd>`                |

---

## 6. Tablas (`Tables`)

Etiquetas para estructurar datos tabulares multidimensionales de forma accesible.

| Etiqueta       | Descripción                                                           | Ejemplo de Uso                              |
| :------------- | :--------------------------------------------------------------------- | :------------------------------------------ |
| `<table>`    | Define una tabla de datos.                                             | `<table>...</table>`                      |
| `<caption>`  | Define el título descriptivo o leyenda de una tabla.                  | `<caption>Tabla de Ventas 2026</caption>` |
| `<thead>`    | Agrupa el contenido del encabezado de la tabla (columnas principales). | `<thead><tr><th>Nombre</th></tr></thead>` |
| `<tbody>`    | Agrupa el cuerpo principal de datos de la tabla.                       | `<tbody><tr><td>Dato</td></tr></tbody>`   |
| `<tfoot>`    | Agrupa el contenido del pie de tabla (totales, resúmenes).            | `<tfoot><tr><td>Total</td></tr></tfoot>`  |
| `<tr>`       | Define una fila dentro de una tabla.                                   | `<tr><td>Fila 1</td></tr>`                |
| `<th>`       | Define una celda de encabezado (en negrita y centrada por defecto).    | `<th>Encabezado</th>`                     |
| `<td>`       | Define una celda de datos estándar en una fila.                       | `<td>Dato estándar</td>`                 |
| `<col>`      | Especifica propiedades de estilo comunes para una columna completa.    | `<col style="background: #f0f0f0">`       |
| `<colgroup>` | Agrupa una o más columnas para aplicarles formato estructural común. | `<colgroup><col span="2"></colgroup>`     |

---

## 7. Formularios (`Forms`)

Componentes interactivos para recopilar y procesar entradas de datos del usuario.

| Etiqueta       | Descripción                                                                                         | Ejemplo de Uso                                              |
| :------------- | :--------------------------------------------------------------------------------------------------- | :---------------------------------------------------------- |
| `<form>`     | Define un formulario HTML para recopilar entradas del usuario.                                       | `<form action="/submit" method="POST">...</form>`         |
| `<label>`    | Define una etiqueta asociada a un control de formulario (`<input>`, `<select>`, etc.).           | `<label for="email">Correo:</label>`                      |
| `<input>`    | Control interactivo versátil para captura de datos (texto, password, checkbox, radio, etc.).        | `<input type="text" id="nombre" name="nombre">`           |
| `<textarea>` | Define un control de entrada de texto multilínea.                                                   | `<textarea rows="4" cols="50"></textarea>`                |
| `<button>`   | Define un botón interactivo y cliqueable.                                                           | `<button type="submit">Enviar</button>`                   |
| `<select>`   | Define un menú desplegable de opciones.                                                             | `<select><option>Opción 1</option></select>`             |
| `<optgroup>` | Agrupa opciones relacionadas dentro de un menú desplegable`<select>`.                             | `<optgroup label="Grupo 1"><option>A</option></optgroup>` |
| `<option>`   | Define una opción individual dentro de un`<select>` o `<datalist>`.                             | `<option value="1">Opción 1</option>`                    |
| `<fieldset>` | Agrupa visual y semánticamente controles y etiquetas de formulario relacionados.                    | `<fieldset><legend>Datos</legend>...</fieldset>`          |
| `<legend>`   | Define el título descriptivo para el contenedor`<fieldset>`.                                      | `<legend>Información Personal</legend>`                  |
| `<datalist>` | Especifica una lista de opciones predefinidas como sugerencias de autocompletado para un`<input>`. | `<datalist id="colores"><option value="Azul"></datalist>` |
| `<output>`   | Muestra el resultado de un cálculo o de una acción del usuario.                                    | `<output name="resultado">0</output>`                     |
| `<progress>` | Representa visualmente el progreso de una tarea o carga.                                             | `<progress value="70" max="100">70%</progress>`           |
| `<meter>`    | Representa una medición escalar dentro de un rango conocido (ej. uso de disco, puntuación).        | `<meter min="0" max="100" value="75">75%</meter>`         |

---

## 8. Semántica y Otros Elementos (`Semantic / Other`)

Etiquetas de soporte visual, contenedores genéricos y elementos semánticos adicionales.

| Etiqueta         | Descripción                                                                                                        | Ejemplo de Uso                                                         |
| :--------------- | :------------------------------------------------------------------------------------------------------------------ | :--------------------------------------------------------------------- |
| `<figure>`     | Especifica contenido autónomo (imágenes, diagramas, fragmentos de código) con referencia propia.                 | `<figure><img src="gato.jpg"><figcaption>Gato</figcaption></figure>` |
| `<figcaption>` | Define el pie de foto o descripción para el contenido de un elemento`<figure>`.                                  | `<figcaption>Figura 1: Diagrama de flujo</figcaption>`               |
| `<details>`    | Define un contenedor interactivo de detalles adicionales desplegables por el usuario.                               | `<details><summary>Más info</summary><p>Contenido</p></details>`    |
| `<summary>`    | Define el encabezado visible e interactivo para el elemento`<details>`.                                           | `<summary>Haga clic para ver detalles</summary>`                     |
| `<dialog>`     | Define un cuadro de diálogo, ventana modal o mensaje emergente.                                                    | `<dialog open><p>Ventana modal</p></dialog>`                         |
| `<template>`   | Define una plantilla de contenido HTML que permanece oculta y no se renderiza hasta ser instanciada con JavaScript. | `<template id="card-tpl"><div>...</div></template>`                  |
| `<slot>`       | Define un marcador de posición de inserción dentro de un Web Component o`<template>`.                           | `<slot name="titulo"></slot>`                                        |
| `<span>`       | Contenedor genérico en línea (`inline`) para aplicar estilos o manipular texto con JS.                          | `<span class="resaltado">texto</span>`                               |
| `<div>`        | Contenedor genérico a nivel de bloque (`block`) para maquetación y estructura de diseño.                       | `<div class="contenedor">...</div>`                                  |
| `<sup>`        | Define texto superíndice (ej. potencias matemáticas, notas al pie).                                               | `x<sup>2</sup>`                                                      |
| `<sub>`        | Define texto subíndice (ej. fórmulas químicas).                                                                  | `H<sub>2</sub>O`                                                     |
| `<i>`          | Define texto en cursiva por estilo visual alternativo (voz, pensamiento, términos técnicos).                      | `<i>Homo sapiens</i>`                                                |
| `<u>`          | Define texto subrayado no articulado (ej. términos mal escritos).                                                  | `<u>palabra</u>`                                                     |
| `<s>`          | Define texto tachado para indicar contenido que ya no es preciso o relevante.                                       | `<s>$50.00</s> $35.00`                                               |
| `<wbr>`        | Especifica una posición donde el navegador puede insertar un salto de línea opcional si es necesario.             | `Super<wbr>califragilistico`                                         |

---

### Resumen Técnico

- **Total de Etiquetas cubiertas**: 100+ (Estándar HTML5)
- **Buenas Prácticas**: El uso de **etiquetas semánticas** optimiza la accesibilidad web (lectores de pantalla), la legibilidad del código y el posicionamiento en motores de búsqueda (SEO).
