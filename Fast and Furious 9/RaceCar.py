import pygame
import time
import random


# COLORS
black = (0, 0, 0)
gray = (122, 122, 122)
white = (255, 255, 255)

red = (200, 0, 0)
light_red = (255, 0, 0)

green = (0, 200, 0)
light_green = (0, 255, 0)


# CAR DIMENSIONS
car_width = 15
car_height = 40

# DISPLAY DIMENSIONS
display_width = 800
display_height = 800



game_display = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()

score_game = 0

def game_init():
    pygame.init()

#Score
def display(count, x, y, message_format='Text: %d'):
    font = pygame.font.SysFont("Arial", 40)
    text = font.render(message_format % count, True, black)
    game_display.blit(text, (x, y))


#UPLOAD IMAGES
def load_image(x, y, image_name):
    img = pygame.image.load(image_name)
    game_display.blit(img, (x, y))

#TYPE OF TEXT
def text_object(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

#DISPLAY TO SHOW MESSAGES
def message_display(text):
    largeText = pygame.font.SysFont("Arial", 115)
    textSurf, textRect = text_object(text, largeText)
    textRect.center = ((display_width / 2), (display_height / 2))
    game_display.blit(textSurf, textRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()

#BUTTONS
#button(text, dimensions/location of the text, colors of the text, action(e.g. if you want to quit the game)
def button(msg, x, y, w, h, ic, ac, action=None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(game_display, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(game_display, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("Arial", 20)
    textSurf, textRect = text_object(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    game_display.blit(textSurf, textRect)


#CAR COLLISION
def crash(x, y):
    largeText = pygame.font.SysFont("Arial", 90)
    textSurf, textRect = text_object("GAME OVER", largeText)
    textRect.center = ((display_width / 2), (display_height / 4))
    game_display.blit(textSurf, textRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again", 150, 250, 100, 50, green, light_green, game_loop)
        button("Quit", 550, 250, 100, 50, red, light_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def quitgame():
    pygame.quit()
    quit()


#INTRODUCTION SCREEN
def game_intro():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        game_display.fill(gray)

        largeText = pygame.font.SysFont("Arial", 80)
        textSurf, textRect = text_object("FAST & FURIOUS", largeText)
        textRect.center = ((display_width / 2), (display_height / 2))
        game_display.blit(textSurf, textRect)

        button("GO", 200, 450, 100, 50, green, light_green, game_loop)
        button("Quit", 500, 450, 100, 50, red, light_red, quitgame)

        pygame.display.update()
        clock.tick(15)

#GAME LOOP
def game_loop():
    global score_game


    x = (display_width * 0.45)
    y = (display_height * 0.75)

    x_change = 0


    thing_width = 70
    thing_height = 140

    thing_startx = random.randrange(100, display_width - 200)
    thing_starty = -600
    thing_speed = 18

    lineY = 0
    lineH = 450
    line_speed = 20



    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    x_change = -10
                if event.key == pygame.K_RIGHT:
                    x_change = 10

            if event.type == pygame.KEYUP:
                x_change = 0

        x += x_change

        game_display.fill(gray)

        load_image(thing_startx, thing_starty, 'images/ObstaculoAzul2.png')
        load_image(x, y, 'images/CocheAzul1.png')

        thing_starty += thing_speed
        lineY += line_speed

        display(((thing_speed * 60)-1020), 5, 45, "Speed: %d km/h")
        display(score_game, 5, 5, "Score: %d")

        #CRASH BOUNDARIES ON THE DISPLAY
        if x > display_width - car_width - 70 or x < 0:
            crash(x, y)

        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(170, display_width - thing_width - 150)
            score_game += 1  #INCREASE SCORE WHEN DODGING
            thing_speed += 1 / 20  # ACCELERATE

        if lineY > display_height:
            lineY = 0 - lineH
            thing_speed += 1 / 15



        #CHECK CRASHES
        if y < (thing_starty + thing_height) and y + car_height >= thing_starty + thing_height:
            if x > thing_startx and x < (thing_startx + thing_width) or x + car_width > thing_startx \
                    and x + car_width < thing_startx + thing_width:
                crash(x, y)

        pygame.display.update()
        clock.tick(60)


def main():
    game_init()
    game_intro()
    game_loop()
    pygame.quit()
    quit()


if __name__ == '__main__':
    main()
