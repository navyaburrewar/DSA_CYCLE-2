#Stable counting sort--------------
#a = [3, 3, 2, 4]
"""
def count_sort(arr):

    max_val = max(arr)

    count = [0]*(max_val+1)#[0 0 0 0 0] = [0 0 1 2 1]

    #freq
    for num in arr:
        count[num]+=1

    #cumulative count

    for i in range(1, len(count)): #[0 0 1 3 4]
        count[i]+=count[i-1]

    output = [0]*len(arr)

    #right-left--

    for j in reversed(arr):
        output[count[j]-1] = j
        count[j]-=1

    return output


b= [3, 3, 2, 4]
a = [8,6,4,9,1,2]

print(count_sort(a))
print(count_sort(b)) 

"""

### prob-2 

def counting_sort(arr):
    max_value=max(arr)   #9
    count=[0]*(max_value+1) #[0,1,0,1,1,0,0,0,2,1]

    for i in arr:
        count[i]+=1

    for i in range(1,len(count)): #[0,1,1,2,3,3,3,3,5,6,] 
        count[i]+=count[i-1]      #[0,1,2,3,4,5,6,7,8,9]

    output=[0]*len(arr)  # [0,0,0,0,0,0]

    for j in reversed(arr): #[8,3,1,8,4,9]

        output[count[j]-1]=j    # output[count[8]-1]=8  ---> output[4]=8
        count[j]-=1              # output[count[3]-1]=3---> output[1]=3
                                 # output[count[1]-1]=1---> output[0]=1
                                 # output[count[8]-1]=8---> output[3]=8
    return output               # output[count[4]-1]=4---> output[2]=4    
                                # output[count[9]-1]=9---> output[5]=9
arr=[9,4,11,1,3,1,1]

print(counting_sort(arr))







    



   