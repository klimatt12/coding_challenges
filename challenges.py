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

    #reverse the string but exclude first and last characters
    #print("Reversed string:", input_string[len(input_string) - 2:0:-1])

    # def reverse_string(input_string):
    #     return input_string[::-1]
