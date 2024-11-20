import re

number = input().strip()


def is_valid_number(number):
    
    if len(number) == 10 and number.isdigit():
        return "Correct"

    country_code_pattern = r'^\+?\d{1,2} \d{10}$'
    
    if re.match(country_code_pattern, number):

        di
        if sum(int(digit) for digit in digits) > 0:
            return "Correct"
    
   
    return "Incorrect"


print(is_valid_number(number))
