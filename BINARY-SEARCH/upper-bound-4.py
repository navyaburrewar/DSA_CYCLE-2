## upper bound which is here nothing but we haveb to find the value which is less than target and highest value if target is notpresent else we have return target

#arr=[1,2,3,5,6,7]
# target=4  -->so hence upper-bound we have return value lessthan or equal to
#  target and upper

def upper_bound(arr,target):
    start=0
    end=len(arr)-1
    ans=start
    while start<=end:
        mid=(start+end)//2
        if arr[mid]<=target:
            ans=mid
            start=mid+1
        else:
            end=mid-1
    return ans            
print(upper_bound([9,2,3,5,6,7],8))