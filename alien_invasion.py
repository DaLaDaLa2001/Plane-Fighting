# -*- coding: utf-8 -*-
"""
Created on Fri May  7 09:40:06 2021

@author: 梁盼
"""

import sys
import pygame

from time import sleep
from game_stats import GameStats
from button import Button
from settings import Settings
from ship_player1 import Ship1
from ship_player2 import Ship2
from bullet1 import Bullet1
from bullet2 import Bullet2
from wall import Wall

class AlienInvasion:
    """管理游戏资源和行为类"""
 
    def __init__(self):
        """初始化游戏并创建游戏资源。"""
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_heigth = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        
        self.ship_player1 = Ship1(self)
        self.ship_player2 = Ship2(self)
        self.play_button = Button(self,"Play ! ! !")
        self.bullets1 = pygame.sprite.Group()
        self.bullets2 = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.stats = GameStats(self)
        
    def run_game(self):
        self._build_wall()
        #开始游戏的主循环
        while True:
            self._check_events()
            self._check_hit()
            
            if self.stats.game_active:
                self.ship_player1.update()
                self.ship_player2.update()
                self._update_bullets1()
                self._update_bullets2()
            self._update_screen()

    def _check_events(self):
        """响应键盘和鼠标事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
                
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
                
    def _check_play_button(self,mouse_pos):
        """在玩家单击Play按钮时开始新游戏。"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # 重置游戏统计信息。
            self.stats.game_active = True

    def _check_keydown_events(self,event):
        """响应按键"""
        if event.key == pygame.K_d:
            self.ship_player1.moving_right = True
        elif event.key == pygame.K_a:
            self.ship_player1.moving_left = True
        elif event.key == pygame.K_w:
            self.ship_player1.moving_up = True
        elif event.key == pygame.K_s: 
            self.ship_player1.moving_down = True
        
        elif event.key == pygame.K_RIGHT:
            self.ship_player2.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship_player2.moving_left = True
        elif event.key == pygame.K_UP:
            self.ship_player2.moving_up = True
        elif event.key == pygame.K_DOWN: 
            self.ship_player2.moving_down = True
            
        elif event.key == pygame.K_q:
            pygame.quit()
            sys.exit()
            
        elif event.key == pygame.K_SPACE:
            self._fire_bullet1()
        elif event.key == pygame.K_l:
            self._fire_bullet2()
            
    def _check_keyup_events(self,event):
        """响应松开"""
        if event.key == pygame.K_d:
            self.ship_player1.moving_right = False  
        elif event.key == pygame.K_a:
            self.ship_player1.moving_left = False
        elif event.key == pygame.K_w:
            self.ship_player1.moving_up = False  
        elif event.key == pygame.K_s:
            self.ship_player1.moving_down = False
            
        elif event.key == pygame.K_RIGHT:
            self.ship_player2.moving_right = False  
        elif event.key == pygame.K_LEFT:
            self.ship_player2.moving_left = False
        elif event.key == pygame.K_UP:
            self.ship_player2.moving_up = False  
        elif event.key == pygame.K_DOWN:
            self.ship_player2.moving_down = False
            
    def _build_wall(self):
        """创建一个障碍，并将其加入编组 walls 中。"""
        for i in range(self.settings.walls_number):
            new_wall = Wall(self)
            self.walls.add(new_wall)
                
    def _fire_bullet1(self):
        """创建一颗子弹，并将其加入编组 buttets 中。"""
        if len(self.bullets1) < self.settings.bullets1_allowed:
            new_bullet1 = Bullet1(self)
            self.bullets1.add(new_bullet1)
            
    def _update_bullets1(self):
        """更新子弹的位置并删除消失的子弹。"""
        # 更新子弹的位置。
        self.bullets1.update()
            
        # 删除消失的子弹。
        for bullet1 in self.bullets1.copy():
            if bullet1.rect.bottom < 0 or bullet1.rect.top > self.ship_player1.screen_rect.bottom or bullet1.rect.left > self.ship_player1.screen_rect.right or bullet1.rect.right < 0:
                self.bullets1.remove(bullet1)
            
        collisions = pygame.sprite.groupcollide(
          self.bullets1,self.walls,True,False)
        
    def _fire_bullet2(self):
        """创建一颗子弹，并将其加入编组 buttets 中。"""
        if len(self.bullets2) < self.settings.bullets2_allowed:
            new_bullet2 = Bullet2(self)
            self.bullets2.add(new_bullet2)
            
    def _update_bullets2(self):
        """更新子弹的位置并删除消失的子弹。"""
        # 更新子弹的位置。
        self.bullets2.update()
            
        # 删除消失的子弹。
        for bullet2 in self.bullets2.copy():
            if bullet2.rect.bottom < 0 or bullet2.rect.top > self.ship_player1.screen_rect.bottom or bullet2.rect.left > self.ship_player1.screen_rect.right or bullet2.rect.right < 0:
                self.bullets2.remove(bullet2)
                   
        collisions = pygame.sprite.groupcollide(
          self.bullets2,self.walls,True,False)
        collisions = pygame.sprite.groupcollide(
          self.bullets1,self.bullets2,True,True)
        
        
    def _check_hit(self): 
        if pygame.sprite.collide_rect(self.ship_player1,self.ship_player2):
            print("It ends in a draw!")
            self.image = pygame.image.load('images/ship1 up.bmp')
            self.rect = self.image.get_rect()
            self.rect.center = self.screen_rect.center
            flag = 1
            sleep(2)
            pygame.quit()
            
        if pygame.sprite.spritecollideany(self.ship_player1,self.walls) or pygame.sprite.spritecollideany(self.ship_player1,self.bullets2):
            print("player2 win!!!")
            self.image = pygame.image.load('images/ship1 up.bmp')
            self.rect = self.image.get_rect()
            self.rect.center = self.screen_rect.center
            flag = 1
            sleep(2)
            pygame.quit()
            
        if pygame.sprite.spritecollideany(self.ship_player2,self.walls) or pygame.sprite.spritecollideany(self.ship_player2,self.bullets1):
            print("player1 win!!!")
            self.image = pygame.image.load('images/ship1 up.bmp')
            self.rect = self.image.get_rect()
            self.rect.center = self.screen_rect.center           
            flag = 1
            sleep(2)
            pygame.quit()
            
    def _update_screen(self):
        """更新屏幕上的图像，并切换到新屏幕"""
        self.screen.fill(self.settings.bg_color)
        self.ship_player1.blitme()
        self.ship_player2.blitme()
        for bullet1 in self.bullets1.sprites():
            bullet1.draw_bullet1()
        for bullet2 in self.bullets2.sprites():
            bullet2.draw_bullet2()
        for wall in self.walls.sprites():
            wall.draw_wall()
        if not self.stats.game_active:
            self.play_button.draw_button()
        if self._check_hit.flag:
            self.screen.blit(self._check_hit.image,self._check_hit.rect)
        pygame.display.flip()
                    
    
if __name__=='__main__':
    # 创建游戏实例并运行游戏。
    ai = AlienInvasion()
    ai.run_game()