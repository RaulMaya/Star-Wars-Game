import pygame.font

class Button:

    def __init__(self, sw_app_game, msg):

        #Initialize button attributes
        self.screen = sw_app_game.screen
        self.screen_rect = self.screen.get_rect()

        # Dimensions and properties of the button
        self.width, self.height =  200, 50
        self.button_color = (220,20,60)
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None, 48)

        # Build the button's rect object and center it
        self.rect = pygame.Rect(100, 0, self.width, self.height)
        

        self._prep_msg(msg)

    
    def _prep_msg(self, msg):
        # Turn msg into an image and center the text inside
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

