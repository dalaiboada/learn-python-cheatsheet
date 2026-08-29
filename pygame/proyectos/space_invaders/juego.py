from pygame import *
from random import randint

# CORRECIONES
# 1. la función del player fire()
# 2. velocidad del ship
# 3. el sonido
# 4. time.delay(50)

class GameSprite(sprite.Sprite):
    # constructor de clase
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
	def update(self):
		keys = key.get_pressed()

		if keys[K_LEFT] and self.rect.x > 5:
			self.rect.x -= self.speed
			
		if keys[K_RIGHT] and self.rect.x < win_width - 85:
			self.rect.x += self.speed
            
	def fire(self):
		bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, 15)
		bullets.add(bullet)
		fire_sound.play()
    
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost += 1

class Bullet(GameSprite):
  def update(self):
    self.rect.y -= self.speed
    
    if self.rect.y < 0:
      self.kill()
            
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Shooter")

background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))

# Musica y sonidos
mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()

fire_sound = mixer.Sound('fire.ogg')

# fuentes
font.init()
font1 = font.SysFont("Arial", 36)

win = font1.render('GANASTE', True, (255,255,255))
lose = font1.render('PERDISTE', True, (180, 0, 0))

font2 = font.SysFont(None, 35)

# estadisticas
score = 0
lost = 0
goal = 10
max_lost = 3

ship = Player("rocket.png", 5, win_height - 100, 80, 100, 10)

monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy("ufo.png", randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)

bullets = sprite.Group()    
    
run = True
finish = False
clock = time.Clock()
FPS = 60

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False
            
        elif e.type == KEYDOWN:
          if e.key == K_SPACE:
            ship.fire()

    if not finish:
        window.blit(background, (0, 0))
				
        # Movimiento
        ship.update()
        monsters.update()
        bullets.update()
				
        # Renderizado
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)
				
        # Textos
        text_score = font2.render("Cuenta: " + str(score), 1, (255, 255, 255))
        window.blit(text_score, (10, 20))

        text_lost = font2.render("Perdido: " + str(lost), 1, (255, 255, 255))
        window.blit(text_lost, (10, 50))
        
        # Colisiones
        collides = sprite.groupcollide(monsters, bullets, True, True)
        
        for c in collides:
          score = score + 1
          
          monster = Enemy('ufo.png', randint(80, win_width - 80), -40, 80, 60, randint(1,5))
          monsters.add(monster)
          
        # Derrota
        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
          finish = True
          window.blit(lose, (200,200))
          
        
        # Victoria
        if score >= goal:
          finish = True
          window.blit(win, (200,200))

        display.update()
    time.delay(50)