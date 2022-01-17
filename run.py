from MyClasses.BoardClass import *
from MyClasses.PlayerClass import *
from MyClasses.WallClass import *

if __name__ == '__main__':
    pygame.init()
    size = width, height = 1220, 720
    screen = pygame.display.set_mode(size)
    board = Board(24, 14, cell_size=50)  # поле 24х14 со стороной клетки 50пкс
    screen.fill((0, 0, 0))  # пока фон игры просто залит черным цветом
    player = Player(0, 0, board)
    wall1 = Wall(10, 10, board)
    wall2 = Wall(10, 11, board)
    wall3 = Wall(10, 12, board)
    board.sprite_group.add(player)
    board.sprite_group.add(wall1)
    board.sprite_group.add(wall2)
    board.sprite_group.add(wall3)
    board.render(screen)  # первая отрисовка поля
    # clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                board.on_click(event.pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    player.update('up')
                if event.key == pygame.K_DOWN:
                    player.update('down')
                if event.key == pygame.K_LEFT:
                    player.update('left')
                if event.key == pygame.K_RIGHT:
                    player.update('right')

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
