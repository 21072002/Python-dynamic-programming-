'''Given an array of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.


Example 1:

Input:
N = 6
arr[] = {3, 34, 4, 12, 5, 2}
sum = 9
Output: 1
Explanation: Here there exists a subset with
sum = 9, 4+3+2 = 9.
Example 2:

Input:
N = 6
arr[] = {3, 34, 4, 12, 5, 2}
sum = 30
Output: 0
Explanation: There is no subset with sum 30.

Your Task:
You don't need to read input or print anything. Your task is to complete the function isSubsetSum() which takes the array arr[], its size N and an integer sum as input parameters and returns boolean value true if there exists a subset with given sum and false otherwise.
The driver code itself prints 1, if returned value is true and prints 0 if returned value is false.


Expected Time Complexity: O(sum*N)
Expected Auxiliary Space: O(sum*N)


Constraints:
1 <= N <= 100
1<= arr[i] <= 100
1<= sum <= 105

'''

class Solution:
    def perfectSum(self, arr, N, sum):
        dp = [[0]*(sum+1) for _ in range(N)]
        mod = 10**9+7
        for i in range(N):
            for j in range(sum+1):
                sm = j
                item = arr[i]
                if i==0:
                    if sm==0:
                        if item==0:
                            dp[i][j] = 2
                        else:
                            dp[i][j] = 1
                    else:
                        if item==sm:
                            dp[i][j] = 1
                else:
                    item = arr[i]
                    if item<=sm:
                        dp[i][j] = (dp[i-1][sm-item]+dp[i-1][sm])%mod
                    else:
                        dp[i][j] = dp[i-1][sm]
        return dp[N-1][sum]