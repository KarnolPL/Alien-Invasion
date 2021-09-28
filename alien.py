# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Klasa przedstawiajaca pojdeynczego obcego we flocie."""
    
    def __init__(self, ai_game):
        """Inicjalizacja obcego i zdefinioweanie jego polozenia początkowego"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        #Wczytywanie obrazu obcego i zdefiniowanie jego atrybuty rect
        
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        
        #Umieszczenie nowego obcego w poblizuu lewego górnego roku ekranu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #Przechowywanie dokładnego poziomego połozenia obcego
        self.x = float(self.rect.x)
        
    
    def check_edges(self):
        """Zwraca warosc True jeli obcy znajduje sie przy krawedzi ekranu"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True
    
    def update(self):
        """Przesuniecie obcego w prawo."""
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
        
        
    
        
    





















