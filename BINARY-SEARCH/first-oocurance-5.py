## first occurance

# arr=[1,2,2,3,4,5,3,5]
# target=3
def first_occurance(arr,target):

    start=0
    end=len(arr)-1
    ans=-1
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            ans=mid
            end=mid-1
        elif arr[mid]<target :
            start=mid+1
        else:
            end=mid-1
    return ans

print(first_occurance([1,2,2,3,3,4,5,5],3))
               