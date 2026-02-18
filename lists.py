# -- Lists --
# [1] List Items Are Enclosed in Square Brackets
# [2] List Are Ordered, To Use Index To Access Item
# [3] List Are Mutable => Add, Delete, Edit
# [4] List Items Is Not Unique
# [5] List Can Have Different Data Types

myAwesomeList = ["One", "Two", "One", 1, 100.5, True]

print(myAwesomeList)  # Whole List
print(myAwesomeList[1])  # "Two"
print(myAwesomeList[-1])  # True
print(myAwesomeList[-3])  # 1

print(myAwesomeList[1:4])  # ['Two', 'One', 1]
print(myAwesomeList[:4])  # ['One', 'Two', 'One', 1]
print(myAwesomeList[1:])  # ['Two', 'One', 1, 100.5, True]

print(myAwesomeList[::1])  # ['One', 'Two', 'One', 1, 100.5, True]
print(myAwesomeList[::2])  # ['One', 'One', 100.5]

# -- Lists Methods --

# append()
myFriends = ["zaina", "Batool", "Lana"]
myOldFriends = ["layan", "Samah", "Nameer"]

myFriends.append("Alaa") #str
myFriends.append(100) #int
myFriends.append(150.200) #float
myFriends.append(True) #bool
myFriends.append(myOldFriends) #list inside a list 

print(myFriends)
print(myFriends[2]) #Lana
print(myFriends[7][2]) #Nameer

# extend()
a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["One", "Two"]

a.extend(b) #add list b to list a and make it one list 
a.extend(c)

print(a)

# remove()
x = [1, 2, 3, 4, 5, "Zaina", True, "Zaina", "Zaina"]
x.remove("Zaina") #Remove the first element 
print(x) #[1,2,3,4,5,True,"Zaina","Zaina"]

# sort()
y = [1, 2, 100, 120, -10, 17, 29]
# y = ["A", "Z", "C"]
y.sort(reverse=True) #sort them in the opposite way  
print(y)

# reverse()
z = [10, 1, 9, 80, 100, "Zaina", 100]
z.reverse() #without sorting 
print(z)

# clear()
a = [1, 2, 3, 4]
a.clear() #Remove all items from list
print(a)

# copy()
b = [1, 2, 3, 4]
c = b.copy() #Return all shallow copy of the list 
print(b)  # Main List
print(c)  # Copied List

# count()
d = [1, 2, 3, 4, 3, 9, 10, 1, 2, 1]
print(d.count(1))

# index()
e = ["zaina", "Batool", "Lana", "layan", "Samah", "Nameer"]
print(e.index("layan")) #3

# insert()
f = [1, 2, 3, 4, 5, "A", "B"]
f.insert(0, "Test")
print(f)

# pop()
g = [1, 2, 3, 4, 5, "A", "B"]
print(g.pop(-3)) #Remove and return item at index
