# This code removes any number that ends with a '.' from your text or code

with open(r'FullFilePath') as f: # the txt file that has the code / text you want to remove the numbers that ends with a '.'
    lines = f.readlines()

# Iterate through each line
for i in range(len(lines)):
    # Split the line into a list of words
    words = lines[i].split()
    # Iterate through each word in the line
    for j in range(len(words)):
        # Check if the word contains a "."
        if "." in words[j]:
            # Split the word into two parts along the "."
            parts = words[j].split(".")
            # Check if the first part is a number
            if parts[0].isdigit():
                # If it is a number, remove spaces around it and join it back with the second part
                words[j] = "".join([parts[1], parts[2]]) if len(parts) > 2 else parts[1]
    # Join the updated words back into a line
    lines[i] = " ".join(words)

# Write the updated lines to a new file
with open(r'FullFilePath', mode='w') as f: # the result will be copied there
    for line in lines:
        f.write("%s\n" % line)
