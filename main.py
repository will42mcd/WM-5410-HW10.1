# TictacToe code taken from: https://www.geeksforgeeks.org/tic-tac-toe-gui-in-python-using-pygame/
# Minimax code taken from: https://www.geeksforgeeks.org/finding-optimal-move-in-tic-tac-toe-using-minimax-algorithm-in-game-theory/
# Acessed on 10/10/2024
# No atribution listed
# CHANGELOG
# - changed mouse interaction to be mouse up and requires double click
# - Cleared events on game initiation 
# - Added a random move computer for single player
# - Combined minimax code with tictactoe
# - added evaluate function for minimax implementation 
# - adjusted check_win function for combatibility with minimax


from game_functions import *
import pygame as pg
import sys
from pygame.locals import *
from game_functions import winner

 
def main():
    game_initiating_window()
    count = 0
    while(True):
        for event in pg.event.get():
            if event.type == QUIT:
                pg.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                keeping_score()
                pg.quit()
                sys.exit()
        
        random_move()
        
        computer_move()
        
        pg.display.update()
        CLOCK.tick(fps)
        if (winner or draw):
            count += 1
            print(count)
            if count == 200:
                keeping_score()
                pg.quit()
                sys.exit()

if __name__ == "__main__":
    main()