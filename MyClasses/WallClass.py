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
    general_image = pygame.image.load('Sprites/wall.png')
    crash_image = pygame.image.load('Sprites/crash.png')

    def __init__(self, columns, rows, x, y, boardclass, *group):
        super().__init__(*group)
        self.boardclass = boardclass
        self.frames = []
        self.cut_sheet(Wall.crash_image, columns, rows)
        self.cur_frame = 0
        self.image = Wall.general_image
        self.rect = self.image.get_rect()
        self.rect.x = x * self.boardclass.cell_size + self.boardclass.indleft
        self.rect.y = y * self.boardclass.cell_size + self.boardclass.indleft
        self.matrix_coords = [y, x]
        self.boardclass.board[self.matrix_coords[0]][self.matrix_coords[1]] = 3

    def check_collision(self):
        # проверка того, врезался ли игрок в стену
        if (self.boardclass.board[self.matrix_coords[0]][self.matrix_coords[1]]
                == 1):
            self.boardclass.board[self.matrix_coords[0]][self.matrix_coords[1]]\
                = 3
            if self.cur_frame == 0:
                self.cur_frame = 1
            return True
        return False

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

    def update(self):
        if self.cur_frame == 0:  # когда стоит спрайт стены
            pass
        else:
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame - 1]
            if self.cur_frame == 80:
                self.kill()
