from MyClasses.BoardClass import *
from MyClasses.PlayerClass import *
from MyClasses.WallClass import *
from MyClasses.ExitClass import *
from MyClasses.HunterClass import *
from random import randint, choice
from pprint import pprint

SIZE = 1220, 750
level = 1
FPS = 60
BEST_RESULT_FILE = 'data_files/best_result.txt'
cell_color = (93, 161, 48)


def set_best_result(file, value):
    with open(file, 'w', encoding='utf-8') as text:
        text.write(str(value))


def get_best_result(file):
    with open(file, encoding='utf-8') as text:
        return text.readline()


def change_color(r, g, b):
        if board.cell_color[0] < r:
            board.set_cell_color(screen, (board.cell_color[0] + 1,
                                          board.cell_color[1],
                                          board.cell_color[2]))
        elif board.cell_color[0] > r:
            board.set_cell_color(screen, (board.cell_color[0] - 1,
                                          board.cell_color[1],
                                          board.cell_color[2]))
        if board.cell_color[1] < g:
            board.set_cell_color(screen, (board.cell_color[0],
                                          board.cell_color[1] + 1,
                                          board.cell_color[2]))
        elif board.cell_color[1] > g:
            board.set_cell_color(screen, (board.cell_color[0],
                                          board.cell_color[1] - 1,
                                          board.cell_color[2]))
        if board.cell_color[2] < b:
            board.set_cell_color(screen, (board.cell_color[0],
                                          board.cell_color[1],
                                          board.cell_color[2] + 1))
        elif board.cell_color[2] > b:
            board.set_cell_color(screen, (board.cell_color[0],
                                          board.cell_color[1],
                                          board.cell_color[2] - 1))


def start_new_level(level):
    global movecount, board, screen, clock, player, crash_waiting
    pygame.init()
    pygame.display.set_caption('PygameProject')
    movecount = 0
    crash_waiting = False
    if level > int(get_best_result(BEST_RESULT_FILE)):
        set_best_result(BEST_RESULT_FILE, level)
    screen = pygame.display.set_mode(SIZE)
    font = pygame.font.Font(None, 30)
    level_text = font.render('Уровень - ' + str(level), True, (200, 200, 200))
    best_result_text = font.render('Рекорд - ' +
                                   get_best_result(BEST_RESULT_FILE),
                                   True, (200, 200, 200))
    screen.blit(level_text, (450, 720))
    screen.blit(best_result_text, (650, 720))
    board = Board(24, 14, cell_color=cell_color, cell_size=50)
    player = Player(0, 0, board)
    board.sprite_group.add(player)
    x = randint(10, 23)
    y = randint(0, 13)
    while board.board[y][x] != 0:
        x = randint(10, 23)
        y = randint(0, 13)
    exit = Exit(x, y, board)
    board.sprite_group.add(exit)
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
        x = randint(0, 23)
        y = randint(0, 13)
        while board.board[y][x] != 0:
            x = randint(0, 23)
            y = randint(0, 13)
        wall = Wall(9, 9, x, y, board)
        board.wall_sprite_group.add(wall)
    clock = pygame.time.Clock()
    board.render(screen)  # первая отрисовка поля


if __name__ == '__main__':
    start_new_level(level)
    running = True
    was_move = False

    while running:
        if level == 1:
            change_color(93, 161, 48)
            cell_color = (93, 161, 48)
        elif level == 2:
            change_color(158, 178, 93)
            cell_color = (158, 178, 93)
        elif level == 3:
            change_color(187, 10, 33)
            cell_color = (187, 10, 33)
        elif level == 4:
            change_color(237, 255, 113)
            cell_color = (237, 255, 113)
        elif level == 5:
            change_color(241, 219, 75)
            cell_color = (241, 219, 75)
        elif level == 6:
            change_color(75, 136, 162)
            cell_color = (75, 136, 162)
        elif level == 7:
            change_color(167, 198, 218)
            cell_color = (167, 198, 218)
        elif level == 8:
            change_color(241, 153, 83)
            cell_color = (241, 153, 83)
        elif level == 9:
            change_color(86, 53, 30)
            cell_color = (86, 53, 30)
        elif level == 10:
            change_color(196, 115, 53)
            cell_color = (196, 115, 53)
        elif level == 11:
            change_color(38, 96, 164)
            cell_color = (38, 96, 164)
        elif level == 12:
            change_color(171, 155, 150)
            cell_color = (171, 155, 150)
        elif level == 13:
            change_color(196, 110, 110)
            cell_color = (196, 110, 110)
        elif level == 14:
            change_color(166, 58, 80)
            cell_color = (166, 58, 80)
        elif level == 15:
            change_color(37, 38, 39)
            cell_color = (37, 38, 39)
        elif level == 16:
            change_color(159, 184, 173)
            cell_color = (159, 184, 173)
        elif level == 17:
            change_color(71, 88, 65)
            cell_color = (71, 88, 65)
        elif level == 18:
            change_color(63, 64, 63)
            cell_color = (63, 64, 63)

        for hs in board.hunter_sprite_group:
            hs.update(player.matrix_coords, False)
            if hs.cur_frame == 81 and hs.collided == 'player':
                start_new_level(level)
        for ws in board.wall_sprite_group:
            if ws.collided == 'player':
                ws.update()
                if ws.cur_frame == 80:
                    start_new_level(level)
            if ws.collided == 'hunter':
                ws.update()
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
                                        board.board[wallsprite.matrix_coords[0]][wallsprite.matrix_coords[1]] = 3
                                        hs.kill()
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
                        # pprint(board.board)
                        was_move = False
        clock.tick(FPS)
        board.render(screen)  # новая отрисовка поля
        pygame.display.flip()
