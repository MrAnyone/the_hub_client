import pygame
# import game_modules
import splash_screen
import sound_manager
import menu_screen
import login_screen


# todo: - change windows icones
# Objet gérant la boucle principale de la fenetre
class MainRuntime:

    def __init__(self):
        self.main_modules = [
            splash_screen,
            login_screen,
            menu_screen,
        ]
        sound_manager.init_manadger()
        pygame.init()
        self.settings = {
            'width': 720,
            'height': 360,
            'full_screen': False,
            'screen_index': 0,
            'stay_open': True,
            'music_volume': 0.5,
            'sound_volume': 0.5,
            'fps': 60
        }
        # self.settings = {
        #     'width': 1920,
        #     'height': 1080,
        #     'full_screen': True,
        #     'screen_index': 0,
        #     'stay_open': True,
        #     'fps': 60
        # }

    def run(self):

        # todo: une barre de chargement peut etre mise en place ici pour modeliser
        #  l'avancement de l'initialisation de tout les modules
        window = pygame.display.set_mode((self.settings['width'], self.settings['height']), flags= pygame.FULLSCREEN if self.settings['full_screen'] else 0)
        pygame.display.set_caption('The Hub')
        for modules in self.main_modules:
            modules.init_screen(self.settings)
        clock = pygame.time.Clock()

        # Boucle principale + garde la fenetre ouverte
        while self.settings['stay_open']:
            window.fill((0, 0, 0)) # Clear the window (in black) between each fram
            clock.tick(self.settings['fps']) # (optimisation) synchronise the loop for scaling to a given frame rate
            if not self.main_modules[self.settings['screen_index']].running:
                self.main_modules[self.settings['screen_index']].show_screen() # lance le rendu d'image
            self.main_modules[self.settings['screen_index']].render_screen(window) # Effectue un rendu d'image
            for event in pygame.event.get():  # Parcours la liste de tous les événements reçus
                if event.type == pygame.QUIT:  # Si un de ces événements est de type QUIT
                    self.main_modules[self.settings['screen_index']].stop_jobs()  # Impose l'arret des processus pour la fenetre en cour de rendue
                    self.main_modules[self.settings['screen_index']].wait_job_end()  # Attend que les processus soit terminé
                    self.settings['stay_open'] = False  # Change l'état de la boucle principal
                elif event.type == pygame.KEYDOWN:
                    self.main_modules[self.settings['screen_index']].trigger_input(event.key)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.main_modules[self.settings['screen_index']].trigger_click(event.pos)
            pygame.display.update()
            # pygame.display.flip()  # Met a jour la fenetre
