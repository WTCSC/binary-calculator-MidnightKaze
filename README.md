[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17650609)
# Binary Calculator

## Overview

There are a lot of people who can do basic mathmatics without a calculator. 1+1? That's pretty easy. The answer is clearly 2. How about 00000001 + 00000001? Well that's also 2, but you probably can't do that in your head. That's why people like you need this calculator! Because seriously, who can do binary in their head or even on a piece of paper.

This calculator can perform the 4 basic operations in math: multiplication, divison, addidtion, and subtraction.

## How to Use

1. Simply download the calculator.py file and import it into a project, VScode, or anywhere else you see fit.
2. Call the *binary_calculator* function, which will take in three arguments:
    - __bin1__, a simple number that will serve as the first number in the equation.

    - __bin2__, another simple number that will serve as the second number in the equation.

    - __operation__, choose either multiplication (*), divison (/), addition (+), or subtraction(-) to act as the desired operation of the equation.
    
    __*Do note that bin1 and bin2 must be passed in as strings and it's expected that the string passed is in binary. Only 1s and 0s with any number of digits up to 8.*__

## Converters

This calculator comes with two converters for your convenience:

1. __Binary to Decimal__. Call the *binary_to_decimal* function to convert a binary value into a decimal value.

2. __Decimal to Binary__. Since there's no automatic decimal to binary, use the *decimal_to_binary* to convert your decimal to a binary before hand. 

_Automatic decimal detection and conversion may be added later on._

## Error Detection

This calculator comes with a few checks to ensure that you recieve a real answer.

1. You cannot divide by 0. If you pass in "0" for bin2 and "/" for operation, you will recieve a __NaN__ as your answer.

2. Only numbers can be passed in. Passing through any letter will result in an __Error__.

3. Additonally, any resulting value that acceeds the [0,255] range will result in an __Overflow__.

<!--

The following requirements must be met to receive full credit on this assignment. The calculator must handle binary arithmetic operations accurately while following proper error handling procedures and output formatting guidelines.

- Your solution must have a well-written and thorough README file. [done]
- The solution must be implemented as a function called `binary_calculator()` with three parameters: [done]
    - `bin1` - A string parameter representing the first binary number to be used in the calculation. Must contain only 0s and 1s.
    - `bin2` - A string parameter representing the second binary number to be used in the calculation. Must contain only 0s and 1s.
    - `operator` - A string containing one of the following arithmetic operators: `'+'`, `'-'`, `'*'`, or `'/'`
- Do not use Python's built-in `bin()` function. [done]
- Implement your own binary-to-decimal and decimal-to-binary conversion logic. [done]
- All binary inputs and outputs should be strings. [done]
- Handle division by zero by returning `"NaN"` [done]
- Handle decimal numbers by rounding down to the nearest whole number (flooring). [done]
- Return `"Error"` for invalid binary inputs (containing characters other than `0` and `1`) [done]
- Return `"Overflow"` for any operations that overflow (i.e. negative numbers, numbers greater than 8-bits). [done]
- Outputs must be returned as 8-bit numbers (padded with leading zeros if necessary). For example, the decimal number `5` should be returned as `"00000101"` . [done]

Your solution will be tested against various test cases including edge cases, invalid inputs, and all four arithmetic operations.

/ᐠ - ˕ -マᶻ 𝗓 𐰁

 -->