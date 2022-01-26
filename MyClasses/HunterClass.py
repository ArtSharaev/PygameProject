"""
Класс объектов - охотников, столкнувшись с которыми игрок умирает.
Охотники пытаются догнать игрока, двигаясь за ним каждый его ход.
В приоритете у охотников движение по вертикали, при этом они должны обходить стены.
На матрице доски стена обозначается цифрой 5
"""

import pygame


class Hunter(pygame.sprite.Sprite):
    image_right = pygame.image.load('Sprites/right_hunter.png')
    image_left = pygame.image.load('Sprites/left_hunter.png')
    crash_image = pygame.image.load('Sprites/crash.png')

    def __init__(self, columns, rows, x, y, boardclass, *group):
        super().__init__(*group)
        self.boardclass = boardclass
        self.frames = [Hunter.image_right, Hunter.image_left]
        self.cut_sheet(Hunter.crash_image, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.prev_object = 0
        self.rect = self.image.get_rect()
        self.rect.x = x * self.boardclass.cell_size + self.boardclass.indleft
        self.rect.y = y * self.boardclass.cell_size + self.boardclass.indleft
        self.matrix_coords = [y, x]
        self.boardclass.board[self.matrix_coords[0]][self.matrix_coords[1]] = 5
        self.notcollision = True

    def cut_sheet(self, sheet, columns, rows):
        """Функция для обрезки листа с кадрами"""
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                if j < rows - 1:
                    frame_location = (self.rect.w * i, (self.rect.h + 2) * j)
                else:
                    frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def check_collision(self, player_matrix_coords):
        # проверка того, догнал ли охотник игрока
        px = player_matrix_coords[1]
        py = player_matrix_coords[0]
        if px == self.matrix_coords[1] and py == self.matrix_coords[0]:
            return True
        elif (self.boardclass.board[self.matrix_coords[0]][self.matrix_coords[1]]
                == 3):
            return True
        return False

    def update(self, player_matrix_coords, was_move):
        if self.notcollision:
            if self.check_collision(player_matrix_coords):
                self.cur_frame = 2
                self.notcollision = False
                return 1
            if was_move:
                if self.notcollision:
                    px = player_matrix_coords[1]
                    py = player_matrix_coords[0]
                    hx = self.matrix_coords[1]
                    hy = self.matrix_coords[0]
                    self.boardclass.board[self.matrix_coords[0]][
                        self.matrix_coords[1]] = self.prev_object
                    if hy < py:
                        self.matrix_coords[0] += 1
                    elif hy > py:
                        self.matrix_coords[0] -= 1
                    elif hx < px:
                        self.cur_frame = 1
                        self.matrix_coords[1] += 1
                    elif hx > px:
                        self.cur_frame = 0
                        self.matrix_coords[1] -= 1
                    x = self.matrix_coords[1] * self.boardclass.cell_size \
                        + self.boardclass.indleft
                    y = self.matrix_coords[0] * self.boardclass.cell_size \
                        + self.boardclass.indtop
                    self.rect.x = x
                    self.rect.y = y
                    print(self.prev_object)
                    self.prev_object = self.boardclass.board[self.matrix_coords[0]][self.matrix_coords[1]]
                    self.boardclass.board[self.matrix_coords[0]][
                        self.matrix_coords[1]] = 5
                    if self.check_collision(player_matrix_coords):
                        self.cur_frame = 2
                        self.notcollision = False
                        return 1
        if self.cur_frame == 0:
            self.image = Hunter.image_left
        elif self.cur_frame == 1:
            self.image = Hunter.image_right
        else:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]
            if self.cur_frame == 81:
                self.kill()
                return True
