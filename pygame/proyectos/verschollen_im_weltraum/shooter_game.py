#create a Maze game!
from pygame import *
from random import randint

#musica
mixer.init()

sonido_fondo = mixer.Sound('fondo.ogg')
fire_sound = mixer.Sound('laser.ogg')

sonido_fondo.set_volume(0.2)  # Ajusta el volumen a 20%
sonido_fondo.play(-1)  # Reproduce el sonido de fondo en bucle

# texto
font.init()
font1 = font.Font(None, 18)
font2 = font.Font(None, 55)

win = font1.render('YEA WIN', True, (255, 255, 0))
lose = font1.render('HA HA LOSER', True, (119, 240, 50))

# imagenes
img_back = "fondo.jpg"
img_hero = "player.png"
img_Enemy = "enemy.png"
img_bullet = "bala.png"
img_bullet_desviada = "bala_desviada.png"
img_bullet_bomba = "bala_bomba.png"

# estadisticas 
score = 0
lost = 0
goal = 11
max_lost = 5 

# ventana
win_width = 900
win_height = 650

ventana = display.set_mode((win_width, win_height))
display.set_caption("Verschollen im Weltraum")
fondo = transform.scale(image.load(img_back), (win_width, win_height))

# CLASES Y ESTRUCTURAS
class Gamesprite(sprite.Sprite):
    def __init__(self, Player_image, Player_x, Player_y, size_x, size_y, Player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(Player_image), (size_x, size_y))
        self.speed = Player_speed
        self.rect = self.image.get_rect()
        self.rect.x = Player_x
        self.rect.y = Player_y

    def reset(self):
        ventana.blit(self.image, (self.rect.x, self.rect.y))

class Player(Gamesprite):
	def update(self):
		keys = key.get_pressed()
		if keys[K_LEFT] and self.rect.x > 5:
			self.rect.x -= self.speed
		if keys[K_RIGHT] and self.rect.x < win_width - 80:
			self.rect.x += self.speed

	def fire(self):
		bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 64, 64, -15)
		bullets.add(bullet)
	
	def fire_sin(self):
		bullet = BulletSin(img_bullet_desviada, self.rect.centerx, self.rect.top, 15, 20, -15)
		bullets.add(bullet)

	def bomb(self):
		bullet = Bullet(img_bullet_bomba, self.rect.centerx, self.rect.bottom-32, 32, 32, 0)
		bullets.add(bullet)

class Enemy(Gamesprite):
	def update(self):
		self.rect.y += self.speed
		global lost

		if self.rect.y > win_height:
			self.rect.x = randint(80, win_width - 80)
			self.rect.y = 0
			lost = lost + 1 

class Bullet(Gamesprite):
	def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
		super().__init__(player_image, player_x, player_y, size_x, size_y, player_speed)
		fire_sound.play()
   
	def update(self):
		self.rect.y += self.speed

		if self.rect.y < 0:
			self.kill()

class BulletSin(Bullet):
	count = 0
	side = 1
	def update(self):
		self.rect.y += self.speed
		self.rect.x += 5 * self.side
		self.count+=1

		if self.count>=10:
			self.count=0
			self.side*=-1

		if self.rect.y < 0:
			self.kill()

# Personajes
Neil_Armstrong = Player(img_hero, 5, win_height - 100, 80, 100, 10)

monsters = sprite.Group()
for i in range(1, 6):
	monster = Enemy(img_Enemy, randint(80, win_width - 80), 70, 48, 48, randint(1, 5))
	monsters.add(monster)

bullets = sprite.Group()

# ciclo de juego
finish = False
ejecutando = True
reloj = time.Clock()
FPS = 60

control_vista = 'menu'  # Variable para controlar la vista actual (puede ser 'menu' o 'juego')

while ejecutando:
	# EVENTOS
	for evento in event.get():
		# cerrar ventana
		if evento.type == QUIT:
			ejecutando = False

		# Teclado
		elif evento.type == KEYDOWN:
			if evento.key == K_SPACE:
				Neil_Armstrong.fire()
    
			if evento.key == K_LSHIFT:
				Neil_Armstrong.bomb()
    
			if evento.key == K_RSHIFT:
				Neil_Armstrong.fire_sin()

	if finish != True:
		ventana.blit(fondo, (0, 0))

		if control_vista == 'menu':
			pass  # Reemplaza esto con código para mostrar el menú y los botones

		elif control_vista == 'juego':
			# texto
			text = font2.render('Puntaje:'+ str(score), 1, (208, 222, 67))
			ventana.blit(text, (10, 20))

			text_lose = font2.render('Fallos:'+ str(lost), 1, (227, 18, 18))
			ventana.blit(text_lose, (10, 50))

			# renderizado
			Neil_Armstrong.reset()
			monsters.draw(ventana)
			bullets.draw(ventana)
	
			# movimiento
			bullets.update()
			monsters.update()
			Neil_Armstrong.update()

			# colisiones
			collides = sprite.groupcollide(monsters, bullets, True, True)
			for c in collides:
				score = score + 1
				monster = Enemy(img_Enemy, randint(80, win_width - 80), 70, 48, 48, randint(1, 5))
				monsters.add(monster)

			# derrota: jugador choca con enemigo O alcanza el límite de fallos
			if sprite.spritecollide(Neil_Armstrong, monsters, False) or lost >= max_lost:
				finish = True
				ventana.blit(lose, (200, 200))

			# victoria: jugador alcanza el puntaje objetivo
			if score >= goal:
				finish = True
				ventana.blit(win, (200, 200))

		display.update()
	reloj.tick(FPS)