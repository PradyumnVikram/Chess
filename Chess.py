__author__ = 'Pradyumn Vikram'
#This file be the brains of the game
#All logic and controls in this file

#function to make new board
def new_board():
    board = [['br', 'bh', 'bb', 'bq', 'bk', 'bb', 'bh', 'br'],
             ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
             ['es', 'es', 'es', 'es', 'es', 'es', 'es', 'es'],
             ['es', 'es', 'es', 'es', 'es', 'es', 'es', 'es'],
             ['es', 'es', 'es', 'es', 'es', 'es', 'es', 'es'],
             ['es', 'es', 'es', 'es', 'es', 'es', 'es', 'es'],
             ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
             ['wr', 'wh', 'wb', 'wq', 'wk', 'wb', 'wh', 'wr']]
    return board

#check if someone won
def won(board):
    val = 0
    for row in board:
        for piece in row:
            if piece == 'bk':
                val += 1
            if piece == 'wk':
                val -= 1
    if val == 0:
        return False
    elif val == 1:
        return 'White won!'
    elif val == -1:
        return 'Black won!'

#move the piece
def move(board, start, finish, count):
    if start != None:
        diffx = start[0] - finish[0]
        diffy = start[1] - finish[1]
        piece = board[start[0]][start[1]]
        if is_valid(board, piece, start, finish):
            if start == finish:
                board[start[0] + diffx][start[1] + diffy] = 'es'
            else:
                board[start[0]][start[1]] = 'es'
            board[finish[0]][finish[1]] = piece
    return board, count

# check for:
# bishop - b
# horse - h
# king - k
# queen - q
# rook - r
# pawn - p

#check if move is valid... used in move()
def is_valid(board, piece, start, finish):
    if piece[1] == 'p':
        if abs(finish[0] - start[0]) == 1 and board[finish[0]][finish[1]] == 'es':
            if finish[1] == start[1]:
                if piece[0] == 'b' and finish[0] > start[0]:
                    return True
                elif piece[0] == 'w' and finish[0] < start[0]:
                    return True
        elif abs(finish[1] - start[1]) == 1 and abs(finish[0] - start[0]) == 1 and board[finish[0]][finish[1]] != 'es' and board[finish[0]][finish[1]][0] != piece[0]:
            #('in', board[finish[0]][finish[1]])
            if piece[0] == 'b' and finish[0] > start[0]:
                return True
            elif piece[0] == 'w' and finish[0] < start[0]:
                return True

    if piece[1] == 'h':
        if board[finish[0]][finish[1]][0] != piece[0]:
            if abs(start[0] - finish[0]) == 2 and abs(start[1] - finish[1]) == 1:
                return True
            if abs(start[0] - finish[0]) == 1 and abs(start[1] - finish[1]) == 2:
                return True
    if piece[1] == 'k':
        if board[finish[0]][finish[1]][0] != piece[0]:
            if abs(start[0] - finish[0]) == 1 and abs(start[1] - finish[1]) == 1:
                return True
            elif abs(start[0] - finish[0]) == 0 and abs(start[1] - finish[1]) == 1:
                return True
            elif abs(start[0] - finish[0]) == 1 and abs(start[1] - finish[1]) == 0:
                return True
            elif abs(start[0] - finish[0]) == 0 and abs(start[1] - finish[1]) == 0:
                return True
    if piece[1] == 'q':
        if board[finish[0]][finish[1]][0] != piece[0]:
            if start[0] == finish[0] or start[1] == finish[1]:
                if start[0] == finish[0]:
                    if start[1] < finish[1]:
                        for col in range(start[1]+1, finish[1]+1):
                            if board[start[0]][col] != 'es':
                                return False
                        return True
                    else:
                        for col in range(finish[1]+1, start[1]-1):
                            if board[start[0]][col] != 'es':
                                return False
                        return True
                elif start[1] == finish[1]:
                    if start[0] < finish[0]:
                        for row in range(start[0]+1, finish[0]+1):
                            if board[row][start[1]] != 'es':
                                return False
                        return True

                    else:
                        for row in range(finish[0]+1, start[0]-1):
                            if board[row][start[1]] != 'es':
                                return False
                        return True
            else:
                if start[1] < finish[1]:
                    if start[0] < finish[0]:
                        while start != finish:
                            start[0] += 1
                            start[1] += 1
                            # (start)
                            if board[start[0]][start[1]] != 'es':
                                if start == finish and board[start[0]][start[1]][0] != piece[0]:
                                    continue
                                else:
                                    return False
                        return True
                    elif start[0] > finish[0]:
                        while start != finish:
                            start[0] -= 1
                            start[1] += 1
                            # (start)
                            if board[start[0]][start[1]] != 'es':
                                if start == finish and board[start[0]][start[1]][0] != piece[0]:
                                    continue
                                else:
                                    return False
                        return True
                if start[1] > finish[1]:
                    if start[0] < finish[0]:
                        while start != finish:
                            start[0] += 1
                            start[1] -= 1
                            # (start)
                            if board[start[0]][start[1]] != 'es':
                                if start == finish and board[start[0]][start[1]][0] != piece[0]:
                                    continue
                                else:
                                    return False
                        return True
                    elif start[0] > finish[0]:
                        while start != finish:
                            start[0] -= 1
                            start[1] -= 1
                            # (start)
                            if board[start[0]][start[1]] != 'es':
                                if start == finish and board[start[0]][start[1]][0] != piece[0]:
                                    continue
                                else:
                                    return False
                        return True
    if piece[1] == 'r':
        if board[finish[0]][finish[1]][0] != piece[0]:
            if start[0] == finish[0]:
                if start[1] < finish[1]:
                    for col in range(start[1]+1, finish[1]+1):
                        if board[start[0]][col] != 'es':
                            return False
                    return True
                else:
                    for col in range(finish[1]+1, start[1]-1):
                        if board[start[0]][col] != 'es':
                            return False
                    return True
            elif start[1] == finish[1]:
                if start[0] < finish[0]:
                    for row in range(start[0]+1, finish[0]+1):
                        if board[row][start[1]] != 'es':
                            return False
                    return True

                else:
                    for row in range(finish[0]+1, start[0]-1):
                        if board[row][start[1]] != 'es':
                            return False
                    return True
    if piece[1] == 'b':
        if board[finish[0]][finish[1]][0] != piece[0]:
            if start[1] < finish[1]:
                if start[0] < finish[0]:
                    while start != finish:
                        start[0] += 1
                        start[1] += 1
                        # (start)
                        if board[start[0]][start[1]] != 'es':
                            if start == finish and board[start[0]][start[1]][0] != piece[0]:
                                continue
                            else:
                                return False
                    return True
                elif start[0] > finish[0]:
                    while start != finish:
                        start[0] -= 1
                        start[1] += 1
                        # (start)
                        if board[start[0]][start[1]] != 'es':
                            if start == finish and board[start[0]][start[1]][0] != piece[0]:
                                continue
                            else:
                                return False
                    return True
            if start[1] > finish[1]:
                if start[0] < finish[0]:
                    while start != finish:
                        start[0] += 1
                        start[1] -= 1
                        # (start)
                        if board[start[0]][start[1]] != 'es':
                            if start == finish and board[start[0]][start[1]][0] != piece[0]:
                                continue
                            else:
                                return False
                    return True
                elif start[0] > finish[0]:
                    while start != finish:
                        start[0] -= 1
                        start[1] -= 1
                        # (start)
                        if board[start[0]][start[1]] != 'es':
                            if start == finish and board[start[0]][start[1]][0] != piece[0]:
                                continue
                            else:
                                return False
                    return True
    return False
