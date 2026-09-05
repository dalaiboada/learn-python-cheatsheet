from pygame import *
from random import randint
# fuentes
font.init()
font1 = font.Font(None, 80)

win = font1.render('GANASTE', True, (255, 255, 255))
lose = font1.render('PERDISTE', True, (180, 0, 0))

font2 = font.Font(None, 35)

# imágenes:
img_back = "galaxy.jpg"  # fondo de juego
img_hero = "rocket.png"  # personaje
img_enemy = 'ufo.png' # enemigo
img_bullet = 'bullet.png' # bala

# estadisticas
score = 0
lost = 0
goal = 10
max_lost = 3

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # cada objeto debe almacenar la propiedad rect en la cual está inscrito
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
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)
        fire_sound.play()
    
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        
        # desaparece si alcanza el borde de la pantalla
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost = lost + 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        
        if self.rect.y < 0:
            self.kill()
        
# Crea la ventana
win_width = 700
win_height = 500
display.set_caption("Tirador")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

# crea objetos
ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)

monsters = sprite.Group()
for i in range(1, 6):
    monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 50, randint(1, 5))
    monsters.add(monster)

bullets = sprite.Group()

finish = False
run = True 

while run:
    # el evento de pulsación del botón Cerrar
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:   
                ship.fire()         

    if not finish:
        # actualizar fondo
        window.blit(background, (0, 0))

		# Textos
        text = font2.render("Puntaje: " + str(score), 1, (255,255,255))
        window.blit(text, (10, 20))

        text_lose = font2.render("Fallos: " + str(lost), 1, (255,255,255))
        window.blit(text_lose, (10, 50))

        # Movimientos
        ship.update()
        monsters.update()
        bullets.update()

        # Renderizado
        ship.reset()
        monsters.draw(window)
        bullets.draw(window)

		# Colisiones
        collides = sprite.groupcollide(monsters, bullets, True, True)
        for c in collides:
            score = score + 1
            monster = Enemy(img_enemy, randint(80, win_width - 80), -40, 80, 60, randint(1, 5))
            monsters.add(monster)

		# Derrota
        if sprite.spritecollide(ship, monsters, False) or lost >= max_lost:
            finish = True
            window.blit(lose, (200, 200))

		# Victoria
        if score >= goal:
            finish = True
            window.blit(win, (200, 200))

        display.update()
    # el ciclo se ejecuta cada 0.05 segundos
    time.delay(50)
