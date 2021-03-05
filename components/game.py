import pygame
from components.snake import Snake
import random
import time
from components.food import Food

WIDTH=640
HEIGHT=480
WHITE=(255, 255, 255)
BLACK=(0, 0, 0)
RED=(255, 0, 0)
DIRECTION='DOWN'

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
little_snake = Snake(WIDTH/2, HEIGHT/2)
clock = pygame.time.Clock()
apple = Food(100, 200)
pygame.display.set_caption('Cobrinha')
pygame.font.init()
font_26 = pygame.font.SysFont(None, 26)
font_48 = pygame.font.SysFont(None, 48)

game_running = True

def handle_user_input():
    global DIRECTION
    LASTDIRECTION = DIRECTION
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    if(LASTDIRECTION == 'UP'): 
                        return
                    little_snake.move('DOWN')
                    DIRECTION = 'DOWN'
                elif event.key == pygame.K_UP:
                    if(LASTDIRECTION == 'DOWN'): 
                        return
                    little_snake.move('UP')
                    DIRECTION = 'UP'
                elif event.key == pygame.K_LEFT:
                    if(LASTDIRECTION == 'RIGHT'): 
                        return
                    little_snake.move('LEFT')
                    DIRECTION = 'LEFT'
                elif event.key == pygame.K_RIGHT:
                    if(LASTDIRECTION == 'LEFT'): 
                        return
                    little_snake.move('RIGHT')
                    DIRECTION = 'RIGHT'

def draw():
 for position in little_snake.body:
       pygame.draw.rect(screen, WHITE, [ position[0], position[1], 10, 10])


def detect_collision(rect):
    little_snake_last_position = little_snake.body[-1]
    return rect.collidepoint(little_snake_last_position[0], little_snake_last_position[1])


def move_apple():
    rangeX= random.randrange(100, WIDTH - 10)
    rangeY = random.randrange(100, HEIGHT - 10)
    little_snake.eat()
    apple.move(rangeX, rangeY)

def game_status():
    global game_running
    if (little_snake.x >= WIDTH  or little_snake.x < 0):
        game_running = False
    if (little_snake.y >= HEIGHT  or little_snake.y < 0):
        game_running = False

def check_bump():
    global game_running
    for position in little_snake.body[:-1]:
        if(little_snake.body[-1] == position):
            game_running = False


def loop():
    pygame.display.update()
    while game_running:
        game_status()
        check_bump()
        little_snake.move(DIRECTION)
        handle_user_input() 
        screen.fill(BLACK)
        draw()
        food = pygame.draw.rect(screen, RED, [apple.x, apple.y, 10, 10])
        pygame.display.update()
        collision = detect_collision(food)
        if(collision == True):
            move_apple()
        clock.tick(15)
    play_again()

def play_again():
    global game_running
    global little_snake
    while game_running == False:
        screen.fill(BLACK)
        score = font_48.render(f'Your score is {little_snake.length}', False, WHITE)
        msg = font_48.render('Deseja jogar de novo?', False, WHITE)
        sub_msg = font_26.render('aperte y', False, WHITE)
        screen.blit(score, ((WIDTH - score.get_width()) / 2, 30))
        screen.blit(msg, ((WIDTH - msg.get_width()) / 2, (HEIGHT - msg.get_height()) / 2))
        screen.blit(sub_msg, ((WIDTH - sub_msg.get_width()) / 2, ((HEIGHT - sub_msg.get_height()) / 2) + 60))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    game_running = True
                    little_snake = Snake(WIDTH/2, HEIGHT/2)
    loop()
