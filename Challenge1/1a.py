def compress(input_string):
    # Check if the input string is empty or has only one character
    if len(input_string) <= 1:
        return input_string

    compressed_string = []
    current_char = input_string[0]
    char_count = 1

    for i in range(1, len(input_string)):
        if input_string[i] == current_char:
            char_count += 1
        else:
            compressed_string.append(current_char + str(char_count))
            current_char = input_string[i]
            char_count = 1

    # Append the last character and its count
    compressed_string.append(current_char + str(char_count))

    # Combine the compressed characters and counts into a single string
    compressed_string = ''.join(compressed_string)

    # Check if the compressed string is shorter than the original
    if len(compressed_string) < len(input_string):
        return compressed_string
    else:
        return input_string

# Example usage:
input_string = "a"
compressed_result = compress(input_string)
print(compressed_result)  # Output: "a4b3c2d6e2"


# time complexity
# The time complexity of the compress function is O(n), where 'n' is the length of the input string
# The function uses a for loop that iterates through the input string exactly once. 
# Therefore, the loop runs in O(n) time, where 'n' is the length of the input string
# Inside the loop, we perform constant-time operations like appending characters and counts to the list. 
# Each append operation is O(1)
# After the loop, we use the join method to concatenate the characters and counts into a single string. 
# This operation takes O(m) time, where 'm' is the length of the compressed string.
