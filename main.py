def main():
    result = []
    start = input('Enter the starting letter: ')
    end = input('Enter the ending letter : ')
    while start.isalpha() == False or (ord(end) < ord(start)):
        start = input('Enter a valid starting letter: ')
        end = input('Enter a valid ending letter : ')
        
    for count in range(ord(start),ord(end) + 1):
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
