# function that reads in a CSV file and returns a list of dictionaries,
# where each dictionary represents a row in the CSV file
import csv

def read_csv(file_name):
    with open(file_name, newline='', encoding='utf-8') as read_file:
        # Using the csv module to read the file
        csv_reader = csv.DictReader(read_file)
        # Create a list to store the dictionaries
        final_list=[]
        # Iterate over the rows in the file
        for row in csv_reader:
            final_list.append(row)
        return final_list

# calling the function
file_name = "Sample_CSV_File.csv"
final_list = read_csv(file_name)
print(final_list)
