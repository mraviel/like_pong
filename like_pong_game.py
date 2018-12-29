# python tamplate for a new pygame project
import pygame
from os import path
import random

#the img folder
img_folder = path.join(path.dirname(__file__), 'img')
sound_folder = path.join(path.dirname(__file__), 'sound')

WIDTH = 400
HEIGHT = 500
FPS = 64

# define colors (red,green,blue)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
COLOR_FOR_INTRO_AND_OVER = (194, 134, 33)
COLOR_FOR_WIN = (168, 49, 19)
COLOR_FOR_GAME = (44, 107, 165)

#the font of the game text
font_name = pygame.font.match_font('arial')

#show text on the screen
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

#the openning screen
def game_intro():
    #the game start function
    screen.fill(COLOR_FOR_INTRO_AND_OVER)
    intro = True
    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                    sound3.play()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        draw_text(screen, 'Like Pong', 50, WIDTH / 2, HEIGHT / 3)
        draw_text(screen, 'all you need to do is remove all the blocks', 20, WIDTH / 2, HEIGHT / 2)
        draw_text(screen, 'Press SPACE to play and Q to quit', 20, WIDTH / 2, HEIGHT / 1.8)
        pygame.display.update()
        clock.tick(FPS)

def game_over():
    #the game over function
    screen.fill(COLOR_FOR_INTRO_AND_OVER)
    sound3.play()
    over = True
    while over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()


        draw_text(screen, 'GAME OVER', 50, WIDTH / 2, HEIGHT / 3)
        draw_text(screen, 'Press Q to quit', 20, WIDTH / 2, HEIGHT / 1.8)
        pygame.display.update()
        clock.tick(FPS)

def game_win():
    #the game win function
    screen.fill(COLOR_FOR_WIN)
    sound3.play()
    win = True
    while win:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        draw_text(screen, 'GOOD JOB', 50, WIDTH / 2, HEIGHT / 3)
        draw_text(screen, 'press Q to quit', 20, WIDTH / 2, HEIGHT / 1.8)
        pygame.display.update()
        clock.tick(FPS)


