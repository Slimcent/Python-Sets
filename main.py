def my_set():
    this_set = {"apple", "banana", "cherry", "mango"}
    return this_set


tropical = {"pineapple", "mango", "papaya"}

mylist = ["kiwi", "orange"]

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

mySet = my_set()
print(mySet)

print(len(mySet))

# Access set items
for x in mySet:
    print(x)

print()

print("banana" in mySet)

# Adding to a set
mySet.add("orange")
print(mySet)

# Adding to a set
mySet.update(tropical)
print(mySet)

print()

mySet.update(mylist)  # Adding an iterable eg a list to a set
print(mySet)
print()

# Removing from a set
mySet.remove("banana")
print(mySet)

mySet.remove("kiwi")
print(mySet)

x = mySet.pop()
print(x)
print(mySet)
print()

# Looping through a set
for x in mySet:
    print(x)

print()

# Joining sets
set3 = set1.union(set2)
print(set3)

print()

set1.update(set2)
print(set1)

print()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.intersection_update(y)  # Keep the items that exist in both set x, and set y
print(x)

z = x.intersection(y)  # returns a new set, that only contains the items that are present in both sets
print(z)

# x.symmetric_difference_update(y)  # will keep only the elements that are NOT present in both sets
# print(x)

z = x.symmetric_difference(y)  # returns a new set, that contains only the elements that are NOT
print(z)


