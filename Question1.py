# program to reads all the lines of a file, create a dictionary:
#                                           where the key is the line number and value is another dictionary:
#                                                                     This another dictionary should contain length of
#                                                                     the words as keys,and the number of words having
#                                                                     same length as values
import shlex


def count_word_length(file_name):
    # Need to create an empty dictionary to store the expected output
    #           3: 4  # This is comment for explanation. There are four words having 3 chars - the, fox, the, dog
    #     		5: 3  # This is comment for explanation. There are 3 words having 5 chars - quick, brown, jumps
    #     		4: 2  # This is comment for explanation. There are 2 words having 4 chars - over, lazy
    dict_output = {}
    with open(file_name) as file_line:
        # Reading each line of the file
        for line_num, line in enumerate(file_line):
            # Count the number of lines in the file.
            line_num += 1
            # Need to create an empty dictionary to store the word length count from the lines of the file.
            count_word_len = {}
            # Now Split the line into words.
            words = line.split()
            # Iterate over each word in the line.
            for word in words:
                # Get the length of the word.
                word_len = len(word)
                # If we have already a word of same length, increment the counter by 1.
                if word_len in count_word_len:
                    count_word_len[word_len] += 1
                # If it is the first word of a considered length, set the count to 1.
                else:
                    count_word_len[word_len] = 1
            # Add the length of words count for the current line to the output dictionary
            dict_output[line_num] = count_word_len
    # Return the output dictionary
    return dict_output


file_name = "SampleText.txt"
result = count_word_length(file_name)
print(result)
