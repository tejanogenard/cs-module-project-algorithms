'''
Input: an integer
Returns: an integer
'''
# With the cache, every n value is now only computer once 
# The cache reduced to runtime from O(3^n) to O(n)
# we did increase space complexity 

def eating_cookies(n, cache):
    # Your code here
    if n < 0: 
        return 0
    if n == 0:
        return 1
    # check the cache to see if it holds the answer this branch is looking for
    elif n in cache: 
        return cache[n]
    else: 
    # otherwise, n is not in the cache, so we need to compute the answer the normal way
    # once the answer is computer, save it in the cache 
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
        return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies), {}} ways for Cookie Monster to each {num_cookies} cookies")
