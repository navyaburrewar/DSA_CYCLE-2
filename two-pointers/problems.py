# 1	Reverse String	344
# 2	Valid Palindrome	125
# 3	Valid Palindrome II	680
# 4	Reverse Vowels of a String	345
# 5	Merge Strings Alternately	1768
# 6	Move Zeroes	283
# 7	Remove Element	27
# 8	Remove Duplicates from Sorted Array	26
# 9	Remove Duplicates from Sorted Array II	80
# 10	Squares of a Sorted Array	977





## 	Reverse String  

s=["n","a","v","y","q"]


left=0
right=len(s)-1

while left <right:
    s[left],s[right]=s[right],s[left]
    left+=1
    right-=1

print(s)    



# 2	Valid Palindrome
s="({[]})"
left=0
right=len(s)-1
while left<right:
    if s[left]!=s[right]:
        print("not palindrome")
        break
    left+=1
    right-=1
else:

    print("valid")    

     