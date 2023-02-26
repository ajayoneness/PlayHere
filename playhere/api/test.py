#QN1

def median_of_number(nums):
    nums.sort()
    mid = nums[0]+nums[-1]
    median = mid/2
    print("median : ",median)

nums =  [3, 5, 2, 1, 4, 6]
median_of_number(nums)




#QN2
listofstr = ["dog", "cat", "car", "race"]
lis= []
for i in range(0,len(listofstr)):
    for j in range(1,len(listofstr)):
        lis.append(listofstr[i]+listofstr[j])

lenlis=[]
for i in lis:
    lenlis.append(len(i))
    index_of_maxstr=lenlis.index(max(lenlis))

print("max length string : ",lis[index_of_maxstr])







#qn3
def fun(nums ,k):
    s=0
    for i in nums:
        s=s+i
        if s==k:
            return True
        else :
            return False

nums = [1, 2, 3, 4]
k = int(input())
fun (nums,k)
