# s = input("Enter string: ")

# vowels = consonants = digits = special = 0

# for ch in s:
#     if ch.lower() in 'aeiou':
#         vowels += 1
#     elif ch.isalpha():
#         consonants += 1
#     elif ch.isdigit():
#         digits += 1
#     else:
#         special += 1

# print("Vowels:", vowels)
# print("Consonants:", consonants)
# print("Digits:", digits)
# print("Special characters:", special)


# -----------string reverse ---------

# s=input("enter the string")
# words= s.split()
# newword=[]
# for w in words:
#     newword.append(w[::-1])

# print(newword)

#-----------string palindrom-----------
# s = input("Enter string: ")

# if s == s[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


#----------each character frequency ---------
# s=input("enter the string : ")
# freq={}

# for ch in s:
#     if ch in freq:
#         freq[ch]+=1
#     else:
#         freq[ch]=1
# print(freq)


#=-----------string immutation------------
s = "hello"
try:
    s[2] = 'H'
except TypeError:
    print("Strings are immutable")


