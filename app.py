# Reverse a String:

s = "Python"
rev = " "

for i in s:
    rev = i + rev
print("Reverse String: ", rev)


# Check Palindrome:

s = "level"
rev = ""

for i in s:
    rev = i + rev

if s == rev:
    print(f"{s} is a Palindrome")
else:
    print(f"{s} is not a palindrome")
