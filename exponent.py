#What? Exponent functions in Python refer to the process of raising a base number to a certain power. The base number is multiplied by itself the specified number of times.
#When? Are used in calculations like interest, Engineering, Sciences and calculating compound interest
#Why?  Help with Modeling growth,
# Define a function called 'raise_to_power' that takes two parameters: 'base_num' and 'pow_num'
def raise_to_power(base_num, pow_num):
    # Initialize 'result' to 1; this will store the final result of the exponentiation
    result = 1

    # Use a for loop to perform the exponentiation operation
    for index in range(pow_num):
        # Multiply 'result' by 'base_num' 'pow_num' times
        result = result * base_num

    # Return the final result after the loop completes
    return result


# Call the 'raise_to_power' function with provided arguments (2 and 16), and print the result
print(raise_to_power(2, 16))
