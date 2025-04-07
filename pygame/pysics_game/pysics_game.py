import pygame,setting,random
from os.path import join

pygame.init()
WINDOWN_WIDTH = 1280
WINDOWN_HIGHT = 720
pygame.display.set_caption("Pysics Game")
screen = pygame.display.set_mode((WINDOWN_WIDTH,WINDOWN_HIGHT))
clock = pygame.time.Clock()

color = setting.Theme.earth_tone_blue_and_brown()
player = pygame.Surface((100,100))
player.fill(color[0])
print((100,20)*4)

running = True
x = 0
y = 0
star = [(random.randint(0,100)) for i in range(20)]
print(star)


while running:
    print (random.uniform(-0.5,0.5))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(color[1])
    x += 0.1
    screen.blit(player,(x,100))
    pygame.display.update()
pygame.quit()
    