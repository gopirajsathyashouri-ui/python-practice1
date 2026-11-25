class Solution:
    def reverse(self, x):
        x1 = x[: : -1]
        return(x1)

result = Solution()
x = eval(input())
print(result.reverse(x))