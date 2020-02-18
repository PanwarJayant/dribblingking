# importing pygame modules and coordinates:
import pygame
import random
from config import *
from pygame.locals import(
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_RIGHT,
    K_ESCAPE,
    K_LEFT,
    KEYDOWN,
    QUIT,
)

# setting up clock for framerate
clk = pygame.time.Clock()

# initializing pygame:
pygame.init()


# making font
fnt = pygame.font.Font("freesansbold.ttf", 32)
txt = fnt.render("Player 1 LOST the ball, Press any key to continue",
                 True, (0, 255, 0), (0, 0, 128))
txt2 = fnt.render("Player 2 LOST the ball, Press any key to continue",
                  True, (0, 255, 0), (0, 0, 128))
txtrt = txt.get_rect()
txtrt2 = txt2.get_rect()
txtrt.center = (scwid/2, sclent/2)
txtrt2.center = (scwid/2, sclent/2)
display_surface = pygame.display.set_mode((scwid, sclent))
display_surface2 = pygame.display.set_mode((scwid, sclent))

yay = 0
ytxt = fnt.render("Player 1 has completed the level, Wait for sometime",
                  True, (0, 255, 0), (0, 0, 128))
ytxt2 = fnt.render("Player 2 has completed the level, Wait for sometime",
                   True, (0, 255, 0), (0, 0, 128))
yrect = ytxt.get_rect()
yrect2 = ytxt2.get_rect()
yrect.center = (scwid/2, sclent/2)
yrect2.center = (scwid/2, sclent/2)


