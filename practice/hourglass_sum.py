#!/bin/python3

import sys


arr = []
for arr_i in range(6):
   arr_t = [int(arr_temp) for arr_temp in input().strip().split(' ')]
   arr.append(arr_t)
    
#first index: row
#second index: column


def hourglass(array):
	# got test case wrong for initializing largest = 0
	# because hourglass might have negative values! sum might not be < largest = 0 
	# can initialize largest to -56, since matrix 6x6, largest min val: -9
    total = arr[0][0] + arr[0][1] + arr[0][2] + arr[1][1] + arr[2][0] + arr[2][1] + arr[2][2] 
    
    for row in range(4): 
        for column in range(4): 
            new_total = arr[row][column] + arr[row][column+1] + arr[row][column+2] + arr[row+1][column+1] + arr[row+2][column] + arr[row+2][column+1] + arr[row+2][column+2] 
            if new_total > total:
                total = new_total
    return total

print(hourglass(arr))
     