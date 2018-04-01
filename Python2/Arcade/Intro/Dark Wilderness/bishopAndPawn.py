def bishopAndPawn(bishop, pawn):
    return abs(float(ord(pawn[0]) - ord(bishop[0])) / (int(pawn[1]) - int(bishop[1]))) == 1
