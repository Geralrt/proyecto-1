def main_triqui():
    board = [[0,0,0],
             [0,0,0],
             [0,0,0]]
    def win(board,pieza):
        if board[0] == [pieza]*3:
            return True
        return False 
    def print_board(board):
        for b in board:
            print(b)
    piezas = ["X","O"]
    turno = 0
    while True:
        x, y =map (int,input().split())
        
        if board[x][y] != 0:
            ...
        else:
            board[x][y] = piezas[turno%2]
            print_board(board)
            
            if win(board, piezas[turno%2]):
                print(f"HA GANADO {piezas[turno%2]}")
                break
            turno += 1
            