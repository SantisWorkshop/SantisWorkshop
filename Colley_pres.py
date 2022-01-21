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


colley = -(voters * np.ones([num_cand,num_cand]))

# Allocate data for wins/loss counters.
wins = np.zeros(num_cand)
losses = np.zeros(num_cand)

# Create the appropriate main diagonal.
for i in range(len(colley)):
    colley[i,i] =  (voters * (num_cand - 1)) + 2


print(colley)
# Create rating vector
rating = np.zeros(num_cand)

#Brute force the wins and losses
for i in range(voters):
    for j in range(num_cand):
        for k in range(j, num_cand):
            
            points = numpy_mat[i,j] - numpy_mat[i,k]
            if points > 0:
                wins[j] += 1
                losses[k] += 1
            elif points < 0:
                wins[k] += 1
                losses[j] += 1
            elif points == 0:
                wins[k] += 0
                losses[j] += 0
                
b_vec = np.zeros(num_cand)

for i in range(num_cand):
    b_vec[i] = 1 + .5*(wins[i] - losses[i])

print('vector b')
print(b_vec)

# Solve system of linear equations.
ratings = np.linalg.solve(colley, b_vec)

#Print results.
print('Colley Ratings:')
print(ratings)

