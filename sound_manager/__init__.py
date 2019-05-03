from .sound_manager import SoundManager

SoundMgr = None


def init_manadger():
    global SoundMgr
    SoundMgr = SoundManager()

