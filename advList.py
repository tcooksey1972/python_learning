lucky_numbers = [3, 7, 8, 13, 54, 69]
friends = ("John", "David", "Luke", "Job", "Mark")

# Convert friends from tuple to a list
friends = list(friends)

#add another value to a list
friends.append("Noah")


#add a value to a specific position in the list
friends.insert(3, "Matt")
print(friends)

#remove a value from the list
friends.remove("Noah")
print(friends)

#Remove the last element from the list using pop method
friends.pop()
print(friends)

#sort the list in assending order
friends.sort()
print(friends)
#sort the list in decending order
lucky_numbers.reverse()
print(lucky_numbers)

#make a copy of an existing list
friends2 = friends.copy()
print(friends2)

#Look for a certian value in our list
print(friends.index("Luke"))

# Extend the list with lucky_numbers
friends.extend(lucky_numbers)

print(friends)

#remove all from list
friends.clear()
print(friends)
