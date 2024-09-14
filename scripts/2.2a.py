def process_string(s):
    # Separate numbers and letters
    numbers = ''.join([char for char in s if char.isdigit()])
    letters = ''.join([char for char in s if char.isalpha()])

    # Get even numbers from the number string
    even_numbers = [int(num) for num in numbers if int(num) % 2 == 0]

    # Convert even numbers to their ASCII code
    ascii_even_numbers = [ord(str(num)) for num in even_numbers]

    # Get uppercase from the letter string
    uppercase_letters = [char for char in letters if char.isupper()]

    # Convert uppercase to ASCII
    ascii_uppercase_letters = [ord(char) for char in uppercase_letters]

    return even_numbers, ascii_even_numbers, uppercase_letters, ascii_uppercase_letters

# Sample input
s = "56aAww1984sktr235270aYmn145ss785fsq31D0"

# Process the string
even_numbers, ascii_even_numbers, uppercase_letters, ascii_uppercase_letters = process_string(s)

# Output
print("Even numbers:", even_numbers)
print("ASCII of even numbers:", ascii_even_numbers)
print("Uppercase letters:", uppercase_letters)
print("ASCII of uppercase letters:", ascii_uppercase_letters)
