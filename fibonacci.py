# https://leetcode.com/problems/fibonacci-number/
# https://blogs.glowscotland.org.uk/glowblogs/jypetrieuodep/2018/10/09/fibonacci-sequence-significant-coincidence/

# will have to use recursion, or a while loop

# class Solution(object):
#     def fib(self, n):
#         """
#         :type n: int
#         :rtype: int
#         """
#         # solution takes forever
#         if n < 2:
#             return n
#         else:
#             return self.false(n-1) + self.false(n-2)
        
        
        # n = 5 does recursion
            # 2         # 3
        
        # 1 1         # 2                     1 
         #  1 0 1 0     #  1         1        # 1  0
                            # 1 0    # 1  0
            # store in cache
            
    # n = 5
        # have to find fib numbers for all of them
        # n is less than 2 done
        
        
class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        def fib_cache(n, cache):
            if n <= 1:
                return n
            else:
                return fib_cache(n-1) + fib_cache(n-2)
        return fib_cache(n, cache)
            