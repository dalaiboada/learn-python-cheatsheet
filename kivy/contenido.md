# Introducción al desarrollo móvil con Kivy

## 1. ¿Qué es Kivy?

* Kivy es una librería de Python para crear aplicaciones móviles y de escritorio.
* Permite crear interfaces gráficas modernas.
* Una misma aplicación puede ejecutarse en diferentes dispositivos (Windows, Android, Linux, etc.).
* Una aplicación de Kivy está formada por **pantallas**, **widgets** y **eventos**.

---

# 2. ¿Qué es un Widget?

Todo lo que aparece en la pantalla es un widget.

Ejemplos:

* Label → muestra texto.
* Button → botón.
* TextInput → caja de texto.
* BoxLayout → organiza widgets.
* ScrollView → permite desplazarse.
* Screen → representa una pantalla.
* ScreenManager → administra varias pantallas.

---

# 3. El método build()

Toda aplicación hereda de `App`.

El método `build()`:

* es el primero que ejecuta la aplicación;
* crea la interfaz principal;
* devuelve el widget principal.

Ejemplo:

```python
class MyApp(App):
    def build(self):
        return Label(text="Hola")
```

---

# 4. Agregar widgets

Los widgets no aparecen automáticamente.

Hay que agregarlos usando:

```python
layout.add_widget(widget)
```

Todo el diseño de una aplicación consiste en ir agregando widgets a otros widgets.

---

# 5. BoxLayout

Es el diseño (layout) más sencillo.

Sirve para ordenar widgets.

Puede organizar:

```python
orientation="vertical"
```

o

```python
orientation="horizontal"
```

Ejemplo:

```python
layout = BoxLayout(orientation="vertical")
```

---

# 6. Parámetros importantes del BoxLayout

## padding

Agrega espacio entre el borde y los widgets.

```python
padding=10
```

---

## spacing

Agrega separación entre widgets.

```python
spacing=8
```

Los estudiantes deben distinguir claramente:

* **padding → borde**
* **spacing → separación entre elementos**

---

# 7. Screen y ScreenManager

Una aplicación puede tener varias pantallas.

Cada pantalla hereda de:

```python
Screen
```

Todas las pantallas son controladas por:

```python
ScreenManager
```

Ejemplo:

```python
sm = ScreenManager()

sm.add_widget(MainScr(name="main"))
sm.add_widget(FirstScr(name="first"))
```

Para cambiar de pantalla:

```python
self.manager.current = "first"
```

El `ScreenManager` permite crear aplicaciones con múltiples vistas sin abrir nuevas ventanas.

---

# 8. Transiciones entre pantallas

Antes de cambiar de pantalla se puede indicar la dirección de la animación.

```python
self.manager.transition.direction = "left"
```

Algunas direcciones:

* left
* right
* up
* down

---

# 9. Crear una clase personalizada

No siempre usamos directamente los widgets de Kivy.

Podemos crear nuestros propios widgets heredando de otro.

Ejemplo:

```python
class ScrButton(Button):
```

Esto permite reutilizar código y añadir comportamientos nuevos.

---

# 10. Herencia

La herencia permite extender una clase existente.

Ejemplo:

```python
class ScrButton(Button):
```

Dentro del constructor siempre se llama:

```python
super().__init__(**kwargs)
```

para inicializar correctamente la clase padre.

---

# 11. **kwargs

Muchos widgets reciben una cantidad variable de parámetros.

Para ello se utiliza:

```python
**kwargs
```

y se pasan al padre mediante:

```python
super().__init__(**kwargs)
```

Esto permite que la clase siga aceptando parámetros como:

* text
* size_hint
* pos_hint
* color
* font_size

entre otros.

---

# 12. Eventos

Los widgets responden a acciones del usuario.

Ejemplo:

* presionar un botón;
* escribir texto.

Existen tres formas principales de manejar eventos:

* `bind()`;
* asignar una función al evento;
* sobrescribir un método como `on_press()`.

---

# 13. Sobrescribir un método

En lugar de usar `bind()`, podemos redefinir un método.

Ejemplo:

```python
def on_press(self):
```

Cuando el botón se presiona, este método se ejecuta automáticamente.

---

# 14. Cambiar el texto de un Label

Los widgets son objetos.

Sus propiedades pueden modificarse.

Ejemplo:

```python
self.label.text = "Hola"
```

En el proyecto, el texto cambia usando el contenido escrito por el usuario en un `TextInput`.

---

# 15. TextInput

Es el widget para introducir texto.

Ejemplo:

```python
TextInput(multiline=False)
```

Propiedad importante:

```python
self.input.text
```

permite leer el texto ingresado por el usuario.

---

# 16. Widget como atributo de la clase

En lugar de crear una variable local:

```python
txt = Label(...)
```

a veces conviene hacer:

```python
self.txt = Label(...)
```

Así podremos modificar el widget desde cualquier método de la clase.

---

# 17. size_hint

Controla cuánto espacio ocupa un widget respecto a su contenedor.

Ejemplo:

```python
size_hint=(0.5, 1)
```

No representa píxeles, sino una proporción del espacio disponible.

---

# 18. pos_hint

Permite posicionar un widget dentro del espacio disponible.

Ejemplo:

```python
pos_hint={
    "center_x":0.5,
    "center_y":0.5
}
```

También puede utilizar:

* left
* right
* top
* bottom

para ubicar el widget.

---

# 19. ScrollView

Se utiliza cuando el contenido no cabe en la pantalla.

Permite desplazarse vertical u horizontalmente.

Ejemplo:

```python
scroll = ScrollView()

scroll.add_widget(label)
```

Ideal para textos largos o listas.

---

# 20. Adaptación a distintos dispositivos

Las aplicaciones móviles deben verse correctamente en pantallas de diferentes tamaños.

Para ello Kivy ofrece:

* `size_hint`;
* `pos_hint`;
* unidades como `sp` (Scale-independent Pixels), que ayudan a mantener tamaños consistentes en distintos dispositivos.

---

# Conceptos que deben dominar al finalizar la lección

* Explicar qué es Kivy y para qué se utiliza.
* Identificar los widgets principales (`Label`, `Button`, `TextInput`, `BoxLayout`, `Screen`, `ScreenManager` y `ScrollView`).
* Crear una aplicación básica con `App` y `build()`.
* Organizar widgets utilizando `BoxLayout`.
* Crear varias pantallas y navegar entre ellas con `ScreenManager`.
* Crear una clase personalizada heredando de `Button`.
* Comprender el uso de `super()` y `**kwargs`.
* Manejar eventos mediante `on_press()` y otras técnicas.
* Leer datos desde un `TextInput` y actualizar otros widgets.
* Utilizar `size_hint` y `pos_hint` para diseñar interfaces adaptables.
* Comprender cómo Kivy facilita la creación de aplicaciones compatibles con diferentes dispositivos.
