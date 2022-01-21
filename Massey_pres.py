import numpy as np
import pandas as pd  

#import time
#Read
data = pd.read_csv('primary_data.csv')

num_data = data.iloc[:,2:]
 
print(np.shape(data.iloc[:,2:]))

numpy_mat = num_data.to_numpy()
mat = pd.DataFrame(numpy_mat)

voters, num_cand = np.shape(mat)

#This fills the matrix with the -n_ij
massey = -(voters * np.ones([num_cand,num_cand]))

#Replace the main diagonal by the total number of games.
for i in range(len(massey)):
    massey[i,i] =  voters * (num_cand - 1) 

print(massey)    

differentials = np.zeros(num_cand)


total_scores = np.sum(num_data, axis = 0)

#print(total_scores)

for i in range(num_cand):
    for j in range(i, num_cand):
        points =  total_scores[i] - total_scores[j]
        differentials[i] += points
        differentials[j] += -points

print('Before zero:')
print(differentials)


massey[ num_cand - 1, :] = 1 
differentials[num_cand - 1] = 0

#print(massey)
print('After zero')
print(differentials)

#Solve the system of linear equations.
solved = np.linalg.solve(massey, differentials)

#print the results
print('These are the results')
print(solved)