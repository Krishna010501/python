#PRINTING EVEN INDEXES
sentence = "Python is amazing"
word = list(sentence)  
for index in range(len(word)): 
    if index % 2 == 0:  
        print(word[index])

#Replacing spaces with "_"
s = "Python is fun and powerful"
word = s.replace(" ","_")
print(word)

#Checking string contains digits
s = "12345"
if s.isdigit():
    print("The string has digits")

#Printing the string in reverse order
s = "Python is amazing"
word = s[::-1]
print(word)

#Capitalizing the first letter of each word in string
s = "python programming is fun"
word = s.title()
print(word)


