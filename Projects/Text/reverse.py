'''
**Reverse a String** - Enter a string and the program will reverse it and print it out.
'''

def reverse(string):
    reversed = []

    for character in string:
        reversed.insert(0, character)

    reversed = ''.join(reversed)

    return reversed

if __name__ == '__main__':
    while True:
        string = input('Enter a string: ')
        print( 'Reversed is: %s' % reverse(string) )
