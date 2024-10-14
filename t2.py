from collections import deque
def check_palindrome(s):
    # Convert the input string to lowercase and remove spaces
    s = ''.join(s.lower().split())

    # Initialize a deque with the processed string characters
    chars = deque(s)

    while len(chars) > 1:
        # Compare and remove characters from both ends
        if chars.popleft() != chars.pop():
            return False

    return True

# Sample strings to test the function
sample_strings = [
    "A man a plan a canal Panama",
    "Racecar",
    "Hello",
    "Was it a car or a cat I saw",
    "No lemon no melon"
]

# Evaluate and print the results for each sample string
for string in sample_strings:
    result = check_palindrome(string)
    print(f"'{string}' is a palindrome: {result}")