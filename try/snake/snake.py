import pgzrun
from random import randint

TITLE = "Snake Game"
WIDTH = 600
HEIGHT = 400

CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

snake = [(5, 5), (4, 5), (3, 5)]
direction = (1, 0)
food = (randint(0, GRID_WIDTH - 1), randint(0, GRID_HEIGHT - 1))
score = 0
game_over = False
move_interval = 12
frame_count = 0

def update():
    global snake, direction, food, score, game_over, frame_count
    frame_count += 1
    if frame_count % move_interval != 0:
        return
    if game_over:
        return

    head_x, head_y = snake[0]
    dx, dy = direction
    new_head = ((head_x + dx) % GRID_WIDTH, (head_y + dy) % GRID_HEIGHT)

    if new_head in snake:
        game_over = True
        return

    snake.insert(0, new_head)
    if new_head == food:
        score += 1
        food = (randint(0, GRID_WIDTH - 1), randint(0, GRID_HEIGHT - 1))
    else:
        snake.pop()

def draw():
    screen.fill("black")
    for segment in snake:
        x, y = segment
        screen.draw.filled_rect(
            Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            "green"
        )
    x, y = food
    screen.draw.filled_rect(
        Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
        "red"
    )
    screen.draw.text(f"Score: {score}", (10, 10), color="white")
    if game_over:
        screen.draw.text("Game Over", (WIDTH // 2 - 50, HEIGHT // 2), color="white")

def on_key_down(key):
    global direction
    if key == keys.UP and direction != (0, 1):
        direction = (0, -1)
    elif key == keys.DOWN and direction != (0, -1):
        direction = (0, 1)
    elif key == keys.LEFT and direction != (1, 0):
        direction = (-1, 0)
    elif key == keys.RIGHT and direction != (-1, 0):
        direction = (1, 0)

pgzrun.go()