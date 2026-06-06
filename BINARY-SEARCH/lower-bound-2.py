# <!-- For lower bound, you want:

# the smallest element that is still greater than or equal to the target.

# In simple words:

# Find the first number that is not smaller than target. -->



def lower_bound(arr, target):    # [1,2,3,4,6]    t=4
 
    low = 0                      # 3
    high = len(arr) - 1       # 4 3

    ans = len(arr)             #4    3 

    while low <= high:           

        mid = low + (high - low) // 2       #0+4/2=2      3+4/2= 3

        if arr[mid] >= target:          # 3>=4            4>=4 
            ans = mid                                     # ans=3
            high = mid - 1                                 # 3

        else:                             # low=3
            low = mid + 1

    return ans
print(lower_bound([2,4,6,8],6))