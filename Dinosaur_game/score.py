import pygame

color = 255,255,255
score = 0
score_increment = 10

class Score:
    def __init__(self):
        pygame.font.init()
        self.score=score
        self.font = pygame.font.Font(None, 36)
        self.text= self.font.render(f'Score: {score}', True, (255, 255, 255))



    def update(self):
        self.score+=score_increment
        # self.text= self.font.render(f'Score: {score}', True, (255, 255, 255))
        # self.draw(gameDisplay=game)

    def draw(self, gameDisplay):
        self.text = self.font.render(f'Score: {self.score}', True, (255, 255, 255))
        gameDisplay.blit(self.text, (10, 10))
