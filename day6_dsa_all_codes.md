# 📚 Day 6 – DSA Practice in Python



### 📌 acronym_gen.py
```python
 def isAcronym(words,s):
        n=len(words)
        return n[0]
```


### 📌 com_sum.py
```python
def generate(ind,curr,ans,candidates,target):
    if (target==0):
        ans.append(curr.copy())
        return
    if(target<0):
        return
    if(ind==len(candidates)):
        return 
    curr.append(candidates[ind])
    generate(ind+1,curr,ans,candidates,target-candidates[ind])
    curr.pop()
    for i in range(ind+1,len(candidates)):
        if(candidates[ind]!=candidates[i]):
            generate(i,curr,ans,candidates,target)
            break
def comibinations(candidates,target):
    candidates.sort()
    ind=0
    curr=[]
    ans=[]
    generate(ind,curr,ans,candidates,target)
    return ans
candidates=[1,2,3,4,7]
target=5
print(comibinations(candidates,target))
```


### 📌 pow(x,n).py
```python
def pow(x,n):
    if(n<0):
        x=1/x
    n=abs(n)
    ans=1
    for i in range(n):
        ans=ans*x
    return ans 
print(pow(2,49))

    
```


### 📌 subseq.py
```python
'''def check(ind,arr,k):
    if (k==0):
        return True
    if(k<0):
        return False
    if(ind==len(arr)):
        return False
    path1=check(ind+1,arr,k-arr[ind])
    if(path1==True):
        return True
    path2=check(ind+1,arr,k)
    return path1 or path2
def checksubseqsum(n,arr,k):
    ind=0
    return check(ind,arr,k)
print(checksubseqsum(n,arr,k))'''
```


### 📌 subsets.py
```python
def generate(ind,curr,ans,nums):
    if(ind==len(nums)):
        ans.append(curr.copy())
        return
    curr.append(nums[ind])
    generate(ind+1,curr,ans,nums)
    curr.pop()
    generate(ind+1,curr,ans,nums)
def subsets(nums):
    ind=0
    curr=[]
    ans=[]
    generate(ind,curr,ans,nums)
    return ans
nums=[1,2,3]
print(subsets(nums))
```


### 📌 untit.py
```python
def generate(ind,curr,ans,candidates,target):
    if (target==0):
        ans.append(curr.copy())
        return
    if(target<0):
        return
    if(ind==len(candidates)):
        return 
    curr.append(candidates[ind])
    generate(ind,curr,ans,candidates,target-candidates[ind])
    curr.pop()
    generate(ind+1,curr,ans,candidates,target)
def comibinations(candidates,target):
    ind=0
    curr=[]
    ans=[]
    generate(ind,curr,ans,candidates,target)
    return ans
candidates=[2,3,6,7]
target=5
print(comibinations(candidates,target))
```


### 📌 valid_parenthsis.py
```python
def generate(ind,curr_ste,ans,o,c,n):
    if(o==c and ind==2*n):
        ans.append(curr_ste)
        return
    if(o>n):
        return
    generate(ind+1,curr_ste+"(",ans,o+1,c,n)
    if(o>c):
        generate(ind+1,curr_ste+")",ans,o,c+1,n)

def generateparenthsis(n):
    ind=0
    curr_ste=""
    ans=[]
    o=0
    c=0
    generate(ind,curr_ste,ans,o,c,n)
    return ans
print(generateparenthsis(2))
```
