#NOTE: Sets are immutable.
s1={1,2,7,8}
s2={3,4,5,6,8}
print(s1.union(s2))
print(s1,s2)              
#To change the value of s1 or s2 we use update keyword.
s1.update(s2)
print(s1)  #Here s1 is updated.


s3={"Hello","Hi"}
s4={"Hi","Namastay"}
s3.intersection_update(s4)
print(s3)

#symmetric_difference_update  -> It print those value which are not common in both the sets.
s5={"Nepal","China"}
s6={"China","Japan"}
s5.symmetric_difference_update(s6)
print(s5)

#symmetric_differece
s7={"Nepal","China"}
s8={"China","Japan"}
result=s7.difference(s8)
s7.difference(s8)
print(result)
s7.difference_update(s8)
print(s7)


#isdisjoint 
""" In set theory in mathematics and formal logic, 
two sets are said to be disjoint sets if they have no element in common."""
a1={"ram","shyam","hari"}
a2={"manju","manjil","manjila"}
a=a1.isdisjoint(a2)
a1.update(a2)
print(a)            #condition fail the true return
                    # otherwise false

#superset 
"""In math, a superset is a set that contains
 all the elements of another set, called a subset. """
a3={"ram","shyam","hari"}
a4={"ram","shyam","hari","kanchi"}
re=a3.issuperset(a4)
print(re)
"""In math, a subset is a collection of elements that are also part of a larger set"""
re1=a3.issubset(a4)
print(re1)

#add()
l1={"ram","shyam","hari"}
l1.add("manjil")
print(l1)

#remove()/discard()
l1.remove("manjil")
print(l1)
l1.discard("ram")
print(l1)


#del()
del(l1)
# print(l1)->Throw error because l1 is alresdy deleted.


#pop  -> take out the random element from the set.
l5={"ram","shyam","hari"}
l5.pop()
print(l5)

#clear()
l3={"ram","shyam","hari"}
l3.clear()
print(l3)


