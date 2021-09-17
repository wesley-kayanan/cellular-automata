import numpy as np

def get_next_state(current_grid):

    for x in range(30):
        for y in range(30):

            nb = 0

            for i in range (-1, 2):
                for j in range (-1, 2):
                    
                    if not(x + i < 0 or x + i > 29 or y + j < 0 or y + j > 29): 
                        if i != 0 and j != 0 and current_grid[x + i][y + j] == 1:
                         nb += 1
            
            if current_grid[x][y] == 0:
                current_grid[x][y] = 1 if (nb > 1 and nb < 4) else 0
            else:
                current_grid[x][y] = 1 if nb == 2 else 0

    return current_grid