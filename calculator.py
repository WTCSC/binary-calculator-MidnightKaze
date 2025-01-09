import math

def decimal_to_binary(num):
    # The binary for 0 is 0, so obviously it should just return 0.
    if num == 0: return 0
    
    bin = ""
    while num > 0:
        # Obtains a remainder after the argument is divided by 2.
        remain = num % 2
        # Adds the remainder to whatever the start of the binary string may be.
        bin = str(remain) + bin
        # Resets the number to continue the loop, until num is 0.
        num = num // 2

    return bin


def binary_to_decimal(num):

    # Removes any leading 0s which is necessary for the conversion to work correctly.
    num = num.lstrip('0')

    # Added a case check; as when lstrip does it's magic, 0 in any form will automatically turn into an empty string.
    if num == '':
        return 0
        
    # Floors the number and turns it into a base 2 integer - binary.
    return math.floor(int(num, 2))


def check_if_binary(num):
    # Checks for an empty string
    if num == '':
        return False
    
    # Checks for anything other than a 1 or 0
    for x in num:
        if x not in "10":
            return False
    
    # Gives the all clear for everything to contrinue
    return True


def binary_calculator(bin1, bin2, operator):
    
    # Starts by checking each number to ensure the starting input is actually binary.
    if check_if_binary(bin1) == False:
        return "Error"
    if check_if_binary(bin2) == False:
        return "Error"

    # Else continues by converting the binary values in decimals.
    num1 = binary_to_decimal(bin1)
    num2 = binary_to_decimal(bin2)

    # Checks if the denominator of a division problem is 0. Throws an error if it it.
    # Will integrate it into the actual thing later on.
    if num2 == 0 and operator == '/':
        return "NaN"
    
print(binary_calculator("00001110", "00000000", "/"))
    