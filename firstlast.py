def extract_first_and_last_name(full_name):
  # Split the full name into parts
  parts = full_name.split()
  # First name is the first word
  first_name = parts[0]
  # Last name is the last word
  last_name = parts[-1]
  return f"{first_name} {last_name}"

# Read data from file
def read_data(filename):
  with open(filename, 'r', encoding='utf-8') as file:
      data = file.readlines()
  return data

# Write extracted names to file
def write_extracted_names(extracted_names, output_filename):
  with open(output_filename, 'w', encoding='utf-8') as file:
      for name in extracted_names:
          file.write(name + '\n')

# File containing data
input_filename = '2ndcleaned_text.txt'
# File to write extracted names
output_filename = 'final_file.txt'

# Read data from the file
data = read_data(input_filename)

# Extract first and last names
first_last_names = [extract_first_and_last_name(line.strip()) for line in data]

# Write extracted names to file
write_extracted_names(first_last_names, output_filename)

print("Extracted first and last names have been written to", output_filename)
