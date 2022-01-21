import numpy as np
import pandas as pd

def plurality( data):
    
   f = open(data)
   candidates = f.readline().split()
   f.close    
        
   data = np.loadtxt(data, skiprows = 1)
   matrix = pd.DataFrame(data)
   print(data)
   print(candidates)
   
   row, col = np.shape(matrix-1)
   
   ranked_counts = np.zeros((row-1,col))
   
   for i in range(row):
       for j in range(col):
           row_max_loc = matrix.idxmax(axis = 1)
           location = row_max_loc[i]
           data[i, location] = 0
           ranked_counts[j,location] += 1
                             
   return ranked_counts
   
              
print(plurality('test_data.txt'))
