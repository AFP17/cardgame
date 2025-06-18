from constants import *
import pygame

class Card:
    def __init__(self, name, attack, defense, cost, trash_type, effect=None):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.cost = cost
        self.trash_type = trash_type
        self.effect = effect
        self.image = pygame.Surface((CARD_WIDTH, CARD_HEIGHT))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.selected = False
        
    def draw(self, surface, position):
        """Draw the card on the surface"""
        # Draw card border
        pygame.draw.rect(surface, BLACK, self.rect, 2)
        
        # Draw card name
        font = pygame.font.Font(FONT_PATH, 24)
        name_text = font.render(self.name, True, BLACK)
        surface.blit(name_text, (position[0] + 5, position[1] + 5))
        
        # Draw stats
        stats_text = font.render(f"{self.attack}/{self.defense}", True, BLACK)
        surface.blit(stats_text, (position[0] + 5, position[1] + 150))
        
        # Draw cost
        pygame.draw.circle(surface, GRAY, (position[0] + 110, position[1] + 15), 15)
        cost_text = font.render(str(self.cost), True, BLACK)
        surface.blit(cost_text, (position[0] + 100, position[1] + 5))
        
        # Draw trash type icon
        if self.trash_type == 'plastic':
            pygame.draw.rect(surface, BLUE, (position[0] + 90, position[1] + 30, 20, 20))
        elif self.trash_type == 'paper':
            pygame.draw.rect(surface, YELLOW, (position[0] + 90, position[1] + 30, 20, 20))
        elif self.trash_type == 'glass':
            pygame.draw.rect(surface, CYAN, (position[0] + 90, position[1] + 30, 20, 20))
        elif self.trash_type == 'organic':
            pygame.draw.rect(surface, GREEN, (position[0] + 90, position[1] + 30, 20, 20))

class Player:
    def __init__(self, name):
        self.name = name
        self.health = STARTING_HEALTH
        self.mana = STARTING_MANA
        self.max_mana = MAX_MANA
        self.deck = []
        self.hand = []
        self.board = []
        self.trash_resources = {
            'plastic': 0,
            'paper': 0,
            'glass': 0,
            'organic': 0
        }
        
    def draw(self, surface, position):
        """Draw player info on screen"""
        y = 50 if position == 0 else WINDOW_HEIGHT - 100
        font = pygame.font.Font(FONT_PATH, 24)
        
        # Draw health
        health_text = font.render(f"HP: {self.health}", True, BLACK)
        surface.blit(health_text, (10, y))
        
        # Draw mana
        mana_text = font.render(f"Mana: {self.mana}/{self.max_mana}", True, BLACK)
        surface.blit(mana_text, (10, y + 20))
        
        # Draw trash resources
        x = 10
        for trash_type, amount in self.trash_resources.items():
            resource_text = font.render(f"{trash_type[0].upper()}: {amount}", True, BLACK)
            surface.blit(resource_text, (x, y + 40))
            x += 100
            
    def add_mana(self):
        """Add mana at the start of turn"""
        self.mana = min(self.mana + 1, self.max_mana)
        
    def draw_card(self):
        """Draw a card from deck"""
        if self.deck:
            self.hand.append(self.deck.pop(0))
            
    def play_card(self, card_index):
        """Play a card from hand"""
        if card_index < len(self.hand):
            card = self.hand[card_index]
            if self.mana >= card.cost:
                # TODO: Implement card playing logic
                pass
