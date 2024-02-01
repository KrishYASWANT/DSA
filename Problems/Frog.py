def frog(a, arr):
    dp = [float('inf')] * a
    dp[0] = 0  # Energy used to reach the 1st stair is 0

    for i in range(1, a):
        dp[i] = min(dp[i], dp[i - 1] + abs(arr[i] - arr[i - 1]))
        if i > 1:
            dp[i] = min(dp[i], dp[i - 2] + abs(arr[i] - arr[i - 2]))

    return dp[-1]  # Minimum energy to reach the last stair

print(frog(4, [10, 20, 30, 10]))
""" Problem statement
There is a frog on the '1st' step of an 'N' stairs long staircase. The frog wants to reach the 'Nth' stair. 'HEIGHT[i]' is the height of the '(i+1)th' stair.If Frog jumps from 'ith' to 'jth' stair, the energy lost in the jump is given by absolute value of ( HEIGHT[i-1] - HEIGHT[j-1] ). If the Frog is on 'ith' staircase, he can jump either to '(i+1)th' stair or to '(i+2)th' stair. Your task is to find the minimum total energy used by the frog to reach from '1st' stair to 'Nth' stair.

For Example
If the given ‘HEIGHT’ array is [10,20,30,10], the answer 20 as the frog can jump from 1st stair to 2nd stair (|20-10| = 10 energy lost) and then a jump from 2nd stair to last stair (|10-20| = 10 energy lost). So, the total energy lost is 20.

def jump(i,arr):
    #base case
    if i==0:
        return 0
        
    left=jump(i-1,arr)+abs(arr[i-1]-arr[i])
    if (i>1):
        right=jump(i-2,arr)+abs(arr[i-2]-arr[i])
    return min(left,right)
    
def frog(a,arr):
    return jump(a-1,arr)

print(frog(4,[10,20,30,10]))

"""