numbers = []
strings = []
names = ["John", "Eric", "Jessica"]

# write your code here, below this line, I added the numbers 1, 2, and 3 to the numbers list and the strings "Hello" and "world" to the strings list.
numbers.append(1)
numbers.append(2)
numbers.append(3)
strings.append("Hello") 
strings.append("world")


second_name = [names[1]]


# this code should write out the filled arrays and the second name in the names list (Eric).
print(numbers)
print(strings)
print("The second name on the names list is %s" % second_name)