import numpy as np
import pandas as pd  
import time
#Read
data = pd.read_csv('primary_data.csv')



total_votes = data.sum(axis = 0, numeric_only= True)

print(total_votes.sort_values(axis = 0, ascending = False))





num_data = data.iloc[:,2:]
 
print(np.shape(data.iloc[:,2:]))

numpy_mat = num_data.to_numpy()
mat = pd.DataFrame(numpy_mat)

row, col = np.shape(mat)
borda_count_mat = np.zeros((col,col))
print(np.shape(borda_count_mat))

t0 = time.time()
for i in range(row):
    for j in range(col):
        
        if mat.max(axis = 1).any() != 0:
            row_max_loc = mat.idxmax(axis = 1)
            location = row_max_loc[i]
            borda_count_mat[location, j] += 1
            numpy_mat[i,location] = -1
        else:
            row_max_loc = mat.idxmax(axis = 1)
            location = row_max_loc[i]
            borda_count_mat[location, j] += 0
            numpy_mat[i,location] = -1
t1 = time.time()   

total = t1-t0         
print(borda_count_mat)

#Assign weights.
weights = [5, 4, 3, 2 ,1]

#Multiply the weights and ranked_counts.
results_mat = weights * borda_count_mat

#Get the row sum to find the points of each candidate.
borda_points = results_mat.sum(axis = 0)
print(borda_points)

