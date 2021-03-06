import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# BTS with O(n) runtime complexity
root_node = BSTNode(names_1[0]) # first item in list is root in our BST.
for name_1 in names_1:
    root_node.insert(name_1) # insert all names into BST
for name_2 in names_2:
    if root_node.contains(name_2): # use our contains function on tree we created from names_1 to look for duplicates.
        duplicates.append(name_2) # append duplicates


# Two nested loops have quadratic runtime complexity of o(n squared)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds\n")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
start_time = time.time()
set1 = set(names_1)
set2 = set(names_2)

list3 = list(set1.intersection(set2))
end_time = time.time()
print(f"{len(list3)} duplicates:")
print(list3)
print (f"\nruntime: {end_time - start_time} seconds\n")

