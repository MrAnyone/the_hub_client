# from threading import Thread
from common_modules.text_box import TextBox
from common_modules.button import Button
import login_screen


# Gére le contenue principale de la page de connection
class Login:

    def __init__(self, screen_setings):
        # Thread.__init__(self)
        self.ready = True
        # self.pygame_instance = pygame_instance
        user_name_pos = (int((screen_setings['width']/2) - 170), int((screen_setings['height']/2) - 35))
        password_pos = (int((screen_setings['width']/2) - 170), int((screen_setings['height']/2) + 5))
        confirm_button_pos = (int((screen_setings['width']/2) + 90), int((screen_setings['height']/2) - 15))
        password_button_pos = (int((screen_setings['width']/2) - 170) + 90, int((screen_setings['height']/2) + 39))
        new_button_pos = (int((screen_setings['width']/2) - 170), int((screen_setings['height']/2) + 39))
        self.screen_entity = {
            'user_name': TextBox(editable=True, pos=user_name_pos, hit_text='Username', text_pos=(5, 0)),
            'password': TextBox(editable=True, pos=password_pos, hit_text='Password', entry_hider='*', text_pos=(5, 0)),
            'confirm_button': Button(box_size=(90, 30), text='Confirm', pos=confirm_button_pos, text_pos=(5, 0)),
            'password_forget': Button(background_color=(0, 0, 0, 0), size=12, box_size=(120, 20), text_pos=(0, 5),
                                      text='Password Lost', pos=password_button_pos, text_underline=True),
            'new_account': Button(background_color=(0, 0, 0, 0), size=12, box_size=(80, 20), text_pos=(0, 5),
                                  text='New account', pos=new_button_pos, text_underline=True)
        }
        self.screen_setings = screen_setings

    def run(self):
        pass

    def spread_mouse_click_event(self, mouse_position, sub_part_to_render_index):
        self.screen_entity['user_name'].trigger_click(mouse_position)
        self.screen_entity['password'].trigger_click(mouse_position)

        onclick_login = self.screen_entity['confirm_button'].on_click
        onclick_new = self.screen_entity['new_account'].on_click
        onclick_forget = self.screen_entity['password_forget'].on_click

        @onclick_login(mouse_position)
        def button_click():
            print('switch view: lobby')

        @onclick_new(mouse_position)
        def button_click():
            login_screen.sub_part_to_render_index = 1
            print('switch view: nouvelle utilisateur')

        @onclick_forget(mouse_position)
        def button_click():
            login_screen.sub_part_to_render_index = 2
            print('switch view: mdp oublier')

    def spread_key_event(self, input_key):
        self.screen_entity['user_name'].trigger_input(input_key)
        self.screen_entity['password'].trigger_input(input_key)

    def kill(self):
        self.ready = False

    def render_part(self, window):
        # self.screen_entity['user_name'].render_part(self.pygame_instance.display.get_surface())
        # self.screen_entity['password'].render_part(self.pygame_instance.display.get_surface())
        # self.screen_entity['confirm_button'].render_part(self.pygame_instance.display.get_surface())
        # self.screen_entity['new_account'].render_part(self.pygame_instance.display.get_surface())
        # self.screen_entity['password_forget'].render_part(self.pygame_instance.display.get_surface())
        self.screen_entity['user_name'].render_part(window)
        self.screen_entity['password'].render_part(window)
        self.screen_entity['confirm_button'].render_part(window)
        self.screen_entity['new_account'].render_part(window)
        self.screen_entity['password_forget'].render_part(window)
