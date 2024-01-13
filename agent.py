from game_logic import *
import math, random

def max_value(state, depth):
    """
    Minimax algorithm for maximizing player (PLAYER_X).

    Args:
        state (list): The current game state represented as a 2D list.
        depth (int): The depth of the current recursive call.

    Returns:
        int: The evaluated score for the current state.
    """
    score = evaluate(state) 

   # If Minimizer has won the game return their 
    # evaluated score  
    if score == 10 :  
        return score - depth
  
    # If Minimizer has won the game return their
    # evaluated score  
    if score == -10 : 
        return score + depth
    
    # If there are no more moves and no winner then  
    # it is a tie  
    if not actions(state): 
        return 0


    val = -math.inf

    for action in actions(state):
        val = max(val, min_value(result(state, action), depth + 1))

    return val


def min_value(state, depth):
    """
    Minimax algorithm for minimizing player (PLAYER_O).

    Args:
        state (list): The current game state represented as a 2D list.
        depth (int): The depth of the current recursive call.

    Returns:
        int: The evaluated score for the current state.
    """
    score = evaluate(state) 

    # If Maximizer has won the game return their 
    # evaluated score  
    if score == 10 :  
        return score - depth
  
    # If Minimizer has won the game return their
    # evaluated score  
    if score == -10 : 
        return score + depth
    
    # If there are no more moves and no winner then  
    # it is a tie  
    if not actions(state): 
        return 0


    val = math.inf

    for action in actions(state):
        val = min(val, max_value(result(state, action), depth + 1))

    return val


def agent(state):
    """
    Select the best move for the current player using the Minimax algorithm.

    Args:
        state (list): The current game state represented as a 2D list.

    Returns:
        action (tuple): The best move for the current player (row, column).
    """
    best_action = None
    evaluated_actions = {}

    # For Maximizer
    if player(state) == PLAYER_X:
        for action in actions(state):
            value = min_value(result(state, action), 0)
            evaluated_actions[action] = value

        best_action = random_best_action(evaluated_actions, max=True)

    # For Minimizer   
    else:
        for action in actions(state):
            value = max_value(result(state, action), 0)
            evaluated_actions[action] = value

        best_action = random_best_action(evaluated_actions, max=False)

    return best_action


def random_best_action(evaluated_actions, max):
    best_actions = []

    if max:
        best_value = -math.inf
        
        for action, value in evaluated_actions.items():
            if value > best_value:
                best_value = value
                best_actions = [action]

            elif value == best_value:
                best_actions.append(action)
    else:
        best_value = math.inf

        for action, value in evaluated_actions.items():
            if value < best_value:
                best_value = value
                best_actions = [action]
                
            elif value == best_value:
                best_actions.append(action)

    return random.choice(best_actions)