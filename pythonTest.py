# [[1,2], [2,4], [1,7], [9,12]]  --> [1,7] [9,12]
# [[0,7],[5,9],[7,8][11,12],[-2,-1]] --> [-2,-1] [0,9] [11,12]

# [[-2,-1],[0,7],[5,9],[8,9][11,12]]

def combine_intervals(arr):
    # step 1: sort
    arr.sort()
    
    # add new intevals by checking boundries
    if not arr:
        return []
    
    res = [arr[0]]

    for i in range(1, len(arr)):
        intr = arr[i]
        # check if new interval comes after a gap
        if intr[0] > res[-1][1]:
            res.append(intr)
        # if not unite
        elif intr[1] > res[-1][1]:
            res[-1][1] = intr[1]
        
    return res

arr = [[0,7],[5,9],[7,8],[11,12],[-2,-1]] 
print(combine_intervals(arr))

arr = [[1,2], [2,4], [1,7], [9,12]]
print(combine_intervals(arr))