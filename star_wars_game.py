import sys
import pygame
from settings import Settings
from space_ship import SpaceShip
from bullets import Bullets
from enemy import Enemy
from pygame.locals import *
from pygame import mixer
import random
from time import sleep
from game_stats import GameStats
from enemy_bullets import Enemy_Bullets

N=200

class StarWars:
    """"Overall class to manage game assets and behavior"""

    def __init__(self):
        """Run the game, and develop necessary resources"""
        pygame.init()
        self.settings = Settings()
         
        mixer.music.load('music/Music  Falcon vs The TIE fighters.mp3')
        mixer.music.play(-1)

        # Full Screen
        # self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height


        
        # Custom Screen
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Star Wars IV: Python Strikes Back")

        # Create an instance to store game statistics
        self.stats = GameStats(self)

        self.space_ship = SpaceShip(self)
        self.bullets = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()

        self._create_fleet()



    def _create_fleet(self):
        # Fleet of enemies
        enemy = Enemy(self)
        enemy_width = enemy.rect.width
        enemy_height = enemy.rect.height
        horizontal_space = self.settings.screen_width - (2 * enemy_width)
        ## horizontal_enemies = random.randint(3,horizontal_space // (2 * enemy_width))
        horizontal_enemies = horizontal_space // (2 * enemy_width)

        # Determine the number of rows
        enemy_ship_height = self.space_ship.rect.height
        vertical_space = (self.settings.screen_height - (3 * enemy_height) - enemy_ship_height)
        row_number = (vertical_space // (2 * enemy_height))+ 1
 
        # Creating the first row of enemies
        for row in range(row_number):
            for enemy_number in range(horizontal_enemies):
                self._create_enemy(enemy_number,row)

    def _create_enemy(self, enemy_number, row):
        # Creating an enemy and place it
        if (row % 2) == 0:
            enemy = Enemy(self)
            enemy_width = enemy.rect.width
            enemy_height = enemy.rect.height
            enemy.x = enemy_width + enemy_width + 2 * enemy_width * enemy_number
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.rect.height + 2 * enemy.rect.height * row 
            self.enemies.add(enemy)
        else:
            enemy = Enemy(self)
            enemy_width = enemy.rect.width
            enemy_height = enemy.rect.height
            enemy.x =  enemy_width + 2 * enemy_width * enemy_number
            enemy.rect.x = enemy.x
            enemy.rect.y = enemy.rect.height + 2 * enemy.rect.height * row 
            self.enemies.add(enemy)


    def _check_fleet_edges(self):
        # Responding if an enemy touch the edges
        for enemy in self.enemies.sprites():
            if enemy.check_edges():
                self._change_fleet_direction()
                break

    
    def _change_fleet_direction(self):
        for enemy in self.enemies.sprites():
            enemy.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1


    def run_game(self):
        """Start the main loop for the game"""
        while True:
            self._check_events()
            self.space_ship.update()
            self._update_bullets()
            self._update_enemy_bullets()
            self._update_enemies()
            self._update_screen()
            self._fire_enemy_bullets()
            
            
    def _check_events(self):
            # Watch for keyboard and mouse events.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Event handler that responds to keypresses"""
        if event.key ==pygame.K_RIGHT:
            # Move the ship to the right.
            self.space_ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            # Move the ship to the left.
            self.space_ship.moving_left = True
        elif event.key == pygame.K_UP:
            # Move the ship up.
            self.space_ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            # Move the ship down.
            self.space_ship.moving_down = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
            

            # Blaster Sound
            bullet_sound = mixer.Sound('music/blaster.mp3')
            bullet_sound.play()

    def _check_keyup_events(self, event):
        """Event handler that responds to keypresses"""
        if event.key ==pygame.K_RIGHT:
            # Blocking the movement of the ship to the right.
            self.space_ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            # Blocking the movement of the ship to the left.
            self.space_ship.moving_left = False
        elif event.key == pygame.K_UP:
            # Blocking the movement the ship up.
            self.space_ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            # Blocking the movement the ship down.
            self.space_ship.moving_down = False

    def _update_bullets(self):
        self.bullets.update()
        # Getting rid of the old bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        # print(len(self.bullets))

        self._check_bullet_enemy_collision()
    
    def _update_enemy_bullets(self):
        self.enemy_bullets.update()
        # Getting rid of the old bullets
        for bullet in self.enemy_bullets.copy():
            if bullet.rect.bottom >= 1200:
                self.enemy_bullets.remove(bullet)
        print(len(self.enemy_bullets))


    def _check_bullet_enemy_collision(self):
        """"Enemies Collision"""
        # Check for any bullets that hit the enemy
        collisions = pygame.sprite.groupcollide(self.bullets,self.enemies, True, True)
        if collisions:
            # Blaster Sound
            bullet_sound = mixer.Sound('music/TIE fighter explode.mp3')
            bullet_sound.play()           

        if not self.enemies:
            # Destroy Bullets and create a new fleet
            self.bullets.empty()
            self._create_fleet()
    

    def _update_enemies(self):
        # Update enemy position
        self._check_fleet_edges()
        self.enemies.update()

        # Looking for collisions enemies vs space ship
        if pygame.sprite.spritecollideany(self.space_ship, self.enemies):
            print("ZAMBOMBAZO")

    
    def _ship_hit(self):
        """Respond to the ship being hit by an enemy"""

        
    
    def _fire_bullets(self):
        """Creating a new bullet"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullets(self)
            self.bullets.add(new_bullet)


    def _fire_enemy_bullets(self):
        if random.randrange(0,50) == 1:
            new_enemy_bullet = Enemy_Bullets(self)
            self.enemy_bullets.add(new_enemy_bullet)
            enemy_bullet_sound = mixer.Sound('music/TIE fighter fire 1.mp3')
            enemy_bullet_sound.play()  

    def _update_screen(self):
            # Redrawing the screen during each loop
            # create background
        background = pygame.Surface(self.screen.get_size())
        background = background.convert()
    
        # generate N stars
        stars = [
            [random.randint(0, self.settings.screen_width),random.randint(0, self.settings.screen_height)]
            for x in range(N)
        ]
    
        # main loop
        background.fill((0,0,0))
        for star in stars:
            pygame.draw.line(background,
                (255, 255, 255), (star[0], star[1]), (star[0], star[1]))
            star[0] = star[0] - 1
            if star[0] < 0:
                star[0] = self.settings.screen_width
                star[1] = random.randint(0, self.settings.screen_height)
        self.screen.blit(background, (0,0))

        self.space_ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullets()

        for bullet_e in self.enemy_bullets.sprites():
            bullet_e.draw_enemy_bullets()

        self.enemies.draw(self.screen)

        # Make the screen visible
        pygame.display.flip()
    

if __name__ == '__main__':
    # Make a game prothotype, and run the game
    alien_app = StarWars()
    alien_app.run_game()