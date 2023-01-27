# Function that takes a list of strings and returns a new list with all strings that are anagrams of a palindrome

# Original list
words = ['racecar', 'hello', 'level', 'carcare', 'carecar', 'civic', 'lehol', 'vicic']
# List to store the palindrome words from the original list
palindromes =[]
for word in words:
   # check if it's a palindrome word or not
   if(word[::-1] == word):
       palindromes.append(word)
# temporary list to store the anagrams of the words
tempList =[]
for p in palindromes:
    # to find the anagrams of the words
    for word in words:
        if(sorted(word) == sorted(p)):
            tempList.append(word)
# using set '-' operator to get the final anagrams of the palindrome word from the list
print(list(set(tempList) - set(palindromes)))


