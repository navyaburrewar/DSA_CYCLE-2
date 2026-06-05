## quesiton
# arr = [1, 3, 5, 7, 9]
# target = 4
# lowerbound

def lowerbound(arr,target):
    start=0
    end=len(arr)-1
    ans=len(arr)   #---> why we use this condition means that when their arr ele are lower then taret then it returns tha last element
    while start<=end:
        mid=(start+end)//2
        if arr[mid]>=target:
            ans=mid
            end=mid-1
        else:
            start=mid+1
    return ans
print(lowerbound([1, 3, 5, 7, 9],4))
