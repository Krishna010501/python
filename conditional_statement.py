#1-Vowel checker

letter = input("Enter the alphabet: ")
if letter in 'aeiouAEIOU':
    print("The letter is a vowel..!")
else :
    print("The letter is a consonant..!")

#Age group classisification:
age = int(input("Enter the age of person?"))
if age >= 0 and age <= 12:
    print("You are a child")
elif age <= 17 and age >= 13:
    print("You are a Teenager")
elif age>=18 and age<=64:
    print("You are an adult")
else:
    print("you are senior")

#Number classification
number = int(input("Enter the number: "))
if number > 0 :
    print("The number is positive.")
elif number == 0 :
    print("The number is zero.")
else :
    print("The number is negative.")

#Leap year calender
year = int(input("Enter the year?"))
if year % 4 ==0 and year % 100 != 0 :
    print(f"The year {year} is a leap year")
else:
    print(f"The year {year} is a non leap year")

#calculator
num_1 = float(input("Enter the first number"))
num_2 = float(input("Enter the second number"))
operator = input("Enter the operation")
if operator == "+" :
    print(f"the result is {num_1+num_2} ")
elif operator == "-" :
    print(f"The result is {num_1-num_2}")
elif operator == "*" :
    print(f"The result is {num_1*num_2}")
elif operator == "/" :
    print(f"The result is {num_1/num_2}")

#short hand if
x = int(input("Enter the number "))
result = "even" if x % 2 ==0 else "odd"
print(result)

#discount calculator
amount = float(input("Enter the price? "))
discount = float(input("Enter the dicount? "))
if discount > 0 :
    print(f"The final amount is {(amount*discount)/100}")
else :
    print(f"The final is {amount} and discount is not applicable")


age = int(input("Enter age "))
print("Eligible") if age > 18 else print("Not Eligible")