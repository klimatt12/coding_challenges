def reverse_string():
    input_string = input("Provide a string: ")
    while not input_string:
        print("String cannot be empty")
        input_string = input("Provide a string: ")
    print("Original string:", input_string)

    #the below code splices the string. It take 3 arguments - start, stop, and step. when omitted, start and stop default
    #to the beginning and end of the string. a negative step interval tells it to go in reverse. when a negative step
    #interval is used, start defaults to the end of the string, and stop to the beginning
    print("Reversed string:", input_string[::-1])

    # Check for palindrome:
    if input_string == input_string[::-1]:
        print("This string is a plaindrome")
    else:
        print("This string is not a palindrome")

    #reverse the string but exclude first and last characters
    #print("Reversed string:", input_string[len(input_string) - 2:0:-1])

    # def reverse_string(input_string):
    #     return input_string[::-1]


def dictionaries():
    # Creates a dictionary where the keys are the first letters of any word in a list, and the values are
    # all words in the list that start with that letter.
    words = ["ape", "banana", "catalyst", "annabelle"]

    #word_dict = {}
    #This also works with a dictionary that already has entries
    word_dict = {
        'd': ['dominion'],
        'e': ['exquisite'],
        'f': ['formality']
    }

    for word in words:
        # Get the first character of the word
        first_char = word[0]
        if first_char in word_dict:
            # If the key exists, append the word to the corresponding value list
            word_dict[first_char].append(word)
        else:
            # If the key doesn't exist, create a new key-value pair with the word
            word_dict[first_char] = [word]
    #alphabetize the dictionary.  sorted_keys puts the keys in alphabetical order.
    sorted_keys = sorted(word_dict.keys())
    #for every key in sorted keys, create the same key in the new dictionary, and the value is looked up
    #from the original dictionary
    alphabetical_dict = {key: word_dict[key] for key in sorted_keys}
    print(alphabetical_dict)


def towers_of_hanoi(n, source, target, intermediate, move=1):
    #move the smallest disc to the destination and quit
    if n == 1:
        print(f"Move {move}: Move disk 1 from {source} to {target}")
        return move +1
    # Move discs from the source to the intermediate tower, using the target as a staging ground
    move = towers_of_hanoi(n-1, source, intermediate, target, move)
    print(f"Move {move}: Move disk {n} from {source} to {target}")
    #Move discs from intermediate to target using source as a staging ground
    move = towers_of_hanoi(n-1, intermediate, target, source, move + 1)
    return move