'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''


def single_number(arr):

#  if we add each number once and multiply the sum by 2, we will get twice the sum of each element of the array.
#  Then we will subtract the sum of the whole array from the twice_sum and get the required number (which appears once in the array).

# Array [] : [a, a, b, b, c, c, d]
# Mathematical Equation = 2*(a+b+c+d) – (a + a + b + b + c + c + d)

# In more simple words: 2*(sum_of_array_without_duplicates) – (sum_of_array)
 
        #Possible future solution
    # we want to loop through the entire array and check for duplicates. 
    # how can we check for duplicates ?  
    # we check the first number index = 0 against every other number inside the array,
    # if we find a duplicate then remove the duplicates from the array
    # else, this means that our number is the single_number inside the array
    # Note "you can call single_number again until you finally reach 1 single number inside the entire array, then return that number "


    # Your code here

    # why is this to be considered to be inefficent ? 

    return 2 * sum(set(arr)) - sum(arr) # O(n) runtime? 

     
     

  
  

 


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")