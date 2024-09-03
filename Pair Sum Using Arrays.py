def pairSum(nums,target):
    seen={}
    
    for index,num in enumerate(nums):
        complement=target-num
         
        if complement in seen:
            return [seen[complement],index]
        else:    
            seen[num]=index
            
numbers=[2,11,7,15]
target=9
print(pairSum(numbers,target))