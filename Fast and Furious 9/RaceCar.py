import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 750

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
brown = (165, 42, 42)

car_width = 60

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Fast and Furious 9")
clock = pygame.time.Clock()

CarImage = pygame.image.load("CocheAzul2.png")
Obstaculo= pygame.image.load("ObstaculoAzul2.png")

#Marcador
def things_dodged(count):
    font = pygame.font.SysFont(None, 45)
    text = font.render("Score " + str(count), True, red)
    gameDisplay.blit(text, (20, 20))

#Coche
def car(x, y):
    gameDisplay.blit(CarImage, (x, y))

#Obstaculos
def things(thingx, thingy, thingw, thingh, color):
    color = green
    pygame.draw.rect(gameDisplay, color,  [thingx, thingy, thingw, thingh])


def text_objects(text, font):
    textSurface = font.render(text, True, red)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.Font('Calibri', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

#Choque con el coche
def crash():
    message_display("You Crashed")

#GAME LOOP
def game_loop():
    x = (display_width * 0.48)
    y = (display_height * 0.79)

    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 20
    thing_width = 100
    thing_height = 100

    dodged = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -6.5
                elif event.key == pygame.K_RIGHT:
                    x_change = 6.5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(black)

        things(thing_startx, thing_starty, thing_width, thing_height, blue)
        thing_starty += thing_speed
        car(x, y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            if thing_speed < 15:
                thing_speed += 0.15

        if y < thing_starty + thing_height:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x + car_width > thing_startx and x + car_width < thing_startx + thing_width:
                print('x crossover')
                crash()

        pygame.display.update()
        clock.tick(60)


game_loop()
pygame.quit()
quit()