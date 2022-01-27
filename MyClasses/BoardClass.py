"""
Класс игрового поля - доски произвольных размеров,
на которой будут происходить игровые события.
Коды объектов на доске.
Игрок - 1
Выход - 2
Стена - 3
Охранник - 4
Охотник - 5
"""


import pygame


class Board:
    """Класс игровой доски - поля"""
    def __init__(self, width, height, cell_color='#5DA130', cell_size=75, indleft=10, indtop=10):
        # ширина и и высота в пкс
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.cell_color = cell_color
        # отступы игрового поля от самого экрана
        self.indleft = indleft
        self.indtop = indtop
        # матрица со значениями клеток поля
        self.board = [[0] * width for _ in range(height)]
        self.sprite_group = pygame.sprite.Group()
        self.wall_sprite_group = pygame.sprite.Group()
        self.hunter_sprite_group = pygame.sprite.Group()

    def render_cell(self, screen, x, y, color, border, value):
        # функция отрисовывает клетку, вставляется в цикл в функции render
        pygame.draw.rect(screen, color, (x, y, self.cell_size, self.cell_size),
                         border)
        if value == 1:  # игрок
            pass

    def set_cell_color(self, screen, color):
        self.cell_color = color
        self.render(screen)

    def render(self, screen):
        # функция заново отрисовывает все окно
        for h in range(self.height):
            for w in range(self.width):
                # координаты клетки в пкс
                x = self.indleft + w * self.cell_size
                y = self.indtop + h * self.cell_size
                self.render_cell(screen, x, y, self.cell_color, 0,
                                 self.board[h][w])
                # self.render_cell(screen, x, y, '#ffff00', 1, self.board[h][w])
        self.sprite_group.draw(screen)
        self.wall_sprite_group.draw(screen)
        self.hunter_sprite_group.draw(screen)
