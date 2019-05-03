import sound_manager
import time
from threading import Thread
import pygame


class Splash(Thread):
    def __init__(self, settings):
        Thread.__init__(self)
        self.ready = True
        self.settings = settings
        self.laughting_screen = pygame.image.load('./common_assets/laughing_screen/laughing screen_side.png').convert_alpha()
        self.size = int(min(settings['width'] * 0.60, settings['height'] * 0.60))
        x, y = ((settings['width'] // 2) - (self.size // 2)), ((settings['height'] // 2) - (self.size // 2))
        self.pos = (
            x,
            y
        )
        self.laughting_screen = pygame.transform.scale(self.laughting_screen, (self.size, self.size))
        self.mask = pygame.Surface((self.size * 2, self.size * 2))
        self.mask.fill((0, 0, 0, 125))
        sound_manager.SoundMgr.load_new_sound(name='splash_screen', path='./common_assets/sound/musics/Crowd Laughing.wav')
        sound_manager.SoundMgr.volume(name='splash_screen', volume=0.2)

    def run(self):
        counter = 0
        alfa_value = 125
        sound_manager.SoundMgr.run_track(name='splash_screen')
        while self.ready and counter != 10:
            if alfa_value >= 0:
                self.mask.set_alpha(alfa_value)
            alfa_value -= 12
            counter += 1
            time.sleep(1)
        sound_manager.SoundMgr.stop_track(name='splash_screen')
        sound_manager.SoundMgr.remove_track(name='splash_screen')
        self.settings['screen_index'] = 1

    def spread_mouse_click_event(self, mouse_position):
        self.ready = False

    def spread_key_event(self, input_key):
        self.ready = False

    def kill(self):
        self.ready = False

    def render_part(self, window):
        window.blit(self.laughting_screen, self.pos)
        window.blit(self.mask, self.pos)
