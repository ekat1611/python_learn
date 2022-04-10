from collections import Counter

s = [1,'r',3,1,2,3,4,5]
x = Counter(s)
for i in x:
    print (x[i])
