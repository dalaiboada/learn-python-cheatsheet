# Sintaxis Jinja

**Jinja** es un **motor de plantillas para Python**.

En pocas palabras, te permite mezclar código (variables, condicionales, bucles) dentro de archivos de texto o HTML para **generar contenido dinámico de forma automática** antes de mostrarlo o procesarlo.

**1. Comentarios**

No aparecen en el resultado final:

```jinja
{# Esto es un comentario y no se renderiza #}

```

---

**2. Mostrar Variables**

Se usan dobles llaves `{{ }}`:

```jinja
<p>Hola, {{ nombre }}</p>
<p>Edad: {{ usuario.edad }}</p>
<p>Primer item: {{ lista[0] }}</p>

```

*Crear una variable local:*

```jinja
{% set ciudad = "Caracas" %}
<p>Ubicación: {{ ciudad }}</p>

```

---

**3. Estructuras de Control**

Se usan llaves con porcentaje `{% %}`:

**Condicional (`if / elif / else`)**

```jinja
{% if edad >= 18 %}
  <p>Mayor de edad</p>
{% elif edad >= 13 %}
  <p>Adolescente</p>
{% else %}
  <p>Menor de edad</p>
{% endif %}

```

**Bucle (`for`)**

```jinja
<ul>
{% for fruta in frutas %}
  <li>{{ fruta }}</li>
{% endfor %}
</ul>

```