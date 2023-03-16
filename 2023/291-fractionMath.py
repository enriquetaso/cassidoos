# Write a function that can do the 4 basic operations
# (add, subtract, multiply and divide) on two fractions.
# Return the most simplified form of the result.
# You can assume a non-zero denominator in the input, and
# don’t use any built-in implementations in your language
# of choice, if you can! 

def parser_fraction(fraction_string):
    fraction_str_list = fraction_string.split("/")
    if fraction_str_list[-1] == '0':
        raise ZeroDivisionError
    numerator = int(fraction_str_list[0])
    denominator = int(fraction_str_list[-1])
    fraction = numerator/denominator
    return fraction

def fractionMath(fraction1_str, operation, fraction2_str):
    fraction1 = parser_fraction(fraction1_str)
    fraction2 = parser_fraction(fraction2_str)

    if operation == "add":
        return fraction1 + fraction2
    elif operation == "sustract":
        return fraction1 - fraction2
    elif operation == "multiply":
        return fraction1 * fraction2
    elif operation == "divide":
        return fraction1 / fraction2
    else:
        return "wrong operation"


if __name__ == "__main__":
    result = fractionMath("3/4", "add", "3/4")
    if result == "3/2":
        print("Test 1 passed")
    else:
        print("wrong output:", result)