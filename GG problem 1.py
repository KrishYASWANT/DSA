from typing import *
T = TypeVar('T')
def subsets(items:Sequence[T])->List[List[T]]:
	result=[[]]
	for i in items:
		result+=[subset + [i] for subset in result]
	return result

a=subsets([1,2,2,3,2,1])
#print(a[1::])

c=[]
for i in a[1::]:
    d={}
    for q in i:
        d[q]=d.get(q,0)+1
    s_max=max(d.keys())
    m=max(i)
    #for k,v in d.items():
        #print(k,v)
    #print("Given subset was",i)
    #print("S_max:",s_max)
    if max(d.values())<s_max:
        c.append(i)
ans = set(tuple(subset) for subset in c)
print(ans)
print(len(ans))
