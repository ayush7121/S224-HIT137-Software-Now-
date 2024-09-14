global_variable = 100  # Set global variable

my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers(numbers):
    global global_variable  # Access global variable
    local_variable = 5  # Local variable
    numbers_list = list(numbers)  # Convert set to list

    while local_variable > 0:
        if local_variable % 2 == 0 and local_variable in numbers_list:
            numbers_list.remove(local_variable)  # Remove even numbers
        local_variable -= 1

    return numbers_list  # Return updated list

my_set = {1, 2, 3, 4, 5}  # Define a set
result = process_numbers(numbers=my_set)  # Process numbers

def modify_dict():
    local_variable = 10  # Local variable
    my_dict['key4'] = local_variable  # Add new key-value pair

modify_dict()  # Modify dictionary

def update_global():
    global global_variable  # Use global variable
    global_variable += 10  # Increment global variable

update_global()  # Update global variable

for i in range(5):
    print(i)  # Print numbers 0 to 4

# Check if dictionary has 'key4' with value 10
if my_set is not None and my_dict['key4'] == 10:
    print("Condition met!")

# Check if 5 is not a key in the dictionary
if 5 not in my_dict:
    print("5 not found in the dictionary!")

print(global_variable)  # Print global variable
print(my_dict)  # Print dictionary
print(my_set)  # Print set
