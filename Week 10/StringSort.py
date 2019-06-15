def case_sort(string):
    """
    Here are some pointers on how the function should work:
    1. Sort the string
    2. Create an empty output list
    3. Iterate over original string
        if the character is lower-case:
            pick lower-case character from sorted string to place in output list
        else:
            pick upper-case character from sorted string to place in output list
    
    Note: You can use Python's inbuilt ord() function to find the ASCII value of a character
    """
    # Sort String
    upper_ch_index = 0
    lower_ch_index = 0
    sorted_string = sorted(string)

    for index, character in enumerate(sorted_string):
        ascii_int = (ord(character))
        # ASCCI value of a = 97
        # ASCCI value of z = 122
        if 97 <= ascii_int <= 122:
            lower_ch_index = index
            break

    
    # 2. Create an empty output list
    output = list()

    for character in string:
        ascii_int = ord(character)
        if 97 <= ascii_int <= 122:
            output.append(sorted_string[lower_ch_index])
            lower_ch_index += 1
        else:
            output.append(sorted_string[upper_ch_index])
            upper_ch_index += 1
    return "".join(output)

def test_function(test_case):
    test_string = test_case[0]
    solution = test_case[1]
    
    if case_sort(test_string) == solution:
        print("Pass")
    else:
        print("False")


test_string = 'fedRTSersUXJ'
solution = "deeJRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)

test_string = "defRTSersUXI"
solution = "deeIRSfrsTUX"
test_case = [test_string, solution]
test_function(test_case)
