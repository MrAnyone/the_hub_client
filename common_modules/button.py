from .text_box import TextBox
import pygame


# todo: handle cicle shape button
class Button:
    def __init__(self, text='Button', font_path='./common_assets/font/Jamma 8x16.ttf', box_size=(250, 30),
                 box_background=None, background_color=(150, 150, 150, 200), circle_shape=None, text_underline=False,
                 size=20, color=(250, 250, 250), pos=(0, 0), text_pos=(0, 0)):
        self.text = TextBox(text=text, font_path=font_path, box_size=box_size,
                            background_color=background_color, size=size,
                            color=color, pos=pos, box_background=box_background, text_pos=text_pos, text_underline=text_underline)
        self.on_screen = False
        # if circle_shape:
        #     self.button_rect = pygame.draw.circle(self.text.box_surface, color, pos, radius, width=0)

    # todo: change the color of the box if the cursor is hover it
    def cursor_hover(self):
        pass

    # decoration for on click action
    def on_click(self, mouse_position):

        def wrapper(function):
            if self.on_screen and self.text.box_rect.collidepoint(mouse_position):
                function()
        return wrapper

    def render_part(self, surface):
        self.on_screen = True
        self.text.render_part(surface)
