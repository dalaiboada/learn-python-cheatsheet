#create a Maze game!
from pygame import *
from random import randint

#musica
mixer.init()
mixer.music.load('fondo.ogg')
mixer.music.play()
#fire_sound = mixer.Sound('Efecto de sonido de un disparo.ogg')

font.init()
font1 = font.Font(None, 18)

win = font1.render('YEA WIN', True, (255, 255, 0))
lose = font1.render('HA HA LOSER', True, (119, 240, 50))

font2 = font.Font(None, 55)

img_back = "galaxy.jpg"
img_hero = "rocket.png"
img_Enemy = "ufo.png"
img_bullet = "bullet.png"

score = 0
lost = 0
goal = 11
max_lost = 5 

win_width = 700
win_height = 500

ventana = display.set_mode((win_width, win_height))
display.set_caption("Verschollen im Weltraum")
fondo = transform.scale(image.load("galaxy.jpg"), (700, 500))

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
		bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
		bullets.add(bullet)
	
	def fire_sin(self):
		bullet = BulletSin(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
		bullets.add(bullet)


	def bomb(self):
		bullet = Bullet(img_bullet, self.rect.centerx, self.rect.bottom-20, 15, 20, 0)
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


#personajes
Neil_Armstrong = Player('rocket.png', 5, win_height - 100, 80, 100, 10)

monsters = sprite.Group()
for i in range(1, 6):
	monster = Enemy(img_Enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
	monsters.add(monster)

bullets = sprite.Group()

# ciclo de juego
finish = False
ejecutando = True
reloj = time.Clock()
FPS = 60



while ejecutando:
	# Botón X
	for evento in event.get():
		if evento.type == QUIT:
			ejecutando = False
		elif evento.type == KEYDOWN:
			if evento.key == K_SPACE:
				Neil_Armstrong.fire()
			if evento.key == K_LSHIFT:
				Neil_Armstrong.bomb()
			if evento.key == K_RSHIFT:
				Neil_Armstrong.fire_sin()

	if finish != True:
		ventana.blit(fondo, (0, 0))

		text = font2.render('Puntaje:'+ str(score), 1, (208, 222, 67))
		ventana.blit(text, (10, 20))

		text_lose = font2.render('Fallos:'+ str(lost), 1, (227, 18, 18))
		ventana.blit(text_lose, (10, 50))

		Neil_Armstrong.update()
		Neil_Armstrong.reset()
		monsters.update()
		monsters.draw(ventana)
		bullets.update()
		bullets.draw(ventana)

		collides = sprite.groupcollide(monsters, bullets, True, True)
		for c in collides:
			score = score + 1
			monster = Enemy(img_Enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
			monsters.add(monster)

		if sprite.spritecollide(Neil_Armstrong, monsters, False) or lost >= max_lost:
			finish = True
			ventana.blit(lose, (200, 200))

		if score >= goal:
			finish = True
			ventana.blit(win, (200, 200))

		display.update()
	reloj.tick(FPS)