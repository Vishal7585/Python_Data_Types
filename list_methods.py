lst=[1,2,3,4,[5,6,7,8,[9,10,11,12]]]

# append
lst.append([13,14])
print(lst)

# extend
lst.extend([15,16,17])
print(lst)

# insert
lst.insert(-1,18)
print(lst)

# remove
print(lst.remove(17))

# pop
print(lst.pop())

# sort
# print(lst.sort(reverse=True))

# sorted
# print(sorted(lst))

# #reversed
# x=reversed(lst)
# print(lst)
l=['rahul','mayur','vishal']
m=[10,56,89]
print(list(zip(l,m)))
print(dict(zip(l,m)))