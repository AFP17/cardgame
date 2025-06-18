import pygame
import random
from pygame.locals import *

# Initialisation de Pygame
pygame.init()

# Configuration de la fenêtre
LARGEUR = 800
HAUTEUR = 600
FENETRE = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Jeu de Cartes")

# Couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)

# Classes

class Carte:
    def __init__(self, nom, attaque, defense, cout, type_dechets, effet=None):
        self.nom = nom
        self.attaque = attaque
        self.defense = defense
        self.cout = cout
        self.type_dechets = type_dechets  # Types: 'plastic', 'paper', 'glass', 'organic'
        self.effet = effet  # Special effect when played
        self.image = pygame.Surface((120, 180))
        self.image.fill(BLANC)
        self.rect = self.image.get_rect()
        self.selectionnee = False
        self.position = None

    def dessiner(self, surface):
        pygame.draw.rect(surface, NOIR, self.rect, 2)
        police = pygame.font.Font(None, 36)
        texte = police.render(f"{self.valeur} {self.couleur}", True, NOIR)
        surface.blit(texte, (self.rect.x + 10, self.rect.y + 10))

class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.deck = []
        self.main = []
        self.terrain = []
        self.points_vie = 30
        self.mana = 0
        self.max_mana = 10
        self.dechets = {
            'plastic': 0,
            'paper': 0,
            'glass': 0,
            'organic': 0
        }

    def draw(self):
        if self.deck:
            self.main.append(self.deck.pop(0))

class Jeu:
    def __init__(self):
        self.joueurs = [Joueur("Joueur 1"), Joueur("Joueur 2")]
        self.tour = 0  # 0 for player 1, 1 for player 2
        self.init_cartes()
        self.init_deck()
        self.init_main()

    def init_cartes(self):
        # Basic cards for testing
        self.cartes = [
            Carte("Plastic Golem", 3, 4, 3, 'plastic'),
            Carte("Paper Beast", 2, 3, 2, 'paper'),
            Carte("Glass Elemental", 4, 2, 4, 'glass'),
            Carte("Organic Spirit", 3, 3, 3, 'organic'),
            Carte("Recycling Bot", 2, 2, 2, 'plastic', effet="Gain 1 plastic"),
            Carte("Waste Incinerator", 4, 4, 5, 'organic', effet="Destroy a card")
        ]

    def init_deck(self):
        for joueur in self.joueurs:
            joueur.deck = self.cartes.copy()
            random.shuffle(joueur.deck)

    def init_main(self):
        for joueur in self.joueurs:
            for _ in range(3):
                joueur.draw()

    def distribuer(self):
        if len(self.cartes) >= 2:
            self.joueur.append(self.cartes.pop())
            self.croupier.append(self.cartes.pop())

    def dessiner(self, surface):
        surface.fill(BLANC)
        
        # Draw player info
        for i, joueur in enumerate(self.joueurs):
            self.dessiner_joueur_info(surface, joueur, i)
        
        # Draw cards in hand
        self.dessiner_main(surface, self.joueurs[self.tour])
        
        # Draw cards on board
        self.dessiner_terrain(surface)

    def dessiner_joueur_info(self, surface, joueur, position):
        y = 50 if position == 0 else 650
        police = pygame.font.Font(None, 24)
        
        # Health
        texte_vie = police.render(f"HP: {joueur.points_vie}", True, NOIR)
        surface.blit(texte_vie, (10, y))
        
        # Mana
        texte_mana = police.render(f"Mana: {joueur.mana}/{joueur.max_mana}", True, NOIR)
        surface.blit(texte_mana, (10, y + 20))
        
        # Trash resources
        x = 10
        for type_dechet, quantite in joueur.dechets.items():
            texte_dechet = police.render(f"{type_dechet[0].upper()}: {quantite}", True, NOIR)
            surface.blit(texte_dechet, (x, y + 40))
            x += 100

    def dessiner_main(self, surface, joueur):
        x = 100
        for carte in joueur.main:
            carte.rect.x = x
            carte.rect.y = 600
            carte.dessiner(surface)
            x += 130

    def dessiner_terrain(self, surface):
        x = 100
        for carte in self.joueurs[0].terrain:
            carte.rect.x = x
            carte.rect.y = 300
            carte.dessiner(surface)
            x += 130
        
        x = 100
        for carte in self.joueurs[1].terrain:
            carte.rect.x = x
            carte.rect.y = 400
            carte.dessiner(surface)
            x += 130

def main():
    jeu = Jeu()
    en_cours = True
    clock = pygame.time.Clock()
    
    while en_cours:
        for event in pygame.event.get():
            if event.type == QUIT:
                en_cours = False
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    # Next turn
                    jeu.tour = 1 - jeu.tour
                    jeu.joueurs[jeu.tour].mana = min(jeu.joueurs[jeu.tour].mana + 1, 10)
                    jeu.joueurs[jeu.tour].draw()
                elif event.key == K_d:
                    # Test playing a card (first card in hand)
                    joueur_actuel = jeu.joueurs[jeu.tour]
                    if joueur_actuel.main and joueur_actuel.mana >= joueur_actuel.main[0].cout:
                        carte = joueur_actuel.main.pop(0)
                        joueur_actuel.terrain.append(carte)
                        joueur_actuel.mana -= carte.cout
                        # Apply card effect if any
                        if carte.effet:
                            if carte.effet == "Gain 1 plastic":
                                joueur_actuel.dechets['plastic'] += 1
                            elif carte.effet == "Destroy a card":
                                # TODO: Implement card destruction
                                pass

        jeu.dessiner(FENETRE)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
