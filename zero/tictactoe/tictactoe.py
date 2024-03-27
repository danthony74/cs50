"""
Tic Tac Toe Player
"""

import random
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if is_empty(board):
        return X
    x_count = 0 
    o_count = 0

    for row in board:
        for column in row:
            if column == X:
                x_count += 1
            elif column == O:
                o_count += 1
    if x_count > o_count:
        return O
    else: 
        return X 


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for row in board:
        for column in row:
            if column == EMPTY:
                actions.append((board.index(row), row.index(column)))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    player_code = player(board)
    new_board = deepcopy(board)
    new_board[action[0]][action[1]] = player_code
    return new_board

def deepcopy(board):
    """
    Returns a deep copy of the board.
    """
    new_board = []
    for row in board:
        new_row = []
        for column in row:
            new_row.append(column)
        new_board.append(new_row)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    return is_won(board, get_winner=True)
    



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # check if the board has a winning layout, or if it's full
    return (is_won(board) or is_full(board))


def is_full(board):
    """
    Returns True if the board is full, False otherwise.
    """
    for row in board:
        for column in row:
            if column == EMPTY:
                return False
    return True


def is_empty(board):
    """
    Returns True if the board is empty, False otherwise.
    """
    for row in board:
        for column in row:
            if column != EMPTY:
                return False
    return True


def is_won(board, get_winner=False):
    for row in board:
        # Does the Row match
        if row[0] == row[1] and row[0] == row[2] and row[0] != EMPTY:
            if get_winner:
                return row[0]
            return True
    for col in range(3):
        # Does the column match
        if board[0][col] == board[1][col] and board[0][col] == board[2][col] and board[0][col] != EMPTY:
            if get_winner:
                return board[0][col]
            return True
        # Check the diagonals
    if (board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY) or\
        (board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY):
        if get_winner:
            return board[1][1]
        return True
    # No matches anywhere
    if get_winner:
        return None
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner = is_won(board, get_winner=True)
    if winner == X:
        return 1
    elif winner == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    player_code = player(board) 
    available_actions = actions(board)
    optimal_value = 0
    if player_code == X:
        optimal_value = -math.inf
    else:
        optimal_value = math.inf

    options = []

    for action in available_actions:
        new_board = result(board, action)
        value = get_value(new_board, player_code)
        options.append((action, value))

    solutions = []
    for option in options:
        if player_code == X:
            optimal_value =  max(option[1], optimal_value)
        else:
            optimal_value =  max(option[1], optimal_value)
    
    for option in options:
        if option[1] == optimal_value:
            solutions.append(option[0])
    
    return random.choice(solutions)
      
        
    
    

def get_value(board, player):

    if terminal(board):
        return utility(board)
    
    next_board  = minimax(board)
    value = get_value(next_board, player)
    base_score = None
    if player == X:
        base_score = -math.inf
        return max(value, base_score)
    else:
        base_score = math.inf
        return min(value, base_score)
        


def calc_value(board, player):
    if terminal(board):
        return utility(board), None
    v = math.inf
    action = None
    for act in actions(board):
        v = min(v, max_value(result(board, act))[0])
        if v == -1:
            return v, act
        if v == 0:
            action = act
    return v, action
