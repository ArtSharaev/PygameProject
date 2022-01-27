from MyClasses.BoardClass import *
from MyClasses.PlayerClass import *
from MyClasses.WallClass import *
from MyClasses.ExitClass import *
from MyClasses.HunterClass import *
from random import randint, choice
from pprint import pprint

SIZE = 1220, 720
level = 1
FPS = 120


def start_new_level(level):
    global movecount, board, screen, clock, player, crash_waiting
    pygame.init()
    pygame.display.set_caption('Уровень ' + str(level))
    movecount = 0
    crash_waiting = False
    screen = pygame.display.set_mode(SIZE)
    board = Board(24, 14, cell_size=50)  # поле 24х14 со стороной клетки 50пкс
    # screen.fill((0, 0, 0))  # пока фон игры просто залит черным цветом
    player = Player(0, 0, board)
    board.sprite_group.add(player)
    wall = Wall(9, 9, 10, 10, board)
    board.wall_sprite_group.add(wall)
    for _ in range(level):
        x = randint(0, 23)
        y = randint(0, 13)
        while board.board[y][x] != 0:
            x = randint(0, 23)
            y = randint(0, 13)
        hunter = Hunter(9, 9, x, y, board)
        board.hunter_sprite_group.add(hunter)
    x = randint(10, 23)
    y = randint(0, 13)
    while board.board[y][x] != 0:
        x = randint(10, 23)
        y = randint(0, 13)
    exit = Exit(x, y, board)
    board.sprite_group.add(exit)
    if level >= 5:
        screen.fill((255, 0, 0))
    elif level >= 10:
        screen.fill((0, 255, 0))
    elif level >= 15:
        screen.fill((0, 0, 255))
    clock = pygame.time.Clock()
    board.render(screen)  # первая отрисовка поля


if __name__ == '__main__':
    start_new_level(level)
    running = True
    was_move = False

    while running:
        for hs in board.hunter_sprite_group:
            hs.update(player.matrix_coords, False)
            if hs.cur_frame == 81 and hs.collided == 'player':
                start_new_level(level)
        for ws in board.wall_sprite_group:
            ws.update()
            if ws.cur_frame == 80 and ws.collided == 'player':
                start_new_level(level)
        if not crash_waiting:
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
                        if player.check_collision():  # переход на новый уровень
                            level += 1
                            start_new_level(level)

                        for huntersprite in board.hunter_sprite_group:
                            # проверка столкновения перед передвижением
                            if huntersprite.check_collision() == 'player':
                                while level % 5 != 0 and level > 1:
                                    level -= 1
                                player.kill()
                                crash_waiting = True
                            huntersprite.update(player.matrix_coords, True)
                            # проверка столкновения после передвижения
                            if huntersprite.check_collision() == 'player':
                                while level % 5 != 0 and level > 1:
                                    level -= 1
                                player.kill()
                                crash_waiting = True

                        for wallsprite in board.wall_sprite_group:
                            # проверка столкновения с одной из стен
                            if wallsprite.check_collision() == 'player':
                                while level % 5 != 0 and level != 1:
                                    level -= 1
                                player.kill()
                                crash_waiting = True
                            elif wallsprite.check_collision() == 'hunter':
                                for hs in board.hunter_sprite_group:
                                    if hs.matrix_coords == wallsprite.matrix_coords:
                                        hs.kill()
                                        break
                        # каждый второй ход с вероятностью 75%
                        # появляется новая стена
                        # в случайной не занятой клетке
                        if movecount % 2 == 0 and choice([0, 1, 1, 1]):
                            x = randint(0, 23)
                            y = randint(0, 13)
                            while board.board[y][x] != 0:
                                x = randint(0, 23)
                                y = randint(0, 13)
                            wall = Wall(9, 9, x, y, board)
                            board.wall_sprite_group.add(wall)
                        # каждый третий ход с вероятностью 25%
                        # появляется новый охотник
                        # в случайной не занятой клетке
                        if movecount % 3 == 0 and choice([0, 0, 0, 1]):
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
        clock.tick(FPS)
        board.render(screen)
        pygame.display.flip()
