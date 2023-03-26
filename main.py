import pygame


SCREEN_WIDTH, SCREEN_HEIGHT = 1080, 720
FPS = 60

SCREEN_COLOR = (50, 50, 50)

BOARD_SIZE = 720
BOARD_AREA = BOARD_SIZE**2
BOARD_COLOR = (20, 20, 20)

BORDER_WIDTH = BOARD_SIZE // 12
BORDER_AREA = 4 * BOARD_SIZE * BORDER_WIDTH - 4 * BORDER_WIDTH**2
BORDER_COLOR = BOARD_COLOR

CARPET_COLOR = (40, 200, 90)

CELL_COUNT = 8**2
CELL_SIZE = ((BOARD_AREA - BORDER_AREA)**(1/2)) / CELL_COUNT**(1/2)
CELL_GAP = CELL_SIZE / 20

COORDINATES_SIZE = 20

class Game:
    def __init__(self):
        self.cells = (0) * CELL_COUNT

class Board:
    def __init__(self, screen):
        self.screen = screen

    def update(self):
        self.board = pygame.draw.rect(
            self.screen,
            BOARD_COLOR, (
                0,
                0,
                BOARD_SIZE,
                BOARD_SIZE
            )
        )

        self.border = pygame.draw.rect(
            self.screen,
            BORDER_COLOR, (
                0,
                0,
                BOARD_SIZE,
                BOARD_SIZE
            ),
            BORDER_WIDTH
        )

        self.carpet = pygame.draw.rect(
            self.screen,
            (0, 0, 0), (
                BORDER_WIDTH,
                BORDER_WIDTH,
                BOARD_SIZE - 2 * BORDER_WIDTH,
                BOARD_SIZE - 2 * BORDER_WIDTH
            )
        )

        self.cells = tuple(map(lambda id: (
            pygame.draw.rect(
                self.screen,
                CARPET_COLOR, (
                    BORDER_WIDTH + id % CELL_COUNT**(1/2) * CELL_SIZE + CELL_GAP / 2,
                    BORDER_WIDTH + id // CELL_COUNT**(1/2) * CELL_SIZE + CELL_GAP / 2,
                    CELL_SIZE - CELL_GAP,
                    CELL_SIZE - CELL_GAP
                )
            )
        ), range(CELL_COUNT)))

        for i in range(int(CELL_COUNT**(1/2) * 4)):
            content = chr(ord('A') + i % int(CELL_COUNT**(1/2))) if i // int(CELL_COUNT**(1/2) * 2) == 0 else str(i % int(CELL_COUNT**(1/2)) + 1)
            text = font.get_rect(content, size=COORDINATES_SIZE)
            x = BORDER_WIDTH + (CELL_SIZE * (i % int(CELL_COUNT**(1/2)) + 1)) - CELL_SIZE / 2
            y = BORDER_WIDTH / 2 if i // int(CELL_COUNT**(1/2)) == 0 or i // int(CELL_COUNT**(1/2)) == 2 else BOARD_SIZE - BORDER_WIDTH / 2
            font.render_to(
                screen, (
                    x - text.x / 2 - (3/2) * CELL_GAP,
                    y - text.y / 2 - (1/2) * CELL_GAP
                ) if i // int(CELL_COUNT**(1/2) * 2) == 0 else (
                    y - text.x / 2 - (3/2) * CELL_GAP,
                    x - text.y / 2 - (1/2) * CELL_GAP
                ),
                content,
                (255, 255, 255),
                size=COORDINATES_SIZE
            )

class Racket:
    def __init__(self, screen, coordinates):
        self.screen = screen
        self.speed = 4
        
        self.x, self.y = coordinates

    def update(self):
        self.rect = pygame.draw.circle(self.screen, (255, 255, 255), (self.x, self.y), 20)

    def up(self):
        self.y -= self.speed
 
    def down(self):
        self.y += self.speed


pygame.init()

pygame.font.init()
font = pygame.freetype.SysFont(pygame.font.get_default_font(), 30)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Othello')
clock = pygame.time.Clock() 

board = Board(screen)
squash = Racket(screen, (50, 50))

while True:
    screen.fill(SCREEN_COLOR)
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_UP]:
        squash.up()
    if keys[pygame.K_DOWN]:
        squash.down()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    board.update()
    
    clock.tick(FPS)
    pygame.display.update()

pygame.quit()
