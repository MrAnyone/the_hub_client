from common_modules.text_box import TextBox
from common_modules.button import Button
import login_screen


# todo: call networkdriver
class PasswordForget:
    def __init__(self, screen_setings):
        self.ready = True

        # (x, y)
        email_pos = (int((screen_setings['width'] / 2) - 170), int((screen_setings['height'] / 2) - 15))
        confirm_button_pos = (int((screen_setings['width'] / 2) + 90), int((screen_setings['height'] / 2) - 15))
        back_pos = (int((screen_setings['width'] / 2) - 170), int((screen_setings['height'] / 2) + 15))

        self.screen_entity = {
            'email': TextBox(editable=True, pos=email_pos, hit_text='Email', text_pos=(5, 0)),
            'confirm_button': Button(box_size=(90, 30), text='Confirm', pos=confirm_button_pos, text_pos=(5, 0)),
            'back': Button(background_color=(0, 0, 0, 0), size=12, box_size=(120, 20), text_pos=(0, 5),
                                      text='Back', pos=back_pos, text_underline=True),
        }
        self.screen_setings = screen_setings

    def run(self):
        pass

    def kill(self):
        pass

    def spread_key_event(self, input_key):
        self.screen_entity['email'].trigger_input(input_key)

    def spread_mouse_click_event(self, mouse_position, sub_part_to_render_index):
        self.screen_entity['email'].trigger_click(mouse_position)

        onclick_login = self.screen_entity['confirm_button'].on_click
        onclick_forget = self.screen_entity['back'].on_click

        @onclick_login(mouse_position)
        def button_click():
            login_screen.sub_part_to_render_index = 0
            print('switch view: send verification and go back')

        @onclick_forget(mouse_position)
        def button_click():
            login_screen.sub_part_to_render_index = 0
            print('switch view: go back')

    def render_part(self, window):
        self.screen_entity['email'].render_part(window)
        self.screen_entity['confirm_button'].render_part(window)
        self.screen_entity['back'].render_part(window)
