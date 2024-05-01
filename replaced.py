def replace_dash(cleaned_data):
  # Replace "-" with " "
  cleaned_data = cleaned_data.replace("-", " ")
  return cleaned_data

# Read cleaned data from file
def read_cleaned_data(filename):
  with open(filename, 'r', encoding='utf-8') as file:
      cleaned_data = file.read()
  return cleaned_data

# Write modified data to file
def write_modified_data(modified_data, output_filename):
  with open(output_filename, 'w', encoding='utf-8') as file:
      file.write(modified_data)

# File containing cleaned data
input_filename = 'cleaned_text.txt'
# File to write modified data
output_filename = '2ndcleaned_text.txt'

# Read cleaned data from the file
cleaned_data = read_cleaned_data(input_filename)

# Replace "-" with " "
modified_data = replace_dash(cleaned_data)

# Write modified data to file
write_modified_data(modified_data, output_filename)

print("Modified data has been written to", output_filename)
