# Find Average and calculate the centroid of varying dimensional points as arguments. author: Jothiswarooban

def average_calc(*args):
    '''This function accepts list of integers as input'''
    if len(args) > 0:
        int_avg = sum(args)/len(args)
        return int_avg
    else :
        return 0

result = average_calc(1,2,3,4,5,8,6)
print("Average of input number:",result)



'''Find centroid of varying dimensional points'''
def centroid(*args):
    '''This function accepts list of varying dimensional points and returns the centroid.
       centroid([1], [0, 2, 31], [2, 3, 4, 5, 6, 7, 8], [1, 2, 3], [4, 5], [97])'''
    max_len = 0
    for point in args:
        if len(point) > max_len:
            max_len = len(point)

    new_points = []
    for point in args:
        new_points.append(point + [0] * (max_len - len(point)))

    # can user zip_longest from itertools
    centroid_val = []
    for i in range(max_len):
        col_sum = 0
        for point in new_points:
            col_sum += point[i]
        centroid_val.append(col_sum / len(new_points))

    return centroid_val

centroid_val = centroid([1, 2, 3], [5, 6], [9, 7, 6, 5, 4], [21, 34], [75], [89], [-25, 90], [2, 3, 4] , [67], [1, 2, 3], [5, 6],[21, 34], [75], [89], [-25, 90], [2, 3, 4])

print("Centroid:", centroid_val)