class Player(pygame.sprite.Sprite):
    """the player class"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,25))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 1)
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -4
        if keystate[pygame.K_RIGHT]:
            self.speedx = 4
        self.rect.x += self.speedx
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

class Ball(pygame.sprite.Sprite):
    """the ball class"""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (30,15))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT / 1.5
        self.speedy = random.randint(2,5)
        self.speedx = random.randint(2,5)
        self.radius = int(self.rect.width * .85 /2)
        self.out = True

    def update(self):
        self.rect.bottom += self.speedy
        self.rect.right += self.speedx
        if (self.rect.right > WIDTH + 10):
            self.speedx = random.randint(-4, -2)
        if (self.rect.left < -10):
            self.speedx = random.randint(2, 4)
        if (self.rect.bottom > HEIGHT):
            self.out = False
            self.speedy = random.randint(-4, -2)
        if (self.rect.bottom < 10):
            self.speedy = random.randint(2, 4)


class Block(pygame.sprite.Sprite):
    """the block class"""

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45,20))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)

pygame.init()
pygame.mixer.init()  # for the sound work

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LIKE_PONG")
clock = pygame.time.Clock()


#load all the photos
player_img = pygame.image.load(path.join(img_folder, 'new_ball.jpg')).convert()
#load all the sound
sound1 = pygame.mixer.Sound(path.join(sound_folder, 'jump_01.wav'))
sound2 = pygame.mixer.Sound(path.join(sound_folder, 'jump_07.wav'))
sound3 = pygame.mixer.Sound(path.join(sound_folder, 'screen_sound.wav'))
pygame.mixer.music.set_volume(0.5)

#all the Groups
all_sprites = pygame.sprite.Group()
all_balls = pygame.sprite.Group()
all_blocks = pygame.sprite.Group()

#all the objects in the game
player = Player()
ball = Ball()

#all the blocks objects
#blocks raw 1
block1 = Block(65,50)
block2 = Block(120,50)
block3 = Block(175, 50)
block4 = Block(230, 50)
block5 = Block(285, 50)
block6 = Block(340, 50)
#blocks raw 2
block1_raw2 = Block(65, 80)
block2_raw2 = Block(120, 80)
block3_raw2 = Block(175, 80)
block4_raw2 = Block(230, 80)
block5_raw2 = Block(285, 80)
block6_raw2 = Block(340, 80)
#blocks raw 3
block1_raw3 = Block(65, 110)
block2_raw3 = Block(120, 110)
block3_raw3 = Block(175, 110)
block4_raw3 = Block(230, 110)
block5_raw3 = Block(285, 110)
block6_raw3 = Block(340, 110)
#blocks raw 4
block1_raw4 = Block(65, 140)
block2_raw4 = Block(120, 140)
block3_raw4 = Block(175, 140)
block4_raw4 = Block(230, 140)
block5_raw4 = Block(285, 140)
block6_raw4 = Block(340, 140)
#blocks raw 5
block1_raw5 = Block(65, 170)
block2_raw5 = Block(120, 170)
block3_raw5 = Block(175, 170)
block4_raw5 = Block(230, 170)
block5_raw5 = Block(285, 170)
block6_raw5 = Block(340, 170)


#add the raw 1
all_sprites.add(block1)
all_blocks.add(block1)
all_sprites.add(block2)
all_blocks.add(block2)
all_sprites.add(block3)
all_blocks.add(block3)
all_sprites.add(block4)
all_blocks.add(block4)
all_sprites.add(block5)
all_blocks.add(block5)
all_sprites.add(block6)
all_blocks.add(block6)
#add the raw 2
all_sprites.add(block1_raw2)
all_blocks.add(block1_raw2)
all_sprites.add(block2_raw2)
all_blocks.add(block2_raw2)
all_sprites.add(block3_raw2)
all_blocks.add(block3_raw2)
all_sprites.add(block4_raw2)
all_blocks.add(block4_raw2)
all_sprites.add(block5_raw2)
all_blocks.add(block5_raw2)
all_sprites.add(block6_raw2)
all_blocks.add(block6_raw2)
#add the raw 3
all_sprites.add(block1_raw3)
all_blocks.add(block1_raw3)
all_sprites.add(block2_raw3)
all_blocks.add(block2_raw3)
all_sprites.add(block3_raw3)
all_blocks.add(block3_raw3)
all_sprites.add(block4_raw3)
all_blocks.add(block4_raw3)
all_sprites.add(block5_raw3)
all_blocks.add(block5_raw3)
all_sprites.add(block6_raw3)
all_blocks.add(block6_raw3)
#add the raw 4
all_sprites.add(block1_raw4)
all_blocks.add(block1_raw4)
all_sprites.add(block2_raw4)
all_blocks.add(block2_raw4)
all_sprites.add(block3_raw4)
all_blocks.add(block3_raw4)
all_sprites.add(block4_raw4)
all_blocks.add(block4_raw4)
all_sprites.add(block5_raw4)
all_blocks.add(block5_raw4)
all_sprites.add(block6_raw4)
all_blocks.add(block6_raw4)
#add the raw 5
all_sprites.add(block1_raw5)
all_blocks.add(block1_raw5)
all_sprites.add(block2_raw5)
all_blocks.add(block2_raw5)
all_sprites.add(block3_raw5)
all_blocks.add(block3_raw5)
all_sprites.add(block4_raw5)
all_blocks.add(block4_raw5)
all_sprites.add(block5_raw5)
all_blocks.add(block5_raw5)
all_sprites.add(block6_raw5)
all_blocks.add(block6_raw5)

all_sprites.add(ball)
all_balls.add(ball)
all_sprites.add(player)

game_intro()
points = 0
# Game loop
running = True
agian = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # process input(events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # update
    all_sprites.update()
    # ball hit the player
    hits = pygame.sprite.spritecollide(player, all_balls, False)
    for hit in hits:
        sound2.play()
        ball.speedy = random.randint(-4, -2)
        ball.rect.bottom += ball.speedy

    # ball hit the block
    hits = pygame.sprite.spritecollide(ball, all_blocks, True, pygame.sprite.collide_circle)
    for hit in hits:
        sound1.play()
        ball.speedy = 4
        ball.rect.bottom += ball.speedy
        points += 1
        if points >= 30:
            game_win()

    # Draw / render
    screen.fill((COLOR_FOR_GAME))
    all_sprites.draw(screen)
    if ball.out == False:
        game_over()

    # after! drawing everything flip to display
    pygame.display.flip()


pygame.quit()