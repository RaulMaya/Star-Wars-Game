import os,sys,random
import pygame
from pygame.locals import *

N = 200

class Settings:
    """Class to store all settings from the Alien Invasion Game"""

    def __init__(self):
        """Execute game's settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 650
        self.bg_color = (0,0,0)

        # Space ship settings
        self.space_ship_speed = 1.25

        # Bullet settings
        self.bullet_speed =  1.00
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (164, 66, 245)
        self.bullets_allowed = 5
  