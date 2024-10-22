def is_armstrong_number(num):
    digits = str(num)
    num_digits = len(digits)
    armstrong_sum = sum(int(digit) ** num_digits for digit in digits)
    return armstrong_sum == num
input_number = int(input("Enter a number: "))
if is_armstrong_number(input_number):
    print("Yes")
else:
    print("No")