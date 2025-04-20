import re

# Deprecated file

def replace_p_with_pound(value):
    # Find the index of the last '/'
    last_slash_index = value.rfind('/')

    # Extract the numeric part before the '/'
    numeric_part = value[:last_slash_index]
    if '£' in value:
        # Extract the numeric part after the '£' symbol
        numeric_part_number = numeric_part.split('£')[1]

        # Convert the numeric part to a float
        pounds = float(numeric_part_number)
    else:
        # Remove any non-digit characters from the numeric part
        numeric_part = ''.join(filter(str.isdigit, numeric_part))

        # Convert the numeric part to pounds
        pounds = float(numeric_part) / 100

    return pounds


def CompareValue(value1, value2):
    """
    Takes in two list objects, and returns the object with the better value
    :param value1: list item 1
    :param value2: list item 2
    :return: the better valued item
    """
    # Make sure units are the same
    value1Pound = replace_p_with_pound(value1.value)
    value2Pound = replace_p_with_pound(value2.value)

    if(value1Pound > value2Pound):
        return value1
    else:
        return value2


