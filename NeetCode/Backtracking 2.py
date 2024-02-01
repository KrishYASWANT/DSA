from typing import List
class solution:
	def permuteUnique(self,nums:List[int])->List[List[int]]:
		res=[]
		perm=[]
		count={ n:0 for n in nums}
		for n in nums:
			count[n]+=1
		def dfs():
			if len(perms)== len(nums):
				res.append(perms.copy())
				return

			for n in count:
				if count[n]>0:
					perms.append(n)
					count[n]-=1

					dfs()

					count[n]+=1
					perms.pop()

			dfs()
		return res

s=solution()
print(s.permuteUnique([3,3,1,4]))