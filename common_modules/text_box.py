class TextBox:

    def __init__(self, pygame_ref, text='', actif=False, editable=False, entry_hider=None,
                 font_path='./common_assets/font/Jamma 8x16.ttf', box_size=(250, 50), box_background=(0, 0, 0, 100),
                 size=20, hit_text='', color=(250, 250, 250), pos=(0, 0)):
        # self.size = size
        self.editable = editable
        self.hit_text = hit_text
        self.pos = pos
        self.font_path = font_path
        self.size = size
        self.box_size = box_size
        self.actif = actif
        self.text = text
        self.color = color
        self.pygame_ref = pygame_ref
        self.window = pygame_ref.display.get_surface()
        self.font = pygame_ref.font.Font(font_path, size)
        self.show_cursor = True
        self.box_background = box_background
        self.box_rect = pygame_ref.Surface(box_size)
        self.box_rect.fill(box_background)

    def rebuild(self, font=None, box_size=None, size=None, box_background=None):
        font_change = (
            font if font else self.font_path,
            size if size else self.size
        )
        if font_change[0] != self.font_path or font_change[1] != self.size:
            self.font = self.pygame_ref.font.Font(font_change[0], font_change[1])
        if box_size:
            self.box_rect = self.pygame_ref.Surface(box_size)
        if box_background:
            self.box_rect.fill(box_background)
        self.font = self.pygame_ref.font.Font(font, size)

    def trigger_input(self, input_key):
        if self.actif and self.editable:
            self.box_rect.fill(self.box_background)
            if input_key == 8:
                self.text = self.text[:-1]
            else:
                self.text += chr(input_key)

    def trigger_click(self, pos):
        if self.box_rect.get_rect().collidepoint(pos):
            if self.text == '':
                self.box_rect.fill(self.box_background)
            self.actif = True
            self.show_cursor = True
        elif self.actif:
            self.actif = False
            # self.show_cursor = False

    def render_part(self):
        text_to_render = self.text if self.text != '' else self.hit_text
        if self.actif:
            text_to_render = self.text
            if self.show_cursor:
                text_to_render += "|"
        else:
            if self.show_cursor:
                self.show_cursor = False
                self.box_rect.fill(self.box_background)
                text_to_render = text_to_render[:-1]
            if self.text == '':
                self.box_rect.fill(self.box_background)
                text_to_render = self.hit_text
        text_surface = self.font.render(text_to_render, False, self.color)
        text_box = self.box_rect.blit(text_surface, (0, 0))
        self.window.blit(self.box_rect, self.pos)