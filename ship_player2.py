# -*- coding: utf-8 -*-
"""
Created on Sat May 22 15:15:28 2021

@author: 梁盼
"""
import pygame

class Ship2:
    """管理飞船的类"""
    
    def __init__(self,ai_game):
        """初始化飞船并设置其初始位置。"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        #加载飞船图像并获取其外接矩形。
        self.image = pygame.image.load('images/ship2 down.bmp')
        self.rect = self.image.get_rect()
        
        #将新飞船放在屏幕顶部中央
        self.rect.midtop = self.screen_rect.midtop
        
        # 在飞船的属性x,y中，存储小数值。
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.direction = "down"
        
    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船而不是rect对象的x,y值。
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_player2_speed
            self.image = pygame.image.load('images/ship2 right.bmp')
            self.direction = "right"
            self.rect = self.image.get_rect()
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_player2_speed
            self.image = pygame.image.load('images/ship2 left.bmp')
            self.direction = "left"
            self.rect = self.image.get_rect()
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_player2_speed
            self.image = pygame.image.load('images/ship2 up.bmp')
            self.direction = "up"
            self.rect = self.image.get_rect()
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_player2_speed
            self.image = pygame.image.load('images/ship2 down.bmp')
            self.direction = "down"
            self.rect = self.image.get_rect()

            
        # 根据self.x y更新rect对象。
        self.rect.x=self.x
        self.rect.y=self.y
    
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)