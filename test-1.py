
# Element greater than neighbors.

# Example:

# [1,2,5,7,6,3]
# peak =7

def peak(arr): 
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]<arr[mid+1]:
            low=mid+1
        else:
            high=mid 
    return low

print(peak([1,2,5,7,6,3]))



