import pygame  
import random  
  
# 定义方块大小和行列数  
BLOCK_SIZE = 30  
ROW = 20  
COL = 10  
  
# 定义方块的形状  
BLOCK_SHAPES = [  
    # I  
    [(1, 0), (1, 1), (1, 2), (1, 3)],  
    # J  
    [(0, 0), (1, 0), (1, 1), (1, 2)],  
    # L  
    [(1, 0), (1, 1), (1, 2), (0, 2)],  
    # O  
    [(0, 0), (0, 1), (1, 0), (1, 1)],  
    # S  
    [(0, 1), (0, 2), (1, 0), (1, 1)],  
    # T  
    [(0, 0), (1, 0), (1, 1), (0, 1)],  
    # Z  
    [(0, 1), (0, 2), (1, 0), (1, 1)]  
]  
  
# 定义方块颜色  
BLOCK_COLORS = [  
    (255, 255, 255),  # 白色  
    (0, 255, 255),  # 青色  
    (0, 0, 255),  # 红色  
    (255, 255, 0),  # 黄色  
    (0, 255, 0),  # 绿色  
    (255, 0, 255),  # 紫色  
    (255, 0, 0),  # 橙色  
]  
  
# 游戏界面大小  
WIN_WIDTH = BLOCK_SIZE * COL  
WIN_HEIGHT = BLOCK_SIZE * ROW  
  
# 方块堆栈  
block_stack = []  
  
# 游戏界面对象  
game_window = None  
  
# 游戏循环标志  
game_over = False  
  
def init():  
    global game_window  
    pygame.init()  
    game_window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))  
    pygame.display.set_caption("俄罗斯方块")  
    pygame.mouse.set_visible(False)  
    pygame.font.init()  
    font = pygame.font.SysFont(None, 36)  
    text = font.render("Press any key to start", True, BLOCK_COLORS[0])  
    game_window.blit(text, (BLOCK_SIZE // 2 - text.get_width() // 2, BLOCK_SIZE // 2 - text.get_height() // 2))  
    pygame.display.update()  
    pygame.time.wait(1000)  
    reset()  
  
def reset():  
    global game_over  
    game_over = False  
    clear()  
    block_stack = []  
    drop()  
    pygame.time.wait(500)  
  
def clear():  
    global game_window, BLOCK_COLORS  
    for i in range(ROW):  
        for j in range(COL):  
            if game_window.get_at((j * BLOCK_SIZE + BLOCK_SIZE // 2, i * BLOCK_SIZE + BLOCK_SIZE // 2)) == BLOCK_COLORS[0]:  
                game_window.set_at((j * BLOCK_SIZE + BLOCK_SIZE // 2, i * BLOCK_SIZE + BLOCK_SIZE // 2), (255, 255, 255))  
    pygame.display.update()