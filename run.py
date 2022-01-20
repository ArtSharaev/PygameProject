from MyClasses.BoardClass import *
from MyClasses.PlayerClass import *
from MyClasses.WallClass import *
from MyClasses.ExitClass import *
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
    wall = Wall(10, 10, board)
    board.wall_sprite_group.add(wall)
    board.sprite_group.add(player)
    board.render(screen)  # первая отрисовка поля
    # clock = pygame.time.Clock()
    x = randint(10, 23)
    y = randint(0, 13)
    while board.board[y][x] != 0:
        x = randint(10, 23)
        y = randint(0, 13)
    exit = Exit(x, y, board)
    board.sprite_group.add(exit)
    running = True
    was_move = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # if event.type == pygame.MOUSEBUTTONDOWN:
            #     board.on_click(event.pos)
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
                    # pprint(board.board)
                    for ws in board.wall_sprite_group:
                        # проверка столкновения с одной из стен
                        if ws.check_collision():
                            player.kill()
                            print('Игрок столкнулся со стеной!')
                            running = False
                    if player.check_collision():
                        player.kill()
                        print('Переход на новый уровень!')
                        running = False
                    if movecount % 2 == 0 and choice([0, 1, 1, 1]):
                        # каждый второй ход с вероятностью 75%
                        # появляется новая стена в случайной не занятой клетке
                        x = randint(0, 23)
                        y = randint(0, 13)
                        while board.board[y][x] != 0:
                            x = randint(0, 23)
                            y = randint(0, 13)
                        wall = Wall(x, y, board)
                        board.wall_sprite_group.add(wall)
                    board.render(screen)  # новая отрисовка поля
                    was_move = False


        # keys = pygame.key.get_pressed()
        # # список всех нажатых клавиш в момент времени
        # if keys[pygame.K_r] and keys[pygame.K_t]:
        #     pass  # пасхалка, которую пока трогать не будем
        # if keys[pygame.K_UP]:
        #     player.update('up')
        # if keys[pygame.K_DOWN]:
        #     player.update('down')
        # if keys[pygame.K_RIGHT]:
        #     player.update('right')
        # if keys[pygame.K_LEFT]:
        #     player.update('left')
        # clock.tick(15)
        board.render(screen)
        pygame.display.flip()
