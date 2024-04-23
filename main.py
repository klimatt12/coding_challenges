import challenges
#Use the below to avoid needing to specify from which module
#from challenges import reverse_string

if __name__ == '__main__':
    # Calling reverse_string this way does all the work in the function itself.
    # variable life spans are limited to the function
    challenges.reverse_string()

    """
    Using this and the commented out code in reverse_string on lines 16 and 17 
    you can move reading the input and printing the  original and modified strings here
     
    input_string = input("Provide a string: ")
    while not input_string:
        print("String cannot be empty")
        input_string = input("Provide a string: ")
    reversed_string = challenges.reverse_string(input_string)
    print("Original string:", input_string)
    print("Reversed string:", reversed_string)
    """

