import pygame, os
from pygame.constants import K_ESCAPE

WIDTH = 1000
HEIGHT = 600
FPS = 30
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 200, 0)
BLUE = (0, 130, 255)
CK = (0, 255, 0)
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("plat1.1")
clock = pygame.time.Clock()
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'img')
player_img = pygame.image.load(os.path.join(img_folder, 'pl-1.png')).convert()
ground_img = pygame.image.load(os.path.join(img_folder, 'gr-1.png')).convert()
menu_img = pygame.image.load(os.path.join(img_folder, 'mn-1.png')).convert()
bg_img = pygame.image.load(os.path.join(img_folder, 'bg-1.png')).convert()
platform_img = pygame.image.load(os.path.join(img_folder, 'pp-1.png')).convert()
particle_img = pygame.image.load(os.path.join(img_folder, 'pr-1.png')).convert()
ground_img = pygame.transform.scale(ground_img, (2500, 75))
particles = ['pr-1.png', 'pr-2.png', 'pr-3.png']
pl_x = 200
pl_y = 422
x = 0
y = 0
pr_x = 0
pr_y = 0
Flip = 0
frFlip = 0
an = 124
e = -0.1
c = 0
co = 0
platd = 0
plata = 0
BR_for = False
cod = 10

class BackGround(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bg_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        global player
        keys = pygame.key.get_pressed()
        if player.rect.x >= 800 and keys[pygame.K_d] and self.rect.x > -1490:
            if keys[pygame.K_LCTRL]:
                self.rect.x -= 9
            else:
                self.rect.x -= 5
        if player.rect.x <= 100 and keys[pygame.K_a] and self.rect.x < -10:
            if keys[pygame.K_LCTRL]:
                self.rect.x += 9
            else:
                self.rect.x += 5

class Player(pygame.sprite.Sprite):
    def __init__(self, pl_x, pl_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_img
        self.image.set_colorkey(CK)
        self.rect = self.image.get_rect()
        self.rect.center = (pl_x, pl_y)

    def update(self):
        global g, pl_x, pl_y, d, jump, god, player_img, Flip, x, platforms, menu, an, e
        keys = pygame.key.get_pressed()
        check()
        fal()
        uphead()
        ddd()
        aaa()
        if keys[pygame.K_r] and not show_menu:
            ground.rect.x = -10
            platform1.rect.x = 500
            bg.rect.x = 0
            self.rect.x = 200
            self.rect.y = 322
            if Flip == 1:
                player_img = pygame.transform.flip(player_img, 1, 0)
                Flip = 0
            self.image = player_img
            g = 1
        if keys[pygame.K_d] and not show_menu:
            if Flip == 1:
                player_img = pygame.transform.flip(player_img, 1, 0)
                Flip = 0
            player.image = player_img
            if player.rect.x <= 800:
                if keys[pygame.K_d] and keys[pygame.K_LCTRL] and platd == 0:
                    player.rect.x += 9
                elif keys[pygame.K_d] and platd == 0:
                    player.rect.x += 5
        if keys[pygame.K_a] and not show_menu:
            if Flip == 0:
                player_img = pygame.transform.flip(player_img, 1, 0)
                Flip = 1
            self.image = player_img
            if self.rect.x >= 100:
                if keys[pygame.K_LCTRL] and not show_menu and plata == 0:
                    self.rect.x -= 9
                elif keys[pygame.K_a] and platd == 0:
                    self.rect.x -= 5
        if (keys[pygame.K_SPACE] or keys[pygame.K_w] or god) and not show_menu:
            if not god:
                god = True
                jump = True
                d = 20
            elif d <= 0:
                d = 20
                god = False
                jump = False
            else:
                self.rect.y -= d
                d -= 0.5
        self.__init__(self.rect.centerx, self.rect.centery)

class Ground(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = ground_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        global player
        keys = pygame.key.get_pressed()
        if player.rect.x >= 800 and keys[pygame.K_d] and self.rect.x > -1490:
            if keys[pygame.K_LCTRL]:
                self.rect.x -= 9
            else:
                self.rect.x -= 5
        if player.rect.x <= 100 and keys[pygame.K_a] and self.rect.x < -10:
            if keys[pygame.K_LCTRL]:
                self.rect.x += 9
            else:
                self.rect.x += 5

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = platform_img
        self.image.set_colorkey(CK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        keys = pygame.key.get_pressed()
        if player.rect.x >= 800 and keys[pygame.K_d] and ground.rect.x > -1490:
            if keys[pygame.K_LCTRL]:
                self.rect.x -= 9
            else:
                self.rect.x -= 5
        if player.rect.x <= 100 and keys[pygame.K_a] and ground.rect.x < -10:
            if keys[pygame.K_LCTRL]:
                self.rect.x += 9
            else:
                self.rect.x += 5

class Menu(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = menu_img
        self.image.set_colorkey(CK)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
    
    def update(self):
        global show_menu, do, mn1, mn2, pl_x, pl_y, running, cur_pl, player_img, hf, Flip
        keys = pygame.key.get_pressed()
        mouse_pressed = pygame.mouse.get_pressed()
        hf += 1
        if (keys[K_ESCAPE] or mn1) and not show_menu:
            mn1 = True
            if Flip == 1:
                player_img = pygame.transform.flip(player_img, 1, 0)
                Flip = 0
                player.__init__(pla_x, pla_y)
            if self.rect.y >= 100 and mn1:
                self.rect.y -= 70
                player.rect.x = self.rect.x + 90
                player.rect.y = self.rect.y + 135
            else:
                show_menu = True
                mn1 = False
        elif (keys[K_ESCAPE] or mn2) and show_menu:
            mn2 = True
            if self.rect.y <= 600 and mn2:
                self.rect.y += 70
                player.rect.x = self.rect.x + 90
                player.rect.y = self.rect.y + 135
            else:
                show_menu = False
                mn2 = False
                player.rect.x = pl_x
                player.rect.y = pl_y
        elif not show_menu and not mn1 and not mn2:
            pl_x = player.rect.x
            pl_y = player.rect.y
        if show_menu and pygame.mouse.get_pos()[0] >= 500 and pygame.mouse.get_pos()[1] >= 150 and pygame.mouse.get_pos()[0] <= 820 and pygame.mouse.get_pos()[1] <= 200:
            if mouse_pressed[0]:
                mn2 = True
        if show_menu and pygame.mouse.get_pos()[0] >= 500 and pygame.mouse.get_pos()[1] >= 290 and pygame.mouse.get_pos()[0] <= 820 and pygame.mouse.get_pos()[1] <= 340:
            if mouse_pressed[0]:
                running = False
        if show_menu and pygame.mouse.get_pos()[0] >= 215 and pygame.mouse.get_pos()[1] >= 160 and pygame.mouse.get_pos()[0] <= 270 and pygame.mouse.get_pos()[1] <= 200:
            if mouse_pressed[0] and hf >= 7:
                hf = 0
                if cur_pl == 3:
                    player_img = pygame.image.load(os.path.join(img_folder, 'pl-2.png')).convert()
                    cur_pl -= 1
                elif cur_pl == 2:
                    player_img = pygame.image.load(os.path.join(img_folder, 'pl-1.png')).convert()
                    cur_pl -= 1
                player.__init__(pla_x, pla_y)
        if show_menu and pygame.mouse.get_pos()[0] >= 215 and pygame.mouse.get_pos()[1] >= 340 and pygame.mouse.get_pos()[0] <= 270 and pygame.mouse.get_pos()[1] <= 380:
            if mouse_pressed[0] and hf >= 7:
                hf = 0
                if cur_pl == 1:
                    player_img = pygame.image.load(os.path.join(img_folder, 'pl-2.png')).convert()
                    cur_pl += 1
                elif cur_pl == 2:
                    player_img = pygame.image.load(os.path.join(img_folder, 'pl-3.png')).convert()
                    cur_pl += 1
                player.__init__(pla_x, pla_y)

class Particle(pygame.sprite.Sprite):
    def __init__(self, pr_x, pr_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = particle_img
        self.image.set_colorkey(CK)
        self.rect = self.image.get_rect()
        self.rect.center = (pr_x, pr_y)
    
    def update(self):
        global frFlip, particle_img, c, co, cod
        keys = pygame.key.get_pressed()
        if keys[pygame.K_d] and not show_menu and not keys[pygame.K_a]:
            if frFlip == 0:
                frFlip = 1
                particle_img = pygame.transform.flip(particle_img, 1, 0)
            self.rect.x = player.rect.x
            self.rect.y = player.rect.y + 110
        elif keys[pygame.K_a] and not show_menu and not keys[pygame.K_d]:
            if frFlip == 1:
                frFlip = 0
                particle_img = pygame.transform.flip(particle_img, 1, 0)
            self.rect.x = player.rect.x + 60
            self.rect.y = player.rect.y + 110
        pr_x = self.rect.centerx; pr_y = self.rect.centery
        if (keys[pygame.K_d] or keys[pygame.K_a]) and not show_menu and (player.rect.y + 124) >= 520:
            c += 1
            if c >= cod:
                c = 0
                co += 1
                particle_img = pygame.image.load(os.path.join(img_folder, particles[co])).convert()
            if co >= 2:
                co = 0
        else:
            particle_img = pygame.image.load(os.path.join(img_folder, "ck.png")).convert()
        self.__init__(pr_x, pr_y)
        if keys[pygame.K_LCTRL]:
            cod = 5
        else:
            cod = 10
        
def ddd():
    global platd
    platd = 0
    for i in platforms:
        if player.rect.x + 80 >= i.rect.x:
            if player.rect.x + 20 <= i.rect.x + 150:
                if player.rect.y <= i.rect.y + 30:
                    if player.rect.y + 115 >= i.rect.y:
                        platd += 1

def aaa():
    global plata
    plata = 0
    for i in platforms:
        if player.rect.x + 80 >= i.rect.x:
            if player.rect.x + 20 <= i.rect.x + 150:
                if player.rect.y <= i.rect.y + 30:
                    if player.rect.y + 115 >= i.rect.y:
                        plata += 1

def uphead():
    global god
    for i in platforms:
        if (i.rect.x) <= (player.rect.x + 70):
            if (i.rect.x + 124) >= (player.rect.x + 10):
                if (i.rect.y + 30) >= (player.rect.y) and (i.rect.y) <= (player.rect.y):
                    god = False

def check():
    global platforms, player, on_plat
    on_plat = 0
    for i in platforms:
        if (i.rect.x) <= (player.rect.x + 60):
            if (i.rect.x + 150) >= (player.rect.x + 40):
                if (i.rect.y + 30) >= (player.rect.y + 124) and (i.rect.y) <= (player.rect.y + 124):
                    on_plat += 1

def fal():
    global g
    if not show_menu:
        if (player.rect.y + 124) <= 520 and on_plat == 0:
            player.rect.y += int(g)
            g += 0.7
        elif (player.rect.y + 124) >= 530:
            player.rect.y -= 5
        else:
            g = 1

all_sprites = pygame.sprite.Group()
bg = BackGround(x + 1240, y + 300)
ground = Ground(x + 1240, y + 563)
platform1 = Platform(x + 500, y + 370)
platform2 = Platform(x + 800, y + 300)
platform3 = Platform(x + 1000, y + 280)
platform4 = Platform(x + 1200, y + 150)
particle = Particle(x, y)
menu = Menu(x + 500, y + 900)
player = Player(pl_x, pl_y)
all_sprites.add(bg)
all_sprites.add(ground)
all_sprites.add(platform1)
all_sprites.add(platform2)
all_sprites.add(platform3)
all_sprites.add(platform4)
all_sprites.add(menu)
all_sprites.add(particle)
all_sprites.add(player)

platforms = []
platforms.append(platform1)
platforms.append(platform2)
platforms.append(platform3)
platforms.append(platform4)

g = 1
d = 20
do = 20
go = False
god = False
jump = True
running = True
on_plat = 0
show_menu = False
mn1 = False
mn2 = False
cur_pl = 1
hf = 0
pla_x = 240
pla_y = 272
f = 0
f1 = 0

while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(BLUE)
    all_sprites.remove()
    all_sprites.update()
    all_sprites.draw(screen)
    if cur_pl == 1 and (f <= 10 and f1 >= 300):
        if Flip == 0:
            morg = pygame.draw.rect(screen, (0, 227, 84), (player.rect.x + 49, player.rect.y + 6, 18, 7))
        elif Flip == 1:
            morg = pygame.draw.rect(screen, (0, 227, 84), (player.rect.x + 32, player.rect.y + 5, 19, 8))
        f += 1
        if f1 >= 310:
            f1 = 0
            f = 0
    f1 += 1
    pygame.display.flip()

pygame.quit()
