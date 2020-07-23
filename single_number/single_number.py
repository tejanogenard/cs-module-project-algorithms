'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''



def single_number(arr):
    #O(n^2)
    #is this the best we can do? 
    # when looping through the elements, let's count how many tiems 
    # they occur 
    # we use list.count(number) and check if the count == 1 
    
#brute force solution: two nested loops 
# loop through every element in the list 
# loop through every element in the list 
# do a comparison to see if the two elements ever match 

    s = set() # 0(1)
    for x in arr: 
        if x in s:
            s.remove(x)
        else:
            s.add(x)
    
    return list(s)[0]





#Solution_one: 
#     Since i ^ i = 0 for any integer i, and i ^ 0 = i, you have
#     (3 ^ 3) ^ (4 ^ 4) ^ 5 = 0 ^ 0 ^ 5 = 5
    # result = 0
    # for i in arr:
    #     result ^= i
    #     print(result)
    # return result



if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]
    arr2 = [1, 4, 1, 4, 3, 5, 5, 3, 0, 9, 0]

    print(f"The odd-number-out is {single_number(arr)}")