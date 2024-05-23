class SelectNumber:
    def __init__(self, pygame, font):
        self.pygame = pygame
        self.btn_w = 80
        self.btn_h = 80
        self.my_font = font
        self.selected_number = 0
        self.color_selected = (0, 255, 0)
        self.color_normal = (200, 200, 200)
        
        self.btn_positions = [
            (950, 50), (1050, 50),
            (950, 150), (1050, 150),
            (950, 250), (1050, 250),
            (950, 350), (1050, 350),
            (1050, 450)
        ]
        
    def draw(self, pygame, surface):
        for index, pos in enumerate(self.btn_positions):
            if self.selected_number > 0 and self.selected_number - 1 == index:
                color = self.color_selected
                text_color = self.color_selected
            elif self.button_hover(pos):
                color = self.color_selected
                text_color = self.color_selected
            else:
                color = self.color_normal
                text_color = self.color_normal

            pygame.draw.rect(surface, color, [pos[0], pos[1], self.btn_w, self.btn_h], width=3, border_radius=10)
            text_surface = self.my_font.render(str(index + 1), False, text_color)
            surface.blit(text_surface, (pos[0] + 26, pos[1]))

    def button_clicked(self, mouse_x: int, mouse_y: int) -> None:
        for index, pos in enumerate(self.btn_positions):
            if self.on_button(mouse_x, mouse_y, pos):
                self.selected_number = index + 1

    def button_hover(self, pos: tuple) -> bool:
        mouse_pos = self.pygame.mouse.get_pos()
        return self.on_button(mouse_pos[0], mouse_pos[1], pos)

    def on_button(self, mouse_x: int, mouse_y: int, pos: tuple) -> bool:
        return pos[0] < mouse_x < pos[0] + self.btn_w and pos[1] < mouse_y < pos[1] + self.btn_h
