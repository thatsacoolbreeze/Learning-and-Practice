# This prints out "Hello, Jake!"
name = "Jake"
age = 26

print("Hello, %s!" % name)
print("Hello, %s! You are %d years old." % (name, age))


# this prints out: A list [1, 2, 3]
my_list = [1, 2, 3]
print(my_list)
print("A list %s" % my_list)

#Exercise: have the code print out Hello, Jake! Your current balance is $53.44.
data = ("Jake", 53.44)
format_string = "Hello, %s! Your current balance is $%.2f." 
print(format_string % data)

