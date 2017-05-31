import sys
import pygame
from settings import Settings
from ship import  Ship

def run_game():
    """初始化游戏并且创建一个屏幕对象"""
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 开始游戏的主循环
    ship = Ship(screen)
    while True:
        screen.fill(ai_settings.bg_color)
        ship.blitme()
        # # 监视键盘和鼠标事件
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()

        # 让最近绘制的屏幕可见
        pygame.display.flip()
run_game()
