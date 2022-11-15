
test_tup=(4,5,4,5,6,6,5,5,4)
print("the original tuple is :"+str(test_tup))
res= defaultdict(int)
for ele in test_tup:
    res[ele]+=1
    print("tuple element frequency is:",+str(dict(res)))
