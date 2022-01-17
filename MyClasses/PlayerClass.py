"""
Класс объекта - игрока, которым будет управлять пользователь.
Игрок занимает одну клетку поля.
На матрице доски игрок обозначается цифрой 1
"""


import pygame
from pprint import *


class Player(pygame.sprite.Sprite):
    image = pygame.image.load('Sprites/player.png')

    def __init__(self, x, y, boardclass, *group):
        super().__init__(*group)
        self.matrix_coords = [x, y]
        self.boardclass = boardclass
        self.image = Player.image
        self.rect = self.image.get_rect()
        self.rect.x = x * self.boardclass.cell_size + self.boardclass.indleft
        self.rect.y = y * self.boardclass.cell_size + self.boardclass.indleft
        self.matrix_coords = [y, x]
        self.boardclass.board[self.matrix_coords[0]][self.matrix_coords[1]] = 1

    def check_collision(self):
        # проверка того, достиг ли игрок выхода
        if(self.boardclass.board[self.matrix_coords[0]][self.matrix_coords[1]]
                == 2):
            return True
        return False

    def update(self, key):
        self.boardclass.board[self.matrix_coords[0]][self.matrix_coords[1]] = 0
        if key == 'up':
            self.matrix_coords[0] -= 1
            if self.matrix_coords[0] < 0:
                self.matrix_coords[0] = self.boardclass.height - 1
        elif key == 'down':
            self.matrix_coords[0] += 1
            if self.matrix_coords[0] >= self.boardclass.height:
                self.matrix_coords[0] = 0
        elif key == 'left':
            self.matrix_coords[1] -= 1
            if self.matrix_coords[1] < 0:
                self.matrix_coords[1] = self.boardclass.height - 1
        elif key == 'right':
            self.matrix_coords[1] += 1
            if self.matrix_coords[1] >= self.boardclass.width:
                self.matrix_coords[1] = 0
        x = self.matrix_coords[1] * self.boardclass.cell_size\
            + self.boardclass.indleft
        y = self.matrix_coords[0] * self.boardclass.cell_size\
            + self.boardclass.indtop
        if not self.check_collision():
            self.boardclass.board[self.matrix_coords[0]][
                self.matrix_coords[1]] = 1
            self.rect.x = x
            self.rect.y = y
        else:
            print('Игрок достиг выхода!')