
with open('summaryLabels.txt', 'r') as file:
    summaryLabels = [line.strip().strip(',') for line in file]

# Format the output to display single quotes
formatted_output = "[" + ", ".join(f"'{item}'" for item in contents) + "]"
print(formatted_output)
