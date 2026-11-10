astring = "Hello world!"
astring2 = 'Hello world!'

#this prints out: Hello world!

astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))

#it prints out: 12 because the length of the string is 12 characters long

astring = "Hello world!"
print(astring.index("o"))

#it prints out: 4 because the first occurrence of the letter "o" is at index 4, remeber that the index starts at 0

astring = "Hello world!"
print(astring.count("l"))

#it prints out: 3 because the letter "l" occurs 3 times in the string

astring = "Hello world!"
print(astring[3:7])
#it prints out: lo w because it prints characters from index 3 to 6 (the end index is not included)

astring = "Hello world!"
print(astring[3:7:2])
#it prints out: l because it prints characters from index 3 to 6 with a step of 2
#follows the format: string[start:end:step]

astring = "Hello world!"
print(astring[3:7])
print(astring[3:7:1])
#it prints out: lo w because it prints characters from index 3 to 6 with a step of 1
#both of these print statements will print the same output because the default step is 1
#note, there is no function to reverse a string, but you can use slicing to reverse a string by using a negative step

print(astring[::-1])
#it prints out: !dlrow olleH because it prints the string in reverse order by using a negative step of -1

astring = "Hello world!"
print(astring.upper())
print(astring.lower())

#it prints out: HELLO WORLD! because it converts the string to uppercase
#it prints out: hello world! because it converts the string to lowercase    

astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))
# it prints out: True because the string starts with "Hello"
# it prints out: False because the string does not end with "asdfasdfasdf"

astring = "Hello world!"
afewwords = astring.split(" ")
print(afewwords)
#it prints out: ['Hello', 'world!'] because it splits the string into a list of words using the space character as the delimiter
# split() is a method that splits a string into a list of substrings based on a specified delimiter. In this case, the delimiter is a space character, so the string is split into two substrings: "Hello" and "world!". The resulting list is then printed to the console.

#Exercise

#s = "Hey there! what should this string be?"
s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5]) # Start to 5
print("The next five characters are '%s'" % s[5:10]) # 5 to 10
print("The thirteenth character is '%s'" % s[12]) # Just number 12
print("The characters with odd index are '%s'" %s[1::2]) #(0-based indexing)
print("The last five characters are '%s'" % s[-5:]) # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))