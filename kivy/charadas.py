from kivy.core.window import Window
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle
import random

# Base de datos de paAplabras por categoría
PALABRAS = {
    "Videojuegos": ["Minecraft", "Fortnite", "Mario Bros", "Roblox", "Pac-Man", "Zelda"],
    "Películas": ["Spider-Man", "Shrek", "Harry Potter", "Minions", "Titanic", "Toy Story"],
    "Animales Locos": ["Unicornio", "T-Rex", "Pingüino bailando", "Gato espacial", "Mono", "Tiburón"],
    "Acciones Extrañas": ["Atrapado en arenas movedizas", "Atacado por abejas", "Dormido de pie", "Zombi hambriento", "Bailando breakdance"]
}

Window.size = (360, 640)


# --- CLASE BOTÓN PARA CAMBIAR DE PANTALLA ---
class BotonPantalla(Button):
    def __init__(self, pantalla_actual, destino, direccion, **kwargs):
        super().__init__(**kwargs)
        self.pantalla_actual = pantalla_actual
        self.destino = destino
        self.direccion = direccion

    def on_press(self):
        self.pantalla_actual.manager.transition.direction = self.direccion
        self.pantalla_actual.manager.current = self.destino


# --- PANTALLA 1: MENÚ DE CATEGORÍAS ---
class PantallaMenu(Screen):
    def __init__(self, **kwargs):
        super(PantallaMenu, self).__init__(**kwargs)
        
        contenedor = BoxLayout(orientation='vertical', padding=[24, 40, 24, 30], spacing=15)
        
        # Fondo oscuro
        with contenedor.canvas.before:
            Color(0.08, 0.08, 0.12, 1)
            self.rectangulo = Rectangle(size=contenedor.size, pos=contenedor.pos)
            contenedor.bind(size=self._actualizar_rectangulo, pos=self._actualizar_rectangulo)

        # Encabezado (título + subtítulo)
        titulo = Label(
            text="CHARADAS", 
            font_size=24, 
            bold=True, 
            color=(1, 0.8, 0.2, 1),
            size_hint_y=0.15
        )
        subtitulo = Label(
            text="Elige una categoría:", 
            font_size=15, 
            color=(0.8, 0.8, 0.9, 1),
            size_hint_y=0.08
        )
        
        contenedor.add_widget(titulo)
        contenedor.add_widget(subtitulo)

        # Contenedor para la lista de botones
        contenedor_botones = BoxLayout(orientation='vertical', spacing=10, size_hint_y=0.45)

        # --- BOTONES CREADOS UNO A UNO (SIN BUCLES) ---
        
        # Botón 1: Videojuegos (Rosa/Rojo)
        btn_videojuegos = BotonPantalla(
            pantalla_actual=self,
            destino='juego',
            direccion='left',
            text="Videojuegos",
            font_size=16,
            bold=True,
            background_normal='',
            background_color=(0.9, 0.2, 0.4, 1)
        )
        btn_videojuegos.bind(on_release=lambda x: self.elegir_categoria("Videojuegos"))
        contenedor_botones.add_widget(btn_videojuegos)

        # Botón 2: Películas (Azul)
        btn_peliculas = BotonPantalla(
            pantalla_actual=self,
            destino='juego',
            direccion='left',
            text="Películas",
            font_size=16,
            bold=True,
            background_normal='',
            background_color=(0.2, 0.6, 1, 1)
        )
        btn_peliculas.bind(on_release=lambda x: self.elegir_categoria("Películas"))
        contenedor_botones.add_widget(btn_peliculas)

        # Botón 3: Animales Locos (Verde)
        btn_animales = BotonPantalla(
            pantalla_actual=self,
            destino='juego',
            direccion='left',
            text="Animales Locos",
            font_size=16,
            bold=True,
            background_normal='',
            background_color=(0.2, 0.8, 0.4, 1)
        )
        btn_animales.bind(on_release=lambda x: self.elegir_categoria("Animales Locos"))
        contenedor_botones.add_widget(btn_animales)

        # Botón 4: Acciones Extrañas (Naranja)
        btn_acciones = BotonPantalla(
            pantalla_actual=self,
            destino='juego',
            direccion='left',
            text="Acciones Extrañas",
            font_size=16,
            bold=True,
            background_normal='',
            background_color=(1, 0.6, 0.1, 1)
        )
        btn_acciones.bind(on_release=lambda x: self.elegir_categoria("Acciones Extrañas"))
        contenedor_botones.add_widget(btn_acciones)

        contenedor.add_widget(contenedor_botones)
        self.add_widget(contenedor)

    def _actualizar_rectangulo(self, instancia, valor):
        self.rectangulo.pos = instancia.pos
        self.rectangulo.size = instancia.size

    def elegir_categoria(self, categoria):
        # Carga la lista de palabras correspondiente en la pantalla del juego
        pantalla_juego = self.manager.get_screen('juego')
        pantalla_juego.cargar_categoria(categoria)


