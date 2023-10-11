'''Given an array arr[] of size N, check if it can be partitioned into two parts such that the sum of elements in both parts is the same.

Example 1:

Input: N = 4
arr = {1, 5, 11, 5}
Output: YES
Explanation:
The two parts are {1, 5, 5} and {11}.
Example 2:

Input: N = 3
arr = {1, 3, 5}
Output: NO
Explanation: This array can never be
partitioned into two such parts.
Your Task:
You do not need to read input or print anything. Your task is to complete the function equalPartition() which takes the value N and the array as input parameters and returns 1 if the partition is possible. Otherwise, returns 0.

Expected Time Complexity: O(N*sum of elements)
Expected Auxiliary Space: O(N*sum of elements)

Constraints:
1 ≤ N ≤ 100
1 ≤ arr[i] ≤ 1000
N*sum of elements ≤ 5*106'''


class Solution:
    def equalPartition(self, N, arr):
        total_sum = sum(arr)

        # If the total sum is odd, it cannot be divided into two equal parts
        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2

        # Initialize a memoization table to store intermediate results
        memo = {}

        def canPartition(index, current_sum):
            # Base case: If the current sum is equal to the target sum, we found a valid partition
            if current_sum == target_sum:
                return True

            # If we have considered all elements or the current sum exceeds the target sum, return False
            if index == 0 or current_sum > target_sum:
                return False

            # Check if we can either include or exclude the current element
            # If either of these options leads to a valid partition, return True
            if (index, current_sum) not in memo:
                include_current = canPartition(index - 1, current_sum + arr[index - 1])
                exclude_current = canPartition(index - 1, current_sum)
                memo[(index, current_sum)] = include_current or exclude_current

            return memo[(index, current_sum)]

        # Start the recursive function from the last element of the array
        return canPartition(N, 0)

# Example usage
solution = Solution()
N = 4
arr = [1, 5, 11, 5]
print(solution.equalPartition(N, arr))  # Output: True
