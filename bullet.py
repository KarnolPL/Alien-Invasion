# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """
    Klasa przeznaczona do zarzadzania pociskami wystrzeliwanymi
    przez statek.
    """
    
    def __init__(self, ai_game):
        """Utworzenie obiektu pocisku w aktualnym położeniu statku."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        #Utworzenie prostokąta pocisku w punkcie (0, 0), a nastepnie
        #zdefiniowanie dla niego odpowiedniego połozenia.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        #Połozenie pocisku jest zdefiniowane za pomoca wartosci 
        #zmiennoprzecinkowej
        self.y = float(self.rect.y)
        
    def update(self):
        """Poruszanie pociskiem po ekranie."""
        #Uaktualnienie połozenia pocisku.
        self.y -= self.settings.bullet_speed
        #Uaktualnienie położenia prostokata pocisku.
        self.rect.y = self.y
        
    def draw_bullet(self):
        """Wyswietlanie pocisku na ekranie."""
        pygame.draw.rect(self.screen, self.color, self.rect)
    