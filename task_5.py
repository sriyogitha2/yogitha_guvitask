#1 question

data = [10, 501, 22, 37, 100, 999, 87, 3511]
result = filter (lambda x: x > 4, data)
print (list (result))
#output :[10, 501, 22, 37, 100, 999, 87, 3511]
         
#2 question
 
data = [10, "hello", 23.5, "world", 42, "python"]

result = list(map(lambda x: f"{x}: Integer" if isinstance(x, int) else f"{x}: String" if isinstance(x, str) else f"{x}: Other", data))

print(result)

#3 question

fibonacci = lambda x: x if x <= 1 else fibonacci(x - 1) + fibonacci(x - 2)

# Generate Fibonacci numbers for the first 50 terms
fib_series = [fibonacci(i) for i in range(50)]

print(fib_series)


#4 question
import re

# a) Validate Email Address
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# b) Validate Mobile Numbers of Bangladesh
def validate_bangladesh_mobile(number):
    pattern = r'^(\+880|880|0)1[3-9]\d{8}$'
    return bool(re.match(pattern, number))

# c) Validate Telephone Numbers of USA
def validate_usa_telephone(number):
    pattern = r'^\+?1?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    return bool(re.match(pattern, number))

# d) Validate 16-character Alpha-Numeric Password
def validate_password(password):
    pattern = r'^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[@$!%?&])[A-Za-z\d@$!%?&]{16}$'
    return bool(re.match(pattern, password))

# Test the functions
email = "example@email.com"
bd_mobile = "+8801712345678"
usa_telephone = "123-456-7890"
password = "Abcdefg!12345678"

print("Email valid:", validate_email(email))                # True or False
print("BD Mobile valid:", validate_bangladesh_mobile(bd_mobile))  # True or False
print("USA Telephone valid:", validate_usa_telephone(usa_telephone))  # True or False
print("Password valid:", validate_password(password))       # True or False
