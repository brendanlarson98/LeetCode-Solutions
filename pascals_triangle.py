# https://leetcode.com/problems/pascals-triangle/
# Given an integer numRows, return the first numRows of Pascal's triangle.

def generate(numRows):
    total_arr = []
    if numRows == 0:
        return total_arr
    def rec_func(arr, numRows, rows):
        total_arr.append(arr)
        if rows == numRows:
            return arr
        new_arr = []
        for i in arr:
            new_arr.append(i)
        new_arr.append(1)
        for i in range(len(arr)-1):
            new_arr[i+1] = arr[i]+arr[i+1]
        return rec_func(new_arr, numRows, rows+1)
        
    rec_func([1], numRows, 1)
    return total_arr

print(generate(5))
