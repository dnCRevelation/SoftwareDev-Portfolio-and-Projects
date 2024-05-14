# Piling Up!

from collections import deque

def vert_piling_up(n, cubes):          # n = number of cubes, cubes = a deque of integers representing the length of the cubes
    while cubes:
        lg_cube = cubes.popleft() if cubes[0] > cubes[-1] else cubes.pop()  # Grabs the larger of the two cubes and checks if it's larger than the next cube to be removed
        if not cubes:       # If all cubes are checked and it hasn't returned no, the function returns "Yes"
            return "Yes"
        if cubes[-1] > lg_cube or cubes[0] > lg_cube: # If the following cube is larger than lg_cube, it returns "No"
            return "No"

T = int(input())    # number of test cases

for n in range(T):      # Runs a loop through the amount of test cases input
    n, cubes = input(), deque(map(int, input().split()))  # Assigns the number of cubes and the length to user input and applies deque to allow for appending the vertical order of cubes
    print(vert_piling_up(n, cubes)) # Executes the function I created and uses the assigned iteration variable in place to represent the number of cubes and the length 

# Sample Input
# 2
# 6
# 4 3 2 1 3 4
# 3
# 1 3 2
# Sample Output
# Yes
# No

# Explanation
# In the first test case, pick in this order: left - 4, right - 4, left - 3, right - 3, left - 2, right - 1.
# In the second test case, no order gives an appropriate arrangement of vertical cubes. 3 will always come after either 1 or 2.

# Time Complexity: O(n)
# Space Complexity: O(n)
# where n is the number of cubes
# The time complexity is O(n) because we iterate through the cubes once. The space complexity is O(n) because we store the cubes in a deque.

# Approach
# 1. Iterate through the cubes.
# 2. Check if the leftmost or rightmost cube is bigger.
# 3. If the leftmost or rightmost cube is bigger than the big cube, return "No".
# 4. If there are no cubes left, return "Yes".
# 5. Otherwise, continue iterating through the cubes.
# 6. If the leftmost or rightmost cube is bigger than the big cube, return "No".
# 7. If there are no cubes left, return "Yes".
# 8. Otherwise, continue iterating through the cubes.
# 9. Repeat steps 6-8 until there are no cubes left.
# 10. Return "Yes" if there are no cubes left.
# 11. Return "No" if the leftmost or rightmost cube is bigger than the big cube.

# The code passes all test cases on HackerRank