'''Given an array arr of non-negative integers and an integer sum, the task is to count all subsets of the given array with a sum equal to a given sum.

Note: Answer can be very large, so, output answer modulo 109+7.

Example 1:

Input:
N = 6
arr = [5, 2, 3, 10, 6, 8]
sum = 10
Output:
3
Explanation:
{5, 2, 3}, {2, 8}, {10} are possible subsets.
Example 2:
Input:
N = 5
arr = [2, 5, 1, 4, 3]
sum = 10
Output:
3
Explanation:
{2, 1, 4, 3}, {5, 1, 4}, {2, 5, 3} are possible subsets.
Your Task:
You don't need to read input or print anything. Complete the function perfectSum() which takes N, array arr and sum as input parameters and returns an integer value.

Expected Time Complexity: O(N*sum)
Expected Auxiliary Space: O(N*sum)

Constraints:
1 ≤ N*sum ≤ 106
0 ≤ arr[i] ≤ 106'''

class Solution:
    def perfectSum(self, arr, N, sum):
        dp = [[0]*(sum+1) for _ in range(N)]
        mod = 10**9+7

        for i in range(N):
            for j in range(sum+1):
                sm = j
                item = arr[i]

                if i == 0:
                    if sm == 0:
                        if item == 0:
                            dp[i][j] = 2
                        else:
                            dp[i][j] = 1
                    else:
                        if item == sm:
                            dp[i][j] = 1
                else:
                    item = arr[i]
                    if item <= sm:
                        dp[i][j] = (dp[i-1][sm-item]+dp[i-1][sm]) % mod
                    else:
                        dp[i][j] = dp[i-1][sm]

        return dp[N-1][sum]

# Sample Test Cases
sol = Solution()

# Test Case 1
arr1 = [1, 2, 3]
N1 = len(arr1)
sum1 = 4
result1 = sol.perfectSum(arr1, N1, sum1)
print("Test Case 1:", result1)  # Expected output: 2
# Explanation: There are two ways to get the sum 4: [1, 3] and [2, 2].

# Test Case 2
arr2 = [1, 2, 3, 4, 5]
N2 = len(arr2)
sum2 = 7
result2 = sol.perfectSum(arr2, N2, sum2)
print("Test Case 2:", result2)  # Expected output: 3
# Explanation: There are three ways to get the sum 7: [2, 2, 3], [3, 4], and [5, 2].
