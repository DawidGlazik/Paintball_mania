import pygame


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
            self.width = pygame.display.Info().current_w * 3 / 4
            self.height = pygame.display.Info().current_h * 3 / 4
            self.size = self.width, self.height
            self.window = pygame.display.set_mode(self.size, pygame.RESIZABLE)
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
        pass

    def lobby(self):
        pass

    def play(self):
        pass
    
    def on_execute(self):
        self.on_init()
        player = pygame.Rect((300, 250, 50, 50))
        while self.run:
            self.window.fill((0, 0, 0))
            pygame.draw.rect(self.window, (255, 0, 0), player)
            key = pygame.key.get_pressed()
            self.on_key_down(player, key)
            for event in pygame.event.get():
                self.on_event(event)
            pygame.display.update()
        self.on_cleanup()


if __name__ == "__main__":
    game_instance = Window()
    game_instance.on_execute()
