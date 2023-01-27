# lambda function to sort the list on the basis of the length of each element
sorted_list = lambda original_list: sorted(original_list , key=lambda word_length: len(word_length) , reverse=True)

original_list = ["dog", "cat", "bird"]
print(sorted_list(original_list))