from threading import Thread
from math import cos,  sin, radians


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

    def scale_x(self, angle):
        return int(self.window.get_width() * 0.45) + int(cos(radians(angle)) * (self.window.get_width() * 0.45))

    def scale_y(self, angle):
        return int(self.window.get_height() * 0.9) + int(sin(radians(angle)) * (self.window.get_width() * 0.45))

    # coord point dans cercle de rayon R a l'angle T
    # y =  sin(T) * R + initial x
    # x = cos(T) * R + initial y
    def run(self):
        moon_angle = 0
        sun_angle = 180
        clock = self.pygame_instance.time.Clock()

        while self.ready:
            # clock.tick(self.screen_option['fps'])
            sun_to_render = self.pygame_instance.transform.rotate(self.sun, sun_angle)
            sun_rect = sun_to_render.get_rect()
            sun_rect.move_ip(self.scale_x(sun_angle), self.scale_y(sun_angle))

            moon_to_render = self.pygame_instance.transform.rotate(self.moon, moon_angle)
            moon_rect = moon_to_render.get_rect()
            moon_rect.move_ip(self.scale_x(moon_angle), self.scale_y(moon_angle))

            self.window.fill((0, 0, 0))
            self.window.blit(sun_to_render, sun_rect)
            self.window.blit(moon_to_render, moon_rect)
            sun_angle = 0 if sun_angle == 360 else sun_angle + 1
            moon_angle = 0 if moon_angle == 360 else moon_angle + 1
            self.pygame_instance.display.flip()

    def kill(self):
        self.ready = False
