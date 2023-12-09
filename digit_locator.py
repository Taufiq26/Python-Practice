def find_digit_at_place(number, place):
    # Convert number to string to easily access digits
    number_str = str(number)
    
    # Count the digits in the number
    digit_count = len(number_str)
    
    # Check if the specified place is valid
    if place <= digit_count:
        # Find the digit at the specified place
        digit = int(number_str[place - 1])
        return digit, digit_count
    else:
        return None, digit_count

# Example usage:
num = int(input("Enter a number: "))
specified_place = int(input("Enter a specified place number: "))

result_digit, total_digits = find_digit_at_place(num, specified_place)

if result_digit is not None:
    print(f"The digit at place {specified_place} in the number {num} is: {result_digit}")
else:
    print(f"There are only {total_digits} digits in the number {num}. Specified place is out of range.")
