# -*- coding: utf-8 -*-
"""
Created on Sat May 22 15:15:28 2021

@author: 梁盼
"""

import pygame
from pygame.sprite import Sprite
import random

class Wall(Sprite):
    """管理障碍的类"""
    
    def __init__(self,ai_game):
        """在屏幕上生成障碍对象"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.wall_color
        
        # 在(0，0)处创建一个表示障碍的正方形，再设置随机的位置。
        self.rect = pygame.Rect(0,0,self.settings.wall_length,self.settings.wall_width)
        self.rect.center =  (random.random()* self.screen.get_rect().width,
                             random.randint(100,950))
        
        # 存储用小数表示的障碍位置
        self.x= float(self.rect.x)
        self.y= float(self.rect.y)
        
        # 更新表示障碍的 rect 的位置。
        self.rect.x = self.x
        self.rect.y = self.y
        
    def draw_wall(self):
        """在屏幕上绘制障碍 。"""
        pygame.draw.rect(self.screen,self.color,self.rect)
        