# GPT-3.5

import random
import pgzrun

WIDTH = 400
HEIGHT = 400

snake = [(20, 20)]
direction = (0, 0)
food = (100, 100)
score = 0
speed = 20
game_over = False


def update():
    global snake, direction, food, score, game_over

    if game_over:
        return
    x, y = snake[0]
    x += direction[0] * speed
    y += direction[1] * speed

    # Wrap around the screen
    x %= WIDTH
    y %= HEIGHT

    if (x, y) in snake[1:] or (x < 0 or y < 0):
        game_over = True
        return
    snake.insert(0, (x, y))

    if (x, y) == food:
        score += 1
        food = (
            random.randint(0, WIDTH // 20 - 1) * 20,
            random.randint(0, HEIGHT // 20 - 1) * 20,
        )
    else:
        snake.pop()


def draw():
    screen.clear()
    screen.draw.text("Score: " + str(score), (10, 10), color="white")

    if game_over:
        screen.draw.text("Game Over", (WIDTH // 2 - 50, HEIGHT // 2), color="white")
        return
    for x, y in snake:
        screen.draw.filled_rect(Rect((x, y), (20, 20)), "white")
    screen.draw.filled_rect(Rect(food, (20, 20)), "red")


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
