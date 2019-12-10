from common_modules.text_box import TextBox
from common_modules.button import Button


class PasswordForget:
    def __init__(self, screen_setings):
        self.ready = True

        # (x, y)
        user_name_pos = (int((screen_setings['width'] / 2) - 170), int((screen_setings['height'] / 2) - 35))
        email_pos = (int((screen_setings['width'] / 2) - 170), int((screen_setings['height'] / 2) + 5))
        password_pos = (int((screen_setings['width'] / 2) - 170), int((screen_setings['height'] / 2) + 17))
        confirm_password_pos = (int((screen_setings['width'] / 2) - 170), int((screen_setings['height'] / 2) + 28))
        confirm_button_pos = (int((screen_setings['width'] / 2) + 90), int((screen_setings['height'] / 2) - 15))
        back_pos = (int((screen_setings['width'] / 2) - 170), int((screen_setings['height'] / 2) + 39))


        self.screen_entity = {
            'user_name': TextBox(editable=True, pos=user_name_pos, hit_text='Username', text_pos=(5, 0)),
            'email': TextBox(editable=True, pos=email_pos, hit_text='Email', text_pos=(5, 0)),
            'password': TextBox(editable=True, pos=password_pos, hit_text='Password', entry_hider='*', text_pos=(5, 0)),
            'confirm_password': TextBox(editable=True, pos=confirm_password_pos, hit_text='confirm password', entry_hider='*', text_pos=(5, 0)),
            'confirm_button': Button(box_size=(90, 30), text='Confirm', pos=confirm_button_pos, text_pos=(5, 0)),
            'back': Button(background_color=(0, 0, 0, 0), size=12, box_size=(120, 20), text_pos=(0, 5),
                                      text='Back', pos=back_pos, text_underline=True),
        }
        self.screen_setings = screen_setings

    def run(self):
        pass

    def kill(self):
        pass

    def spread_key_event(self, window):
        pass

    def render_part(self, window):
        pass
