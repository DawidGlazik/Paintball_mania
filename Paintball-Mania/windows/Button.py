import pygame

class Button:
    def __init__(self, text: str, x: int, y: int, width: int, height: int, inactive_color: str, active_color: str, action=None):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.action = action

    def draw(self, surface):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            pygame.draw.rect(surface, self.active_color, (self.x, self.y, self.width, self.height))
            if click[0] == 1 and self.action is not None:
                self.action()
        else:
            pygame.draw.rect(surface, self.inactive_color, (self.x, self.y, self.width, self.height))

        font = pygame.font.SysFont(None, 40)
        text_obj = font.render(self.text, True, (0, 0, 0))
        text_rect = text_obj.get_rect(center=(self.x + self.width // 2, self.y + self.height // 2))
        surface.blit(text_obj, text_rect)