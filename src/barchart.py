import matplotlib.pyplot as plt
import collections

# File path where keylog data is stored
log_file = "../logs/keylog.txt"

# Read typed data from the keylog file
with open(log_file, "r") as f:
    text = f.read()

# Remove session headers and extract only typed characters
lines = text.split("\n")
cleaned_text = "".join([line for line in lines if "SESSION STARTED" not in line and "===" not in line])

# Count frequency of each character
char_counts = collections.Counter(cleaned_text)

# Extract characters and their frequencies
characters = list(char_counts.keys())
frequencies = list(char_counts.values())

# Create bar chart
plt.figure(figsize=(10, 5))
plt.bar(characters, frequencies, color='dodgerblue', edgecolor='black')

# Formatting
plt.xlabel("Characters Typed", fontsize=12)
plt.ylabel("Frequency", fontsize=12)
plt.title("Character Frequency Bar Chart", fontsize=14)
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# Display the chart
plt.show()

