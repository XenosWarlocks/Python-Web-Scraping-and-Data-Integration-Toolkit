import re

# Function to clean the extracted data
def clean_data(data):
    # Remove unwanted substrings
    for substring in ["Prof. ", "Dr.", "em.", ",", "MA", "J.", "M.A,", "theol.", "Apl.", "PD", "vom", "Dipl.", "-Päd.", "des.", "habil.", "Psych.", "'in", "Apl.", "M.Ed.", "i.R.", "Jun.", "()", "Prof.h.c.", "H.", "Soz.", "M.Ed.", "A.", "'in",  "(LL.M. (Yale))", "(verstorben am 05.07.2014)", "(†)", "Pfr M.", "M.", "apl.", "(M.)"]:
        data = data.replace(substring, "")
    # Remove leading and trailing whitespaces
    cleaned_data = data.strip()
    return cleaned_data

# Read extracted data from file
def read_extracted_data(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        extracted_data = file.read()
    return extracted_data

# Clean the extracted data
def clean_extracted_data(filename):
    extracted_data = read_extracted_data(filename)
    cleaned_data = clean_data(extracted_data)
    return cleaned_data

# Write cleaned data to file
def write_cleaned_data(cleaned_data, output_filename):
    with open(output_filename, 'w', encoding='utf-8') as file:
        file.write(cleaned_data)

# File containing extracted data
input_filename = 'extracted_text.txt'
# File to write cleaned data
output_filename = 'cleaned_text.txt'

# Clean the extracted data from the file
cleaned_data = clean_extracted_data(input_filename)

# Write cleaned data to file
write_cleaned_data(cleaned_data, output_filename)

print("Cleaned data has been written to", output_filename)
