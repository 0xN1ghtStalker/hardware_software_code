def decimal_to_binary(decimal_num):      # conversion method: divides the decimal number by 2 reapetedly and records the remainders.
    binary = ""
    while decimal_num > 0:
        remainder = decimal_num % 2
        binary = str(remainder) + binary
        decimal_num //= 2
    return binary if binary else "0"

def binary_to_decimal(binary_num): # conversion method: this multiplies each binary digit by it's positional value and sums them up.
    decimal = 0
    power = 0
    for digit in binary_num[::-1]:
        if digit == '1':
            decimal += 2 ** power
        power += 1
    return decimal

def decimal_to_hexadecimal(decimal_num): # conversion method: Divides the decimal number by 16 repeatedly as hexadecimal is a base 16 system, records the remainders and maps them to hexadecimal digits
    hexadecimal = ""
    hex_digits = "0123456789ABCDEF"
    while decimal_num > 0:
        remainder = decimal_num % 16
        hexadecimal = hex_digits[remainder] + hexadecimal
        decimal_num //= 16
    return hexadecimal if hexadecimal else "0"

def hexadecimal_to_decimal(hexadecimal_num): # multiplies each hexadecimal digit by it's positional value and sums them up
    decimal = 0
    hex_digits = "0123456789ABCDEF"
    for digit in hexadecimal_num:
        decimal = 16 * decimal + hex_digits.index(digit)
    return decimal

def hexadecimal_to_binary(hexadecimal_num): # this function converts the hexadecimal number to decimal then binary using our preexisting functions
    decimal_num = hexadecimal_to_decimal(hexadecimal_num)
    return decimal_to_binary(decimal_num)

def binary_to_hexadecimal(binary_num): # this function converts the bianry number to decimal then to hexadecimal
    decimal_num = binary_to_decimal(binary_num)
    return decimal_to_hexadecimal(decimal_num)

def decimal_to_octal(decimal_num): # this function divides the decimal number by 8 repeatedly and recors the remainders
    octal = ""
    while decimal_num > 0:
        remainder = decimal_num % 8
        octal = str(remainder) + octal
        decimal_num //= 8
    return octal if octal else "0"

def octal_to_decimal(octal_num): # this function multiplies each octal digit by it's positional value and sums them up
    decimal = 0
    power = 0
    for digit in octal_num[::-1]:
        decimal += int(digit) * (8 ** power)
        power += 1
    return decimal

def main():
    print("Hello my name is Isaiah Halsey and Here is my conversion calculator program which allows you to convert numbers into different bases for your needs")
    while True:
        print("\nChoose conversion:")
        print("1. Decimal to Binary")
        print("2. Binary to Decimal")
        print("3. Decimal to Hexadecimal")
        print("4. Hexadecimal to Decimal")
        print("5. Hexadecimal to Binary")
        print("6. Binary to Hexadecimal")
        print("7. Decimal to Octal")
        print("8. Octal to Decimal")
        print("9. Quit")
        choice = input("Enter choice (1-9): ")

        if choice == '1':
            decimal_num = int(input("Enter a decimal number: "))
            print("Binary representation:", decimal_to_binary(decimal_num))
        elif choice == '2':
            binary_num = input("Enter a binary number: ")
            print("Decimal representation:", binary_to_decimal(binary_num))
        elif choice == '3':
            decimal_num = int(input("Enter a decimal number: "))
            print("Hexadecimal representation:", decimal_to_hexadecimal(decimal_num))
        elif choice == '4':
            hexadecimal_num = input("Enter a hexadecimal number: ")
            print("Decimal representation:", hexadecimal_to_decimal(hexadecimal_num))
        elif choice == '5':
            hexadecimal_num = input("Enter a hexadecimal number: ")
            print("Binary representation:", hexadecimal_to_binary(hexadecimal_num))
        elif choice == '6':
            binary_num = input("Enter a binary number: ")
            print("Hexadecimal representation:", binary_to_hexadecimal(binary_num))
        elif choice == '7':
            decimal_num = int(input("Enter a decimal number: "))
            print("Octal representation:", decimal_to_octal(decimal_num))
        elif choice == '8':
            octal_num = input("Enter an octal number: ")
            print("Decimal representation:", octal_to_decimal(octal_num))
        elif choice == '9':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
