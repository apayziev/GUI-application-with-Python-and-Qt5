#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'counts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY teamA
#  2. INTEGER_ARRAY teamB
#

# Football Scores

# The number of goals achieved by two football teams in matches in a league is given in the form of two lists. For each match of team B, compute the total number of matches of team A where team A has scored less than or equal to the number of goals scored by team B in that match.

# Example

# teamA = [1, 2, 3]

# teamB = [2, 4]

# Team A has played three matches and has scored teamA = [1, 2, 3] goals in each match respectively. Team B has played two matches and has scored teamB = [2, 4] goals in each match respectively. For 2 goals scored by team B in its first match, team A has 2 matches with scores 1 and 2. For 4 goals scored by team B in its second match, team A has 3 matches with scores 1, 2 and 3. Hence, the answer is [2, 3].

# Function Description

# Complete the function counts in the editor below.

# counts has the following parameter(s):

# int teamA[n]: first array of positive integers int teamB[m]: second array of positive integers 

# Return

# int[m]: an array of m positive integers, one for each teamB[i] representing the total number of elements from teamA[j] satisfying teamA[j] ≤ teamB[i] where 0≤j < nand 0≤i < m, in the given order.

# Constraints

# • 2 ≤n, m≤ 105

# • 1 steamA[j] ≤ 10 % , where 0≤j < n.

# • 1 ≤ teamB[i] ≤ 10⁹, where O <= i < m.



def counts(teamA, teamB):
    # Write your code here
    result = []
    for i in teamB:
        count = 0
        for j in teamA:
            if j <= i:
                count += 1
        result.append(count)
    
    return result



# Time limit exceeded
# Allowed time limit: 10 secs
# Your code did not execute in time. Please optimize your code.


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    teamA_count = int(input().strip())

    teamA = []

    for _ in range(teamA_count):
        teamA_item = int(input().strip())
        teamA.append(teamA_item)

    teamB_count = int(input().strip())

    teamB = []

    for _ in range(teamB_count):
        teamB_item = int(input().strip())
        teamB.append(teamB_item)

    result = counts(teamA, teamB)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
