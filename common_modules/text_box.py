class TextBox:

    def __init__(self, pygame_ref, text='', actif=False, editable=False, entry_hider=None,
                 font_path='./common_assets/font/Jamma 8x16.ttf', box_size=(250, 30),
                 box_background=None, background_color=(150, 150, 150, 200),
                 size=20, hit_text='', color=(250, 250, 250), pos=(0, 0)):
        self.editable = editable
        self.hit_text = hit_text
        self.pos = pos
        self.font_path = font_path
        self.size = size
        self.box_size = box_size
        self.actif = actif
        self.text = text
        self.entry_hider = entry_hider
        self.color = color
        self.background_color = pygame_ref.Color(background_color[0], background_color[1],
                                                 background_color[2], background_color[3])
        self.pygame_ref = pygame_ref
        self.window = pygame_ref.display.get_surface()
        self.font = pygame_ref.font.Font(font_path, size)
        self.show_cursor = True
        self.box_background = box_background
        if box_background:
            self.box_background = pygame_ref.image.load(box_background).convert_alpha()
            self.box_background = pygame_ref.transform.scale(self.box_background, box_size)
            self.box_surface = self.box_background
        else:
            self.box_surface = pygame_ref.Surface(box_size, pygame_ref.SRCALPHA)
            self.box_surface.fill(self.background_color)
        self.box_rect = self.box_surface.get_rect()
        self.box_rect.move_ip(pos[0], pos[1])

    def rebuild(self, font=None, box_size=None, size=None, box_background=None, background_color=None):
        font_change = (
            font if font else self.font_path,
            size if size else self.size
        )
        if font_change[0] != self.font_path or font_change[1] != self.size:
            self.font = self.pygame_ref.font.Font(font_change[0], font_change[1])
        if box_size:
            self.box_rect = self.pygame_ref.Surface(box_size)
        if box_background:
            self.box_surface = self.pygame_ref.image.load(box_background).convert_alpha()
            self.box_surface = self.pygame_ref.transform.scale(self.box_surface, box_size)
        if background_color:
            self.box_rect.fill(background_color)
        self.font = self.pygame_ref.font.Font(font, size)

    def trigger_input(self, input_key):
        if self.actif and self.editable:
            if self.box_background:
                self.box_surface = self.box_background
            else:
                self.box_surface.fill(self.background_color)
            if input_key == 8:
                self.text = self.text[:-1]
            else:
                self.text += chr(input_key)

    def trigger_click(self, pos):
        if self.box_rect.collidepoint(pos):
            if self.text == '':
                if self.box_background:
                    self.box_surface = self.box_background
                else:
                    self.box_surface.fill(self.background_color)
            self.actif = True
            self.show_cursor = True
        elif self.actif:
            self.actif = False

    def render_part(self):
        text_to_render = self.text if self.text != '' else self.hit_text
        if self.actif:
            if self.entry_hider:
                text_to_render = str('').zfill(len(self.text)).replace('0', self.entry_hider)
            else:
                text_to_render = self.text
            if self.show_cursor:
                text_to_render += "|"
        else:
            if self.show_cursor:
                self.show_cursor = False
                if self.box_background:
                    self.box_surface = self.box_background
                else:
                    self.box_surface.fill(self.background_color)
                text_to_render = text_to_render[:-1]
            if self.text == '':
                if self.box_background:
                    self.box_surface = self.box_background
                else:
                    self.box_surface.fill(self.background_color)
                text_to_render = self.hit_text
            elif self.text != '' and self.entry_hider:
                text_to_render = str('').zfill(len(self.text)).replace('0', self.entry_hider)

        text_surface = self.font.render(text_to_render, False, self.color)
        text_box = self.box_surface.blit(text_surface, (int(self.box_size[0] * 0.02), int(self.box_size[1] * 0.05)))
        self.window.blit(self.box_surface, self.pos)
