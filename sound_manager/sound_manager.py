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

    def volume(self, name=None, volume=0.5):
        if not name:
            for key, value in self.track_play_list:
                value.set_volume(volume)
        else:
            self.track_play_list[name].set_volume(volume)

    def remove_track(self, name=None):
        if name:
            self.track_play_list.pop(name)
