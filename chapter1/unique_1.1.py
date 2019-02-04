
def determine_unique_1(input):
    """
    This function takes a string variable, input, 
    and determines whether it has all unique characters
    or not.
    Example:
    input = "saim"  Return  "unique"
    input = "yavar" Return  "not unique"
    """
    letter_frequency = {}
    for letter in input:
        if letter not in letter_frequency.keys():
            letter_frequency[letter] = 1
        else:
            return "not unique"
    return "unique"

got = determine_unique_1("jaihoo")
print(got)

            







