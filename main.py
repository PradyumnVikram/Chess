#run this to run project
__author__ = 'Pradyumn Vikram'
#This be the file for the gameplay and displaying stuff

#some imports
import pygame
import Chess as chess #this is the file we made which controls logic
import os

#Declaring some(ALOT) of variables
root = os.path.dirname(__file__)

pygame.init()
n_size = 8
BLACK = (193, 154, 107)
WHITE = (255, 255, 255)
FONT = pygame.font.SysFont('comicsans', 30)

WIDTH = 40
HEIGHT = 40
win_size = (390, 420)

pygame.display.set_caption('Chess')
win = pygame.display.set_mode(win_size)
MARGIN = 8

#loading images of chess pieces
imgs = {}

for file in os.listdir(os.path.join(root, 'data/')):
    imgs[file[:-4]
         ] = pygame.image.load((os.path.join(root, 'data', file))).convert()

players = {'w': 'White', 'b': 'Black'}

#declaring redraw window function
def redraw_window(screen, grid, player, text):
    win.fill((160, 82, 45))
    win.blit(text, (WIDTH - text.get_width() + 200, 395))
    for row in range(n_size):
        for col in range(n_size):
            color = WHITE
            '''
            if row % 2 == 0:
                if col % 2 != 0:
                    color = BLACK
            elif row % 2 != 0:
                if col % 2 == 0:
                    color = BLACK '''
            if grid[row][col] in imgs.keys():
                img = imgs[grid[row][col]]
                img = pygame.transform.scale(img, (WIDTH, HEIGHT))
                rect = img.get_rect()
                rect.x = ((MARGIN + WIDTH)*col + MARGIN)
                rect.y = ((MARGIN + HEIGHT)*row + MARGIN)

                screen.blit(img, rect)
            else:
                pygame.draw.rect(win, color, [(MARGIN + WIDTH)*col + MARGIN,
                                              (MARGIN + HEIGHT)*row + MARGIN,
                                              WIDTH,
                                              HEIGHT])
    pygame.display.flip()
    pygame.display.update()

#converting click to board co-ordinate
def get_col_row(board):
    pos = pygame.mouse.get_pos()
    col = pos[0]//(WIDTH+MARGIN)
    row = pos[1]//(HEIGHT+MARGIN)
    try:
        return [row, col]

    except IndexError as e:
        pass

#main function... Duh!
def main():
    #declaring variables (Again)
    clock = pygame.time.Clock()
    run = True
    board = chess.new_board()
    player = 'w'
    count = 0
    text = FONT.render('White\'s turn!', 1, (10, 10, 10))
    #running the game
    while run:
        clock.tick(60)
        redraw_window(win, board, player, text)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                try:
                    run = False
                    pygame.quit()
                except Exception as e:
                    run = False
                    pygame.quit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                board = chess.new_board()
                player = 'w'
                
                text = FONT.render(
                    players[player] + '\'s turn!', 1, (10, 10, 10))
                redraw_window(win, board, player, text)
            if pygame.mouse.get_pressed()[0]:
                text = FONT.render(
                    players[player] + '\'s turn!', 1, (10, 10, 10))
                print(player)
                try:
                    count += 1

                    if count % 2 != 0:
                        start = get_col_row(board)
                        if player == 'w':
                            player = 'b'
                        elif player == 'b':
                            player = 'w'
                        if board[start[0]][start[1]] == 'es' or board[start[0]][start[1]][0] == player:
                            start = None
                            count += 1
                            if player == 'w':
                                player = 'b'
                            elif player == 'b':
                                player = 'w'
                        #('start', start)

                    elif count % 2 == 0:
                        finish = get_col_row(board)
                        #('finish', finish)
                        if count != False:
                            board, count = chess.move(board, start, finish, count)
                        else:
                            count += 1
                            if player == 'w':
                                player = 'b'
                            elif player == 'b':
                                player = 'w'

                        ans = chess.won(board)
                        print(ans)
                        if ans != False:
                            text = FONT.render(
                                ans, 1, (10, 10, 10))
                            win.blit(text, (WIDTH - text.get_width() + 200, 395))
                            run = False

                except Exception as e:
                    count -= 1
                    pass

    pygame.quit()

#finally putting everything together and running the magic!
main()
