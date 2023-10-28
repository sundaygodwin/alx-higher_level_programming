#!/usr/bin/python3

def text_indentation(text):
    # Check if text is a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Split the text based on '.', '?', and ':'
    lines = text.split('.')
    lines = [line.split('?') for line in lines]
    lines = [item for sublist in lines for item in sublist]  # Flatten the list
    lines = [line.split(':') for line in lines]
    lines = [item for sublist in lines for item in sublist]  # Flatten the list

    # Print the lines with two new lines after each '.', '?', and ':'
    for line in lines:
        line = line.strip()
        if line:  # Skip empty lines
            print(line)
        print("\n")
