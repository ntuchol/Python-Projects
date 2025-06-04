import chess
board = chess.Board()
legal_moves = list(board.legal_moves)
print(legal_moves[0])