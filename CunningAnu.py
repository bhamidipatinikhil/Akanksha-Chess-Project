from enum import Enum
import random





class PieceColor(Enum):
    White = 0
    Black = 1
    Nill=2


class PieceType(Enum):
    Pawn=0
    Bishop = 1
    Knight = 2
    Rook = 3
    Queen = 4
    King = 5
    Nill=6

    
class Piece:
    def __init__(self, c, t):
        self.color = c
        self.type = t


        
    

class Board:

    def return_str(self, sph):
        color = sph.piece.color
        type = sph.piece.type

        color_str = ""
        type_str = ""

        isPiece = False

        if(color == PieceColor.Black):
            isPiece = True
            color_str = "B"
        elif(color == PieceColor.White):
            isPiece = True
            color_str = "W"

        if(type == PieceType.Rook):
            type_str = "R"
        elif(type == PieceType.Knight):
            type_str = "N"
        elif(type == PieceType.Bishop):
            type_str = "B"
        elif(type == PieceType.King):
            type_str = "K"
        elif(type == PieceType.Queen):
            type_str = "Q"
        elif(type==PieceType.Pawn):
            type_str = "P"
        
        ans = color_str + type_str
        if isPiece == True:
            return ans
        else:
            return "  "


    def print_board(self):
        print("")
        print("-" * 32)
        for i in range(8):
            for j in range(8):
                print("|", end= "")
                print(self.return_str(self.board[i][j]), end=" ")
                # print("|", end="")
            print("|")
            print("-"*32)
        print("")
        


    def __init__(self):
        self.board = [[0 for i in range(8)] for j in range(8)]

        
        tmp_hybrid = SquarePieceHybrid(0, 0, PieceColor.Black, PieceType.Rook)

        self.board[0][0] = tmp_hybrid

        for i in range(2, 6):
            for j in range(0, 8):
                self.board[i][j] = SquarePieceHybrid(i, j, PieceColor.Nill, PieceType.Nill)
        
        for j in range(0, 8):
            self.board[1][j] = SquarePieceHybrid(1, j, PieceColor.Black, PieceType.Pawn)
        
        for j in range(0, 8):
            self.board[6][j] = SquarePieceHybrid(6, j, PieceColor.White, PieceType.Pawn)
        
        for j in range(0, 8):
            sph = self.fill_initial_posns(j, PieceColor.Black)
            if(sph!=-1):
                self.board[0][j] = sph
        
        for j in range(0, 8):
            sph = self.fill_initial_posns(j, PieceColor.White)
            if(sph!=-1):
                self.board[7][j] = sph
        
        self.board[0][3] = SquarePieceHybrid(0, 3, PieceColor.Black, PieceType.King)
        self.board[0][4] = SquarePieceHybrid(0, 4, PieceColor.Black, PieceType.Queen)
        self.board[7][3] = SquarePieceHybrid(7, 3, PieceColor.White, PieceType.King)
        self.board[7][4] = SquarePieceHybrid(7, 4, PieceColor.White, PieceType.Queen)

    def fill_initial_posns(self, col, pc):
        dist1 = abs(col-0)
        dist2 = abs(col-7)

        indicator = min(dist1, dist2)

        pt = -1
        if indicator==0:
            pt = PieceType.Rook
        elif indicator==1:
            pt = PieceType.Knight
        elif indicator == 2:
            pt = PieceType.Bishop
        
        row = -1
        if(pc==PieceColor.Black):
            row = 0
        elif(pc==PieceColor.White):
            row=7
        
        if(pt!=-1):
            tmp_ans = SquarePieceHybrid(row, col, pc, pt)
            return tmp_ans
        else:
            return -1




class Square:
    def __init__(self, row, col):
        self.col = col
        self.row = row

class Move:
    def __init__(self, piece, from_sq, to_sq):
        self.piece = piece
        self.from_sq = from_sq
        self.to_sq = to_sq

    def __init__(self, piece_color, piece_type, from_sq, to_sq):
        self.piece = Piece(piece_color, piece_type)
        self.from_sq = from_sq
        self.to_sq = to_sq



class SquarePieceHybrid:
    

    def __init__(self, sq, piece):
        self.sq = sq
        self.piece = piece
    
    def __init__(self, row, col, pc, pt):
        self.sq = Square(row, col)
        self.piece = Piece(pc, pt)
    
    def candidate_squares(self):
        candidates = []
        type = self.piece.type

        if(type==PieceType.King):
            pass

        

