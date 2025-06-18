import pygame
from constants import *
from game_objects import Card, Player

class GameEngine:
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.running = True
        self.players = [Player("Player 1"), Player("Player 2")]
        self.current_player = 0
        self.turn_number = 1
        
    def update(self):
        """Update game state"""
        # Update mana for current player
        self.players[self.current_player].add_mana()
        
    def draw(self, window):
        """Draw game elements"""
        window.fill(BLACK)
        # Draw player info
        for i, player in enumerate(self.players):
            player.draw(window, i)
        
        # Draw cards
        self.draw_cards(window)
        
    def draw_cards(self, window):
        """Draw all cards in players' hands and on board"""
        # TODO: Implement card drawing
        pass
        
    def handle_events(self, events):
        """Handle game events"""
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self.handle_key_events(event)
                
    def handle_key_events(self, event):
        """Handle keyboard events"""
        if event.key == pygame.K_SPACE:
            self.next_turn()
        elif event.key == pygame.K_d:
            self.play_card()
            
    def next_turn(self):
        """Switch to next player's turn"""
        self.current_player = 1 - self.current_player
        self.turn_number += 1
        
    def play_card(self):
        """Play a card from current player's hand"""
        current_player = self.players[self.current_player]
        # TODO: Implement card playing logic
        pass
