#Remove the intersection of a 2nd set from the 1st set.

s1={15,22,34,40,58,64}
s2={4,5,6,7,8,9}

print(s1.intersection(s2))

# #Update a set to equal the intersection of it and another set
# intersection_update()
s1={15,22,34,40,58,64}
s2={4,5,6,7,8,9}
print(s1.intersection_update(s2))
# #Remove an element from a set if it exists
# discard()
numbers={10,20,30,40}
numbers.discard(3) 

print(numbers)

# #Remove and return an unspecified element from a set
# pop()
items={"seat","book","pen"}
removed_item = items.pop()
print(removed_item)


#  #Remove an element from a set
# remove()
agegroup={"baby","child","youth","adult"}
agegroup.remove("youth")

print(agegroup)

# Find the elements in set1 that are not in set2
set1={15,16,17,18,19}
set2={12,13,14,15,16}

print(set1.difference(set2)) 

# #Find the union of 2 sets.
# union()

nums1= {10, 11, 12}
nums2 = {9, 11, 12}

print( nums1.union(numbers2))

#Remove all elements from a set
# clear()
# set of prime numbers
Numbers = {16,17,18,19,20}
Numbers.clear()

print(Numbers)


#Add all elements from another set to an existing set
# update()
names = {"matthew","beatrice"}
age= {20,18}

# updates A after the items of B is added to A
names.update(age)

print(names)


