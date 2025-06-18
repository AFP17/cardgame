from game_engine import GameEngine
from game_window import GameWindow

class GameManager:
    def __init__(self):
        self.window = GameWindow()
        self.engine = GameEngine()
        
    def run(self):
        """Main game loop"""
        while self.engine.running:
            events = pygame.event.get()
            self.engine.handle_events(events)
            self.engine.update()
            self.engine.draw(self.window.screen)
            self.window.update()
        
        pygame.quit()
