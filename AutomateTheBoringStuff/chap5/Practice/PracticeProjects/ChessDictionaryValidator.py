board1 = {
    'a1': 'brook', 'b1': 'bknight', 'c1': 'bbishop', 'd1': 'bqueen', 'e1': 'bking', 'f1': 'bbishop', 'g1': 'bknight', 'h1': 'brook',
    'a2': 'bpawn', 'b2': 'bpawn', 'c2': 'bpawn', 'd2': 'bpawn', 'e2': 'bpawn', 'f2': 'bpawn', 'g2': 'bpawn', 'h2': 'bpawn',
    'a7': 'wpawn', 'b7': 'wpawn', 'c7': 'wpawn', 'd7': 'wpawn', 'e7': 'wpawn', 'f7': 'wpawn', 'g7': 'wpawn', 'h7': 'wpawn',
    'a8': 'wrook', 'b8': 'wknight', 'c8': 'wbishop', 'd8': 'wqueen', 'e8': 'wking', 'f8': 'wbishop', 'g8': 'wknight', 'h8': 'wrook'
}

MAX_PAWNS = 8
MAX_PIECES = 16
VALID_MOVES = [chr(i) + str(j) for i in range(97, 105) for j in range(1, 9)]
print(VALID_MOVES)

def isValidChessBoard(board):
    
    black = {'pawns': 0, 'pieces': 0}
    white = {'pawns': 0, 'pieces': 0}
    
    boardkeys = list(board.keys())
    check = all(item in VALID_MOVES for item in boardkeys)
    print(check)
    
    for k in board:
        if board[k].startswith('w'):
            white['pieces'] += 1
            if board[k] == 'wpawn':
                white['pawns'] += 1
        elif board[k].startswith('b'):
            black['pieces'] += 1
            if board[k] == 'bpawn':
                black['pawns'] += 1
                
    kings =  list(board.values()).count('bking') == 1 and list(board.values()).count('wking') == 1
    print(kings)
                
    if check and kings and black['pawns'] <= MAX_PAWNS and white['pawns'] <= MAX_PAWNS and black['pieces'] <= MAX_PIECES and white['pieces'] <= MAX_PIECES:
        print("this board is valid")
        return True
    else:
        print("this board is not valid")
        return False
        
    # the above if and else statements written in a better way / chatGPT suggestion    
    # if all(piece in board.values() for piece in ['wking', 'bking']) and \
    #    black['pawns'] <= MAX_PAWNS and white['pawns'] <= MAX_PAWNS and \
    #    black['pieces'] <= MAX_PIECES and white['pieces'] <= MAX_PIECES:
    #     return True
    # else:
    #     return False
    
    # print(f"Black :",(black))
    # print(f"White :",white)
    
    
isValidChessBoard(board1)
    