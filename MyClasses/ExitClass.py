"""
Класс объекта - выхода, столкнувшись с которым,
игрок переходит на следующий уровень.
На матрице доски выход обозначается цифрой 2
"""

import pygame


class Exit(pygame.sprite.Sprite):
    image = pygame.image.load('Sprites/exit.png')

    def __init__(self, x, y, boardclass, *group):
        super().__init__(*group)
        self.boardclass = boardclass
        self.image = Exit.image
        self.rect = self.image.get_rect()
        self.rect.x = x * self.boardclass.cell_size + self.boardclass.indleft
        self.rect.y = y * self.boardclass.cell_size + self.boardclass.indleft
        self.matrix_coords = [y, x]
        self.boardclass.board[self.matrix_coords[0]][self.matrix_coords[1]] = 2

    def set_coords(self, matrix_coords):
        self.matrix_coords = matrix_coords
        self.boardclass.board[self.matrix_coords[0]][
            self.matrix_coords[1]] = 1
        x = self.matrix_coords[1] * self.boardclass.cell_size\
            + self.boardclass.indleft
        y = self.matrix_coords[0] * self.boardclass.cell_size\
            + self.boardclass.indtop
        self.rect.x = x
        self.rect.y = y