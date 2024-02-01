from typing import *
T = TypeVar('T')
def subsets(items:Sequence[T])->List[List[T]]:
	result=[[]]
	for i in items:
		result+=[subset + [i] for subset in result]
	return result

print(subsets([1,2,3]))
print(subsets(['A','B','C']))