thislist = ["apple", "banana", "cherry"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
print(len(thislist))


thislist = ["apple", "banana", "cherry"]
print(len(thislist))

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#Access list
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
#Change list

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#Add list

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#Remove list

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)


thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)


thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)


thislist = ["apple", "banana", "cherry"]
del thislist
print(thislist) #this will cause an error because you have succsesfully deleted "thislist".


thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#Loop list


thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
  
  
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  
  
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
  
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]


#List Comprehension


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


newlist = [x for x in range(10)]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)


#Sort Lists

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort(key = str.lower)

print(thislist)



thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Copy Lists

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)


thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)


thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)


# Join Lists


list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)


list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#List Methods

fruits = ['apple', 'banana', 'cherry']

x = fruits.count("cherry")


fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")


fruits = ['apple', 'banana', 'cherry']

fruits.remove("banana")


