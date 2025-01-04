'''Write a Python program that takes a character as input and checks whether it is a vowel or not.
Use the if-else statement.'

alphabet = input("Enter the alphabet: ")
if alphabet in "aeiouAEIOU" :
    print(f"The alphabet {alphabet} is vowel.")
else:
    print(f"The alphabet {alphabet} is consonant ")


'''Table printing'''
# table = int(input("Enter the number: "))
for i in range(1,21):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print()'''

# for i in range (5) :
#     for j in range (5): 
#         print (i,j)


