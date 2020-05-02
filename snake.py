import pygame
import sys
from random import randint

pygame.init()

# storing game state
# draw the snake
# game loop
# handle arrow key input
# handle colliding with wall/self
# generate food
# handle eating food

def draw(snake, location):
    pygame.draw.rect(screen, red, (snake[0][0] * 10, snake[0][1] * 10, 10, 10), 0)
    
    for i in range(1, len(snake)):
        pygame.draw.rect(screen, white, (snake[i][0] * 10, snake[i][1] * 10, 10, 10), 0)
    if snake[0] != location:
        pygame.draw.rect(screen, white, (location[0] * 10, location[1] * 10, 10, 10), 0)
    if len(snake) == 2500:
        pygame.draw.rect(screen, green, (0, 0, 100, 100), 0)

def move_snake(snake):
    global snake_occupied
    snake_occupied = set()
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = snake[i - 1]
        snake_occupied.add(snake[i])

    if facing == 0:
        snake[0] = (snake[0][0] - 1, snake[0][1])
    elif facing == 1:
        snake[0] = (snake[0][0], snake[0][1] - 1) 
    elif facing == 2:
        snake[0] = (snake[0][0] + 1, snake[0][1])
    else:
        snake[0] = (snake[0][0], snake[0][1] + 1)

def collision(snake, snake_occupied, location):
    if snake[0] in snake_occupied or snake[0][0] < 0 or snake[0][0] > 49 or snake[0][1] < 0 or snake[0][1] > 49:
        pygame.draw.rect(screen, red, (0, 0, 100, 100), 0)
        pygame.display.update()
        pygame.time.delay(1000)
        pygame.quit(); sys.exit()
    if snake[0] == location:
        snake.append(location)
        food(snake_occupied)
    
def food(snake_occupied):
    global location
    location = (randint(0, TILES - 1), randint(0, TILES - 1))
    while location in snake_occupied or location == snake[0]:
        location = (randint(0, TILES - 1), randint(0, TILES - 1))

TILES = 50
snake = [(20, 20), (21, 20), (22, 20), (23, 20), (24, 20)] # new segments are added to the last segment opposite the second last segment, if added on top of head it doesn't end the game
facing = 0 # 0 is left, 1 is up, 2 is right, 3 is down
screen = pygame.display.set_mode((TILES * 10, TILES * 10))
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
snake_occupied = set()
location = (randint(0, TILES - 1), randint(0, TILES - 1))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and facing != 2:
                facing = 0
                break
            elif event.key == pygame.K_RIGHT and facing != 0:
                facing = 2
                break
            elif event.key == pygame.K_UP and facing != 3:
                facing = 1
                break
            elif event.key == pygame.K_DOWN and facing != 1:
                facing = 3
                break
    screen.fill(black)
    draw(snake, location)
    move_snake(snake)
    collision(snake, snake_occupied, location)
    
    pygame.time.delay(75)        
    pygame.display.update()
    