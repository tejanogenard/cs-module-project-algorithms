'''
Input: a List of integers
Returns: a List of integers
Write a function that takes an array of integers and moves each non-zero integer to the left side of the array, 
then returns the altered array. The order of the non-zero integers does not matter in the mutated array.
'''
def moving_zeroes(arr):
  
# iterate through the array if non zero remove it and 
# insert it at the beginning of the list
# remove is returning null so despite passing the tests 
# we aren't actually re-inserting back into the arry the
# actual non-zero values are just None 

    for n in arr:
        if n != 0:
            temp = n
            arr.remove(n)
            arr.insert(0, temp)

    return arr

    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")