def process_string(s):
    number_str = ''.join([ch for ch in s if ch.isdigit()])
    letter_str = ''.join([ch for ch in s if ch.isalpha()])

    # Finding even num & converting them to ASCII
    even_numbers = [int(ch) for ch in number_str if int(ch) % 2 == 0]
    even_ascii = [ord(str(num)) for num in even_numbers]

    # Finding uppercase letters & converting them to ASCII
    uppercase_letters = [ch for ch in letter_str if ch.isupper()]
    uppercase_ascii = [ord(ch) for ch in uppercase_letters]

    print(f"Number STring: {number_str} and Letter String: {letter_str}")
    print(f"Even numbers: {even_numbers}")
    print(f"Even numbers in ASCII: {even_ascii}")
    print(f"Uppercase letters: {uppercase_letters}")
    print(f"Uppercase letters in ASCII: {uppercase_ascii}")


scenario_string = input("Please Enter ur string: ")
process_string(scenario_string)
