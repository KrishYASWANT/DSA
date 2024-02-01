#kadane's Algorithm
'''Find the max sum of the contineous array sum'''

def maxsum(a):
    csum=a[0]
    osum=a[0]
    for i in range(1,len(a)):
        if(csum>=0):
            csum+=a[i]
        else:
            csum=a[i]
        if(csum>osum):
            osum=csum
    print(osum)

a=eval(input())
maxsum(a)

        
