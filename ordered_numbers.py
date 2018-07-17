#! python3
# ordered_numbers.py - Program that given a list of numbers returns an 'ordered' version of those numbers
# complexity of order_number() function: O(n - 1) where n is the number of digits of one number
import os


def order_number(number):
    """Return the greatest ordered number given a <number>"""
    ordered_number = number
    digits = [int(n) for n in list(str(ordered_number))]
    for i in range(len(digits))[::-1]:
        if i > 0 and digits[i] < digits[i - 1]:
            number_to_subtract = int(''.join([str(digit) for digit in digits[i:]])) + 1
            digits = [int(n) for n in list(str(ordered_number - number_to_subtract))]
            ordered_number = int(''.join([str(digit) for digit in digits]))
    return ordered_number


def read_file_contents(file_name):
    """Read the content of <file_name> and return a list of each line parsed to integer"""
    path = os.path.join(os.path.dirname(__file__), file_name)
    with open(path, 'r') as entry_file:
        return [int(line.replace('\n', '')) for line in entry_file.readlines()]


def write_result(input_numbers, output_numbers, file_name):
    """Write the unordered and ordered numbers in <file_name>"""
    path = os.path.join(os.path.dirname(__file__), file_name)
    with open(path, 'w') as output_file:
        for i in range(len(output_numbers)):
            output_file.write('Caso {}: N={}, O={}\n'.format(i + 1, input_numbers[i], output_numbers[i]))


def main():
    entry_file_lines = read_file_contents('entrada.txt')
    unordered_numbers = entry_file_lines[1::]
    ordered_numbers = [order_number(number) for number in unordered_numbers]
    write_result(unordered_numbers, ordered_numbers, 'salida.txt')


if __name__ == '__main__':
    main()
