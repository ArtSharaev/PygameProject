"""
Класс объектов - стен, столкнувшись с которыми игрок умирает.
Стены не двигаются, при переходе на новый уровень они отрисовываются заново.
Охотники будут должны двигаться, обходя стены.
Стена занимает одну клетку поля и может быть продлена засчет
других экземпляров данного класса.
На матрице доски стена обозначается цифрой 3
"""

import pygame


class Wall(pygame.sprite.Sprite):
    image = pygame.image.load('Sprites/wall.png')

    def __init__(self, x, y, boardclass, *group):
        super().__init__(*group)
        self.matrix_coords = [x, y]
        self.boardclass = boardclass
        self.image = Wall.image
        self.rect = self.image.get_rect()
        self.rect.x = x * self.boardclass.cell_size + self.boardclass.indleft
        self.rect.y = y * self.boardclass.cell_size + self.boardclass.indleft
        self.matrix_coords = [y, x]
        self.boardclass.board[self.matrix_coords[0]][self.matrix_coords[1]] = 3