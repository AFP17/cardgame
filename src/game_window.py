import pygame
from constants import *

class GameWindow:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Trashstone")
        self.clock = pygame.time.Clock()
        
    def update(self):
        """Update the display"""
        pygame.display.flip()
        self.clock.tick(FPS)
        
    def fill(self, color):
        """Fill the screen with a color"""
        self.screen.fill(color)
        
    def draw_text(self, text, size, color, x, y):
        """Draw text on screen"""
        font = pygame.font.Font(FONT_PATH, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        self.screen.blit(text_surface, text_rect)
        
    def draw_card(self, card, x, y):
        """Draw a card on screen"""
        # TODO: Implement card drawing
        pass
