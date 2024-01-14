PLAYER_X = 1
PLAYER_O = -1

def player(state):
    """
    Get the player whose turn is next (PLAYER_X or PLAYER_O).

    Args:
        state (list): The current game state represented as a 2D list.

    Returns:
        int: The player whose turn is next (PLAYER_X or PLAYER_O).
    """
    x_moves = sum(row.count(PLAYER_X) for row in state)
    o_moves = sum(row.count(PLAYER_O) for row in state)

    if x_moves <= o_moves:
        return PLAYER_X
    else:
        return PLAYER_O
    

def actions(state):
    """
    Get a list of all legal moves (empty cells) in the current state.

    Args:
        state (list): The current game state represented as a 2D list.

    Returns:
        list: A list of tuples representing all legal moves (row, column).
    """
    actions_list = []

    for row in range(len(state)):
        for col in range(len(state)):
            if state[row][col] == 0:
                coordinates = (row, col)
                actions_list.append(coordinates)

    return actions_list


def result(state, action):
    """
    Get the new state after applying the specified move for the given player.

    Args:
        state (list): The current game state represented as a 2D list.
        action (tuple): The move to be applied, represented as a tuple (row, column).

    Returns:
        list: The new state after applying the specified move for the given player.
    """
    x, y = action
    p = player(state)

    new_state = [row.copy() for row in state]
    new_state[x][y] = p
    
    return new_state

def evaluate(state):
    """
    Get the evaluated value of the terminal state.

    Args:
        state (list): The current game state represented as a 2D list.

    Returns:
        int: The evaluated value of the terminal state (positive for PLAYER_X win, negative for PLAYER_O win, 0 for draw).
    """
    max_index = len(state) - 1

    # Check rows
    for row in range(max_index + 1):
        for col in range(max_index):
            if state[row][col] != state[row][col + 1] or state[row][col] == 0:
                break
        else:
            if state[row][0] == PLAYER_X:
                return 10  # PLAYER_X won
            elif state[row][0] == PLAYER_O:
                return -10  # PLAYER_O won

    # Check columns
    for col in range(max_index + 1):
        for row in range(max_index):
            if state[row][col] != state[row + 1][col] or state[row][col] == 0:
                break
        else:
            if state[0][col] == PLAYER_X: 
                return 10 # PLAYER_X won
            elif state[0][col] == PLAYER_O: 
                return -10 # PLAYER_O won

    # Check diagonal
    for i in range(max_index):
        if state[i][i] != state[i + 1][i + 1] or state[i][i] == 0:
            break
    else:
        if state[0][0] == PLAYER_X: 
            return 10 # PLAYER_X won
        elif state[0][0] == PLAYER_O: 
            return -10 # PLAYER_O won

    # Check antidiagonal
    for i in range(max_index):
        if state[i][max_index - i] != state[i + 1][max_index - i - 1] or state[i][max_index - i] == 0:
            break
    else:
        if state[0][max_index] == PLAYER_X: 
            return 10 # PLAYER_X won
        elif state[0][max_index] == PLAYER_O: 
            return -10 # PLAYER_O won
        
    return 0 # Draw

# Check if game is over
def terminal(state):
    score = evaluate(state) 

    # If Maximizer or Minimizer has won the game or Draw, return True
    if score == 10 or score == -10 or not actions(state):  
        return True
  
    return False

# Check if state is corecctly formatted
def correctly_formatted(state):
    for row in state:
        for element in row:
            if element not in [PLAYER_X, 0, PLAYER_O]:
                return False
    return True
