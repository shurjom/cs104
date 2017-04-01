 
# set the current maximum and minimum to the first index


k = [1, 2, 3, 4, 5]
def findMaxDiff(k):

    max_i, min_i = 0, 0
    
    # iterate the list from the second index
    for i in range(1, len()):
        # check if were larger than the current maximum
        if [i] > [max_i]:
            max_i = i
    
        # check if were smaller than the current minimum
        if [i] < [min_i]:
            min_i = i
    
    distance = [max_i] - [min_i]
    print(min_i, max_i, distance) # 0 0 4

