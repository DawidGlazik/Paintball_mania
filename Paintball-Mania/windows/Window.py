import pygame
from windows.Button import Button


class Window:
    def __init__(self):
        self.run = True
        self.window = None
        self.width = 0
        self.height = 0
        self.size = self.width, self.height

    def on_init(self):
        try:
            pygame.init()
            self.width = int(pygame.display.Info().current_w * 3 / 4)
            self.height = int(pygame.display.Info().current_h * 3 / 4)
            self.size = self.width, self.height
            self.window = pygame.display.set_mode(self.size, pygame.NOFRAME | pygame.RESIZABLE)
            pygame.display.set_caption("Paintball Mania")
            self.run = True
        except pygame.error as e:
            print(f"Error initializing Pygame: {e}")

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.run = False

    def on_key_down(self, player, key):
        if key[pygame.K_a] or key[pygame.K_LEFT]:
            player.move_ip(-1, 0)
        elif key[pygame.K_d] or key[pygame.K_RIGHT]:
            player.move_ip(1, 0)
        elif key[pygame.K_w] or key[pygame.K_UP]:
            player.move_ip(0, -1)
        elif key[pygame.K_s] or key[pygame.K_DOWN]:
            player.move_ip(0, 1)

    def on_cleanup(self):
        pygame.quit()

    def main_menu(self):
        image = pygame.image.load("../../img/main_menu.jpg")
        button_height = int(self.height / 15)
        button_width = int(self.width / 8)
        button_pos_x = int(self.width / 2 - button_width / 2)
        button_pos_y = button_height * 3
        new_lobby_button = Button("Create lobby", button_pos_x, button_pos_y, button_width,
                         button_height, "blue", "red")
        button_pos_y += button_height * 2
        join_lobby_button = Button("Join lobby", button_pos_x, button_pos_y, button_width,
                         button_height, "blue", "red")
        button_pos_y += button_height * 2
        options_button = Button("Options", button_pos_x, button_pos_y, button_width,
                         button_height, "blue", "red")
        button_pos_y += button_height * 2
        exit_button = Button("Exit", button_pos_x, button_pos_y, button_width,
                         button_height, "blue", "red", self.on_cleanup)
        button_pos_y += button_height * 2
        font = pygame.font.Font(None, int(self.height / 10))
        text = font.render("Paintball Mania!", True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.width // 2, self.height // 10))
        while self.run:
            scaled_image = pygame.transform.scale(image, (self.width, self.height))
            self.window.fill((0, 0, 0))
            self.window.blit(scaled_image, (0, 0))
            new_lobby_button.draw(self.window)
            join_lobby_button.draw(self.window)
            options_button.draw(self.window)
            exit_button.draw(self.window)
            self.window.blit(text, text_rect)
            for event in pygame.event.get():
                self.on_event(event)
            pygame.display.update()
        pass

    def options(self):
        pass

    def lobby(self):
        pass

    def play(self):
        pass
    
    def on_execute(self):
        self.on_init()
        self.main_menu()
        self.on_cleanup()


if __name__ == "__main__":
    game_instance = Window()
    game_instance.on_execute()
