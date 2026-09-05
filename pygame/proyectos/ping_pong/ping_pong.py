from pygame import *

# --- ASSETS ---

# Imágenes

# Texto

# Música y sonidos

# Colores
bg_color = (200, 255, 255)

# --- AJUSTES VENTANA ---
ventana_ancho = 700
ventana_alto = 500

display.set_caption("Ping pong")
ventana = display.set_mode((ventana_ancho, ventana_alto))
ventana.fill(bg_color)

# --- CLASES Y ESTRUCTURAS ---

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
 
        self.image = transform.scale(image.load(player_image), (wight, height))
        self.speed = player_speed
 
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        ventana.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
	# Flechas direccionales
	def update_r(self):
		keys = key.get_pressed()

		if keys[K_UP] and self.rect.y > 5:
			self.rect.x -= self.speed

		if keys[K_DOWN] and self.rect.y < ventana_alto - 80:
			self.rect.x += self.speed

	def update_l(self):
		keys = key.get_pressed()

		if keys[K_w] and self.rect.y > 5:
			self.rect.x -= self.speed

		if keys[K_s] and self.rect.y < ventana_alto - 80:
			self.rect.x += self.speed

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

		# Textos
  
        # Movimientos

        # Renderizado

		# Colisiones

        display.update()
    # el ciclo se ejecuta cada 0.05 segundos
    time.delay(50)
