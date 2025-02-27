s1={1,2,3,45,5}
s2={1,2,3,4,5,6,7,8}
print(s1.union(s2))
s1.update(s2)
print(s1,s2)

a={1,2}
b={2,3}
a.intersection_update(b)
print(a,b)