# creating first player object:
class Plyr(pygame.sprite.Sprite):
    def __init__(self):
        super(Plyr, self).__init__()
        self.srf = pygame.image.load("messi.jpg").convert()
        self.srf = pygame.transform.scale(self.srf, (40, 50))
        self.srf.set_colorkey((0, 128, 128), RLEACCEL)
        self.rect = self.srf.get_rect(
            center=(
                scwid/2,
                sclent,
            )
        )

    # moving the player
    def mov(self, presskey):
        if presskey[K_UP]:
            self.rect.move_ip(0, -5)
        if presskey[K_DOWN]:
            self.rect.move_ip(0, 5)
        if presskey[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if presskey[K_RIGHT]:
            self.rect.move_ip(5, 0)
        # keep player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > scwid:
            self.rect.right = scwid
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > sclent:
            self.rect.bottom = sclent

# creating second player object


class Plyr2(pygame.sprite.Sprite):
    def __init__(self):
        super(Plyr2, self).__init__()
        self.srf = pygame.image.load("messi.jpg").convert()
        self.srf = pygame.transform.scale(self.srf, (40, 50))
        self.srf.set_colorkey((0, 128, 128), RLEACCEL)
        self.rect = self.srf.get_rect(
            center=(
                scwid/2,
                0,
            )
        )

    # moving the 2nd player
    def mov(self, presskey):
        if presskey[K_UP]:
            self.rect.move_ip(0, -5)
        if presskey[K_DOWN]:
            self.rect.move_ip(0, 5)
        if presskey[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if presskey[K_RIGHT]:
            self.rect.move_ip(5, 0)
        # keep 2nd player on screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > scwid:
            self.rect.right = scwid
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > sclent:
            self.rect.bottom = sclent


# making enemies or obstacles:
i = 1


class Enem(pygame.sprite.Sprite):
    def __init__(self):
        super(Enem, self).__init__()
        self.srf = pygame.image.load("enemy.jpg").convert()
        self.srf = pygame.transform.scale(self.srf, (70, 30))
        self.srf.set_colorkey((255, 255, 255), RLEACCEL)
        global i
        if i == 1:

            self.rect = self.srf.get_rect(
                center=(
                    0,
                    random.randint(80, 120),
                )
            )

        if i == 2:
            self.rect = self.srf.get_rect(
                center=(
                    0,
                    random.randint(230, 320),
                )
            )
        if i == 3:
            self.rect = self.srf.get_rect(
                center=(
                    0,
                    random.randint(430, 520),
                )
            )
        if i == 4:
            self.rect = self.srf.get_rect(
                center=(
                    0,
                    random.randint(630, 720),
                )
            )
        if i == 5:
            self.rect = self.srf.get_rect(
                center=(
                    0,
                    random.randint(830, 920),
                )
            )

        i = i+1

        if i == 6:
            # global i
            i = 1
        self.speed = random.randint(5, 15)

    # moving enemy
    def update(self, lvl):
        lvl = (lvl-1) * 10
        self.rect.move_ip(self.speed+lvl, 0)
        if self.rect.x > scwid:
            #	print('killing')
            self.kill()

# making fixed enemies


class Enemyfix(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super(Enemyfix, self).__init__()
        self.srf = pygame.image.load("enf.png")
        self.srf = pygame.transform.scale(self.srf, (50, 40))
        self.rect = self.srf.get_rect(
            center=(
                x,
                y,
            )
        )


# creating fixed enemy sprite group
enf = pygame.sprite.Group()

# creating custom event for adding new enemies
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 3000)

# instantiating the player and player2 objects
player = Plyr()
# player2 = Plyr2()

# building enemies and sprite groups
enemies = pygame.sprite.Group()
allene = pygame.sprite.Group()
allene.add(player)

# Title and ICon
pygame.display.set_caption("Dribble King")
ic = pygame.image.load("soccer.png")
pygame.display.set_icon(ic)

# flag for checking interrupt in game
# interupt=0


# flag for checking collision
global col1
col1 = 0
global col2
col2 = 0

# flag for checking player number
global pl
pl = 1

prev = 0

player1scr = 0
player2scr = 0
s = 0
p = 0
d = 0
p1 = 0
d1 = 0
p2 = 0
d2 = 0
p3 = 0
d3 = 0
p4 = 0
d4 = 0

s2p = 0
p2p = 0
d2p = 0
p12p = 0
d12p = 0
p22p = 0
d22p = 0
p32p = 0
d32p = 0
p42p = 0
d42p = 0
enemf = Enemyfix(390, 780)
enemf2 = Enemyfix(250, 580)
enemf3 = Enemyfix(380, 380)
enemf4 = Enemyfix(1000, 180)
enemf5 = Enemyfix(440, 980)
enemf6 = Enemyfix(290, 180)
enemf7 = Enemyfix(606, 180)
enemf8 = Enemyfix(990, 380)
enemf9 = Enemyfix(777, 980)
enemf91 = Enemyfix(712, 30)
enemf92 = Enemyfix(833, 580)
enf.add(enemf)
enf.add(enemf2)
enf.add(enemf3)
enf.add(enemf4)
enf.add(enemf5)
enf.add(enemf6)
enf.add(enemf7)
enf.add(enemf8)
enf.add(enemf9)
enf.add(enemf91)
enf.add(enemf92)
# creating the main loop for running the game
running = True
while running:
    if pl == 1 and col1 == 0:
        for event in pygame.event.get():
            # close the game if close button is pressed
            if event.type == pygame.QUIT:
                running = False
            # close the game if ESC key is pressed
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            # adding a new enemy
            elif event.type == ADDENEMY:
                newenemy = Enem()
                enemies.add(newenemy)
                allene.add(newenemy)

            # making object of enemyfix and adding to sprite group

            # filling the screen with color
        scrn.fill((255, 165, 0))

        # making different slabs
        pygame.draw.rect(scrn, (86, 178, 218), (0, 950, 1200, 50))
        pygame.draw.rect(scrn, (86, 178, 218), (0, 750, 1200, 50))
        pygame.draw.rect(scrn, (86, 178, 218), (0, 550, 1200, 50))
        pygame.draw.rect(scrn, (86, 178, 218), (0, 350, 1200, 50))
        pygame.draw.rect(scrn, (86, 178, 218), (0, 0, 1200, 50))
        pygame.draw.rect(scrn, (86, 178, 218), (0, 150, 1200, 50))

        crnt = pygame.time.get_ticks()

        tim = crnt - prev
        text = "Time: " + str(round(tim/1000))
        scrn.blit(fnt.render(text, True, (255, 0, 0)), (0, 0))

        # creating and setting player on screen
        scrn.blit(player.srf, player.rect)

        # moving enemy
        enemies.update(lvl1)

        # updating score
        y = player.rect.top
        if y < 950 and s == 0:
            player1scr += 5
            s = 1
        if y <= 800 and p == 0:
            player1scr += 10
            p = 1
        if y < 750 and d == 0:
            player1scr += 5
            d = 1
        if y <= 600 and p1 == 0:
            player1scr += 10
            p1 = 1
        if y < 550 and d1 == 0:
            player1scr += 5
            d1 = 1
        if y <= 400 and p2 == 0:
            player1scr += 10
            p2 = 1
        if y < 350 and d2 == 0:
            player1scr += 5
            d2 = 1
        if y <= 200 and p3 == 0:
            player1scr += 10
            p3 = 1
        if y < 150 and d3 == 0:
            player1scr += 5
            d3 = 1
        if y <= 50 and p4 == 0:
            player1scr += 10
            p4 = 1
        if y <= 0 and d4 == 0:
            # print("player 1 has completed the level")
            player1scr += 5
            d4 = 1
            yay = 1
            lvl1 += 1

        if yay == 1:
            # messageTime = clk.get_ticks()
            s = 0
            p = 0
            d = 0
            p1 = 0
            d1 = 0
            p2 = 0
            d2 = 0
            p3 = 0
            d3 = 0
            p4 = 0
            d4 = 0
            player.kill()
            pl = 2
            display_surface.blit(ytxt, yrect)
            prev = crnt
            player1scr = player1scr - round(((prev/1000))/(lvl1-1))
            if col2 == 1:
                pl = 1
                player = Plyr()
            elif col2 == 0:
                player2 = Plyr2()

        ts2 = "Player2 Score: " + str(player2scr)
        scrn.blit(fnt.render(ts2, True, (255, 0, 0)), (755, 0))
        ts = "Player1 Score: " + str(player1scr)
        scrn.blit(fnt.render(ts, True, (255, 0, 0)), (155, 0))

        # check for keys pressed and move player
        presskey = pygame.key.get_pressed()
        player.mov(presskey)

        # create all enemies on screen
        for enm in allene:
            scrn.blit(enm.srf, enm.rect)

        # creating fixed enemies
        for e in enf:
            scrn.blit(e.srf, e.rect)

        # global interupt
        # interupt=0

        # collision detection for all enemies
        if pygame.sprite.spritecollideany(player, enemies) or pygame.sprite.spritecollideany(player, enf):
            # print("hitting enemey")
            col1 = 1

    elif pl == 1 and col1 == 1:
        # print("Collided")
        display_surface.blit(txt, txtrt)
        prev = crnt
        player.kill()
        s = 0
        p = 0
        d = 0
        p1 = 0
        d1 = 0
        p2 = 0
        d2 = 0
        p3 = 0
        d3 = 0
        p4 = 0
        d4 = 0

        # while interupt==1:
        for event in pygame.event.get():
            # close the game if close button is pressed
            if event.type == pygame.QUIT:
                running = False
            # close the game if ESC key is pressed
            elif event.type == KEYDOWN:
                # interupt=0
                pl = 2
                player2 = Plyr2()
                if yay == 1:
                    player1scr = player1scr - round(((prev/1000))/(lvl1-1))
                    yay = 0

    elif pl == 2 and col2 == 0:
        # print("player 2 hasnt collided")
        for event in pygame.event.get():
            # close the game if close button is pressed
            if event.type == pygame.QUIT:
                running = False

            # close the game if ESC key is pressed
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

            # adding a new enemy
            elif event.type == ADDENEMY:
                newenemy = Enem()
                enemies.add(newenemy)
                allene.add(newenemy)

        # filling the screen with color
        scrn.fill((255, 165, 0))

        # making different slabs
        pygame.draw.rect(scrn, (86, 178, 218), (0, 950, 1200, 50))
        pygame.draw.rect(scrn, (86, 178, 218), (0, 750, 1200, 50))
        pygame.draw.rect(scrn, (86, 178, 218), (0, 550, 1200, 50))
        pygame.draw.rect(scrn, (86, 178, 218), (0, 350, 1200, 50))
        pygame.draw.rect(scrn, (86, 178, 218), (0, 0, 1200, 50))
        pygame.draw.rect(scrn, (86, 178, 218), (0, 150, 1200, 50))

        # timer
        crnt = pygame.time.get_ticks()
        tim = crnt - prev
        text = "Time: " + str(round(tim/1000))
        scrn.blit(fnt.render(text, True, (255, 0, 0)), (0, 0))

        # creating and setting player on screen
        scrn.blit(player2.srf, player2.rect)

        # moving enemy
        enemies.update(lvl2)

        # updating score
        y = player2.rect.top
        if y > 50 and p42p == 0:
            player2scr += 5
            p42p = 1
        if y > 150 and d32p == 0:
            player2scr += 10
            d32p = 1
        if y > 200 and p32p == 0:
            player2scr += 5
            p32p = 1
        if y > 350 and d22p == 0:
            player2scr += 10
            d22p = 1
        if y > 400 and p22p == 0:
            player2scr += 5
            p22p = 1
        if y > 550 and d12p == 0:
            player2scr += 10
            d12p = 1
        if y > 600 and p12p == 0:
            player2scr += 5
            p12p = 1
        if y > 750 and d2p == 0:
            player2scr += 10
            d2p = 1
        if y > 800 and p2p == 0:
            player2scr += 5
            p2p = 1
        if y >= 940 and s2p == 0:
            player2scr += 10
            s2p = 1
        if s2p == 1:
            s2p = 3
            player2scr += 5
            d42p = 1
            yay = 1
            lvl2 += 1

        if yay == 1:
            s2p = 0
            p2p = 0
            d2p = 0
            p12p = 0
            d12p = 0
            p22p = 0
            d22p = 0
            p32p = 0
            d32p = 0
            p42p = 0
            d42p = 0
            pl = 1
            player2.kill()
            prev = crnt
            player2scr = player2scr - round(((prev/1000))/(lvl2-1))
            display_surface.blit(ytxt2, yrect2)
            if col1 == 0:
                player = Plyr()
            elif col1 == 1:
                pl = 2
                player2 = Plyr2()

        ts2 = "Player2 Score: " + str(player2scr)
        scrn.blit(fnt.render(ts2, True, (255, 0, 0)), (755, 0))
        ts = "Player1 Score: " + str(player1scr)
        scrn.blit(fnt.render(ts, True, (255, 0, 0)), (155, 0))

        # check for keys pressed and move player
        presskey = pygame.key.get_pressed()
        player2.mov(presskey)

        # create all enemies on screen
        for enm in allene:
            scrn.blit(enm.srf, enm.rect)

        # creating fixed enemies
        for e in enf:
            scrn.blit(e.srf, e.rect)

        # global interupt
        # interupt=0

        # collision detection for moving enemies
        if pygame.sprite.spritecollideany(player2, enemies):
            # interupt=1
            col2 = 1

        # collision detection for fixed enemies
        if pygame.sprite.spritecollideany(player2, enf):
            # interupt=1
            col2 = 1

    elif col2 == 1 and pl == 2:
        prev = crnt
        player2.kill()
        s2p = 0
        p2p = 0
        d2p = 0
        p12p = 0
        d12p = 0
        p22p = 0
        d22p = 0
        p32p = 0
        d32p = 0
        p42p = 0
        d42p = 0
        display_surface.blit(txt2, txtrt2)

        # while interupt==1:
        for event in pygame.event.get():
            # close the game if close button is pressed
            if event.type == pygame.QUIT:
                running = False

            if event.type == KEYDOWN:
                pl = 1
                player = Plyr()
                if yay == 1:
                    player2scr = player2scr - round(((prev/1000))/(lvl2-1))
                yay = 0

    if col1 == 1 and col2 == 1:
        # print("game over")
        for event in pygame.event.get():
            # close the game if close button is pressed
            if event.type == pygame.QUIT:
                running = False

            # close the game if ESC key is pressed
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

        fnt = pygame.font.Font("freesansbold.ttf", 28)
        twl = fnt.render("Player 1 won the game, as he went till level: " + str(lvl1) +
                         "while Player2 went till level: " + str(lvl2), True, (0, 255, 0), (0, 0, 128))
        twl2 = fnt.render("Player 2 won the game, as he went till level: " + str(lvl2) +
                          "while Player1 went till level: " + str(lvl1), True, (0, 255, 0), (0, 0, 128))
        tws = fnt.render("Player 1 won the game, as he had score: " + str(player1scr) +
                         "while Player2 had score:" + str(player2scr), True, (0, 255, 0), (0, 0, 128))
        tws2 = fnt.render("Player 2 won the game, as he had score: " + str(player2scr) +
                          "while Player1 had score:" + str(player1scr), True, (0, 255, 0), (0, 0, 128))
        tiy = fnt.render("The game is tied, both had the same level and score: " +
                         str(player1scr), True, (0, 255, 0), (0, 0, 128))
        twlrt = twl.get_rect()
        twlrt2 = twl2.get_rect()
        twsrt = tws.get_rect()
        twsrt2 = tws2.get_rect()
        tiyrt = tiy.get_rect()
        twlrt.center = (scwid/2, sclent/2)
        twlrt2.center = (scwid/2, sclent/2)
        twsrt.center = (scwid/2, sclent/2)
        twsrt2.center = (scwid/2, sclent/2)
        tiyrt.center = (scwid/2, sclent/2)
        display_surface = pygame.display.set_mode((scwid, sclent))
        if lvl1 > lvl2:
            display_surface.blit(twl, twlrt)
        elif lvl2 > lvl1:
            display_surface.blit(twl2, twlrt2)
        elif lvl2 == lvl1:
            if player2scr > player1scr:
                display_surface.blit(tws2, twsrt2)
            elif player1scr > player2scr:
                display_surface.blit(tws, twsrt)
            elif player2scr == player1scr:
                display_surface.blit(tiy, tiyrt)

    # displaying contents on screen
    if yay == 1:
        pygame.display.flip()
        pygame.time.delay(1500)
        yay = 0
    pygame.display.flip()

    # setting framerate
    clk.tick(30)

pygame.quit()
