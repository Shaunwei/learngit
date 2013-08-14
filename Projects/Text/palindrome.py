'''
**Check if Palindrome** - Checks if the string entered by the user
is a palindrome. That is that it reads the same forwards
as backwards like “racecar”
'''

from reverse import reverse

def ispalindrome(original_string):
    reversed_string = reverse(original_string)
    return original_string == reversed_string

if __name__ == '__main__':
    while True:
        string = input('Enter a string: ')

        if ispalindrome(string):
            print( '%s is a palindrome' % string )
        else:
            print( '%s is not a palindrome' % string )

