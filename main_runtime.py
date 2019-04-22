import pygame
# import game_modules
import menu_screen
import login_screen


class MainRuntime:

    def __init__(self):
        pygame.init()
        self.settings = {
            'weidth': 640,
            'heigth': 480,
            'full_screen': False,
            'screen_index': 0,
            'stay_open': True,
            'fps': 60
        }
        self.main_modules = [login_screen, menu_screen]

    def run(self):

        # todo: une barre de chargement peut etre mise en place ici pour modeliser
        #  l'avancement de l'initialisation de tout les modules
        window = pygame.display.set_mode((self.settings['weidth'], self.settings['heigth']))
        for modules in self.main_modules:
            modules.init_screen(pygame, self.settings)

        clock = pygame.time.Clock()

        # maintient de la fenétre
        while self.settings['stay_open']:
            # window.fill((0, 0, 0))
            # clock.tick(self.settings['fps'])
            if not self.main_modules[self.settings['screen_index']].running:
                self.main_modules[self.settings['screen_index']].show_screen()
            for event in pygame.event.get():  # On parcours la liste de tous les événements reçus
                if event.type == pygame.QUIT:  # Si un de ces événements est de type QUIT
                    self.main_modules[self.settings['screen_index']].stop_jobs()
                    self.main_modules[self.settings['screen_index']].wait_job_end()
                    self.settings['stay_open'] = False
            # pygame.display.flip()
