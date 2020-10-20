age = 20  # integer
price = 19.95  # float
first_name = "Sebastian"  # string
is_online = False  # bool
print(age)

# name = input("What is your name?:  ")
# print(f"Hello {name}.")

# birth_year = input("Enter your birth year: ")
# age = 2020 - int(birth_year)
# print(f"Your age is: {age}")

course = "Python for Beginners"
print(course.find('y'))
print(course.replace('for', '4'))
print('Python' in course)


weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print(f"Weight in Lbs: {converted:.2f}")
else:
    converted = weight * 0.45
    print(f"Weight in Kgs: {converted:.2f}")
