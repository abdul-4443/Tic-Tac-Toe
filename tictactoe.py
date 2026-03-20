import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(b):
    xc = sum(row.count(X) for row in b)
    oc = sum(row.count(O) for row in b)
    return X if xc == oc else O


def actions(b):
    moves = set()
    for r in range(3):
        for c in range(3):
            if b[r][c] == EMPTY:
                moves.add((r, c))
    return moves


def result(b, action):
    r, c = action
    if b[r][c] != EMPTY:
        raise Exception("Invalid move.")
    nb = copy.deepcopy(b)
    nb[r][c] = player(b)
    return nb


def winner(b):
    for row in b:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]
    for c in range(3):
        if b[0][c] == b[1][c] == b[2][c] and b[0][c] is not EMPTY:
            return b[0][c]
    if b[0][0] == b[1][1] == b[2][2] and b[0][0] is not EMPTY:
        return b[0][0]
    if b[0][2] == b[1][1] == b[2][0] and b[0][2] is not EMPTY:
        return b[0][2]
    return None


def terminal(b):
    if winner(b) is not None:
        return True
    for row in b:
        if EMPTY in row:
            return False
    return True


def utility(b):
    w = winner(b)
    if w == X:
        return 1
    elif w == O:
        return -1
    return 0


def minimax(b):
    if terminal(b):
        return None
    p = player(b)
    if p == X:
        best, move = -math.inf, None
        for a in actions(b):
            val = min_value(result(b, a))
            if val > best:
                best, move = val, a
                if best == 1:
                    break
        return move
    else:
        best, move = math.inf, None
        for a in actions(b):
            val = max_value(result(b, a))
            if val < best:
                best, move = val, a
                if best == -1:
                    break
        return move


def max_value(b):
    if terminal(b):
        return utility(b)
    v = -math.inf
    for a in actions(b):
        v = max(v, min_value(result(b, a)))
        if v == 1:
            return v
    return v


def min_value(b):
    if terminal(b):
        return utility(b)
    v = math.inf
    for a in actions(b):
        v = min(v, max_value(result(b, a)))
        if v == -1:
            return v
    return v