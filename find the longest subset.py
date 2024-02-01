def long(a):
    Charset=set()
    l=0
    res=0
    for r in range(len(a)):
    	while a[r] in Charset:
            Charset.remove(a[l])
            l+=1
        
        Charset.add(a[r])
        res=max(res,r-l+1)
    return res


print(long('abcabcde'))
