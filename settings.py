# -*- coding: utf-8 -*-
"""
Created on Sat May 22 15:15:28 2021

@author: 梁盼
"""

class Settings:
    """存储《外星人入侵》的所有设置的类。"""
    
    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.bg_color = (230,230,230)
        
        # 飞船设置
        self.ship_player1_speed = 1
        self.ship_player2_speed = 1
        
        # 子弹设置
        self.bullet1_speed = 1.3
        self.bullet1_width = 8
        self.bullet1_height = 8
        self.bullet1_color = (255, 0, 0)
        self.bullets1_allowed = 5
        
        self.bullet2_speed = 1.3
        self.bullet2_width = 8
        self.bullet2_height = 8
        self.bullet2_color = (0, 0, 255)
        self.bullets2_allowed = 5
        
        # 障碍设置
        self.wall_length = 80
        self.wall_width = 80
        self.wall_color = (130,130,130)
        self.walls_number = 30