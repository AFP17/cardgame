from game_engine import GameEngine
from game_window import GameWindow
from game_manager import GameManager

def main():
    # Initialize game components
    window = GameWindow()
    engine = GameEngine()
    manager = GameManager()
    
    # Start the game loop
    manager.run()

if __name__ == "__main__":
    main()
