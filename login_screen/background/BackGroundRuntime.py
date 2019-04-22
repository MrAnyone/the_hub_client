from threading import Thread
from time import sleep
from math import cos,  sin, radians


# Gere l'animation de l'arriere plan de la page login
class BackGroundRuntime(Thread):

    def __init__(self, pygame_instance, screen_option):
        Thread.__init__(self)
        self.ready = True
        self.pygame_instance = pygame_instance
        self.window = pygame_instance.display.get_surface()
        self.screen_option = screen_option
        self.sun = pygame_instance.image.load("./login_screen/background/assets/sun.png").convert_alpha()
        self.sun = pygame_instance.transform.scale(self.sun, (int(self.window.get_width() * 0.1), int(self.window.get_height() * 0.1)))
        self.moon = pygame_instance.image.load("./login_screen/background/assets/moon.png").convert_alpha()
        self.moon = pygame_instance.transform.scale(self.moon, (int(self.window.get_width() * 0.1), int(self.window.get_height() * 0.1)))
        self.sun_to_render = [self.sun.copy(), self.sun.get_rect()]
        self.moon_to_render = [self.moon.copy(), self.moon.get_rect()]

    # coord de point dans cercle de rayon R a l'angle T
    # y =  sin(T) * R + initial x
    # x = cos(T) * R + initial y
    def scale_x(self, angle):
        return int(self.window.get_width() * 0.45) + int(cos(radians(angle)) * (self.window.get_width() * 0.45))

    def scale_y(self, angle):
        return int(self.window.get_height() * 0.9) + int(sin(radians(angle)) * (self.window.get_width() * 0.45))

    # Boucle principal du thread/processus
    def run(self):
        moon_angle = 0
        sun_angle = 180
        # Vitesse de defilement augmenter la valeur diminue la vitesse et vise versa
        speed = 0.02

        while self.ready:
            # Calcule des coordonnées pour l'objet 1
            self.sun_to_render[0] = self.pygame_instance.transform.rotate(self.sun, sun_angle)
            self.sun_to_render[1] = self.sun_to_render[0].get_rect()
            self.sun_to_render[1].move_ip(self.scale_x(sun_angle), self.scale_y(sun_angle))

            # Calcule des coordonnées pour l'objet 2
            self.moon_to_render[0] = self.pygame_instance.transform.rotate(self.moon, sun_angle)
            self.moon_to_render[1] = self.moon_to_render[0].get_rect()
            self.moon_to_render[1].move_ip(self.scale_x(moon_angle), self.scale_y(moon_angle))

            # Calcule de l'angle suivant
            sun_angle = 0 if sun_angle == 360 else sun_angle + 1
            moon_angle = 0 if moon_angle == 360 else moon_angle + 1

            # Regulation de la vitesse avec un sleep
            sleep(speed)

    # Permet d'arreter la boucle principal du thread/processus
    def kill(self):
     self.ready = False

    # Permet de rendre à l'écran les image calculer par le thread/processus
    def render_part(self):
        self.window.blit(self.sun_to_render[0], self.sun_to_render[1])
        self.window.blit(self.moon_to_render[0], self.moon_to_render[1])
