import pygame
from pygame.locals import *
import random


SCREEN_WIDTH, SCREEN_HEIGHT = 1080, 720
FPS = 60

SCREEN_COLOR = (50, 50, 50)

BOARD_SIZE = 720
BOARD_AREA = BOARD_SIZE**2
BOARD_COLOR = (20, 20, 20)

BOARD_BORDER_WIDTH = BOARD_SIZE // 12
BOARD_BORDER_AREA = 4 * BOARD_SIZE * BOARD_BORDER_WIDTH - 4 * BOARD_BORDER_WIDTH**2
BOARD_BORDER_COLOR = BOARD_COLOR

BOARD_CARPET_COLOR = (40, 200, 90)

CELL_SIZE = ((BOARD_AREA - BOARD_BORDER_AREA)**(1/2)) / 8
CELL_GAP = 4


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
            BOARD_BORDER_COLOR, (
                0,
                0,
                BOARD_SIZE,
                BOARD_SIZE
            ),
            BOARD_BORDER_WIDTH
        )

        self.carpet = pygame.draw.rect(
            self.screen,
            (0, 0, 0), (
                BOARD_BORDER_WIDTH,
                BOARD_BORDER_WIDTH,
                BOARD_SIZE - 2 * BOARD_BORDER_WIDTH,
                BOARD_SIZE - 2 * BOARD_BORDER_WIDTH
            )
        )

        self.cells = tuple(map(lambda id: (
            pygame.draw.rect(
                self.screen,
                BOARD_CARPET_COLOR, (
                    BOARD_BORDER_WIDTH + id % 8 * CELL_SIZE + CELL_GAP / 2,
                    BOARD_BORDER_WIDTH + id // 8 * CELL_SIZE + CELL_GAP / 2,
                    CELL_SIZE - CELL_GAP,
                    CELL_SIZE - CELL_GAP
                )
            )
        ), range(64)))

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Othello')
clock = pygame.time.Clock() 

board = Board(screen)

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