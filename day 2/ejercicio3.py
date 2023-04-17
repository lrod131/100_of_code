
#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
#It will take your current age as the input and output a message with our time left in this format:
#You have x days, y weeks, and z months left.
#Where x, y and z are replaced with the actual calculated numbers.


# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆



#Write your code below this line 👇
age = int(age)
remaining_time = 90 - age
days_remaining = 365 * remaining_time
weeks_remaining = 52 * remaining_time
months_remaining = 12 * remaining_time

print(f'you have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left')

