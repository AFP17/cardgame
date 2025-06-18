import unittest
from game_objects import Card, Player
from constants import *

class TestGameObjects(unittest.TestCase):
    def setUp(self):
        self.test_card = Card("Test Card", 3, 4, 2, "plastic")
        self.test_player = Player("Test Player")
        
    def test_card_creation(self):
        self.assertEqual(self.test_card.name, "Test Card")
        self.assertEqual(self.test_card.attack, 3)
        self.assertEqual(self.test_card.defense, 4)
        self.assertEqual(self.test_card.cost, 2)
        self.assertEqual(self.test_card.trash_type, "plastic")
        
    def test_player_creation(self):
        self.assertEqual(self.test_player.name, "Test Player")
        self.assertEqual(self.test_player.health, STARTING_HEALTH)
        self.assertEqual(self.test_player.mana, STARTING_MANA)
        self.assertEqual(self.test_player.max_mana, MAX_MANA)
        
    def test_player_mana(self):
        self.test_player.add_mana()
        self.assertEqual(self.test_player.mana, 2)
        
    def test_player_resources(self):
        self.assertEqual(len(self.test_player.trash_resources), 4)
        for resource in TRASH_TYPES:
            self.assertIn(resource, self.test_player.trash_resources)
            self.assertEqual(self.test_player.trash_resources[resource], 0)

if __name__ == '__main__':
    unittest.main()
