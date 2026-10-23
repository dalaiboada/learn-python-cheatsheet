from kivy.core.window import Window
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, Rectangle

Window.size = (360, 640)

class PantallaMenu(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  
        
        contendor = BoxLayout(orientation='vertical', spacing=10, padding=[24, 40, 24, 30])
        contenedor_botones = BoxLayout(orientation='vertical', spacing=10, size_hint_y = 0.45)
        
        # fondo
        with contendor.canvas.before:
            Color(0.08, 0.08, 0.12, 1)  # Color de fondo (negro)
            self.rectangulo = Rectangle(size=contendor.size, pos=contendor.pos)
            #contendor.bind()
        
        titulo = Label(
            text='CHARADAS', 
            font_size=24,
            bold=True,
            color=(1, 0.8, 0.2, 1), 
            size_hint_y=0.15
        )
        
        subtitulo = Label(
            text='Selecciona una categoria:', 
            font_size=15, 
            color=(0.8, 0.8, 0.9, 1),
            size_hint_y=0.08
        )
        
        btn1 = Button(text='Viedeojuegos', background_color = (0.9, 0.2, 0.4,1))
        btn2 = Button(text='Peliculas', background_color = (0.2, 0.6, 1,1))
        btn3 = Button(text='Acciones', background_color = (0.2, 0.8, 0.4,1))
        btn4 = Button(text='Animales', background_color = (1, 0.6, 0.1,1))
        
        contendor.add_widget(titulo)
        contendor.add_widget(subtitulo)
        
        contenedor_botones.add_widget(btn1)
        contenedor_botones.add_widget(btn2)
        contenedor_botones.add_widget(btn3)
        contenedor_botones.add_widget(btn4)
        
        contendor.add_widget(contenedor_botones)
        
        self.add_widget(contendor) 
        
class PantallaJuego(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)   
        
class PantallaResueltado(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)   

class Charadas(App):
    def build(self):
        administrador_pantallas = ScreenManager()
        administrador_pantallas.add_widget(PantallaMenu(name='menu'))
        administrador_pantallas.add_widget(PantallaJuego(name='juego'))
        administrador_pantallas.add_widget(PantallaResueltado(name='resueltado'))
        return administrador_pantallas
    
Charadas().run()