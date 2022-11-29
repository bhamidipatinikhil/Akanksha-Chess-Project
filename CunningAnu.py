import random

from Board import *
from Move import *
from Piece import *
from PieceColor import *
from PieceType import *
from Square import *
from SquarePieceHybrid import *

class CunningAnu:
    def __init__(self, color):
        self.color = color
        self.opp_color = -1
        if(self.color==PieceColor.White):
            self.opp_color = PieceColor.Black
        else:
            self.opp_color = PieceColor.White
        

    def not_crossing(self, x, board):
        # x is a move type
        pt = x.piece.type
        pc = x.piece.color
        from_sq = x.from_sq
        to_sq = x.to_sq

        if(pt != PieceType.Knight):
            
            pass
        else:
            return True

    def move(self, board):
        pieces = []
        candidate_moves = []
        for i in range(8):
            for j in range(8):
                tmp_sph = board[i][j]
                if(self.color == tmp_sph.piece.color):
                    pm = self.possible_moves(tmp_sph, board)
                    for move in pm:
                        candidate_moves.append(move)
                    # candidate_moves.append(self.possible_moves(tmp_sph))
        
        # print("Candidate moves reached")
        # non_cands = []
        # for c in candidate_moves:
            # print("I ran")
            # print(isinstance(c, Move))
            # print(type(c))
            # if not isinstance(c, Move):
            #     non_cands.append(c)
        
        # print(f"The length of candidates is:: {len(candidate_moves)}")
        # print(f"The length of non candidtae moves is:: {len(non_cands)}")
        # print(candidate_moves)
        # candidate_moves = list(filter(lambda x: board[x.to_sq.row][x.to_sq.col].piece.type == PieceType.Nill, candidate_moves))
        # candidate_moves = list(filter(lambda x: self.not_crossing(x, board), candidate_moves))
        chosen_move = random.choice(candidate_moves)
        # print(type(chosen_move))
        board[chosen_move.from_sq.row][chosen_move.from_sq.col] = SquarePieceHybrid(chosen_move.from_sq.row, chosen_move.from_sq.col, PieceColor.Nill, PieceType.Nill)
        board[chosen_move.to_sq.row][chosen_move.to_sq.col] = SquarePieceHybrid(chosen_move.to_sq.row, chosen_move.to_sq.col, chosen_move.piece.color, chosen_move.piece.type)


    
    def possible_moves(self, sph, board):
        poss_moves = []
        poss_squares = []
        # match sph.piece.type:
        if sph.piece.type== PieceType.King:
            row = sph.sq.row
            col = sph.sq.col

            arr1 = [row-1, row, row+1]
            arr2 = [col-1, col, col+1]
            for i in arr1:
                for j in arr2:
                    if((i!= row or j!=col) and (i > -1 and i < 8) and (j > -1 and j < 8)):
                        if(board[i][j].piece.type == PieceType.Nill or board[i][j].piece.color == self.opp_color):
                            tmp_sq = Square(i, j)
                            poss_squares.append(tmp_sq)
                            poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(i, j)))
                    
            pass
        elif sph.piece.type ==  PieceType.Queen:
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
                    if(board[tmp1][col].piece.type == PieceType.Nill or board[tmp1][col].piece.color == self.opp_color):
                        poss_squares.append(Square(tmp1, col))
                        poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(tmp1, col)))
                    else:
                        break
            
            for i in arr3:
                tmp1 = col+i
                if(tmp1 > -1 and tmp1 < 8):
                    if(board[row][tmp1].piece.type == PieceType.Nill or board[row][tmp1].piece.color == self.opp_color):
                        poss_squares.append(Square(row, tmp1))
                        poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(row, tmp1)))
                    else:
                        break
            #Bishop time
            arr1 = [1, 2, 3, 4, 5, 6, 7]
            arr3 = [-1, -2, -3, -4, -5, -6, -7]
            arr1 = arr1 + arr3
            arr3 = arr3 + arr1
            row = sph.sq.row
            col = sph.sq.col
            tmp_arr = []
            break_outer = False
            for i in arr1:
                for j in arr3:
                    if(abs(i)==abs(j)):
                        ans1 = row+i
                        ans2 = col + j
                        if((ans1 > -1 and ans1 < 8) and (ans2 > -1 and ans2 < 8)):
                            if(board[ans1][ans2].piece.type == PieceType.Nill or board[ans1][ans2].piece.color == self.opp_color):
                                poss_squares.append(Square(ans1, ans2))
                                poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(ans1, ans2)))
                            else:
                                break_outer = True
                                break
                if(break_outer):
                    break
            pass
        elif sph.piece.type== PieceType.Rook:
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
                    if(board[tmp1][col].piece.type == PieceType.Nill or board[tmp1][col].piece.color == self.opp_color):
                        poss_squares.append(Square(tmp1, col))
                        poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(tmp1, col)))
                    else:
                        break
            
            for i in arr3:
                tmp1 = col+i
                if(tmp1 > -1 and tmp1 < 8):
                    if(board[row][tmp1].piece.type == PieceType.Nill or board[row][tmp1].piece.color == self.opp_color):
                        poss_squares.append(Square(row, tmp1))
                        poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(row, tmp1)))
                    else:
                        break
                    
            pass
        elif sph.piece.type== PieceType.Bishop:
            arr1 = [1, 2, 3, 4, 5, 6, 7]
            arr3 = [-1, -2, -3, -4, -5, -6, -7]
            arr1 = arr1 + arr3
            arr3 = arr3 + arr1
            row = sph.sq.row
            col = sph.sq.col
            tmp_arr = []
            break_outer = False
            for i in arr1:
                for j in arr3:
                    if(abs(i)==abs(j)):
                        ans1 = row+i
                        ans2 = col + j
                        if((ans1 > -1 and ans1 < 8) and (ans2 > -1 and ans2 < 8)):
                            if(board[ans1][ans2].piece.type == PieceType.Nill or board[ans1][ans2].piece.color == self.opp_color):
                                poss_squares.append(Square(ans1, ans2))
                                poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(ans1, ans2)))
                            else:
                                break_outer = True
                                break
                if(break_outer):
                    break
            pass
        elif sph.piece.type== PieceType.Knight:
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
                            if(board[tmp1][tmp2].piece.type == PieceType.Nill or board[tmp1][tmp2].piece.color == self.opp_color):
                            
                                tmp_sq = Square(tmp1, tmp2)
                                poss_squares.append(tmp_sq)
                                poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(tmp1, tmp2)))

            pass
        elif sph.piece.type== PieceType.Pawn:
            if(sph.piece.color==PieceColor.White):
                row = sph.sq.row
                col = sph.sq.col

                arr1 = [row-1]
                arr2 = [col]
                for i in arr1:
                    for j in arr2:
                        if((i > -1 and i < 8) and (j > -1 and j < 8)):
                            if(board[i][j].piece.type == PieceType.Nill):
                                tmp_sq = Square(i, j)
                                poss_squares.append(tmp_sq)
                                poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(i, j)))
                
            elif(sph.piece.color==PieceColor.Black):
                row = sph.sq.row
                col = sph.sq.col

                arr1 = [row+1]
                arr2 = [col]
                for i in arr1:
                    for j in arr2:
                        if((i > -1 and i < 8) and (j > -1 and j < 8)):
                            tmp_sq = Square(i, j)
                            poss_squares.append(tmp_sq)
                            poss_moves.append(Move(sph.piece.color, sph.piece.type, Square(row, col), Square(i, j)))

        # print("Possible moves reached")
        return poss_moves








if __name__ == '__main__':
    b = Board()
    b.print_board()
    ca = CunningAnu(PieceColor.White)
    ca2 = CunningAnu(PieceColor.Black)
    for i in range(200):
        ca.move(b.board)
        b.print_board()
        if(b.check_win()):
            print("White won the game")
            break
        ca2.move(b.board)
        b.print_board()
        if(b.check_win()):
            print("Black won the game")
            break
        