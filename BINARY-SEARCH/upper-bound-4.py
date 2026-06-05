## upper bound which is here nothing but we haveb to find the value which is less than target and highest value if target is notpresent else we have return target

#arr=[1,2,3,5,6,7]
# target=4  
def upper_bound(arr,target):
    start=0
    end=len(arr)-1
    ans=len(arr)
    while start<=end:
        mid=(start+end)//2
        if arr[mid]>target:
            ans=mid
            end=mid-1
        else:
            start=mid+1
    return ans            
print(upper_bound([1,2,3,5,6,7],8))