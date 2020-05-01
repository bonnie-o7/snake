import pygame
import sys

pygame.init()

# storing game state
# draw the snake
# game loop
# handle arrow key input
# handle colliding with wall/self
# generate food
# handle eating food

def draw(snake):
    screen.fill(black)
    for i in range(len(snake)):
        pygame.draw.rect(screen, white, (snake[i][0] * 10 + 50, snake[i][1] * 10 + 50, 10, 10), 0)

def move_snake(snake):
    for i in range(len(snake) - 1, 0, -1):
        snake[i] = snake[i - 1]

    if facing == 0:
        snake[0] = (snake[0][0] - 1, snake[0][1])
    elif facing == 1:
        snake[0] = (snake[0][0], snake[0][1] - 1) 
    elif facing == 2:
        snake[0] = (snake[0][0] + 1, snake[0][1])
    else:
        snake[0] = (snake[0][0], snake[0][1] + 1)

snake = [(20, 20), (21, 20), (22, 20), (23, 20), (24, 20)] # new segments are added to the last segment opposite the second last segment, if added on top of head it doesn't end the game
facing = 0 # 0 is left, 1 is up, 2 is right, 3 is down
snake_occupied = set(snake)
screen = pygame.display.set_mode((500, 500))
white = (255, 255, 255)
black = (0, 0, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                facing = 0
            elif event.key == pygame.K_RIGHT:
                facing = 2
            elif event.key == pygame.K_UP:
                facing = 1
            elif event.key == pygame.K_DOWN:
                facing = 3
            
    draw(snake)
    move_snake(snake)
    pygame.time.delay(100)        
    pygame.display.update()
    