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
    def __init__(self, width, height, cell_size=75, indleft=10, indtop=10):
        # ширина и и высота в пкс
        self.width = width
        self.height = height
        self.cell_size = cell_size
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

    def render(self, screen):
        # функция заново отрисовывает все окно
        for h in range(self.height):
            for w in range(self.width):
                # координаты клетки в пкс
                x = self.indleft + w * self.cell_size
                y = self.indtop + h * self.cell_size
                self.render_cell(screen, x, y, '#5DA130', 0, self.board[h][w])
                # self.render_cell(screen, x, y, '#ffff00', 1, self.board[h][w])
        self.sprite_group.draw(screen)
        self.wall_sprite_group.draw(screen)
        self.hunter_sprite_group.draw(screen)

    # def get_cell_coords(self, mouse_pos):
    #     # функция возвращает координаты клетки на поле
    #     mouse_pos_x = mouse_pos[0]
    #     mouse_pos_y = mouse_pos[1]
    #     x = (mouse_pos_x - self.indleft) // self.cell_size
    #     y = (mouse_pos_y - self.indtop) // self.cell_size
    #     if x >= self.width or y >= self.height or y < 0 or x < 0:
    #         return None
    #     return x, y

    # def on_click(self, mouse_pos):
    #     # после клика по экрану
    #     cell_coords = self.get_cell_coords(mouse_pos)
    #     if cell_coords:
    #         self.change_cell_value(cell_coords, 4)