# --- PANTALLA 2: LA PALABRA / ACCIÓN ---
class PantallaJuego(Screen):
    def __init__(self, **kwargs):
        super(PantallaJuego, self).__init__(**kwargs)
        self.categoria_actual = ""
        self.palabras_disponibles = []
        self.puntos = 0
        
        contenedor = BoxLayout(orientation='vertical', padding=[24, 30, 24, 25], spacing=15)
        
        with contenedor.canvas.before:
            Color(0.12, 0.12, 0.18, 1)
            self.rectangulo = Rectangle(size=contenedor.size, pos=contenedor.pos)
            contenedor.bind(size=self._actualizar_rectangulo, pos=self._actualizar_rectangulo)

        self.etiqueta_categoria = Label(text="", font_size=15, color=(0.7, 0.7, 0.9, 1), size_hint_y=0.1)
        contenedor.add_widget(self.etiqueta_categoria)

        self.etiqueta_palabra = Label(
            text="¡Preparados!", 
            font_size=26, 
            bold=True, 
            color=(1, 1, 1, 1),
            halign='center',
            valign='middle',
            size_hint_y=0.78
        )
        self.etiqueta_palabra.bind(size=self.etiqueta_palabra.setter('text_size'))
        contenedor.add_widget(self.etiqueta_palabra)

        # Botones de juego ("Pasar" y "¡Adivinado!")
        contenedor_botones = BoxLayout(orientation='horizontal', spacing=12, size_hint_y=0.12)
        
        btn_pasar = Button(
            text="Pasar", 
            font_size=15, 
            background_normal='', 
            background_color=(0.8, 0.2, 0.2, 1)
        )
        btn_pasar.bind(on_press=self.siguiente_palabra)

        btn_acierto = Button(
            text="¡Adivinado!", 
            font_size=15, 
            background_normal='', 
            background_color=(0.2, 0.7, 0.3, 1)
        )
        btn_acierto.bind(on_press=self.sumar_punto)

        contenedor_botones.add_widget(btn_pasar)
        contenedor_botones.add_widget(btn_acierto)
        
        contenedor.add_widget(contenedor_botones)
        self.add_widget(contenedor)

    def _actualizar_rectangulo(self, instancia, valor):
        self.rectangulo.pos = instancia.pos
        self.rectangulo.size = instancia.size

    def cargar_categoria(self, categoria):
        self.categoria_actual = categoria
        self.etiqueta_categoria.text = f"Categoría: {categoria}"
        self.palabras_disponibles = list(PALABRAS[categoria])
        random.shuffle(self.palabras_disponibles)
        self.puntos = 0
        self.siguiente_palabra()

    def siguiente_palabra(self, instancia=None):
        if self.palabras_disponibles:
            palabra = self.palabras_disponibles.pop()
            self.etiqueta_palabra.text = palabra
        else:
            pantalla_resultado = self.manager.get_screen('resultado')
            pantalla_resultado.mostrar_resultado(self.puntos)
            self.manager.transition.direction = 'left'
            self.manager.current = 'resultado'

    def sumar_punto(self, instancia):
        self.puntos += 1
        self.siguiente_palabra()


# --- PANTALLA 3: RESULTADOS ---
class PantallaResultado(Screen):
    def __init__(self, **kwargs):
        super(PantallaResultado, self).__init__(**kwargs)
        
        contenedor = BoxLayout(orientation='vertical', padding=[30, 40, 30, 35], spacing=20)
        
        with contenedor.canvas.before:
            Color(0.08, 0.08, 0.12, 1)
            self.rectangulo = Rectangle(size=contenedor.size, pos=contenedor.pos)
            contenedor.bind(size=self._actualizar_rectangulo, pos=self._actualizar_rectangulo)

        titulo = Label(text="¡FIN DE RONDA!", font_size=24, bold=True, color=(1, 0.8, 0.2, 1), size_hint_y=0.2)
        
        self.etiqueta_puntaje = Label(text="", font_size=18, color=(1, 1, 1, 1), size_hint_y=0.2)
        self.etiqueta_mensaje = Label(text="", font_size=15, color=(0.4, 0.9, 1, 1), italic=True, size_hint_y=0.35)

        # Botón para regresar al menú usando BotonPantalla
        btn_reiniciar = BotonPantalla(
            pantalla_actual=self,
            destino='menu',
            direccion='right',
            text="Volver al Menú", 
            font_size=16, 
            bold=True, 
            background_normal='', 
            background_color=(0.4, 0.2, 0.8, 1),
            size_hint_y=0.13
        )

        contenedor.add_widget(titulo)
        contenedor.add_widget(self.etiqueta_puntaje)
        contenedor.add_widget(self.etiqueta_mensaje)
        contenedor.add_widget(btn_reiniciar)

        self.add_widget(contenedor)

    def _actualizar_rectangulo(self, instancia, valor):
        self.rectangulo.pos = instancia.pos
        self.rectangulo.size = instancia.size

    def mostrar_resultado(self, puntos):
        self.etiqueta_puntaje.text = f"Puntaje: {puntos}"
        if puntos >= 4:
            self.etiqueta_mensaje.text = "¡Nivel: Actor de Hollywood!"
        elif puntos >= 2:
            self.etiqueta_mensaje.text = "¡Nivel: Muy bien, se entiende!"
        else:
            self.etiqueta_mensaje.text = "¡Nivel: Estatua de piedra!"


# --- APLICACIÓN PRINCIPAL ---
class AplicacionCharadas(App):
    def build(self):
        administrador_pantallas = ScreenManager()
        administrador_pantallas.add_widget(PantallaMenu(name='menu'))
        administrador_pantallas.add_widget(PantallaJuego(name='juego'))
        administrador_pantallas.add_widget(PantallaResultado(name='resultado'))
        return administrador_pantallas

AplicacionCharadas().run()