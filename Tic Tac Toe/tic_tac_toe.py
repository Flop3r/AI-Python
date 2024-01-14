from game_logic import *
from agent import *

import time

def game():
    state = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    ai_player = True

    while not terminal(state):
        action = None
        if ai_player:
            action = agent(state)
        else:
            x = int(input("X:"))
            y = int(input("Y:"))
            action = (y, x)

        state = result(state, action)
        ai_player = not ai_player
        draw_game(state)
        # input()



def draw_game(state):
    display_state = [row.copy() for row in state]

    for row in range(len(state)):
        for col in range(len(state[row])):
            if state[row][col] == 0:
                display_state[row][col] = ' '
            elif state[row][col] == 1:
                display_state[row][col] = 'X'
            elif state[row][col] == -1:
                display_state[row][col] = 'O'

    for row in display_state:
        print("|".join(row))
        print("-" * (len(row) * 2 - 1))

    print("")   


if __name__ == "__main__":
    game()