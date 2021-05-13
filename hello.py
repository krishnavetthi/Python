message = "Hello World"
print(message)

# In a certain encrypted message which has information about the location(area, city), 
# the characters are jumbled such that first character of the first word is followed by the first character of the second word, 
# then it is followed by second character of the first word and so on
#In other words, let’s say the location is bandra,mumbai
#The encrypted message says ‘bmaunmdbraai’
#Let’s say the size or length of the two words wouldn’t match then the smaller word is appended with # and then encrypted in the above format.

input_str = input("Enter")
message1 = input_str[0::2]
message2 = input_str[1::2]
print(message1.strip('#') + "," + message2.strip('#'))


#String Methods
# upper()
# lower()
# strip()
# lstrip()
# rstrip()
# count(substring, beg, end)

