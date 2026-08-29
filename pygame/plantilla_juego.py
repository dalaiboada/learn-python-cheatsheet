from pygame import *

# --- ASSETS ---

# Imágenes
img_fondo = "nombre_imagen.png"  # fondo de juego

# Texto

# Música y sonidos


# --- AJUSTES VENTANA ---
ventana_ancho = 700
ventana_alto = 500

display.set_caption("Tirador")

ventana = display.set_mode((ventana_ancho, ventana_alto))
fondo = transform.scale(image.load(img_fondo), (ventana_ancho, ventana_alto))


# --- CLASES Y ESTRUCTURAS ---

class GameSprite(sprite.Sprite):
    pass


# ELEMENTOS DEL JUEGO

# Personajes


# CICLO PRINCIPAL DE JUEGO

finish = False
run = True 

while run:
    # EVENTOS
    for e in event.get():
        if e.type == QUIT:
            run = False       

    if not finish:
        # actualizar fondo
        ventana.blit(fondo, (0, 0))

		# Textos
  
        # Movimientos

        # Renderizado

		# Colisiones

        display.update()
    # el ciclo se ejecuta cada 0.05 segundos
    time.delay(50)