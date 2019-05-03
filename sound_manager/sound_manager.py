import pygame


class SoundManager:

    def __init__(self):
        pygame.mixer.pre_init(size=16)
        self.track_play_list = {}

    def load_new_sound(self, path=None, name=None):
        if path and name:
            self.track_play_list[name] = pygame.mixer.Sound(path)

    def run_track(self, name=None, loop=0):
        if name:
            self.track_play_list[name].play(loops=loop)

    def stop_track(self, name=None):
        if name:
            self.track_play_list[name].stop()

    def remove_track(self, name=None):
        if name:
            self.track_play_list.pop(name)
