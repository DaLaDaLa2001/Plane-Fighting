# -*- coding: utf-8 -*-
"""
Created on Sat May 22 15:15:28 2021

@author: 梁盼
"""

import pygame
from pygame.sprite import Sprite

class Bullet2(Sprite):
    """管理飞船所发射子弹的类"""
    
    def __init__(self,ai_game):
        """在飞船当前位置创建一个个子弹对象。"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet2_color
        self.direction = ai_game.ship_player2.direction
        
        # 在(0，0)处创建一个表示子弹的矩形，再设置正确的位置。
        self.rect = pygame.Rect(0,0,self.settings.bullet2_width,
                self.settings.bullet2_height)
        self.rect.center = ai_game.ship_player2.rect.center
        
        # 存储用小数表示的子弹位置
        self.x= float(self.rect.x)
        self.y= float(self.rect.y)
        
    def update(self):
        """向上移动子弹。"""
        # 更新表示子弹位置的小数值。
        if self.direction == "up":
            self.y -= self.settings.bullet2_speed
        elif self.direction == "down":
            self.y += self.settings.bullet2_speed
        elif self.direction == "right":
            self.x += self.settings.bullet2_speed
        elif self.direction == "left":
            self.x -= self.settings.bullet2_speed

        # 更新表示子弹的 rect 的位置。
        self.rect.x = self.x
        self.rect.y = self.y
        
    def draw_bullet2(self):
        """在屏幕上绘制子弹。"""
        pygame.draw.rect(self.screen,self.color,self.rect)
        
        