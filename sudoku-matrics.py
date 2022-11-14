# THREE GOLD STARS

# Sudoku [http://en.wikipedia.org/wiki/Sudoku]
# is a logic puzzle where a game
# is defined by a partially filled
# 9 x 9 square of digits where each square
# contains one of the digits 1,2,3,4,5,6,7,8,9.
# For this question we will generalize
# and simplify the game.

# Define a procedure, check_sudoku,
# that takes as input a square list
# of lists representing an n x n
# sudoku puzzle solution and returns the boolean
# True if the input is a valid
# sudoku square and returns the boolean False
# otherwise.

# A valid sudoku square satisfies these
# two properties:

#   1. Each column of the square contains
#       each of the whole numbers from 1 to n exactly once.

#   2. Each row of the square contains each
#       of the whole numbers from 1 to n exactly once.

# You may assume the the input is square and contains at
# least one row and column.

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

incorrect2 = [[1,2,3,4],
             [2,3,1,4],
             [4,1,2,3],
             [3,4,1,2]]

incorrect3 = [[1,2,3,4,5],
              [2,3,1,5,6],
              [4,5,2,1,3],
              [3,4,5,2,1],
              [5,6,4,3,2]]

incorrect4 = [['a','b','c'],
              ['b','c','a'],
              ['c','a','b']]

incorrect5 = [ [1, 1.5],
               [1.5, 1]]
               
def check_sudoku(matrix):
    #height = len(matrix)
    #width = len(matrix[0])
    #assert height == width
    #correct = {i for i in range(1,height+1)}
    #for row in matrix:
    #    if set(row) != correct:
    #        return False
    #for col in zip(*matrix):
    #    if set(col) != correct:
    #        return False
    #return True
    height, width = len(matrix), len(matrix[0])
    assert height == width
    correct = {i for i in range(1,height+1)}
    return all(set(row) == correct for row in matrix) and all(set(col) == correct for col in zip(*matrix))


print(check_sudoku(incorrect))
#>>> False
print(check_sudoku(correct))
#>>> True
print(check_sudoku(incorrect2))
#>>> False
print(check_sudoku(incorrect3))
#>>> False
print(check_sudoku(incorrect4))
#>>> False
print(check_sudoku(incorrect5))
#>>> False


