def decimal_to_binary(num):
    num = int(num)
    if num == 0: return 00000000
    # Some decimal to binary magic

def binary_to_decimal(num):
    num = int(num)
    num = num.lstrip()    
    return int(num, 2) # Removes the leading 0s and converts the number into base2 aka binary
    # Floor it too
    # Fix it too

def check_if_binary(num):
    
    check = "good"
    
    for x in num:
        if x == "abcdefghijklmnopqrtuvwxyz":
            check = "bad"
        elif x != "0" or "1":
            check = "bad"

def binary_calculator(bin1, bin2, operator):
    
    """
    > Logically would check bin1 and bin2 in order to convert them to the proper dec/bin whatever before ensuing the math
    > Would also logicaly check if it's binary first, before moving onto decimals
    > Would also have to check if any input was alpha
    """

    if bin2 == 0 and operator == '/': # If denominator is 0, return NaN
        return "NaN"