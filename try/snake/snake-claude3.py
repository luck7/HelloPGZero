import pgzrun
from random import randint

# Game dimensions and configuration
WIDTH = 800
HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
snake_dir = 0  # 0-up, 1-right, 2-down, 3-left
apple = (randint(0, GRID_WIDTH - 1), randint(0, GRID_HEIGHT - 1))
score = 0


def draw():
    screen.fill("black")
    for x, y in snake:
        screen.draw.filled_rect(
            Rect((x * GRID_SIZE, y * GRID_SIZE), (GRID_SIZE, GRID_SIZE)), "green"
        )
    screen.draw.filled_rect(
        Rect((apple[0] * GRID_SIZE, apple[1] * GRID_SIZE), (GRID_SIZE, GRID_SIZE)),
        "red",
    )
    screen.draw.text(f"Score: {score}", color="white", topleft=(10, 10))


def update():
    global snake_dir, apple, score, snake

    # Control the snake direction
    if keyboard.up and snake_dir != 2:
        snake_dir = 0
    if keyboard.right and snake_dir != 3:
        snake_dir = 1
    if keyboard.down and snake_dir != 0:
        snake_dir = 2
    if keyboard.left and snake_dir != 1:
        snake_dir = 3
    # Move the snake
    x, y = snake[-1]
    if snake_dir == 0:
        y -= 1
    elif snake_dir == 1:
        x += 1
    elif snake_dir == 2:
        y += 1
    elif snake_dir == 3:
        x -= 1
    new_head = (x, y)

    # Check for game over conditions
    if new_head in snake or x < 0 or x >= GRID_WIDTH or y < 0 or y >= GRID_HEIGHT:
        print("Game Over! Your score was:", score)
        quit()
    # Add new head to the snake
    snake.append(new_head)

    # Check apple collision
    if new_head == apple:
        score += 1
        apple = (randint(0, GRID_WIDTH - 1), randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop(0)  # Remove the tail part


def on_key_down(key):
    global snake_dir
    if key == keys.UP:
        snake_dir = 0
    elif key == keys.RIGHT:
        snake_dir = 1
    elif key == keys.DOWN:
        snake_dir = 2
    elif key == keys.LEFT:
        snake_dir = 3


pgzrun.go()
