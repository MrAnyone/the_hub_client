import pygame
from threading import Thread
from time import sleep
from math import cos,  sin, radians


# class BackGroundRuntime(Thread):
#
#     def __init__(self, screen_option):
#         Thread.__init__(self)
#         self.ready = True
#         # self.window = pygame_instance.display.get_surface()
#         self.screen_option = screen_option
#         self.sun = pygame.image.load("./login_screen/background/assets/sun.png").convert_alpha()
#         self.sun = pygame.transform.scale(self.sun, (int(screen_option['width'] * 0.1), int(screen_option['height'] * 0.1)))
#         self.moon = pygame.image.load("./login_screen/background/assets/moon.png").convert_alpha()
#         self.moon = pygame.transform.scale(self.moon, (int(screen_option['width'] * 0.1), int(screen_option['height'] * 0.1)))
#         self.sun_to_render = [self.sun.copy(), self.sun.get_rect()]
#         self.moon_to_render = [self.moon.copy(), self.moon.get_rect()]
#
#     # coord de point dans cercle de rayon R a l'angle T
#     # y =  sin(T) * R + initial x
#     # x = cos(T) * R + initial y
#     def scale_x(self, angle):
#         return int(self.screen_option['width'] * 0.45) + int(cos(radians(angle)) * (self.screen_option['width'] * 0.45))
#
#     def scale_y(self, angle):
#         return int(self.screen_option['height'] * 0.9) + int(sin(radians(angle)) * (self.screen_option['width'] * 0.45))
#
#     # Boucle principal du thread/processus
#     def run(self):
#         moon_angle = 0
#         sun_angle = 180
#         # Vitesse de defilement augmenter la valeur diminue la vitesse et vise versa
#         speed = 0.02
#
#         while self.ready:
#             # Calcule des coordonnées pour l'objet 1
#             self.sun_to_render[0] = pygame.transform.rotate(self.sun, sun_angle)
#             self.sun_to_render[1] = self.sun_to_render[0].get_rect()
#             self.sun_to_render[1].move_ip(self.scale_x(sun_angle), self.scale_y(sun_angle))
#
#             # Calcule des coordonnées pour l'objet 2
#             self.moon_to_render[0] = pygame.transform.rotate(self.moon, sun_angle)
#             self.moon_to_render[1] = self.moon_to_render[0].get_rect()
#             self.moon_to_render[1].move_ip(self.scale_x(moon_angle), self.scale_y(moon_angle))
#
#             # Calcule de l'angle suivant
#             sun_angle = 0 if sun_angle == 360 else sun_angle + 1
#             moon_angle = 0 if moon_angle == 360 else moon_angle + 1
#
#             # Regulation de la vitesse avec un sleep
#             sleep(speed)
#
#     # Permet d'arreter la boucle principal du thread/processus
#     def kill(self):
#      self.ready = False
#
#     # Permet de rendre à l'écran les image calculer par le thread/processus
#     def render_part(self, window):
#         window.blit(self.sun_to_render[0], self.sun_to_render[1])
#         window.blit(self.moon_to_render[0], self.moon_to_render[1])
class BackGroundRuntime(Thread):

    def __init__(self, screen_option):
        Thread.__init__(self)
        self.ready = True
        # self.window = pygame_instance.display.get_surface()
        self.screen_option = screen_option
        self.background_surface = pygame.image.load('./login_screen/background/assets/fantasy-2048-x-1536_008.png').convert_alpha()
        self.middle_ground_surface = None
        self.foreground_surface_elem_1 = pygame.image.load('./login_screen/background/assets/fantasy-2048-x-1536_002.png').convert_alpha()
        self.foreground_surface_elem_1 = pygame.transform.scale(self.foreground_surface_elem_1, (screen_option['width'], screen_option['height']))
        self.foreground_surface_elem_2 = pygame.image.load('./login_screen/background/assets/fantasy-2048-x-1536_001.png').convert_alpha()
        self.foreground_surface_elem_2 = pygame.transform.scale(self.foreground_surface_elem_2, (screen_option['width'], screen_option['height']))
        self.foreground_surface_elem_3 = pygame.image.load('./login_screen/background/assets/fantasy-2048-x-1536_000.png').convert_alpha()
        self.foreground_surface_elem_3 = pygame.transform.scale(self.foreground_surface_elem_3, (screen_option['width'], screen_option['height']))
        self.foreground_surface_elem_4 = pygame.image.load('./login_screen/background/assets/fantasy-2048-x-1536_003.png').convert_alpha()
        self.foreground_surface_elem_4 = pygame.transform.scale(self.foreground_surface_elem_4, (screen_option['width'], screen_option['height']))
        self.foreground_surface_elem_5 = pygame.image.load('./login_screen/background/assets/fantasy-2048-x-1536_004.png').convert_alpha()
        self.foreground_surface_elem_5 = pygame.transform.scale(self.foreground_surface_elem_5, (screen_option['width'], screen_option['height']))

        self.foreground_surface_elem_6 = pygame.image.load('./login_screen/background/assets/fantasy-2048-x-1536_005.png').convert_alpha()
        self.foreground_surface_elem_6 = pygame.transform.scale(self.foreground_surface_elem_6, (screen_option['width'], screen_option['height']))
        self.foreground_surface_elem_7 = pygame.image.load('./login_screen/background/assets/fantasy-2048-x-1536_006.png').convert_alpha()
        self.foreground_surface_elem_7 = pygame.transform.scale(self.foreground_surface_elem_7, (screen_option['width'], screen_option['height']))
        self.foreground_surface_elem_8 = pygame.image.load('./login_screen/background/assets/fantasy-2048-x-1536_007.png').convert_alpha()
        self.foreground_surface_elem_8 = pygame.transform.scale(self.foreground_surface_elem_8, (screen_option['width'], screen_option['height']))


        self.rel_x_rock_foreground = 0
        self.rel_x_rock_middle = 0
        self.rel_x_rock_background = 0

        self.rel_x_cloud_foreground = 0
        self.rel_x_cloud_middle = 0
        self.rel_x_cloud_background = 0

    # Boucle principal du thread/processus
    def run(self):
        bckground_pos = 0
        speed = 0.02
        while self.ready:
            self.rel_x_cloud_foreground = bckground_pos % self.screen_option['width']
            # # self.rel_x_rock_foreground = bckground_pos % self.screen_option['width']
            self.rel_x_rock_foreground = (bckground_pos//2) % self.screen_option['width']
            self.rel_x_rock_middle = (bckground_pos//3) % self.screen_option['width']
            self.rel_x_rock_background = (bckground_pos//4) % self.screen_option['width']
            bckground_pos -= 1
            if bckground_pos == 4 * self.screen_option['width']:
                print('reset indecx')
                bckground_pos = 0
            sleep(speed)

    # Permet d'arreter la boucle principal du thread/processus
    def kill(self):
     self.ready = False

    # Permet de rendre à l'écran les image calculer par le thread/processus
    def render_part(self, window):
        window.blit(self.background_surface, (0, 0))

        if self.rel_x_rock_background < self.screen_option['width']:
            window.blit(self.foreground_surface_elem_5, (self.rel_x_rock_background, 100))
            window.blit(self.foreground_surface_elem_8, (self.rel_x_rock_background, 0))
        window.blit(self.foreground_surface_elem_5, (self.rel_x_rock_background - self.screen_option['width'], 100))
        window.blit(self.foreground_surface_elem_8, (self.rel_x_rock_background - self.screen_option['width'], 0))

        if self.rel_x_rock_middle < self.screen_option['width']:
            window.blit(self.foreground_surface_elem_4, (self.rel_x_rock_middle, 100))
            window.blit(self.foreground_surface_elem_7, (self.rel_x_rock_middle, 0))
        window.blit(self.foreground_surface_elem_4, (self.rel_x_rock_middle - self.screen_option['width'], 100))
        window.blit(self.foreground_surface_elem_7, (self.rel_x_rock_middle - self.screen_option['width'], 0))

        if self.rel_x_rock_foreground < self.screen_option['width']:
            window.blit(self.foreground_surface_elem_1, (self.rel_x_rock_foreground, 50))
            window.blit(self.foreground_surface_elem_2, (self.rel_x_rock_foreground, -10))
            window.blit(self.foreground_surface_elem_3, (self.rel_x_rock_foreground, 100))
        window.blit(self.foreground_surface_elem_1, (self.rel_x_rock_foreground - self.screen_option['width'], 50))
        window.blit(self.foreground_surface_elem_2, (self.rel_x_rock_foreground - self.screen_option['width'], -10))
        window.blit(self.foreground_surface_elem_3, (self.rel_x_rock_foreground - self.screen_option['width'], 100))

        if self.rel_x_cloud_foreground < self.screen_option['width']:
            window.blit(self.foreground_surface_elem_6, (self.rel_x_cloud_foreground, 0))
        # pygame.draw.line(window, (0, 0, 0), (self.rel_x_rock_foreground, 0), (self.rel_x_rock_foreground, self.screen_option['height']), 3)
        window.blit(self.foreground_surface_elem_6, (self.rel_x_cloud_foreground - self.foreground_surface_elem_6.get_rect().width, 0))
