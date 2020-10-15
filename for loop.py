#friends = ["Jim","Karen","Selva"]

#for letter in range(3,10):
#    print(letter)
# For straight range (range(100)) of 100 means 0-99
# For reversed range (range(100,-1,-1)) of 100 means 100-0


# Palimdrome

word = input("Enter a word:")

new_word=word[::-1]
lw = len(word)

if word.lower()==new_word.lower():
    print("This is a Palindrome word")
else:
    print("This is not a Palindrome word")

#print(lw)