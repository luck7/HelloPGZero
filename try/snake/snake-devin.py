import pgzrun
from random import randint

WIDTH = 600
HEIGHT = 600
CELL_SIZE = 30
WIDTH_CELLS = WIDTH // CELL_SIZE
HEIGHT_CELLS = HEIGHT // CELL_SIZE

snake = [(WIDTH_CELLS // 2, HEIGHT_CELLS // 2)]
snake_direction = 0, 1
apple = (randint(0, WIDTH_CELLS - 1), randint(0, HEIGHT_CELLS - 1))


def draw():
    screen.fill("black")
    for x, y in snake:
        screen.draw.filled_rect(
            Rect((x * CELL_SIZE, y * CELL_SIZE), (CELL_SIZE, CELL_SIZE)), "green"
        )
    ax, ay = apple
    screen.draw.filled_rect(
        Rect((ax * CELL_SIZE, ay * CELL_SIZE), (CELL_SIZE, CELL_SIZE)), "red"
    )


def update():
    global snake, apple, snake_direction
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])

    if (
        (new_head in snake)
        or (new_head[0] not in range(WIDTH_CELLS))
        or (new_head[1] not in range(HEIGHT_CELLS))
    ):
        exit()
    snake.insert(0, new_head)

    if new_head == apple:
        apple = (randint(0, WIDTH_CELLS - 1), randint(0, HEIGHT_CELLS - 1))
    else:
        snake.pop()


def on_key_down(key):
    global snake_direction
    if key == keys.LEFT and snake_direction != (1, 0):
        snake_direction = (-1, 0)
    elif key == keys.RIGHT and snake_direction != (-1, 0):
        snake_direction = (1, 0)
    elif key == keys.UP and snake_direction != (0, 1):
        snake_direction = (0, -1)
    elif key == keys.DOWN and snake_direction != (0, -1):
        snake_direction = (0, 1)


pgzrun.go()
