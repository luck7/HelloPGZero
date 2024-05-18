import pgzrun
import random

# Constants
WIDTH = 800
HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Snake
snake = [(10, 10)]
snake_dir = RIGHT
snake_grow = False

# Apple
apple = (15, 15)

# Game state
game_over = False


def draw():
    screen.clear()
    draw_snake()
    draw_apple()
    if game_over:
        screen.draw.text(
            "GAME OVER", center=(WIDTH // 2, HEIGHT // 2), fontsize=50, color="red"
        )


def draw_snake():
    for segment in snake:
        screen.draw.filled_rect(
            Rect(segment[0] * GRID_SIZE, segment[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE),
            "green",
        )


def draw_apple():
    screen.draw.filled_rect(
        Rect(apple[0] * GRID_SIZE, apple[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE), "red"
    )


def update():
    if not game_over:
        move_snake()
        check_collisions()


def move_snake():
    global snake, snake_grow, apple

    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    snake = [new_head] + snake[:-1]

    if snake_grow:
        snake.append(snake[-1])
        snake_grow = False
    if new_head == apple:
        snake_grow = True
        place_apple()


def check_collisions():
    global game_over
    head = snake[0]

    if head[0] < 0 or head[0] >= GRID_WIDTH or head[1] < 0 or head[1] >= GRID_HEIGHT:
        game_over = True
    if head in snake[1:]:
        game_over = True


def place_apple():
    global apple
    apple = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
    while apple in snake:
        apple = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))


def on_key_down(key):
    global snake_dir
    if key == keys.UP and snake_dir != DOWN:
        snake_dir = UP
    elif key == keys.DOWN and snake_dir != UP:
        snake_dir = DOWN
    elif key == keys.LEFT and snake_dir != RIGHT:
        snake_dir = LEFT
    elif key == keys.RIGHT and snake_dir != LEFT:
        snake_dir = RIGHT


pgzrun.go()
