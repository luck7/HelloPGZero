import pgzrun
from random import randint

WIDTH = 400
HEIGHT = 400

SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 0, 0)

snake = [(WIDTH / 2, HEIGHT / 2)]
dx, dy = 0, 0
food = (randint(0, WIDTH - 20) // 20 * 20, randint(0, HEIGHT - 20) // 20 * 20)


def draw():
    screen.clear()
    for segment in snake:
        screen.draw.filled_rect(Rect(segment[0], segment[1], 20, 20), SNAKE_COLOR)
    screen.draw.filled_rect(Rect(food[0], food[1], 20, 20), FOOD_COLOR)


def update():
    global dx, dy, food

    head = (snake[0][0] + dx, snake[0][1] + dy)

    if (
        head in snake
        or head[0] < 0
        or head[0] >= WIDTH
        or head[1] < 0
        or head[1] >= HEIGHT
    ):
        print("Game Over!")
        quit()
    snake.insert(0, head)

    if head == food:
        food = (randint(0, WIDTH - 20) // 20 * 20, randint(0, HEIGHT - 20) // 20 * 20)
    else:
        snake.pop()


def on_key_down(key):
    global dx, dy

    if key == keys.UP:
        dx, dy = 0, -20
    elif key == keys.DOWN:
        dx, dy = 0, 20
    elif key == keys.LEFT:
        dx, dy = -20, 0
    elif key == keys.RIGHT:
        dx, dy = 20, 0


pgzrun.go()
