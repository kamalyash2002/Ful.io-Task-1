import re

def is_valid_contact_number(number):
    # this is the regukar expression 
    pattern = r'^(\+?\d{1,2}\s?)?(\(\d{3}\)|\d{3})([-.\s]?)\d{3}([-.\s]?)\d{4}$'
    #now checking the pattern
    if re.match(pattern, number):
        return True
    else:
        return False

#given examples
numbers_to_check = [
    "2124567890",
    "212-456-7890",
    "(212)456-7890",
    "(212)-456-7890",
    "212.456.7890",
    "212 456 7890",
    "+12124567890",
    "+12124567890",
    "+1 212.456.7890",
    "+212-456-7890",
    "1-212-456-7890"
]

# Checking the examples whether they are valid or not
for number in numbers_to_check:
    if is_valid_contact_number(number):
        print(f"{number} is a valid contact number.")
    else:
        print(f"{number} is an invalid contact number.")


# code by Yash Kamal Saxena