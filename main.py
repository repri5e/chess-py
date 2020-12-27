class Color:
    EMPTY = 0
    BLACK = 1
    WHITE = 2

class Empty:
    color = Color.EMPTY
    def __str__(self):
        return '.'

class Board:
    def __init__(self, playing):
        self.playing = playing
        self.board = [[Empty()]*8 for i in range(8)]
        self.board[0][4] = King(Color.BLACK)
        self.board[7][4] = King(Color.WHITE)
        self.board[0][3] = Queen(Color.BLACK)
        self.board[7][3] = Queen(Color.WHITE)
        for i in (1, 6):
            for j in range(8):
                self.board[i][j] = Pawn(Color.BLACK if i%2 == 1 else Color.WHITE)
        for i in (0, 7):
            for j in (0, 7):
                self.board[i][j] = Rook(Color.BLACK if i%2 == 0 else Color.WHITE)
        for i in (0, 7):
            for j in (1, 6):
                self.board[i][j] = Knight(Color.BLACK if i%2 == 0 else Color.WHITE)
        for i in (0, 7):
            for j in (2, 5):
                self.board[i][j] = Bishop(Color.BLACK if i%2 == 0 else Color.WHITE)
        

    def get_moves(self, x, y):
        return self.board[y][x].get_moves(self, x, y)

    def get_color(self, x, y):
        return self.board[y][x].color
    
    def move(self, xy_from, xy_to):
        self.board[xy_to[1]][xy_to[0]] = self.board[xy_from[1]][xy_from[0]]
        self.board[xy_from[1]][xy_from[0]] = Empty()

    def __str__(self):
        output = ''
        if self.playing == 0:
            for i in range(8):
                output += ' '.join(map(str, self.board[i])) + '\n'
            return output
        else:
            for i in range(7, -1, -1):
                output += (' '.join(map(str, self.board[i])) + '\n')[::-1]
            return output
            

class Figure:
    image = None
    def __init__(self, color):
        self.color = color
    def __str__(self):
        return self.image[0 if self.color == Color.WHITE else 1]

class Pawn(Figure):
    image = ('♙', '♟')
    def get_moves(self, board, x, y):
        moves = []
        if self.color == Color.BLACK:
            if y < 7 and board.get_color(x, y+1) == Color.EMPTY:
                moves.append([x, y+1])
                if y == 1 and board.get_color(x, y-2) == Color.EMPTY:
                    moves.append([x, y+2])
        elif self.color == Color.WHITE:
            if y > 0 and board.get_color(x, y-1) == Color.EMPTY:
                moves.append([x, y-1])
                if y == 6 and board.get_color(x, y-2) == Color.EMPTY:
                    moves.append([x, y-2])
        return moves

class King(Figure):
    image = ('♔', '♚')
    def get_moves(self, board, x, y):
        pass

class Queen(Figure):
    image = ('♕', '♛')
    def get_moves(self, board, x, y):
        pass

class Bishop(Figure):
    image = ('♗', '♝')
    def get_moves(self, board, x, y):
        pass

class Knight(Figure):
    image = ('♘', '♞')
    def get_moves(self, board, x, y):
        pass

class Rook(Figure):
    image = ('♖', '♜')
    def get_moves(self, board, x, y):
        pass

def prettify(moves):
    output = []
    for move in moves:
        movement = ''
        movement += chr(ord('a') + move[0])
        movement += str((8 - move[1]))
        output.append(movement)
    return output

board = Board(0)
movement = board.get_moves(4, 6)
board.move([4, 6], movement[0])
print(movement)
print(prettify(movement))
print(board)
