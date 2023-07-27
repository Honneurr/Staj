#!/usr/bin/env python
# coding: utf-8

# In[1]:


### Split Strings by Separator

class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        al = []
        for data in words:
            word = data.split(separator)
            for data in word:
                if(data != ""):
                    al.append(data)
        return al            


# In[ ]:


### Plus One

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
        else:
            sayi = len(digits) - 1
            while digits[sayi] == 9:
                digits[sayi] = 0
                sayi -= 1
            if digits == [0] * len(digits):
                digits = [1] + [0] * len(digits)
            else:
                digits[sayi] += 1
        return digits


# In[2]:


### Final Value of Variable After Performing Operations

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        X = 0
        for operation in operations:
            if "++" in operation:
                X += 1
            elif "--" in operation:
                X -= 1
        return X

    


# In[3]:


### Remove Duplicates from Sorted Array

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x=0
        for i in range(1,len(nums)):
            if nums[i] !=nums[x]:
                x+=1
                nums[x]=nums[i]
        return x+1


# In[ ]:


### Two Sum

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a=[]
        for x in range(len(nums)):
            for i in range(x+1,len(nums)):
                if (nums[x]+nums[i]==target):
                    a.append(x)
                    a.append(i)
                    break
                else:
                    continue        
        return a

