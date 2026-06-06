## last occurance:
# arr=[1,2,3,4,5,6,6,7]
# target=6
def last_occurance(arr,target):
    start=0
    end= len(arr)-1
    ans=-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            ans=mid
            start=mid+1
        elif arr[mid]<target:
            start=mid+1
        else:
            end=mid-1

    return ans
print(last_occurance([1,2,3,4,5,6,6,7],6))

                
