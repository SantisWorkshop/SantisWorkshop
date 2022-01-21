import numpy as np
import pandas as pd

def plurality(data):
    
        
   data = np.loadtxt(data, skiprows = 1)
   matrix = pd.DataFrame(data)
   print(data)
   #print(candidates)
   
   row, col = np.shape(matrix-1)
   row_max = matrix.max(axis = 1)
   
   results = np.zeros(row - 1)
   
   for i in range(row):
       for j in range(col):
           if matrix.loc[i,j] == row_max[i]:
               results[j] += 1
               
   return results
   
              
print(plurality('test_data.txt'))
