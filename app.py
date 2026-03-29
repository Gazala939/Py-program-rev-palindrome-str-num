# Reverse a String:

s = "Python"
rev = " "

for i in s:
    rev = i + rev
print("Reverse String: ", rev) # Reverse String:  nohtyP 


# Check Palindrome of String:

s = "level"
rev = ""

for i in s:
    rev = i + rev

if s == rev:
    print(f"{s} is a Palindrome")
else:
    print(f"{s} is not a palindrome") # level is a Palindrome


# Reverse a Number:

num = 1234
rev = 0

while num > 0:
    digit = num % 10   # gry the last digit
    rev = rev * 10 + digit
    num = num // 10 # Remove the last digit
print("Reversed number: ", rev)

# Check Palindrome of number

num = 121
rev = 0
original = num

while num > 0:
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if original == rev:
    print(f"{original} is a Palindrome") 
else:
    print(f"{original} is not a Palindrome")