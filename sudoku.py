import numpy as np
spzl=[[9,6,2,0,7,8,5,0,0],
      [1,0,5,0,0,9,3,0,0],
      [3,0,0,5,0,0,8,2,0],
      [0,0,1,0,0,0,0,7,0],
      [6,0,0,0,5,0,0,0,8],
      [0,0,0,6,0,3,9,0,5],
      [0,1,8,0,0,5,0,0,1],
      [0,0,6,8,3,2,7,0,0],
      [7,5,3,1,9,0,4,8,0]]

def possibility(row, col, num):
         global spzl
         for i in range(0, 9):
             if spzl[row][i] == num:
                 return False
         for i in range(0, 9):
             if spzl[i][col] == num:
                 return False

         x = (col // 3) * 3
         y  = (row // 3) * 3
         for i in range(0, 3):
             for j in range(0, 3):
                 if spzl[y + 1][x + 1] == num:
                     return False
         return True 
      
def solution():
          global spzl
          for row in range(0,9):
            for col in range(0,9):
              if spzl[row][col]==0:
                for num in range (1,10):
                    if possibility(row ,col ,num):
                       spzl [row][col]=num
                       solution()
                       spzl [row][col]=0
                return 

          print(np.matrix(spzl))          
          input("More possible solutions ")
solution()

