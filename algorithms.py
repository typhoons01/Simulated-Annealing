from random import randint, uniform
from time import time
from math import *
from dataset_generator import *

    #
    ##
#######
########
#######
    ##
    #

def simulated_annealing_2D(arr,i,j, time_limit, T):
    current = arr[i][j]
    m = len(arr)
    n = len(arr[0])
    
    ilist = []
    for x in arr:
        ilist.append(max(x))
    
    start_time = time()
    
    while (time() - start_time < time_limit):
        t = time() - start_time
        x = randint(0,7)
        indices = [[max(0,i-1),j],[min(m-1,i+1),j],[i,max(0,j-1)],[i,min(n-1,j+1)],[max(0,i-1),max(0,j-1)],[max(0,i-1),min(n-1,j+1)],[min(m-1,i+1),max(0,j-1)],[min(m-1,i+1),min(n-1,j+1)]]
        neighbour = arr[indices[x][0]][indices[x][1]]
        E = neighbour - current
        #print(neighbour,indices[x])
        if E>=0:
            current = neighbour
            [i,j]= indices[x]
        else :
            z = uniform(0,1)
            try:
                prob = exp(E/T(t))
            except:
                prob = 0
            if  z <=  :
                current = neighbour
                [i,j]= indices[x]
    
    return [time_limit,max(ilist)-current]



arr = lessrandom3d_ver2(100, 44, 3)

print(simulated_annealing_2D(arr, 50, 22, 10, exp))

pretty_print_1(arr)
