from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen

class BotonPantalla(Button):
    def __init__(self, pantalla_actual, destino, direccion, **kwargs):
        super().__init__(**kwargs)
        self.pantalla_actual = pantalla_actual
        self.destino = destino
        self.direccion = direccion
    
    def on_press(self):
        self.pantalla_actual.manager.transition.direction = self.direccion
        self.pantalla_actual.manager.current = self.destino

class PantallaPrincipal(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        etiqueta_texto = Label(text='Escoger pantalla')
        btn1 = BotonPantalla(self, destino='primera_pantalla', direccion='left', text='1')
        btn2 = BotonPantalla(self, destino='segunda_pantalla', direccion='left', text='2')
        btn3 = BotonPantalla(self, destino='tercera_pantalla', direccion='left', text='3')
        btn4 = BotonPantalla(self, destino='cuarta_pantalla', direccion='left', text='4')
        
        # layouts
        layout_principal = BoxLayout()
        layout_botones = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        layout_botones.add_widget(btn1)
        layout_botones.add_widget(btn2)
        layout_botones.add_widget(btn3)
        layout_botones.add_widget(btn4)
        
        layout_principal.add_widget(etiqueta_texto)
        layout_principal.add_widget(layout_botones)
        
        self.add_widget(layout_principal)

class PrimeraPantalla(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  
        
        layout = BoxLayout()
        
        btn1 = BotonPantalla(self, destino='pantalla_principal', direccion='left', text='volver')
        layout.add_widget(btn1)
        self.add_widget(layout)
           
class SegundaPantalla(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)   
            
class TerceraPantalla(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)    
           
class CuartaPantalla(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)       

class MyApp(App):
    def build(self):
        admin_pantallas = ScreenManager()
        admin_pantallas.add_widget(PantallaPrincipal(name='pantalla_principal'))
        admin_pantallas.add_widget(PrimeraPantalla(name='primera_pantalla'))
        admin_pantallas.add_widget(SegundaPantalla(name='segunda_pantalla'))
        admin_pantallas.add_widget(TerceraPantalla(name='tercera_pantalla'))
        admin_pantallas.add_widget(CuartaPantalla(name='cuarta_pantalla'))

        return admin_pantallas
    
MyApp().run()