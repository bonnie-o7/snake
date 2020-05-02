import pygame
import sys
from random import randint

pygame.init()

def draw(snake, location):
    # draws the snake head
    pygame.draw.rect(screen, red, (snake[0][0] * 10, snake[0][1] * 10, 10, 10), 0)
    
    for i in range(1, len(snake)): # draws the snake body
        pygame.draw.rect(screen, white, (snake[i][0] * 10, snake[i][1] * 10, 10, 10), 0)
    if snake[0] != location: # draws the food
        pygame.draw.rect(screen, white, (location[0] * 10, location[1] * 10, 10, 10), 0)
    if len(snake) == 2500: # draws the victory signal
        pygame.draw.rect(screen, green, (0, 0, 100, 100), 0)

def move_snake(snake):
    global snake_occupied
    snake_occupied = set()
    # keeps track of where snake segments are after moving
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = snake[i - 1]
        snake_occupied.add(snake[i])

    # adjusts snake position based off the direction it's facing
    if facing == 0:
        snake[0] = (snake[0][0] - 1, snake[0][1])
    elif facing == 1:
        snake[0] = (snake[0][0], snake[0][1] - 1) 
    elif facing == 2:
        snake[0] = (snake[0][0] + 1, snake[0][1])
    else:
        snake[0] = (snake[0][0], snake[0][1] + 1)

def collision(snake, snake_occupied, location):
    # Collide with wall or self => lose game
    if snake[0] in snake_occupied or snake[0][0] < 0 or snake[0][0] > 49 or snake[0][1] < 0 or snake[0][1] > 49:
        pygame.draw.rect(screen, red, (0, 0, 100, 100), 0)
        pygame.display.update()
        pygame.time.delay(1000)
        pygame.quit(); sys.exit()
    # Collide with food => add segment to snake and generate new food
    if snake[0] == location:
        snake.append(location)
        food(snake_occupied)
    
def food(snake_occupied):
    global location
    # randomly generates new food
    location = (randint(0, TILES - 1), randint(0, TILES - 1))
    while location in snake_occupied or location == snake[0]:
        location = (randint(0, TILES - 1), randint(0, TILES - 1))

TILES = 50
snake = [(20, 20), (21, 20), (22, 20), (23, 20), (24, 20)] 
facing = 0 # 0 is left, 1 is up, 2 is right, 3 is down
screen = pygame.display.set_mode((TILES * 10, TILES * 10))
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
snake_occupied = set()
location = (randint(0, TILES - 1), randint(0, TILES - 1))

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # "X" button on window
            pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN: # arrow keys
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
    