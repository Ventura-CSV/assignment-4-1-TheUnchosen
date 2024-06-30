def main():
    result = []
    start = input('Enter the starting letter: ')
    while start.isalpha() == False:
        start = input('Enter a valid starting letter: ')
    end = input('Enter the ending letter : ')
    while end.isalpha() == False:
        end = input('Enter a valid ending letter : ')
        
    for count in range(ord(start),ord(end)):
        result.append(start)
        start = chr(ord(start) + 1)
        
    """
    ########################################
    Code Your Program here
    ########################################
    """


    print(*result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
