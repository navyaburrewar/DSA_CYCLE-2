def target_ele(arr,target):
    start=0
    end=len(arr)-1
    while start <=end:
        mid=(start+end)//2
        if target==arr[mid]:
            return mid
        elif target<arr[mid] :
            end=mid-1
        else:
            start=mid+1

    return -1
print(target_ele([1,2,3,4,5],4))        


  