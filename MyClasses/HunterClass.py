import pygame


class Hunter(pygame.sprite.Sprite):
    image = pygame.image.load('Sprites/hunter.png')

    def __init__(self, columns, rows, x, y, boardclass):
        self.boardclass = boardclass
        super().__init__()
        self.frames = []
        self.cut_sheet(Hunter.image, columns, rows)
        self.cur_frame = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        """Функция для обрезки листа с кадрами"""
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        self.cur_frame = (self.cur_frame + 1) % len(self.frames)
        self.image = self.frames[self.cur_frame]