class CunningAnu:
    def __init__(self, color):
        self.color = color
        self.opp_color = -1
        if(self.color==PieceColor.White):
            self.opp_color = PieceColor.Black
        else:
            self.opp_color = PieceColor.White
        

    def move(self, board):
        pieces = []
        candidate_moves = []
        for i in range(8):
            for j in range(8):
                tmp_sph = board[i][j]
                if(self.color == tmp_sph.piece.color):
                    candidate_moves.append(self.possible_moves(tmp_sph))
        
        candidate_moves = list(candidate_moves.filter(lambda x: board[x.to_sq.row][x.to_sq.col].piece.type != PieceType.Nill))

        chosen_move = random.choice(candidate_moves)

        board[chosen_move.from_sq] = SquarePieceHybrid(chosen_move.from_sq.row, chosen_move.from_sq.col, PieceColor.Nill, PieceType.Nill)
        board[chosen_move.to_sq] = SquarePieceHybrid(chosen_move.to_sq.row, chosen_move.to_sq.col, chosen_move.piece.color, chosen_move.piece.type)


    
    def possible_moves(self, sph):
        poss_moves = []
        poss_squares = []
        match sph.piece.type:
            case PieceType.King:
                row = sph.sq.row
                col = sph.sq.col

                arr1 = [row-1, row, row+1]
                arr2 = [col-1, col, col+1]
                for i in arr1:
                    for j in arr2:
                        if((i!= row or j!=col) and (i > -1 and i < 8) and (j > -1 and j < 8)):
                            tmp_sq = Square(i, j)
                            poss_squares.append(tmp_sq)
                            poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(i, j)))
                        
                pass
            case PieceType.Queen:
                # Rook moves
                arr1 = [1, 2, 3, 4, 5, 6, 7]
                arr2 = [1, -1]
                row = sph.sq.row
                col = sph.sq.col
                arr3 = []
                for i in arr1:
                    for j in arr2:
                        arr3.append(i*j)
                
                for i in arr3:
                    tmp1 = row+i
                    if(tmp1 > -1 and tmp1 < 8):
                        poss_squares.append(Square(tmp1, col))
                        poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(tmp1, col)))
                
                for i in arr3:
                    tmp1 = col+i
                    if(tmp1 > -1 and tmp1 < 8):
                        poss_squares.append(Square(row, tmp1))
                        poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(row, tmp1)))
                
                        
                # Bishop Moves
                arr1 = [1, 2, 3, 4, 5, 6, 7]
                arr2 = [1, -1]
                arr3 = []
                for i in arr1:
                    for j in arr2:
                        arr3.append(i*j)
                
                tmp_arr = []
                for i in arr3:
                    for j in arr3:
                        if(abs(i)==abs(j)):
                            ans1 = row+i
                            ans2 = col + j
                            if((ans1 > -1 and ans1 < 8) and (ans2 > -1 and ans2 < 8)):
                                poss_squares.append(Square(ans1, ans2))
                                poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(ans1, ans2)))

                
                
                pass
            case PieceType.Rook:
                arr1 = [1, 2, 3, 4, 5, 6, 7]
                arr2 = [1, -1]
                row = sph.sq.row
                col = sph.sq.col
                arr3 = []
                for i in arr1:
                    for j in arr2:
                        arr3.append(i*j)
                
                for i in arr3:
                    tmp1 = row+i
                    if(tmp1 > -1 and tmp1 < 8):
                        poss_squares.append(Square(tmp1, col))
                        poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(tmp1, col)))
                
                for i in arr3:
                    tmp1 = col+i
                    if(tmp1 > -1 and tmp1 < 8):
                        poss_squares.append(Square(row, tmp1))
                        poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(row, tmp1)))
                        
                pass
            case PieceType.Bishop:
                arr1 = [1, 2, 3, 4, 5, 6, 7]
                arr2 = [1, -1]
                arr3 = []
                for i in arr1:
                    for j in arr2:
                        arr3.append(i*j)
                
                tmp_arr = []
                for i in arr3:
                    for j in arr3:
                        if(abs(i)==abs(j)):
                            ans1 = row+i
                            ans2 = col + j
                            if((ans1 > -1 and ans1 < 8) and (ans2 > -1 and ans2 < 8)):
                                poss_squares.append(Square(ans1, ans2))
                                poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(ans1, ans2)))

                pass
            case PieceType.Knight:
                row = sph.sq.row
                col = sph.sq.col

                arr1 = [-1, -2, 1, 2]
                arr2 = [-1, -2, 1, 2]

                for i in arr1:
                    for j in arr2:
                        if(abs(i) != abs(j)):
                            tmp1 = row + i
                            tmp2 = col + j

                            if((tmp1 > -1 and tmp1 < 8) and (tmp2 > -1 and tmp2 < 8)):
                                tmp_sq = Square(tmp1, tmp2)
                                poss_squares.append(tmp_sq)
                                poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(tmp1, tmp2)))

                pass
            case PieceType.Pawn:
                if(sph.piece.color==PieceColor.White):
                    row = sph.sq.row
                    col = sph.sq.col

                    arr1 = [row-1]
                    arr2 = [col]
                    for i in arr1:
                        for j in arr2:
                            if((i > -1 and i < 8) and (j > -1 and j < 8)):
                                tmp_sq = Square(i, j)
                                poss_squares.append(tmp_sq)
                                poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(i, j)))
                    
                elif(sph.piece.color==PieceColor.Black):
                    pass
                pass

        return poss_moves






b = Board()
b.print_board()
ca = CunningAnu(PieceColor.White)
ca.move(b)
b.print_board()