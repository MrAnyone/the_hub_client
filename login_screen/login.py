# from threading import Thread
from common_modules.text_box import TextBox


# Gére le contenue principale de la page de connection
class Login:

    def __init__(self, pygame_instance, screen_option):
        # Thread.__init__(self)
        self.ready = True
        self.screen_entity = {
            'user_name': TextBox(pygame_instance, editable=True, hit_text='Username'),
            'password': TextBox(pygame_instance, editable=True, pos=(0, 150), hit_text='Password', entry_hider='*'),
        }

    def run(self):
        while self.ready:
            # todo: affichage des champs de saisie de donnée + bouton de connexion + creation de compte et mdp oublier
            pass

    def spread_mouse_click_event(self, mouse_position):
        self.screen_entity['user_name'].trigger_click(mouse_position)
        self.screen_entity['password'].trigger_click(mouse_position)
        pass

    def spread_key_event(self, input_key):
        self.screen_entity['user_name'].trigger_input(input_key)
        self.screen_entity['password'].trigger_input(input_key)
        pass

    def kill(self):
        self.ready = False

    def render_part(self):
        self.screen_entity['user_name'].render_part()
        self.screen_entity['password'].render_part()
        pass
