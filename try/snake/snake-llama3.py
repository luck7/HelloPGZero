import random

TITLE = "Snake Game"
WIDTH = 400
HEIGHT = 400

snake = [(20, 20)]
direction = (1, 0)
food = (
    random.randint(0, WIDTH // 20 - 1) * 20,
    random.randint(0, HEIGHT // 20 - 1) * 20,
)


def update():
    global snake, direction, food

    # Move the snake
    x, y = snake[0]
    x += direction[0] * 20
    y += direction[1] * 20

    # Check for collision with walls
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        snake = [(20, 20)]
        direction = (1, 0)
    # Check for collision with food
    if (x, y) == food:
        snake.append(snake[-1])
        food = (
            random.randint(0, WIDTH // 20 - 1) * 20,
            random.randint(0, HEIGHT // 20 - 1) * 20,
        )
    # Move the snake
    snake = [(x, y)] + snake[:-1]


def on_key_down(key):
    global direction

    if key == keys.UP:
        direction = (0, -1)
    elif key == keys.DOWN:
        direction = (0, 1)
    elif key == keys.LEFT:
        direction = (-1, 0)
    elif key == keys.RIGHT:
        direction = (1, 0)


def draw():
    screen.clear()

    # Draw the snake
    for segment in snake:
        screen.draw.rect(Rect(segment, (20, 20)), "green")
    # Draw the food
    screen.draw.rect(Rect(food, (20, 20)), "red")
