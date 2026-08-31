import pgzrun
import random

WIDTH = 800
HEIGHT = 600

snake = [(40, 40)]
snake_direction = (20, 0)
food = (200, 200)
game_over = False

update_counter = 0
update_interval = 10


def draw():
    screen.clear()
    for segment in snake:
        screen.draw.filled_rect(Rect(segment, (20, 20)), "green")
    screen.draw.filled_rect(Rect(food, (20, 20)), "red")
    if game_over:
        screen.draw.text(
            "Game Over", center=(WIDTH // 2, HEIGHT // 2), fontsize=50, color="white"
        )


def update():
    global game_over, update_counter
    if not game_over:
        update_counter += 1
        if update_counter >= update_interval:
            move_snake()
            check_collisions()
            update_counter = 0


def move_snake():
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake.insert(0, new_head)
    if new_head == food:
        place_food()
    else:
        snake.pop()


def check_collisions():
    global game_over
    head = snake[0]
    if head[0] < 0 or head[0] >= WIDTH or head[1] < 0 or head[1] >= HEIGHT:
        game_over = True
    if head in snake[1:]:
        game_over = True


def place_food():
    global food
    food = (
        random.randint(0, (WIDTH - 20) // 20) * 20,
        random.randint(0, (HEIGHT - 20) // 20) * 20,
    )


def on_key_down(key):
    global snake_direction
    if key == keys.UP and snake_direction != (0, 20):
        snake_direction = (0, -20)
    elif key == keys.DOWN and snake_direction != (0, -20):
        snake_direction = (0, 20)
    elif key == keys.LEFT and snake_direction != (20, 0):
        snake_direction = (-20, 0)
    elif key == keys.RIGHT and snake_direction != (-20, 0):
        snake_direction = (20, 0)


pgzrun.go()
