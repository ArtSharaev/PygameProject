from MyClasses.BoardClass import *
from MyClasses.PlayerClass import *
from MyClasses.WallClass import *
from MyClasses.ExitClass import *
from MyClasses.HunterClass import *
from random import randint, choice
from pprint import pprint

if __name__ == '__main__':
    pygame.init()
    movecount = 0
    size = width, height = 1220, 720
    screen = pygame.display.set_mode(size)
    board = Board(24, 14, cell_size=50)  # поле 24х14 со стороной клетки 50пкс
    screen.fill((0, 0, 0))  # пока фон игры просто залит черным цветом
    player = Player(0, 0, board)
    board.sprite_group.add(player)
    wall = Wall(9, 9, 10, 10, board)
    board.wall_sprite_group.add(wall)
    hunter = Hunter(9, 9, 15, 6, board)
    board.hunter_sprite_group.add(hunter)
    x = randint(10, 23)
    y = randint(0, 13)
    while board.board[y][x] != 0:
        x = randint(10, 23)
        y = randint(0, 13)
    exit = Exit(x, y, board)
    board.sprite_group.add(exit)
    clock = pygame.time.Clock()
    board.render(screen)  # первая отрисовка поля

    running = True
    was_move = False
    while running:
        for hs in board.hunter_sprite_group:
            hs.update(player.matrix_coords, was_move)
        for ws in board.wall_sprite_group:
            ws.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    player.update('up')
                    was_move = True
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    player.update('down')
                    was_move = True
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    player.update('left')
                    was_move = True
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    player.update('right')
                    was_move = True
                if was_move:
                    movecount += 1  # счетчик ходов
                    for hs in board.hunter_sprite_group:
                        hs.update(player.matrix_coords, was_move)
                    for wallsprite in board.wall_sprite_group:
                        # проверка столкновения с одной из стен
                        if wallsprite.check_collision():
                            print('Игрок столкнулся со стеной!')
                    if player.check_collision():
                        print('Переход на новый уровень!')
                    if movecount % 2 == 0 and choice([0, 1, 1, 1]):
                        # каждый второй ход с вероятностью 75%
                        # появляется новая стена в случайной не занятой клетке
                        x = randint(0, 23)
                        y = randint(0, 13)
                        while board.board[y][x] != 0:
                            x = randint(0, 23)
                            y = randint(0, 13)
                        wall = Wall(9, 9, x, y, board)
                        board.wall_sprite_group.add(wall)
                    if movecount % 3 == 0 and choice([0, 0, 0, 0, 1]):
                        # каждый третий ход с вероятностью 25%
                        # появляется новый охотник в случайной не занятой клетке
                        x = randint(0, 23)
                        y = randint(0, 13)
                        while board.board[y][x] != 0:
                            x = randint(0, 23)
                            y = randint(0, 13)
                        hunter = Hunter(9, 9, x, y, board)
                        board.hunter_sprite_group.add(hunter)
                    pprint(board.board)
                    board.render(screen)  # новая отрисовка поля
                    was_move = False
        clock.tick(50)
        board.render(screen)
        pygame.display.flip()
