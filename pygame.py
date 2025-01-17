import pygame, sys

class Main:
    def __init__(self):
        pygame.init()
        self.win = pygame.display.set_mode((1280, 720))
        self.clock = pygame.time.Clock()

    def run(self):
        while True:
            dt = self.clock.tick() / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()

if __name__ == '__main__':
    main = Main()
    main.run()