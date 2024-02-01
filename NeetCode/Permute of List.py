'''Given an List The aim is to find the number of permutations 
and return the List[of permutations it can make]'''
from typing import List
class Sol:
	def permute(self,nums:List[int])->List[List[int]]:
		res=[]

		#Base Case
		if(len(nums)==1):
			return [nums[:]]

		for i in range(len(nums)):
			n=nums.pop(0)
			perms =self.permute(nums)

			for perm in perms:
				perm.append(n)
			res.extend(perms)
			nums.append(n)
		return res
s=Sol()
nums=[1,2,3]
print(s.permute([3,2,1,4]))