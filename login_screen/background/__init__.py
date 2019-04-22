from .BackGroundRuntime import BackGroundRuntime


# Renvoie une instace de l'objet BackGroundRuntime
def init_background(pygame_instance, option):
    return BackGroundRuntime(pygame_instance, option)