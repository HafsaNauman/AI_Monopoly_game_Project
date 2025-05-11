
import pickle
import pygame
from board import Board
from strategy import HumanRandom

class Game:
    def __init__(self, num_players=4, strategies=None):
        if strategies is None:
            strategies = [HumanRandom() for _ in range(num_players)]
        self.board = Board(num_players=num_players, strategies=strategies)
        self.last_roll = (0, 0)
        self.last_message = ""

    def _init_ui(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 800))
        pygame.display.set_caption("AI‐Monopoly")
        self.clock = pygame.time.Clock()

        # Board
        bg = pygame.image.load("assets/board.png").convert_alpha()
        self.board_image = pygame.transform.smoothscale(bg, (800, 800))

        # Tokens
        self.token_images = []
        for p in ("red", "blue", "green", "yellow"):
            img = pygame.image.load(f"assets/token_{p}.png").convert_alpha()
            self.token_images.append(pygame.transform.smoothscale(img, (30, 30)))

        # House/Hotel
        h = pygame.image.load("assets/house.png").convert_alpha()
        self.house_image = pygame.transform.smoothscale(h, (20, 20))
        h2 = pygame.image.load("assets/hotel.png").convert_alpha()
        self.hotel_image = pygame.transform.smoothscale(h2, (25, 25))

        # Dice
        self.dice_images = []
        for i in range(1, 7):
            d = pygame.image.load(f"assets/dice_{i}.png").convert_alpha()
            self.dice_images.append(pygame.transform.smoothscale(d, (40, 40)))

        # Font
        self.font = pygame.font.SysFont(None, 24)

    def _get_tile_pos(self, idx):
        size, edge = 800, 800//11
        if idx <= 10:
            return size-edge*(idx+1), size-edge
        if idx <= 20:
            return 0, size-edge*(idx-10)-edge
        if idx <= 30:
            return edge*(idx-20), 0
        return size-edge, edge*(idx-30)

    def _draw_board(self):
        self.screen.blit(self.board_image, (0, 0))

        # tokens
        for i, pl in enumerate(self.board.players):
            x,y = self._get_tile_pos(self.board.positions[i])
            self.screen.blit(self.token_images[i], (x+8*i, y+8*i))

        # houses/hotels
        for idx, sq in enumerate(self.board.squares):
            x,y = self._get_tile_pos(idx)
            if hasattr(sq, "house_count") and sq.house_count>0:
                for h in range(sq.house_count):
                    self.screen.blit(self.house_image, (x+5+12*h, y+5))
            if hasattr(sq, "hotel_count") and sq.hotel_count>0:
                self.screen.blit(self.hotel_image, (x+5, y+20))

        # dice
        d1,d2 = self.last_roll
        if d1>0:
            self.screen.blit(self.dice_images[d1-1], (10,10))
            self.screen.blit(self.dice_images[d2-1], (60,10))

        # move text
        if self.last_message:
            txt = self.font.render(self.last_message, True, (0,0,0))
            self.screen.blit(txt, (10,760))

        pygame.display.flip()

    def run(self):
        self._init_ui()
        running = True
        while running:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    running = False
                if ev.type == pygame.KEYDOWN and ev.key == pygame.K_SPACE:
                    self.last_roll = self.board.play_single_turn()
                    self.last_message = self.board.last_move_msg
                    if len(self.board.players) == 1:
                        self.last_message = f"🎉 {self.board.players[0]} wins! 🎉"
                        running = False

            self._draw_board()
            self.clock.tick(30)

        pygame.quit()

if __name__=="__main__":
    choice = input("Load saved game? (y/n): ")
    if choice.lower().startswith("y"):
        try:
            with open("savegame.pkl","rb") as f:
                game = pickle.load(f)
        except FileNotFoundError:
            num = int(input("Number of players? "))
            game = Game(num_players=num)
    else:
        num = int(input("Number of players? "))
        game = Game(num_players=num)

    game.run()
