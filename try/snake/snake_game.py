import pgzrun
import random

# 设置游戏窗口尺寸
WIDTH = 800
HEIGHT = 600

# 蛇的初始属性
snake = {"positions": [(100, 100), (90, 100), (80, 100)], "direction": "RIGHT", "color": "green"}
# 食物的属性
food = {"position": (0, 0), "color": "red", "exists": False}
# 游戏状态
score = 0
game_over = False
# 游戏速度（数字越小越快）
SNAKE_SPEED = 0.1

# 创建食物
def create_food():
    x = random.randint(1, WIDTH // 10 - 1) * 10
    y = random.randint(1, HEIGHT // 10 - 1) * 10
    # 确保食物不会出现在蛇身上
    while (x, y) in snake["positions"]:
        x = random.randint(1, WIDTH // 10 - 1) * 10
        y = random.randint(1, HEIGHT // 10 - 1) * 10
    food["position"] = (x, y)
    food["exists"] = True

# 处理按键事件
def on_key_down(key):
    global game_over
    # 控制蛇的方向
    if not game_over:
        if key == keys.UP and snake["direction"] != "DOWN":
            snake["direction"] = "UP"
        elif key == keys.DOWN and snake["direction"] != "UP":
            snake["direction"] = "DOWN"
        elif key == keys.LEFT and snake["direction"] != "RIGHT":
            snake["direction"] = "LEFT"
        elif key == keys.RIGHT and snake["direction"] != "LEFT":
            snake["direction"] = "RIGHT"
    # 游戏结束后按空格键重新开始
    elif key == keys.SPACE:
        reset_game()

# 更新游戏状态
def update():
    global score, game_over
    if not game_over:
        # 获取蛇头的位置
        head_x, head_y = snake["positions"][0]
        # 根据当前方向移动蛇头
        if snake["direction"] == "UP":
            head_y -= 10
        elif snake["direction"] == "DOWN":
            head_y += 10
        elif snake["direction"] == "LEFT":
            head_x -= 10
        elif snake["direction"] == "RIGHT":
            head_x += 10
        
        # 检查是否撞墙
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            game_over = True
            return
        
        # 检查是否撞到自己
        if (head_x, head_y) in snake["positions"]:
            game_over = True
            return
        
        # 将新的头部位置添加到蛇的位置列表的最前面
        snake["positions"].insert(0, (head_x, head_y))
        
        # 检查是否吃到食物
        if food["exists"] and (head_x, head_y) == food["position"]:
            score += 1
            food["exists"] = False
            create_food()
        else:
            # 如果没有吃到食物，删除尾部位置（保持蛇的长度不变）
            snake["positions"].pop()
        
        # 如果食物不存在，创建新食物
        if not food["exists"]:
            create_food()

# 绘制游戏界面
def draw():
    # 清空屏幕
    screen.clear()
    screen.fill("black")
    
    # 绘制蛇
    for position in snake["positions"]:
        screen.draw.filled_rect(Rect(position[0], position[1], 10, 10), snake["color"])
    
    # 绘制食物
    if food["exists"]:
        screen.draw.filled_circle(food["position"], 5, food["color"])
    
    # 绘制分数
    screen.draw.text(f"分数: {score}", (10, 10), color="white", fontsize=30)
    
    # 如果游戏结束，显示游戏结束信息
    if game_over:
        screen.draw.text("游戏结束! 按空格键重新开始", 
                        center=(WIDTH // 2, HEIGHT // 2), 
                        color="red", 
                        fontsize=50)

# 重置游戏
def reset_game():
    global snake, food, score, game_over
    snake = {"positions": [(100, 100), (90, 100), (80, 100)], "direction": "RIGHT", "color": "green"}
    food = {"position": (0, 0), "color": "red", "exists": False}
    score = 0
    game_over = False
    create_food()

# 初始化游戏
create_food()

# 设置游戏更新速度
def update_speed():
    clock.schedule_interval(update, SNAKE_SPEED)

# 启动游戏循环
update_speed()
pgzrun.go()