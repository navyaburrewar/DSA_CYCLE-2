##### rotated-sorted-array ############
# 
#  arr = [4,5,6,7,0,1,2]
# target = 0

def rotated_array(arr,target):
    start=0
    end=len(arr)-1
    while start <=end:
        mid=(start+end)//2
        if arr[mid]==target:
            return mid
        if arr[start]<arr[end]:
            if arr[start]<=target<arr[mid]:
                end=mid-1
            else:
                start=mid+1
        else:
            if arr[mid]<target<=arr[end]:
                end=mid-1
            else:
                start=mid+1
    return -1   
print(rotated_array([4,5,6,7,0,1,2],0))   
print(rotated_array([4,5,6,7,0,1,2],1))                          
print(rotated_array([4,5,6,7,0,1,2],9))         
           
               